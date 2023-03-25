# enzyme-classification
# Enzyme Classification using Deep Learning
This repository contains code for enzyme classification using deep learning techniques. The aim is to predict the class of an enzyme based on its amino acid sequence.

# Data
The data used in this project is provided in two CSV files, Train.csv and Test.csv. The Train.csv file contains amino acid sequences and their corresponding enzyme classes for training the model, while the Test.csv file contains sequences for which the model should predict the corresponding enzyme class.

# Code
The Python script com.py performs the following steps:

Reads in the training and test data from CSV files.
Creates a dictionary to encode amino acid sequence data using integer encoding.
Uses Keras' pad_sequences function to pad the integer encoded data to a maximum length of 500.
Performs one-hot encoding on the target variable.
Builds a deep learning model using Keras' functional API, which includes embedding, bidirectional LSTM layers, and a dense output layer with a softmax activation function.
Trains the model on the training data.
Predicts the labels for the test data and writes them to a CSV file.
Usage
To use this code, simply download or clone the repository and run the com.py script. The predicted labels for the test data will be written to a CSV file named csv_file4.csv.

# Dependencies
The code requires the following Python packages:

pandas
numpy
tensorflow
Keras
scikit-learn
Credits
This project was completed by HusseinMansourMohd as part of a machine learning course.

License
This project is licensed under the MIT License - see the LICENSE file for detail
