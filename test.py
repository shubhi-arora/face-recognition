from gettext import install
import cv2
from matplotlib import collections
import numpy as np
from deepface import DeepFace
from collections import Counter
import matplotlib.pyplot as plt

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
# if not cap.isOpened():
#     cap = cv2.VideoCapture(1)
# if not cap.isOpened():
#     raise IOError("Cannot open Webcam")
l=[];
while True:
        ret,frame = cap.read()
        result = DeepFace.analyze(frame,actions=['emotion'],enforce_detection=False)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.32, 5)
        for(x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 255), 4)
            
        font = cv2.FONT_HERSHEY_SIMPLEX
        l.append(result['dominant_emotion'])
        cv2.putText(frame, result['dominant_emotion'],(100, 100), font, 4, (0, 0, 255), 9)
        
        cv2.imshow('Video', frame)
        if cv2.waitKey(2) == ord('q'):  # wait until 'q' key is pressed
          break
emotion={"neutral":l.count("neutral"),"happy":l.count("happy"),"sad":l.count("sad"),"angry":l.count("angry"),"fear":l.count("fear"),"surprise":l.count("surprise"),"disgust":l.count("disgust")}
v=list(emotion.values())
k=list(emotion.keys())
print(k[v.index(max(v))])
print(max(v))

cap.release()
cv2.destroyAllWindows()
