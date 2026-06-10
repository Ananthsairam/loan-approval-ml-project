import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load Dataset
df = pd.read_csv('loan_data.csv')

print("Dataset Loaded Successfully")
print(df.head())

# Remove spaces from column names
df.columns = df.columns.str.strip()

print("\nDataset Columns:")
print(df.columns)

# Fill missing values
df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])

df['Married'] = df['Married'].fillna(df['Married'].mode()[0])

df['Dependents'] = df['Dependents'].fillna(df['Dependents'].mode()[0])

df['Self_Employed'] = df['Self_Employed'].fillna(
    df['Self_Employed'].mode()[0]
)

df['LoanAmount'] = df['LoanAmount'].fillna(
    df['LoanAmount'].mean()
)

df['Loan_Amount_Term'] = df['Loan_Amount_Term'].fillna(
    df['Loan_Amount_Term'].mean()
)

df['Credit_History'] = df['Credit_History'].fillna(
    df['Credit_History'].mode()[0]
)

# Drop Loan_ID
df.drop('Loan_ID', axis=1, inplace=True)

# Encode categorical columns
label_encoder = LabelEncoder()

categorical_columns = [
    'Gender',
    'Married',
    'Dependents',
    'Education',
    'Self_Employed',
    'Property_Area',
    'Loan_Status'
]

for col in categorical_columns:
    df[col] = label_encoder.fit_transform(df[col])

# Features and Target
X = df.drop('Loan_Status', axis=1)

y = df['Loan_Status']

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Feature Scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

# Models
models = {
    'Logistic Regression': LogisticRegression(),
    'Random Forest': RandomForestClassifier(),
    'SVM': SVC()
}

best_model = None
best_accuracy = 0

# Train Models
for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f"{name} Accuracy: {accuracy:.2f}")

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model

# Save Model and Scaler
joblib.dump(best_model, 'model.pkl')

joblib.dump(scaler, 'scaler.pkl')

print("\nBest Model Saved Successfully")

print(f"Best Accuracy: {best_accuracy:.2f}")