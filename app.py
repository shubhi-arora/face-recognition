############################################## Importing Libraries################################################
# Flask is used to connect python backend to HTML
from flask import Flask, render_template
from gettext import install
import cv2
from matplotlib import collections
import numpy as np
from deepface import DeepFace  # deepface is used to detect emotions and face
from collections import Counter
import matplotlib.pyplot as plt  # matplotlib is used to plot the image
app = Flask(__name__)


@app.route("/")
######################################## Routing to homepage when get request occurs #################################
@app.route("/home")
def home():
    return render_template("index.html")

######################################## Routing to About page when get request occurs #################################


@app.route("/about", methods=['GET'])
def about():
    return render_template("about.html")

######################################## Routing to Result page when get and post request occurs #################################


@app.route("/result", methods=['POST', "GET"])
def result():
    config_file = './ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
    frozen_model = './frozen_inference_graph.pb'
    model = cv2.dnn_DetectionModel(frozen_model, config_file)
    classLabels = []
    file_name = './Labels.txt'  # File containing list of objects
    with open(file_name, 'rt') as fpt:
        classLabels = fpt.read().rstrip('\n').split('\n')
    model.setInputSize(320, 320)
    model.setInputScale(1.0/127.5)
    model.setInputMean((127.5, 127.5, 127.5))
    model.setInputSwapRB(True)

    l = []  # Making array/list to store various emotions
    race = []  # Making array/list to store race
    font_scale = 3
    font = cv2.FONT_HERSHEY_PLAIN
    global res, k, v
    global maxrace
    global gender
    global age
    faceCascade = cv2.CascadeClassifier(
        cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)  # Turn on the camera to take image of a face
    while True:
        ret, frame = cap.read()
        # Code to detect object and distinguish between object and face
        ClassIndex, confidece, bbox = model.detect(frame, confThreshold=0.55)
        if(len(ClassIndex) != 0):
            for ClassInd, conf, boxes in zip(ClassIndex.flatten(), confidece.flatten(), bbox):
                if(ClassInd <= 80):
                    cv2.rectangle(frame, boxes, (255, 0, 0), 2)
                    cv2.putText(frame, classLabels[ClassInd-1], (boxes[0]+10, boxes[1]+40),
                                font, fontScale=font_scale, color=(0, 255, 0), thickness=3)
                    # If a person is detected then only emotions will be detected and displayed
                    if classLabels[ClassInd-1] == 'person':
                        # Deepface library is used to detect emotions and race
                        result = DeepFace.analyze(
                            frame, actions=['emotion', 'race','gender'], enforce_detection=False)
                        # Convert the face from BGR to GRAY
                        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                        faces = faceCascade.detectMultiScale(gray, 1.32, 5)
                        gender=result['gender']
                        #maxrace=result['dominant_race']
                        for(x, y, w, h) in faces:
                            # Put rectangle over person's face
                            cv2.rectangle(
                                frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
                        font = cv2.FONT_HERSHEY_DUPLEX

                        # Append the race to the list
                        race.append(result['dominant_race'])
                        # Append the emotions to the list
                        l.append(result['dominant_emotion'])
                        cv2.putText(
                            frame, result['dominant_emotion'], (100, 100), font, 4, (0, 0, 255), 9)

                        cv2.imshow('Video', frame)
                        # wait until 'q' key is pressed for emotion detector
                        if cv2.waitKey(5) == ord('q'):
                            break
                       #### Make a dictionary of emotions and their respective count ############
                        emotion = {"neutral": l.count("neutral"), "happy": l.count("happy"), "sad": l.count("sad"), "angry": l.count(
                            "angry"), "fear": l.count("fear"), "surprise": l.count("surprise"), "disgust": l.count("disgust")}
                        v = list(emotion.values())
                        k = list(emotion.keys())
                        l = []
                        raceval = {"asian": race.count("asian"), "indian": race.count("indian"), "black": race.count("black"), "white": race.count(
                            "white"), "middle eastern": race.count("middle eastern"), "latino hispanic": race.count("latino hispanic")}
                        v2 = list(raceval.values())
                        k2 = list(raceval.keys())
                        race = []
        if cv2.waitKey(5) == ord('q'):  # wait until 'q' key is pressed for object detector
            break
    cap.release()
    cv2.destroyAllWindows()
    res = k[v.index(max(v))]  # Store the emotion with maximum count ##########
    maxrace = k2[v2.index(max(v2))]  # Store the race ################
    # Get result.html and pass res and maxrace
    return render_template("result.html", emotion=res, race=maxrace,gender=gender)

############## Routing to contact page when get request occurs ###########################


@app.route("/contact", methods=['GET'])
def contact():
    return render_template("contact.html")


if(__name__) == '__main__':
    app.run(debug=True, port=5001)  # Run on localhost 5001
