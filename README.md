# Image-Sentiment
This project was made by me and Abhilash Rath(https://github.com/AbhilashRath).

The project presents an 'Android Application' thay help users to recognise text from any Image and learn about its 'Sentiments' in the form of an audio. This is our first attempt in developing an Android App where the backend logic was developed in python. The driving force for the project was the urge build an accessible sentiment analyser and to learn building machine learning apps.

Firebase ML-Kit was used to host our custom ML model of sentiment analysis and pre-built API of text recognition by Firebase was used to recognise texts from images.

## Sentiments Analysis
We used supervised machine learning classification algorithm to make the sentiment analysis model in python. 
The data was downloaded from here: https://archive.ics.uci.edu/ml/datasets/Sentiment+Labelled+Sentences. 

### Data Preprocessing
We did data preprocessing using NLTK(natural langauge toolkit library) in python. The steps are as follows:
1. Make all alphabets into lowercase.
2. Word tokenizing.
3. Stemming
4. Removed the stopwords like is,this,am.

### Training machine learning model
We used 1000 most frequent words that were in dataset and used them to make the machine learning model.

The machine learning model was made using tensorflow and we made three neural network layers with 128,64,1 nodes respectively, then used sigmoid function on third node to classify the sentiment into 1(positive class) and 0(negative class).

Accuracy on training data was 95 percent.
Accuracy on test data was 85 percent.

### Saving the model
Now, we saved the trained model in .tflite format to use it in the app.

## Tools and Libraries
* Android Studio
* Tensorflow
* Firebase MLkit: https://firebase.google.com/docs/ml-kit
* Android-Image-Cropper: https://github.com/ArthurHub/Android-Image-Cropper
* Picasso: https://github.com/square/picasso
