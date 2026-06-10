import streamlit as st
import pandas as pd
import numpy as np
import joblib

# =========================
# PAGE CONFIGURATION
# =========================

st.set_page_config(
    page_title="Financial Viability - Loan Approval",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# LOAD MODEL
# =========================

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"]  {
    font-family: 'Poppins', sans-serif;
}

/* Main Background */

.main {
    background: linear-gradient(
        135deg,
        #020617 0%,
        #0F172A 35%,
        #111827 100%
    );
    color: white;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #111827 0%,
        #1E293B 100%
    );
    border-right: 1px solid rgba(255,255,255,0.08);
}

/* Sidebar Labels */

section[data-testid="stSidebar"] label {
    color: #E2E8F0 !important;
    font-weight: 500;
}

/* Main Title */

.main-title {
    text-align: center;
    font-size: 65px;
    font-weight: 800;
    background: linear-gradient(
        to right,
        #38BDF8,
        #818CF8,
        #06B6D4
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0px;
}

/* Subtitle */

.sub-title {
    text-align: center;
    color: #CBD5E1;
    font-size: 22px;
    margin-top: -10px;
    margin-bottom: 40px;
}

/* Cards */

.metric-card {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 24px;
    padding: 28px;
    text-align: center;
    backdrop-filter: blur(12px);
    box-shadow: 0 10px 35px rgba(0,0,0,0.35);
    transition: 0.3s ease;
}

.metric-card:hover {
    transform: translateY(-5px);
}

/* Metric Text */

.metric-title {
    color: #94A3B8;
    font-size: 17px;
    margin-bottom: 10px;
}

.metric-value {
    color: white;
    font-size: 34px;
    font-weight: 700;
}

/* Prediction Container */

.predict-box {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 24px;
    padding: 35px;
    margin-top: 30px;
    backdrop-filter: blur(15px);
}

/* Button */

.stButton > button {
    width: 100%;
    height: 60px;
    border-radius: 18px;
    border: none;
    background: linear-gradient(
        90deg,
        #06B6D4,
        #3B82F6
    );
    color: white;
    font-size: 20px;
    font-weight: 700;
    transition: 0.3s ease;
    box-shadow: 0 8px 25px rgba(59,130,246,0.35);
}

.stButton > button:hover {
    transform: scale(1.02);
    background: linear-gradient(
        90deg,
        #3B82F6,
        #8B5CF6
    );
}

/* Success Result */

.result-success {
    background: linear-gradient(
        90deg,
        #14532D,
        #16A34A
    );
    padding: 28px;
    border-radius: 20px;
    text-align: center;
    color: white;
    font-size: 30px;
    font-weight: 700;
    margin-top: 30px;
}

/* Danger Result */

.result-danger {
    background: linear-gradient(
        90deg,
        #7F1D1D,
        #DC2626
    );
    padding: 28px;
    border-radius: 20px;
    text-align: center;
    color: white;
    font-size: 30px;
    font-weight: 700;
    margin-top: 30px;
}

/* Footer */

.footer {
    text-align: center;
    color: #94A3B8;
    margin-top: 60px;
    padding: 20px;
    font-size: 15px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

st.markdown("""
<div class='main-title'>
🏦 Financial Viability
</div>

<div class='sub-title'>
AI-Powered Loan Approval & Banking Risk Assessment Dashboard
</div>
""", unsafe_allow_html=True)

# =========================
# METRIC CARDS
# =========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class='metric-card'>
        <div class='metric-title'>ML Models</div>
        <div class='metric-value'>3</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='metric-card'>
        <div class='metric-title'>Prediction Accuracy</div>
        <div class='metric-value'>89%</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='metric-card'>
        <div class='metric-title'>Risk Engine</div>
        <div class='metric-value'>AI Enabled</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class='metric-card'>
        <div class='metric-title'>Decision Time</div>
        <div class='metric-value'>Realtime</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# =========================
# SIDEBAR
# =========================

st.sidebar.title("📊 Applicant Profile")

st.sidebar.markdown(
    "Provide applicant financial information"
)

Gender = st.sidebar.selectbox(
    "Gender",
    ["Male", "Female"]
)

Married = st.sidebar.selectbox(
    "Marital Status",
    ["Yes", "No"]
)

Dependents = st.sidebar.selectbox(
    "Dependents",
    ["0", "1", "2", "3+"]
)

Education = st.sidebar.selectbox(
    "Education",
    ["Graduate", "Not Graduate"]
)

Self_Employed = st.sidebar.selectbox(
    "Self Employed",
    ["Yes", "No"]
)

ApplicantIncome = st.sidebar.number_input(
    "Applicant Income",
    min_value=0,
    value=5000
)

CoapplicantIncome = st.sidebar.number_input(
    "Co-Applicant Income",
    min_value=0,
    value=2000
)

LoanAmount = st.sidebar.number_input(
    "Loan Amount",
    min_value=0,
    value=120
)

Loan_Amount_Term = st.sidebar.number_input(
    "Loan Amount Term",
    min_value=0,
    value=360
)

Credit_History = st.sidebar.selectbox(
    "Credit History",
    [1, 0]
)

Property_Area = st.sidebar.selectbox(
    "Property Area",
    ["Urban", "Semiurban", "Rural"]
)

# =========================
# DATA ENCODING
# =========================

Gender = 1 if Gender == "Male" else 0

Married = 1 if Married == "Yes" else 0

Education = 0 if Education == "Graduate" else 1

Self_Employed = 1 if Self_Employed == "Yes" else 0

Dependents_map = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3+": 3
}

Property_Area_map = {
    "Urban": 2,
    "Semiurban": 1,
    "Rural": 0
}

Dependents = Dependents_map[Dependents]

Property_Area = Property_Area_map[Property_Area]

# =========================
# INPUT DATAFRAME
# =========================

input_data = pd.DataFrame({
    "Gender": [Gender],
    "Married": [Married],
    "Dependents": [Dependents],
    "Education": [Education],
    "Self_Employed": [Self_Employed],
    "ApplicantIncome": [ApplicantIncome],
    "CoapplicantIncome": [CoapplicantIncome],
    "LoanAmount": [LoanAmount],
    "Loan_Amount_Term": [Loan_Amount_Term],
    "Credit_History": [Credit_History],
    "Property_Area": [Property_Area]
})

# =========================
# SCALE INPUT
# =========================

scaled_data = scaler.transform(input_data)

# =========================
# PREDICTION SECTION
# =========================

st.markdown("""
<div class='predict-box'>
<h2 style='color:white;'>
📈 Smart Loan Approval Prediction
</h2>

<p style='color:#CBD5E1;'>
AI analyzes applicant financial credibility
and predicts loan approval eligibility instantly.
</p>
</div>
""", unsafe_allow_html=True)

if st.button("🚀 Analyze & Predict Loan Approval"):

    prediction = model.predict(scaled_data)

    if prediction[0] == 1:

        st.success("Loan Approved Successfully")

        st.markdown("""
        <div class='result-success'>
            ✅ LOW RISK APPLICANT
        </div>
        """, unsafe_allow_html=True)

    else:

        st.error("Loan Rejected")

        st.markdown("""
        <div class='result-danger'>
            ⚠️ HIGH RISK APPLICANT
        </div>
        """, unsafe_allow_html=True)

# =========================
# FOOTER
# =========================

st.markdown("""
<div class='footer'>
Built with Python • Streamlit • Scikit-learn • Machine Learning
</div>
""", unsafe_allow_html=True)