import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset

df = pd.read_csv('data/loan_data.csv')

# Loan status count

sns.countplot(x='Loan_Status', data=df)
plt.title('Loan Approval Distribution')
plt.show()

# Income distribution

sns.histplot(df['ApplicantIncome'], kde=True)
plt.title('Applicant Income Distribution')
plt.show()

# Credit history analysis

sns.countplot(x='Credit_History', hue='Loan_Status', data=df)