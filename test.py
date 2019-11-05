import cv2
import numpy as np
import pickle

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('model.yml')

print('Press "q" to end testing.')

labels = {}
with open('labels.pkl', 'rb') as file:
    labels = pickle.load(file)
    labels = {v:k for k,v in labels.items()}

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+h]
        id, confidence = recognizer.predict(roi_gray)
        # if confidence >= 20: #and confidence <= 85:
        print("--> Prediction :", labels[id], end='\r')
        cv2.putText(frame, labels[id], (x, y-7), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 1, cv2.LINE_AA)
        # cv2.imwrite("capture.png", roi_gray)

    # displaying the frame
    cv2.imshow("cam", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

print('Testing terminated.')
