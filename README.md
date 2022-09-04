# ImageClassification
Python based Image classification

1. Check out the project on local machine
2. First train the model. python3 guddantest2.py. epoch is 10. It will take around 1 hour to run this program
3. It will generate a file called model_inception.h5. It will also generate images called AccVal_acc and LossVal_loss
4. Take that file and paste in Tomato-Leaf-Disease-Prediction-master folder
5. Go to folder Tomato-Leaf-Disease-Prediction-master
6. Run the flask server. python3 app.py
7. Go to http://127.0.0.1:5001/#
8. Click on the choose button and uplad a image. Sample are present in Tomato-Leaf-Disease-Prediction-master/uploads
9. Click on Predict button.
10. The program will print the disease name in the UI. It will also play the audio for the name of the disease



Important links:

1. https://github.com/krishnaik06/Tomato-Leaf-Disease-Prediction
2. https://www.kaggle.com/datasets/noulam/tomato

Architecture diagram


Accuracy and Loss value graphs
![Alt text](AccVal_acc.png?raw=true "Title")
![Alt text](AccVal_acc.png?raw=true "Title")
