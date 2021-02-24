# -*- coding: utf-8 -*-
"""com.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L2D8a_LqjwF7pzieh8AjQaKreixlFyNt
"""

#@title Default title text
import pandas as pd
import numpy as np
train=pd.read_csv('/content/drive/MyDrive/Train.csv')
train.head()

#Download  the Train.csv as a dataframe

codes = ['A', 'C', 'D' ,'E', 'F', 'G', 'H', 'I', 'K', 'L',
         'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

def create_dict(codes):
  char_dict = {}
  for indx, val in enumerate(codes):
    char_dict[val] = indx+1

  return char_dict

char_dict = create_dict(codes)

print(char_dict)

def integer_encoding(data):
 
  
  encode_list = []
  for row in data['SEQUENCE'].values:
    row_encode = []
    for code in row:
      row_encode.append(char_dict.get(code, 0))
    encode_list.append(np.array(row_encode))
  
  return encode_list
  
train_encode = integer_encoding(train)

from tensorflow import keras
from keras.preprocessing.sequence import pad_sequences

max_length = 500
train_pad = pad_sequences(train_encode, maxlen=max_length, padding='post', truncating='post')
print(train_pad.shape)

train_pad_df = pd.DataFrame(train_pad)

from sklearn.preprocessing import OneHotEncoder
# creating instance of one-hot-encoder
enc = OneHotEncoder(handle_unknown='ignore')
# passing bridge-types-cat column (label encoded values of bridge_types)
enc_df = pd.DataFrame(enc.fit_transform(train[['LABEL']]).toarray())

enc_df = np.array(enc_df)
enc_df.shape

from tensorflow.keras import layers
from tensorflow.keras import Model

x_input = layers.Input(shape=(500,))

emb = layers.Embedding(500, 256, input_length=max_length)(x_input)

bi_rnn1 = layers.Bidirectional(layers.LSTM(128,return_sequences=True))(emb)

bi_rnn2 = layers.Bidirectional(layers.LSTM(128,))(bi_rnn1)

x_output = layers.Dense(20,  activation="softmax")(bi_rnn2)

model1 = Model(inputs=x_input, outputs=x_output)
model1.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'] )

model1.summary()

train=0
train_encode=0

history = model1.fit(train_pad,enc_df,epochs=25,verbose=2,steps_per_epoch=1000)

submission=pd.read_csv('/content/drive/MyDrive/Test.csv')
submission_encode = integer_encoding(submission)

submission_pad = pad_sequences(submission_encode, maxlen=max_length, padding='post', truncating='post')

submission_encode=0

A =['','', '','','','','','','','','','','','','','','','','','']
for i in range(0,1000):
    r=np.argmax(enc_df[i], axis=0)
    A[r] = str(train['LABEL'][i])
A

h=model1.predict(submission_pad)

H=[]
import csv
csv_file = open("csv_file4.csv", "w")
writer = csv.writer(csv_file)
writer.writerow(['SEQUENCE_ID', 'LABEL'])
for i in range(0,253146): 
    max_index_row = np.argmax(h[i], axis=0)
    writer.writerow([submission['SEQUENCE_ID'][i], A[max_index_row]])
csv_file.close()