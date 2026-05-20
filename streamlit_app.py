import streamlit as st
import pickle
import numpy as np

# load trained model
model = pickle.load(open("model.pkl","rb"))

st.title("Chronic Kidney Disease Prediction System")

st.write("Enter patient details below:")

age = st.number_input("Age", 1, 100)
bp = st.number_input("Blood Pressure", 50, 200)
sg = st.number_input("Specific Gravity", 1.0, 1.05)
al = st.number_input("Albumin", 0, 5)
su = st.number_input("Sugar", 0, 5)
bgr = st.number_input("Blood Glucose Random", 50, 500)
bu = st.number_input("Blood Urea", 1, 200)
sc = st.number_input("Serum Creatinine", 0.1, 20.0)
hemo = st.number_input("Hemoglobin", 1.0, 20.0)
pcv = st.number_input("Packed Cell Volume", 10, 60)

if st.button("Predict"):
    input_data = np.array([[age,bp,sg,al,su,bgr,bu,sc,hemo,pcv]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ CKD Detected")
    else:
        st.success("✅ No CKD Detected")
