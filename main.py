# Step 01 importing all the libraries
from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
import streamlit as st

#Loading the imdb dataset
word_index = imdb.get_word_index()
reverse_word_index = {value: key for key,value in word_index.items()}

#loading the model
model = load_model("simple_rnn_imdb.h5")

## Step 02 Helper functions
def decode_review(encoded_review):
    return " ".join([reverse_word_index.get(i -3, "?") for i in encoded_review])

def preprocess_text(text):
    words = text.lower().split()
    encoded_review = [word_index.get(word, 2) + 3 for word in words]
    padded_review = sequence.pad_sequences([encoded_review],maxlen=500)
    return padded_review

## Step 03 Prediction function
def predict_sentiment(review):
    encoded_review = preprocess_text(review)
    prediction = model.predict(encoded_review)

    sentiment = 'Positive' if prediction[0][0] > 0.5 else 'Negative'
    return sentiment,prediction[0][0]

# Step 04 Streamlit app

st.title("IMDB Moview review Sentiment Analysis")
st.write('Enter a movie review to classify it as positive or negative.')

user_input = st.text_area("Movie Review")

if st.button("Classify"):
    sentiment,probability = predict_sentiment(user_input)
    st.write(f"The sentiment is {sentiment} by this probabilit: {probability}")

else:
    st.write("Please enter the review")


    

