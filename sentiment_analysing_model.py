
import numpy as np
import pandas as pd

df_1=pd.read_csv("amazon_cells_labelled.csv", names=['Sentences', 'Sentiments', "1", '2', '3', '4'], header=None)
df_2=pd.read_csv("yelp_labelled.csv", names=['Sentences', 'Sentiments', "1", '2', '3', '4'], header=None)
df_3=pd.read_csv("data.csv", names=['Sentences', 'Sentiments']).iloc[1:]

di={'1': '0', '0': '1', 1: '0', 0: '1'};
df_3['Sentiments']=df_3['Sentiments'].map(di)
df_3.head()

df_1.drop(['1', '2', '3', '4'], axis=1, inplace=True);
df_2.drop(['1', '2', '3', '4'], axis=1, inplace=True);

df=pd.concat([df_1, df_2, df_3], axis=0);
df.shape

df=df.reset_index()
df.drop(['index'], axis=1, inplace=True);

from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.manifold import TSNE
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, LSTM, Conv1D, MaxPooling1D, Dropout, Activation, MaxPooling2D
from tensorflow.keras.layers import Embedding
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from tensorflow.keras.optimizers import Adam

import nltk; nltk.download('punkt'); nltk.download('stopwords');

df['Sentiments']=df['Sentiments'].astype(int)
train_x=df['Sentences'].apply(lambda x: x.lower());
train_x=train_x.apply(lambda x: word_tokenize(x));
sw=stopwords.words('english');
listed=[];
for i in range(len(train_x)):
  k=train_x[i];
  k=[z for z in k if z not in sw];
  listed.append(k);

df.shape

X=listed; y=df['Sentiments'];
from sklearn.model_selection import train_test_split;
trn_x, val_x, trn_y, val_y=train_test_split(X, y, test_size=0.20, random_state=0);

words=1000;
tokenizer=Tokenizer(num_words=words,filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n')
tokenizer.fit_on_texts(trn_x)

trn_x = tokenizer.texts_to_sequences(trn_x)
trn_x = tokenizer.sequences_to_matrix(trn_x, mode='binary')

val_x = tokenizer.texts_to_sequences(val_x)
val_x = tokenizer.sequences_to_matrix(val_x, mode='binary')

# Define model

adam=Adam(learning_rate=0.0007, beta_1=0.9, beta_2=0.999)

model = Sequential()
model.add(Dense(128, input_shape=(words,),activation='relu'))
model.add(Dense(64,activation='relu'))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer=adam, metrics=['accuracy'])
model.fit(trn_x, trn_y, batch_size=64, epochs=15, verbose=1,validation_data=(val_x, val_y))

def predict_data(data):                                                                                                            
    input_data = tokenizer.texts_to_sequences(data);
    print(input_data)
    input_data = tokenizer.sequences_to_matrix(input_data,mode='binary');
    print(input_data)
    d=model.predict(input_data);
    return d

name='model.h5';
model.save(name);

import tensorflow as tf
converter=tf.lite.TFLiteConverter.from_keras_model_file('model.h5');

mod=converter.convert();
file=open('model_lite.tflite', 'wb');
file.write(mod);

files.download('model_lite.tflite')

import io
import json
tokenizer_json = tokenizer.to_json()
with io.open('tokenizer.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(tokenizer_json, ensure_ascii=False))

files.download('tokenizer.json')

