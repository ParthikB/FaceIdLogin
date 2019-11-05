# FaceIdLogin

To run this model on your machine, follow the steps:

Step 0 | Download the repo on your machine using the download button, or the following command

        git clone https://github.com/ParthikB/FaceIdLogin.git faceId
        cd faceId

<i> for Windows </i>

Step 1 | Run the following command to install necessary dependencies

        pip install -r requirements.txt

Step 2 | To create data/record face data, run the following command

        python run.py record
        
Step 3 | Once after the faces are recorded, train the model using

        python run.py train
        
Step 4 | Once training completes, test the model using

        python run.py test
        
<i>(Optional)</i>

If you want to erase the database, run the following command,

        python run.py reset
