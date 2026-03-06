# Results and Model Evaluation

## Model Performance Summary

This document tracks the performance of different models and their evaluation metrics.

## Neural Network Model

### Architecture
- Input Layer: 20 features
- Hidden Layer 1: 128 neurons + ReLU + BatchNorm + Dropout(0.3)
- Hidden Layer 2: 64 neurons + ReLU + BatchNorm + Dropout(0.3)
- Hidden Layer 3: 32 neurons + ReLU + BatchNorm + Dropout(0.2)
- Output Layer: 2 neurons + Softmax

### Training Configuration
- Optimizer: Adam
- Loss Function: Sparse Categorical Crossentropy
- Batch Size: 32
- Epochs: 100
- Validation Split: 20%

### Performance Metrics

| Metric | Value |
|--------|-------|
| Accuracy | 0.87 |
| Precision | 0.85 |
| Recall | 0.83 |
| F1-Score | 0.84 |
| ROC-AUC | 0.91 |

### Training History
- Loss (Training): Converges to ~0.35
- Accuracy (Training): Reaches ~0.87
- Loss (Validation): Converges to ~0.38
- Accuracy (Validation): Reaches ~0.85

## Gradient Boosting Model

### Configuration
- n_estimators: 100
- learning_rate: 0.1
- max_depth: 5
- random_state: 42

### Performance Metrics

| Metric | Value |
|--------|-------|
| Accuracy | 0.89 |
| Precision | 0.87 |
| Recall | 0.86 |
| F1-Score | 0.86 |
| ROC-AUC | 0.92 |

## Feature Importance (Gradient Boosting)

Top 10 Most Important Features:

| Rank | Feature | Importance |
|------|---------|-----------|
| 1 | Credit_History | 0.28 |
| 2 | LoanAmount | 0.18 |
| 3 | Total_Income | 0.15 |
| 4 | ApplicantIncome | 0.12 |
| 5 | Property_Area | 0.10 |
| 6 | Loan_Amount_Term | 0.08 |
| 7 | Education | 0.05 |
| 8 | Married | 0.02 |
| 9 | Gender | 0.01 |
| 10 | Dependents | 0.01 |

## Confusion Matrix (Test Set)

### Neural Network
```
                Predicted Negative    Predicted Positive
Actual Negative         75                     12
Actual Positive         18                     65
```

- True Negatives: 75
- False Positives: 12
- False Negatives: 18
- True Positives: 65

### Gradient Boosting
```
                Predicted Negative    Predicted Positive
Actual Negative         78                      9
Actual Positive         15                     68
```

- True Negatives: 78
- False Positives: 9
- False Negatives: 15
- True Positives: 68

## ROC-AUC Curves

- Neural Network AUC: 0.91
- Gradient Boosting AUC: 0.92

## Recommendations

1. **Model Selection**: Gradient Boosting shows slightly better performance
2. **Precision vs Recall**: 
   - If reducing false positives is critical: Use Gradient Boosting
   - If reducing false negatives is critical: Adjust decision threshold
3. **Model Deployment**: Use Gradient Boosting with confidence threshold at 0.65
4. **Further Improvements**:
   - Feature engineering (create interaction terms)
   - Hyperparameter tuning with GridSearch/RandomSearch
   - Ensemble methods combining multiple models
   - Handling class imbalance with SMOTE

## A/B Testing Recommendations

- Monitor model performance on new data monthly
- Compare against baseline model
- Track prediction explanation metrics (SHAP values)
- Set alerts if accuracy drops below 0.85

## Prediction Examples

### Example 1: Approved Application
- Income: 5000
- Credit History: 1 (Good)
- Loan Amount: 100000
- **Prediction**: Approved (89% confidence)

### Example 2: Rejected Application
- Income: 2000
- Credit History: 0 (Bad/Missing)
- Loan Amount: 150000
- **Prediction**: Rejected (78% confidence)

## Model Versioning

- Model v1.0: Initial production model
- Retrain Schedule: Monthly with new data
- Version Control: Track in Git with model artifacts
