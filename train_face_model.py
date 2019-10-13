import os
from PIL import Image
import numpy as np
import cv2
import pickle

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "data")

current_id = 0
label_ids = {}
y_train = []
x_train = []

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            label = os.path.basename(root).lower()

            if label not in label_ids:
                label_ids[label] = current_id
                current_id += 1

            id = label_ids[label]

            pil_img = Image.open(path).convert("L") # comverting into GrayScale
            pil_img = pil_img.resize((550, 550), Image.ANTIALIAS)
            img_arr = np.array(pil_img, "uint8")

            faces = face_cascade.detectMultiScale(img_arr, 1.3, 5)

            for (x, y, w, h) in faces:
                roi = img_arr[y:y + h, x:x + h]
                x_train.append(roi)
                y_train.append(id)

with open('model.pkl', 'wb') as file:
    pickle.dump(label_ids, file)

recognizer.train(x_train, np.array(y_train))
recognizer.save("model.yml")
