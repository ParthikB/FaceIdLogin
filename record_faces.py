import cv2
import os

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
file_number = 0

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, 'data')
os.chdir(image_dir)

label = input("Enter name : ").lower()
if not os.path.isdir(os.path.join(image_dir, label)):
    os.mkdir(label)
label_dir = os.path.join(BASE_DIR, 'data', label)
os.chdir(label_dir)


while file_number < 200:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+h]
        file_name = label + str(file_number) + ".jpg"
        cv2.imwrite(file_name, gray)
        file_number += 1

    cv2.imshow("frame", frame)

    if cv2.waitKey(25) & 0XFF == ord('q'):
        cv2.destroyAllWindows()
        break
