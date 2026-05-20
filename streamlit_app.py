import streamlit as st
import joblib
import numpy as np

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(
    page_title="CKD Prediction System",
    page_icon="🩺",
    layout="centered"
)

# ======================
# CUSTOM CSS
# ======================
st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(to right, #141e30, #243b55);
    color: white;
}

/* Title */
h1 {
    text-align: center;
    color: #00ffd5;
    font-size: 42px !important;
}

/* Input Labels */
label {
    color: white !important;
    font-weight: bold;
}

/* Input Boxes */
.stNumberInput input {
    border-radius: 10px;
    border: 2px solid #00ffd5;
    padding: 10px;
}

/* Button */
.stButton>button {
    width: 100%;
    background: linear-gradient(to right, #00c6ff, #0072ff);
    color: white;
    font-size: 20px;
    font-weight: bold;
    border-radius: 12px;
    height: 3.5em;
    border: none;
    transition: 0.3s;
}

.stButton>button:hover {
    background: linear-gradient(to right, #11998e, #38ef7d);
    transform: scale(1.03);
}

/* Success Message */
.stSuccess {
    border-radius: 10px;
}

/* Error Message */
.stError {
    border-radius: 10px;
}

/* Mobile Responsive */
@media (max-width: 768px) {
    h1 {
        font-size: 28px !important;
    }

    .stButton>button {
        font-size: 18px;
    }
}

</style>
""", unsafe_allow_html=True)

# ======================
# LOAD MODEL
# ======================
model = joblib.load("model.pkl")

# ======================
# SIDEBAR
# ======================
st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/2966/2966488.png",
    width=120
)

st.sidebar.title("CKD Prediction App")

st.sidebar.info("""
This AI system predicts whether a patient is at risk of Chronic Kidney Disease (CKD).

Enter patient clinical values and click Predict.
""")

# ======================
# MAIN TITLE
# ======================
st.title("🩺 CKD Prediction System")

st.markdown("""
<div style='text-align:center; font-size:18px; margin-bottom:30px;'>
Machine Learning Based Chronic Kidney Disease Detection
</div>
""", unsafe_allow_html=True)

# ======================
# INPUTS
# ======================

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 1, 100)
    bp = st.number_input("Blood Pressure", 50, 200)
    sg = st.number_input("Specific Gravity", 1.0, 1.05)
    al = st.number_input("Albumin", 0, 5)
    su = st.number_input("Sugar", 0, 5)

with col2:
    bgr = st.number_input("Blood Glucose Random", 50, 500)
    bu = st.number_input("Blood Urea", 1, 200)
    sc = st.number_input("Serum Creatinine", 0.1, 20.0)
    hemo = st.number_input("Hemoglobin", 1.0, 20.0)
    pcv = st.number_input("Packed Cell Volume", 10, 60)

# ======================
# PREDICTION
# ======================


        if st.button("🔍 Predict CKD"):

    input_data = np.array([[age,bp,sg,al,su,bgr,bu,sc,hemo,pcv]])

    prediction = model.predict(input_data)

    st.markdown("---")

    pred = prediction[0]

    # Handle all prediction types
    if pred == 1 or pred == "ckd" or pred == "CKD":
        st.error("⚠️ CKD Detected")
        st.warning("Please consult a doctor.")

    else:
        st.success("✅ No CKD Detected")
        st.balloons()

# ======================
# FOOTER
# ======================

st.markdown("""
<hr>
<div style='text-align:center'>
Developed using Streamlit & Machine Learning
</div>
""", unsafe_allow_html=True)
