# API Documentation

## Overview

The Loan Approval Prediction System provides a REST API for making loan approval predictions in real-time and batch mode.

## Base URL

```
http://localhost:5000/api
```

## Endpoints

### 1. Health Check

**Endpoint**: `/health`
**Method**: `GET`

Check if the API is running and healthy.

**Response**:
```json
{
  "status": "healthy",
  "service": "Loan Approval Prediction API",
  "version": "1.0.0"
}
```

### 2. Single Prediction

**Endpoint**: `/predict`
**Method**: `POST`

Predict loan approval status for a single applicant.

**Request Body**:
```json
{
  "loan_id": "LOAN123",
  "ApplicantIncome": 5000,
  "CoapplicantIncome": 1500,
  "LoanAmount": 100000,
  "Loan_Amount_Term": 360,
  "Credit_History": 1,
  "Gender": "Male",
  "Married": "Yes",
  "Education": "Graduate",
  "Self_Employed": "No",
  "Property_Area": "Urban"
}
```

**Response**:
```json
{
  "loan_id": "LOAN123",
  "approval_status": "Approved",
  "approval_probability": 0.85,
  "confidence": "High"
}
```

**Status Codes**:
- `200`: Success
- `400`: Invalid request
- `500`: Server error

### 3. Batch Predictions

**Endpoint**: `/batch-predict`
**Method**: `POST`

Process multiple loan applications in batch mode.

**Request**: 
- Content-Type: `multipart/form-data`
- File field: `file` (CSV format)

**CSV Format Example**:
```csv
loan_id,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Gender,Married,Education,Self_Employed,Property_Area
LOAN001,5000,1500,100000,360,1,Male,Yes,Graduate,No,Urban
LOAN002,4000,0,80000,180,1,Female,No,Graduate,Yes,Rural
```

**Response**:
```json
{
  "message": "Batch prediction completed",
  "processed_records": 100,
  "results_file": "predictions_20240101_120000.csv"
}
```

### 4. Model Information

**Endpoint**: `/model-info`
**Method**: `GET`

Get information about the deployed model.

**Response**:
```json
{
  "model_name": "Neural Network",
  "model_type": "TensorFlow",
  "version": "1.0",
  "accuracy": 0.87,
  "precision": 0.85,
  "recall": 0.83,
  "f1_score": 0.84
}
```

## Error Handling

All error responses follow this format:

```json
{
  "error": "Error message describing what went wrong"
}
```

**Common Errors**:

| Status | Message | Cause |
|--------|---------|-------|
| 400 | No data provided | Missing JSON body in request |
| 404 | Endpoint not found | Invalid endpoint URL |
| 500 | Internal server error | Server-side error during processing |

## Example Usage

### Python

```python
import requests
import json

# Single prediction
url = "http://localhost:5000/predict"
data = {
    "ApplicantIncome": 5000,
    "CoapplicantIncome": 1500,
    "LoanAmount": 100000,
    "Loan_Amount_Term": 360,
    "Credit_History": 1,
    "Gender": "Male"
}

response = requests.post(url, json=data)
print(response.json())

# Batch prediction
with open('applicants.csv', 'rb') as f:
    files = {'file': f}
    response = requests.post("http://localhost:5000/batch-predict", files=files)
    print(response.json())
```

### cURL

```bash
# Health check
curl http://localhost:5000/health

# Single prediction
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"ApplicantIncome": 5000, "CoapplicantIncome": 1500}'

# Batch prediction
curl -X POST http://localhost:5000/batch-predict \
  -F "file=@applicants.csv"
```

## Rate Limiting

Currently, no rate limiting is implemented. This should be added for production deployments.

## Authentication

Currently, no authentication is required. Add JWT or API key authentication for production.

## CORS Policy

CORS is enabled for all origins. Update in production for security.

## Performance

- Single prediction: ~50-100ms
- Batch prediction: ~1-2 seconds per 100 records

## Deployment

To deploy the API:

```bash
# Development
python src/api/app.py

# Production (using gunicorn)
gunicorn -w 4 -b 0.0.0.0:5000 src.api.app:app
```

## Future Enhancements

- Add authentication/authorization
- Implement rate limiting
- Add request caching
- Implement async batch processing
- Add prediction explanation (SHAP, LIME)
- GraphQL endpoint option
