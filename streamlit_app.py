import streamlit as st
import joblib
import numpy as np

# load model
model = joblib.load("model.pkl")

st.set_page_config(
    page_title="CKD Prediction",
    layout="centered"
)

st.title("🩺 Chronic Kidney Disease Prediction")

st.write("Enter patient details below:")

age = st.number_input("Age")
bp = st.number_input("Blood Pressure")
sg = st.number_input("Specific Gravity")
al = st.number_input("Albumin")
su = st.number_input("Sugar")
bgr = st.number_input("Blood Glucose Random")
bu = st.number_input("Blood Urea")
sc = st.number_input("Serum Creatinine")
hemo = st.number_input("Hemoglobin")
pcv = st.number_input("Packed Cell Volume")

if st.button("Predict"):

    data = np.array([[age,bp,sg,al,su,bgr,bu,sc,hemo,pcv]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("⚠️ CKD Detected")
    else:
        st.success("✅ No CKD Detected")
