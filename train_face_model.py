import os
from PIL import Image
import numpy as np
import cv2
import pickle

def startTraining():

    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(BASE_DIR, "data")

    if len(os.listdir(image_dir)) == 0:
        return print(
'''No training data. Terminating program.        
        
-- to create training data, run the following command,
   python3 run.py record''')

    print('Initializing Training...')

    current_id = 0
    label_ids = {}
    y_train = []
    x_train = []
    percentage = 0

    dirs = os.listdir(image_dir)
    total_data = [len(os.listdir(os.path.join(image_dir, file))) for file in dirs]
    step = (1/sum(total_data))*100

    for root, dirs, files in os.walk(image_dir):
        
        for file in files:

            percentage += step
            print(f'Training completed : {round(percentage, 2)}%', end='\r')

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

    with open('labels.pkl', 'wb') as file:
        pickle.dump(label_ids, file)

    recognizer.train(x_train, np.array(y_train))
    recognizer.save("model.yml")

    print('............................')
    print('Training Completed!')
    print('Model saved.')
    print()
    print(
'''--you can now test your model using the command,
        python3 run.py test''')


startTraining()