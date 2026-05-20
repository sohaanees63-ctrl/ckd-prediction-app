import streamlit as st
import joblib
import numpy as np
import time

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
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    background-size: 400% 400%;
    animation: gradientBG 12s ease infinite;
    color: white;
}

/* Animated Background */
@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Main Container */
.main {
    animation: fadeIn 1.5s ease-in;
}

/* Fade Animation */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0px);
    }
}

/* Title */
h1 {
    text-align: center;
    color: #00ffd5;
    font-size: 46px !important;
    text-shadow: 0px 0px 15px #00ffd5;
    animation: pulse 2s infinite;
}

/* Pulse Animation */
@keyframes pulse {
    0% {transform: scale(1);}
    50% {transform: scale(1.03);}
    100% {transform: scale(1);}
}

/* Subtitle */
.subtitle {
    text-align:center;
    font-size:20px;
    color:#d9faff;
    margin-bottom:30px;
}

/* Cards */
[data-testid="column"] {
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
}

/* Input Labels */
label {
    color: white !important;
    font-weight: bold;
}

/* Input Boxes */
.stNumberInput input {
    border-radius: 12px;
    border: 2px solid #00ffd5;
    padding: 12px;
    background-color: rgba(255,255,255,0.1);
    color: white;
}

/* Button */
.stButton>button {
    width: 100%;
    background: linear-gradient(to right, #00c6ff, #0072ff);
    color: white;
    font-size: 22px;
    font-weight: bold;
    border-radius: 15px;
    height: 3.5em;
    border: none;
    transition: 0.4s;
    box-shadow: 0px 0px 15px rgba(0,255,213,0.5);
}

/* Hover Button */
.stButton>button:hover {
    background: linear-gradient(to right, #11998e, #38ef7d);
    transform: scale(1.05);
    box-shadow: 0px 0px 25px rgba(56,239,125,0.8);
}

/* Success Message */
.stSuccess {
    border-radius: 15px;
    animation: fadeIn 1s ease-in;
}

/* Error Message */
.stError {
    border-radius: 15px;
    animation: fadeIn 1s ease-in;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #141e30, #243b55);
}

/* Footer */
.footer {
    text-align:center;
    color:white;
    padding-top:20px;
    font-size:16px;
}

/* Floating Effect */
img {
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0% {transform: translateY(0px);}
    50% {transform: translateY(-10px);}
    100% {transform: translateY(0px);}
}

/* Mobile Responsive */
@media (max-width: 768px) {

    h1 {
        font-size: 30px !important;
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
    width=130
)

st.sidebar.title("🩺 CKD Prediction App")

st.sidebar.success("AI Powered Disease Detection")

st.sidebar.info("""
This AI system predicts whether a patient is at risk of Chronic Kidney Disease (CKD).

✔ Fast Prediction  
✔ ML Based System  
✔ User Friendly Interface  
""")

st.sidebar.markdown("---")
st.sidebar.write("⚡ Developed with Streamlit")

# ======================
# MAIN TITLE
# ======================
st.title("🩺 CKD Prediction System")

st.markdown("""
<div class='subtitle'>
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

    # Loading Animation
    with st.spinner("Analyzing Patient Data..."):
        time.sleep(2)

    input_data = np.array([
        [age,bp,sg,al,su,bgr,bu,sc,hemo,pcv]
    ])

    prediction = model.predict(input_data)

    st.markdown("---")

    if prediction[0] == 0:

        st.success("✅ No CKD Detected")
        st.balloons()

        st.markdown("""
        <div style='
        background:rgba(0,255,100,0.1);
        padding:20px;
        border-radius:15px;
        text-align:center;
        font-size:20px;
        color:#7CFC00;
        box-shadow:0px 0px 20px rgba(0,255,100,0.4);
        '>
        Patient appears Healthy 💚
        </div>
        """, unsafe_allow_html=True)

    else:

        st.error("⚠️ CKD Detected")

        st.markdown("""
        <div style='
        background:rgba(255,0,0,0.1);
        padding:20px;
        border-radius:15px;
        text-align:center;
        font-size:20px;
        color:#ff6b6b;
        box-shadow:0px 0px 20px rgba(255,0,0,0.4);
        '>
        Please consult a kidney specialist immediately 🩺
        </div>
        """, unsafe_allow_html=True)

# ======================
# FOOTER
# ======================

st.markdown("""
<hr>
<div class='footer'>
✨ Developed using Streamlit, Python & Machine Learning ✨
</div>
/* Input Boxes FIX */
div[data-baseweb="input"] > div {
    background-color: white !important;
    border-radius: 12px !important;
    border: 2px solid #00ffd5 !important;
}

div[data-baseweb="input"] input {
    color: black !important;
    background-color: white !important;
    font-weight: bold !important;
    font-size: 18px !important;
}
""", unsafe_allow_html=True)

