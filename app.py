##################################  Importing Libraries      ###########################################

from flask import Flask,render_template
from gettext import install
import cv2
from matplotlib import collections
import numpy as np
from deepface import DeepFace
from collections import Counter
import matplotlib.pyplot as plt
app=Flask(__name__)
@app.route("/")

#################################   Render index.html page   #############################################

@app.route("/home")
def home():
    return render_template("index.html")
@app.route("/result",methods=['POST',"GET"])
def result():
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
#################################  Turn on the camera and capture the image  ##############################
    cap = cv2.VideoCapture(0)
    l=[];
    while True:
        ret,frame = cap.read()
#################################   Detect the emotions    ####################################
        result = DeepFace.analyze(frame,actions=['emotion'],enforce_detection=False)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.32, 5)
        for(x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 4)  #Put rectangle over the face
            
        font = cv2.FONT_HERSHEY_SIMPLEX
        l.append(result['dominant_emotion'])  # Insert the dominant emotion into list
        cv2.putText(frame, result['dominant_emotion'],(100, 100), font, 4, (0, 0, 255), 9)
        
        cv2.imshow('Video', frame)
        if cv2.waitKey(2) == ord('q'):  # wait until 'q' key is pressed
           break
    # Make a map of emotions with their count
    emotion={"neutral":l.count("neutral"),"happy":l.count("happy"),"sad":l.count("sad"),"angry":l.count("angry"),"fear":l.count("fear"),"surprise":l.count("surprise"),"disgust":l.count("disgust")}
    v=list(emotion.values())
    k=list(emotion.keys())
    print(k[v.index(max(v))])  # Detect the emotion with the maximum count
    print(max(v))
    l=[]
    cap.release()
    cv2.destroyAllWindows()
    return {k[v.index(max(v))]}

if(__name__)=='__main__':
    app.run(debug=True,port=5001)  # Run on localhost 5001

