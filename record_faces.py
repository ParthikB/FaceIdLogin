import cv2
import os

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
file_number = 0

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, 'data')

if not os.path.isfile(image_dir):
    os.mkdir(image_dir)

os.chdir(image_dir)

label = input("Enter name : ").lower()
if not os.path.isdir(os.path.join(image_dir, label)):
    os.mkdir(label)
label_dir = os.path.join(BASE_DIR, 'data', label)
os.chdir(label_dir)

completed = True
TOTAL_SAMPLES = 200

while file_number < TOTAL_SAMPLES:

    percentage = round((file_number/TOTAL_SAMPLES)*100, 2)
    print(f'{percentage}% data collected.', end='\r')


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
        completed = False        
        break

if completed:
    print(
'''Training Sample collected! Now please train the model.

-- to train the model, use the command:
    python3 run.py train''')