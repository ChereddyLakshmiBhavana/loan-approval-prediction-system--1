# Data Dictionary

## Dataset Overview

This document describes all fields in the loan approval dataset.

## Applicant Features

### Demographic Information

| Field | Type | Description | Values |
|-------|------|-------------|--------|
| Loan_ID | String | Unique loan identifier | LOANXXXXX |
| Gender | Categorical | Applicant gender | Male, Female |
| Age | Integer | Age of the applicant | 18-80 years |
| Married | Categorical | Marital status | Yes, No |
| Dependents | Categorical | Number of dependents | 0, 1, 2, 3+ |
| Education | Categorical | Education level | Graduate, Not Graduate |
| Self_Employed | Categorical | Self-employment status | Yes, No |

### Financial Information

| Field | Type | Description | Values |
|-------|------|-------------|--------|
| ApplicantIncome | Integer | Applicant's annual income | In rupees |
| CoapplicantIncome | Float | Co-applicant's annual income | In rupees (0 if none) |
| LoanAmount | Float | Loan amount requested | In thousands |
| Loan_Amount_Term | Integer | Loan repayment period | In months |

### Credit Information

| Field | Type | Description | Values |
|-------|------|-------------|--------|
| Credit_History | Binary | Credit history status | 1 (Good), 0 (Bad/Missing) |

### Property Information

| Field | Type | Description | Values |
|-------|------|-------------|--------|
| Property_Area | Categorical | Area where property is located | Urban, Rural, Semi-urban |

## Target Variable

| Field | Type | Description | Values |
|-------|------|-------------|--------|
| Loan_Status | Binary | Loan approval status | 1 (Approved), 0 (Not Approved) |

## Data Statistics

- **Total Records**: ~600 (varies with dataset)
- **Missing Values**: Present in some fields (handled in preprocessing)
- **Class Distribution**: Imbalanced (more approvals than rejections)
- **Features**: 11 input features + 1 target variable

## Preprocessing Steps

1. **Missing Value Imputation**
   - Numeric fields: Mean imputation
   - Categorical fields: Mode imputation

2. **Feature Scaling**
   - StandardScaler for numeric features
   - Maintains zero mean and unit variance

3. **Categorical Encoding**
   - One-hot encoding for categorical variables
   - Creates binary columns for each category

4. **Outlier Detection**
   - IQR-based outlier detection
   - Optional removal or capping

## Feature Engineering

### Derived Features

- `Total_Income`: Sum of ApplicantIncome and CoapplicantIncome
- `Loan_to_Income_Ratio`: LoanAmount / Total_Income
- `Income_per_Dependent`: Total_Income / (Dependents + 1)
- `Monthly_Income`: Total_Income / 12
- `Monthly_Payment`: LoanAmount / (Loan_Amount_Term + 1)

### Feature Selection

Top features by importance:
1. Credit_History
2. LoanAmount
3. Total_Income
4. ApplicantIncome
5. Property_Area

## Data Quality Issues

### Missing Values
- Gender: ~5% missing
- Dependents: ~1% missing
- Credit_History: ~5% missing
- LoanAmount: ~20% missing
- Loan_Amount_Term: ~0.5% missing

### Outliers
- ApplicantIncome: Upper quartile may have outliers
- CoapplicantIncome: High concentration at 0

### Imbalance
- Approved: ~68%
- Rejected: ~32%
- Handled using class weights or sampling techniques

## Data Split

- **Training Set**: 70% of data
- **Validation Set**: 15% of data
- **Test Set**: 15% of data

Random seed: 42 for reproducibility
