# 🏦 Loan Approval Prediction System

A Machine Learning-powered web application that predicts whether a loan application is likely to be approved based on applicant information. The project uses data analytics, machine learning, and an interactive Streamlit dashboard to assist in loan eligibility assessment.

---

## 📌 Project Overview

Financial institutions receive thousands of loan applications every day. Manually reviewing applications can be time-consuming and prone to inconsistencies.

This project automates the loan approval process by leveraging Machine Learning algorithms to analyze applicant information and predict loan approval status.

The application provides:

- Real-time loan approval prediction
- Risk assessment of applicants
- User-friendly web interface
- Data-driven decision support

---

## 🎯 Objectives

- Analyze loan applicant data.
- Identify factors influencing loan approval.
- Build a machine learning model for prediction.
- Deploy an interactive dashboard using Streamlit.
- Provide quick and reliable loan eligibility assessment.

---

## 🛠️ Technology Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-Learn |
| Model Serialization | Pickle |
| Web Application | Streamlit |
| Version Control | Git & GitHub |

---

## 📂 Project Structure

```text
loan-approval-ml-project/
│
├── app.py                 # Streamlit Application
├── analysis.py            # Exploratory Data Analysis
├── train_model.py         # Model Training Script
├── loan_data.csv          # Dataset
├── model.pkl              # Trained ML Model
├── scaler.pkl             # Feature Scaler
├── requirements.txt       # Project Dependencies
├── .gitignore             # Git Ignore Rules
└── README.md              # Project Documentation
```

---

## 📊 Dataset Features

The model uses applicant details such as:

- Applicant Income
- Co-applicant Income
- Loan Amount
- Loan Term
- Credit History
- Education
- Marital Status
- Gender
- Property Area
- Dependents

These features are used to determine loan eligibility.

---

## 🔍 Exploratory Data Analysis (EDA)

The project includes:

- Missing Value Analysis
- Distribution Analysis
- Correlation Analysis
- Feature Engineering
- Data Cleaning and Transformation

Key insights help improve model accuracy and understand applicant behavior.

---

## 🤖 Machine Learning Workflow

### Data Preprocessing

- Handling Missing Values
- Encoding Categorical Variables
- Feature Scaling
- Data Splitting

### Model Training

The machine learning model is trained using Scikit-Learn and optimized for loan approval prediction.

### Model Evaluation

Performance is evaluated using:

- Accuracy Score
- Confusion Matrix
- Classification Report

---

## 🚀 Application Features

### Loan Approval Prediction

Users can enter applicant information and instantly receive:

- Loan Approval Status
- Risk Classification
- Decision Recommendation

### Risk Assessment

The application categorizes applicants into:

- Low Risk
- Medium Risk
- High Risk

based on prediction confidence and applicant profile.


 ▶️ Installation & Setup
 Clone Repository
 bash
git clone https://github.com/Ananthsairam/loan-approval-ml-project.git
```

### Navigate to Project Folder

```bash
cd loan-approval-ml-project
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux/Mac

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

After launching:

```text
Local URL: http://localhost:8501
```

Open the URL in your browser.

---

## 📈 Sample Workflow

1. Enter applicant details.
2. Click Predict.
3. Model processes the inputs.
4. Prediction is displayed.
5. Risk level is generated.
6. Loan recommendation is shown.

---

## 📌 Future Enhancements

- Multiple Machine Learning Models Comparison
- Hyperparameter Optimization
- Feature Importance Dashboard
- Cloud Deployment
- Loan Default Prediction
- Database Integration
- User Authentication

---

## 📚 Learning Outcomes

Through this project, the following concepts were applied:

- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Machine Learning Modeling
- Model Deployment
- Streamlit Dashboard Development
- Git & GitHub Version Control

---

## 👨‍💻 Author

**Ananthsairam Goud**

Data Analytics & Machine Learning Enthusiast

GitHub:
https://github.com/Ananthsairam

---

## 📄 License

This project is developed for educational and portfolio purposes.
