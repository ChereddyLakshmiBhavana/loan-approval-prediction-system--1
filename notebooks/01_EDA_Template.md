# EDA Template

This template can be used for exploratory data analysis in notebooks.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from src.data.loader import DataLoader

# Load data
loader = DataLoader()
df = loader.load_csv('loan_data.csv')

# Basic Information
print("Dataset shape:", df.shape)
print("\nFirst few rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nBasic statistics:")
print(df.describe())

# Data Visualization
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Distribution of target variable
df['Loan_Status'].value_counts().plot(kind='bar', ax=axes[0, 0])
axes[0, 0].set_title('Loan Status Distribution')

# Income distribution
axes[0, 1].hist(df['ApplicantIncome'], bins=30)
axes[0, 1].set_title('Applicant Income Distribution')

# Loan amount distribution
axes[1, 0].hist(df['LoanAmount'], bins=30)
axes[1, 0].set_title('Loan Amount Distribution')

# Categorical variables
sns.countplot(x='Gender', hue='Loan_Status', data=df, ax=axes[1, 1])
axes[1, 1].set_title('Loan Status by Gender')

plt.tight_layout()
plt.show()

# Correlation analysis
correlation = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Feature Correlation Matrix')
plt.show()
```

## Key EDA Questions

1. What is the distribution of approved vs rejected loans?
2. How do income levels vary across the dataset?
3. What is the relationship between credit history and loan approval?
4. Are there significant differences by gender, education, or location?
5. What patterns exist in loan amounts and terms?
6. Which features have the strongest correlation with loan approval?
