# facefusion
This project aims to develop a facial recognition system to assess the engagement levels of students in a classroom setting. The system will use predictive analysis to determine whether students are actively participating and listening during class sessions.

here the procedure for how this project works
1. run capture. py-it opens the webcam and captures the face in front of the webcam
2. run analysis.py-it analyzes the the captured picture which was saved in the captured images directory in your project directory
3. run app. py-it is the connectivity Python script which opens the webpage

steps to implement this project
1. download the FER2013 dataset from Kaggle, link is given below
https://www.kaggle.com/datasets/msambare/fer2013
2. run the preprocess. ipynb to preprocess the image, build the CNN model, train the model with preprocessed images, and test it
3. save the model for future reference
4. run capture.py to capture the human faces to detect the engagement level(it cannot terminate itself)
5. run the analysis.py to analyze the captured images which were saved in the project directory automatically while running the capture.py
6.run app.py which fetches the result of the analysis.py and displays it on the webpage

The webpage contains a pie chart of the engagement level and you can see the past engagement level the model.py create the database in the webpage so that we can see the past engagement level 
