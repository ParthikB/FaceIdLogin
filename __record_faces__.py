import cv2
import os

TOTAL_SAMPLES = 200 # Total number of Samples that would be taken

# Creating a Cascade for detecting the face.
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
file_number = 0 # Itrator to assign Names to the samples.

# The directory where this python script is stores.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Database directory
database_dir = os.path.join(BASE_DIR, 'data')
# Creating the Database directory if not present
if not 'data' in os.listdir(BASE_DIR):
    os.mkdir(database_dir)
# Changing the dir to the Database dir
os.chdir(database_dir)

# The NAME of the person aka LABEL
LABEL = input("Enter name : ").lower()
# Creating a Database for the current Label
if not os.path.isdir(os.path.join(database_dir, LABEL)):
    os.mkdir(LABEL)
label_dir = os.path.join(BASE_DIR, 'data', LABEL)
# Changing the dir to the Label's Database dir
os.chdir(label_dir)

completed = True

while file_number < TOTAL_SAMPLES:

    # Baby Script to print the Percentage Completion
    percentage = round((file_number/TOTAL_SAMPLES)*100, 2)
    print(f'{percentage}% data collected.', end='\r')

    # Reading the Frames from the Stream
    _, frame = cap.read()
    
    # Converting into Grayscale to reduce size
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecting any face in the frame if present
    faces = face_cascade.detectMultiScale(gray)

    # Marking the Face Detected and writing it to the Database
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+h]
        file_name = LABEL + str(file_number) + ".jpg"
        cv2.imwrite(file_name, gray)
        file_number += 1

    # Streaming the Frames
    cv2.imshow("frame", frame)

    if cv2.waitKey(25) & 0XFF == ord('q'):
        cv2.destroyAllWindows()
        completed = False        
        break

if completed:
    print('............................')
    print(
'''Training Sample collected! Now please train the model.

-- to train the model, use the command:
    python3 run.py train''')