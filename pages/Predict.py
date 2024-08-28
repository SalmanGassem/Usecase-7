import streamlit as st
from PIL import Image
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import requests

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

with st.sidebar:
      st.caption("By Salman Gassem © 2024")

st.title("Predictions")



# Model

st.header('Enter the new data below to get a prediction')

# Prompt the user for the first input (text input)
appearance = st.number_input("The number of appearances on the field:", min_value=0)

# Prompt the user for the second input (number input)
minutes_played = st.number_input("The amount of time played (in minutes):", min_value=0)

# Prompt the user for the third input (dropdown selection)
highest_value = st.number_input("The highest value amount the player achieved:", min_value=0)

api_url = "http://127.0.0.1:8000/predict"

if st.button("Get Prediction"):
    # Prepare the data to be sent to the FastAPI model
    input_data = {
        "Appearance": appearance,
        "Minutes_played": minutes_played,
        "Highest_value": highest_value
    }

    # Send the data to the FastAPI model via a POST request
    response = requests.post(api_url, json=input_data)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the prediction from the response
        prediction = response.json().get("pred")
        st.success(f"The predicted value is: {prediction}")
    else:
        st.error("There was an error with the prediction request.")