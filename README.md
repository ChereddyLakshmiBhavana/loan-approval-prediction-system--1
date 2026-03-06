# AI-Driven Loan Approval Prediction System

A deep learning-based system for predicting loan approval status using machine learning models.

## Project Overview

This project implements a comprehensive machine learning solution to predict loan approval decisions based on applicant information and historical loan data. The system uses deep learning models and is deployed as both a batch processing system and a REST API.

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

## Key Features

- **Data Processing**: Comprehensive data cleaning and feature engineering
- **Deep Learning Models**: Neural network architectures for prediction
- **API Server**: Flask/FastAPI REST API for real-time predictions
- **Web Interface**: User-friendly frontend for loan prediction
- **Testing**: Unit and integration tests
- **Documentation**: Detailed project and API documentation

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd deep-learning-loan-prediction-system

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```

## Usage

### Testing Data Pipeline

Before training, test the data loading and preprocessing pipeline:

```bash
python test_data_pipeline.py
```

### Training the Model

Train models using the integrated data pipeline:

```bash
# Train neural network (default)
python src/models/train.py

# Train gradient boosting model
python src/models/train.py --model gradient_boosting

# Train with custom dataset
python src/models/train.py --data path/to/your/dataset.csv
```

### Making Predictions (API)

```bash
python src/api/app.py
```

Visit `http://localhost:5000` for the API documentation.

### Web Interface

```bash
cd frontend
npm install
npm start
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
