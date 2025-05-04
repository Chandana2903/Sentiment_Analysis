import streamlit as st
import pickle

# Load the model
model = pickle.load(open("best_model.pkl", "rb"))

st.title("Sentiment Analysis Web App")

# User input
user_input = st.text_input("Enter a sentence to analyze:")

if user_input:
    result = model.predict([user_input])[0]
    st.write("Predicted Sentiment:", result)
