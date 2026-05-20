import streamlit as st
import joblib
import numpy as np

# Load model and scaler
model = joblib.load("ckd_model.pkl")
scaler = joblib.load("scaler.pkl")

# Title
st.title("Chronic Kidney Disease Prediction System")

st.write("Enter Patient Details")

# Inputs
age = st.number_input("Age", min_value=1, max_value=100)
bp = st.number_input("Blood Pressure", min_value=50, max_value=200)
sg = st.number_input("Specific Gravity", min_value=1.0, max_value=1.05)
al = st.number_input("Albumin", min_value=0, max_value=5)
su = st.number_input("Sugar", min_value=0, max_value=5)
bgr = st.number_input("Blood Glucose Random", min_value=50, max_value=500)
bu = st.number_input("Blood Urea", min_value=1, max_value=300)
sc = st.number_input("Serum Creatinine", min_value=0.1, max_value=20.0)
hemo = st.number_input("Hemoglobin", min_value=1.0, max_value=20.0)
pcv = st.number_input("Packed Cell Volume", min_value=10, max_value=60)

# Prediction
if st.button("Predict"):

    input_data = np.array([[age, bp, sg, al, su, bgr, bu, sc, hemo, pcv]])

    # scale input
    input_scaled = scaler.transform(input_data)

    # predict
    prediction = model.predict(input_scaled)

    # result
    if prediction[0] == 1:
        st.error("⚠️ CKD Detected")
    else:
        st.success("✅ No CKD Detected")
