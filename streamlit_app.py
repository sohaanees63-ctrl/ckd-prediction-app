import streamlit as st
import joblib
import numpy as np
from PIL import Image
import time

# Page settings
st.set_page_config(
    page_title="CKD Prediction System",
    page_icon="🩺",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>

    .stApp {
        background-color: #f4f8fb;
    }

    h1 {
        color: #0b5394;
        text-align: center;
    }

    .stButton>button {
        background-color: #0b5394;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 18px;
    }

    .stButton>button:hover {
        background-color: #073763;
        color: white;
    }

    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🩺 CKD Prediction App")
st.sidebar.info("""
This system predicts Chronic Kidney Disease (CKD) 
using Machine Learning Ensemble Models.
""")

st.sidebar.success("Developed using Streamlit")

# Main title
st.title("🩺 Chronic Kidney Disease Prediction")

st.write("### Enter Patient Clinical Details")

# Input fields
age = st.number_input("Age", min_value=1, max_value=100)

bp = st.number_input(
    "Blood Pressure",
    min_value=50,
    max_value=200
)

sg = st.number_input(
    "Specific Gravity",
    min_value=1.00,
    max_value=1.05,
    step=0.01
)

al = st.number_input(
    "Albumin",
    min_value=0,
    max_value=5
)

su = st.number_input(
    "Sugar",
    min_value=0,
    max_value=5
)

bgr = st.number_input(
    "Blood Glucose Random",
    min_value=50,
    max_value=500
)

bu = st.number_input(
    "Blood Urea",
    min_value=1,
    max_value=300
)

sc = st.number_input(
    "Serum Creatinine",
    min_value=0.1,
    max_value=20.0
)

hemo = st.number_input(
    "Hemoglobin",
    min_value=1.0,
    max_value=20.0
)

pcv = st.number_input(
    "Packed Cell Volume",
    min_value=10,
    max_value=60
)

# Load model and scaler
model = joblib.load("ckd_model.pkl")
scaler = joblib.load("scaler.pkl")

# Prediction button
if st.button("🔍 Predict CKD"):

    with st.spinner("Analyzing Patient Data..."):
        time.sleep(2)

        input_data = np.array([[
            age, bp, sg, al, su,
            bgr, bu, sc, hemo, pcv
        ]])

        input_scaled = scaler.transform(input_data)

        prediction = model.predict(input_scaled)

        # Result
        st.markdown("---")

        if prediction[0] == 0:
            st.error("⚠️ CKD Detected")
            st.warning("Please consult a medical professional.")
        else:
            st.success("✅ No CKD Detected")
            st.balloons()

# Footer
st.markdown("---")
st.caption("Machine Learning based CKD Prediction System")
