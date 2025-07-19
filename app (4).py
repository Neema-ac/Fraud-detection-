

import streamlit as st
import pandas as pd
import joblib

st.title("Credit Card Fraud Detection System")

# Load the trained model
model = joblib.load('fraud_detection_model.pkl')

st.write("Upload a CSV file containing transactions (excluding the 'Class' column).")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    input_data = pd.read_csv(uploaded_file)
    st.write("Uploaded Data Preview:")
    st.write(input_data.head())
    
    predictions = model.predict(input_data)
    input_data['Fraud Prediction'] = predictions
    st.write("Prediction Results (0: Not Fraud, 1: Fraud):")
    st.write(input_data)
