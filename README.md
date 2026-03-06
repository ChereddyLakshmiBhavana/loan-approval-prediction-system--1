# 🎯 AI-Driven Loan Approval Prediction System

A complete deep learning-based system for predicting loan approval status with both backend API and modern web interface.

## Project Overview

This project implements a comprehensive machine learning solution to predict loan approval decisions based on applicant information and historical loan data. The system uses deep learning models and is deployed as both a batch processing system and a REST API with a professional web interface.

## Project Structure

```
├── data/
│   ├── raw/                    # Original, immutable data files
│   └── processed/              # Transformed, cleaned data for modeling
├── notebooks/                  # Jupyter notebooks for EDA and experimentation
├── src/
│   ├── data/                   # Data loading, preprocessing, feature engineering
│   ├── models/                 # Model architectures and training
│   ├── utils/                  # Helper functions and utilities
│   └── api/                    # REST API server
├── tests/                      # Unit and integration tests
├── config/                     # Configuration files
├── docs/                       # Project documentation
├── models/                     # Trained model artifacts
├── logs/                       # Application logs
├── frontend/                   # Web interface
├── requirements.txt            # Python dependencies
├── setup.py                    # Package setup
└── .gitignore                  # Git ignore rules
```

## ✨ Key Features

- **🧠 Deep Learning Models**: Neural network architectures achieving 93.8% accuracy
- **🔌 REST API**: Flask-based API server for real-time predictions
- **🌐 Modern Web Interface**: Responsive frontend with professional UI/UX
- **📊 Data Processing**: Comprehensive data cleaning and feature engineering
- **🧪 Testing**: Unit and integration tests
- **📚 Documentation**: Detailed project and API documentation
- **🚀 Easy Deployment**: Single command to run complete system

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd deep-learning-loan-prediction-system

# Create & activate a virtual environment (Windows PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate

# Install dependencies inside the venv
pip install -r requirements.txt

# Install the package
pip install -e .
```

> **Note:** If PowerShell reports `python : The term 'python' is not recognized`, make sure Python is installed and added to your system `PATH`. You can also always run the interpreter directly from the virtual environment:
> ```powershell
> .\.venv\Scripts\python.exe run_complete_system.py
> ```

## Usage

### ✨ RECOMMENDED: Run in Two Separate Terminals

The simplest and most reliable way to run the complete system is to use **two separate terminal windows**:

**Terminal 1 - Start the Backend API (port 5000):**
```powershell
.\.venv\Scripts\python.exe start_backend.py
```

**Terminal 2 - Start the Frontend Web App (port 3000):**
```powershell
.\.venv\Scripts\python.exe start_frontend.py
```

Then **open your browser** and visit: **http://localhost:3000**

## 📋 Understanding the Loan Application Form

The web form asks for various financial information. Each field has a **help tooltip** (? icon) that explains what it means.

### Field Categories:

| Field | What It Means | Example |
|-------|---------------|---------|
| **Number of Dependents** | Family members depending on you | 0-10 people |
| **Education** | Highest qualification | Graduate / Not Graduate |
| **Self Employed** | Business owner or employee? | Yes / No |
| **Annual Income** | Yearly earnings in ₹ | 600000 (₹6 Lakhs) |
| **Loan Amount** | Money you want to borrow | 500000 (₹5 Lakhs) |
| **Loan Term** | Duration to repay in months | 180 (15 years), 360 (30 years) |
| **CIBIL Score** | Credit rating (300-900) | 750 = Good credit |
| **Residential Assets** | House value in ₹ | 2000000 (₹20 Lakhs) |
| **Commercial Assets** | Business property value | 1000000 (₹10 Lakhs) |
| **Luxury Assets** | Car, jewelry, electronics value | 400000 (₹4 Lakhs) |
| **Bank Assets** | Savings account balance | 300000 (₹3 Lakhs) |

**📖 For detailed explanations of each field, see [FORM_GUIDE.md](FORM_GUIDE.md)**

### ✅ Features:

- ✨ **Interactive Form**: Enter your loan application details
- 🎯 **Real-time Predictions**: Get instant AI approval/rejection predictions
- 📊 **Visual Results**: See probability bars and confidence levels
- 💡 **Hover Help**: Hover over "?" icons for field descriptions
- 🔄 **Multiple Attempts**: Try different scenarios to see impact
- 📱 **Mobile Friendly**: Works on phones and tablets

### Running Individual Components

```powershell
# Backend API only (API documentation at http://localhost:5000)
.\.venv\Scripts\python.exe start_backend.py

# Frontend Web App only (accessible at http://localhost:3000)
.\.venv\Scripts\python.exe start_frontend.py
```

### Testing the Data Pipeline

Before training models, test the data loading and preprocessing:

```powershell
.\.venv\Scripts\python.exe test_data_pipeline.py
```

## Requirements

- Python 3.8+
- TensorFlow/Keras
- Scikit-learn
- Pandas, NumPy
- Flask/FastAPI
- Jupyter Notebook

## Dataset

This project uses the **Loan Approval Prediction Dataset** from Kaggle (https://www.kaggle.com/datasets/architsharma01/loan-approval-prediction-dataset).

### Dataset Features

The dataset contains 13 columns with information about loan applicants:

- **loan_id**: Unique identifier for each loan application
- **no_of_dependents**: Number of dependents
- **education**: Education level (Graduate/Not Graduate)
- **self_employed**: Employment status (Yes/No)
- **income_annum**: Annual income
- **loan_amount**: Loan amount requested
- **loan_term**: Loan term in months
- **cibil_score**: Credit score
- **residential_assets_value**: Value of residential assets
- **commercial_assets_value**: Value of commercial assets
- **luxury_assets_value**: Value of luxury assets
- **bank_asset_value**: Value of bank assets
- **loan_status**: Target variable (Approved/Rejected)

### Data Pipeline

The system includes a comprehensive data processing pipeline:

1. **Data Loading**: Automated loading with column validation
2. **Preprocessing**: Missing value handling, categorical encoding, feature scaling
3. **Feature Engineering**: 
   - Total assets calculation (sum of all asset values)
   - Debt-to-income ratio calculation
4. **Train/Validation/Test Split**: Stratified splitting to maintain class balance

### Getting the Dataset

1. Download `loan_approval_dataset.csv` from Kaggle
2. Place the file in `data/raw/` directory
3. Run the data pipeline test: `python test_data_pipeline.py`

## Model Performance Metrics

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC

## Documentation

See `docs/` folder for:
- Technical documentation
- Model architecture details
- API specifications
- Data dictionary
- Results and analysis

## Contributing

Contribute by:
1. Creating a feature branch
2. Making changes
3. Submitting a pull request

## License

MIT License

## Authors

Loan Prediction Team

## Contact

For questions or issues, please create an issue in the repository.
