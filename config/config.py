"""Configuration settings for the Loan Approval Prediction System"""

import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Data paths
DATA_RAW_PATH = BASE_DIR / "data" / "raw"
DATA_PROCESSED_PATH = BASE_DIR / "data" / "processed"

# Model paths
MODEL_DIR = BASE_DIR / "models"
MODEL_WEIGHTS_PATH = MODEL_DIR / "model_weights.h5"
MODEL_PKL_PATH = MODEL_DIR / "model.pkl"

# Log paths
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "app.log"

# API Configuration
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", 5000))
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"

# Database Configuration (Optional)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///app.db")

# Model Configuration
MODEL_NAME = "neural_network"
MODEL_TYPE = "tensorflow"
INPUT_SHAPE = (None, 20)  # Adjust based on number of features
OUTPUT_CLASSES = 2  # Binary classification: Approved/Rejected

# Training Configuration
BATCH_SIZE = 32
EPOCHS = 100
VALIDATION_SPLIT = 0.2
TEST_SPLIT = 0.2
RANDOM_STATE = 42

# Feature Configuration
NUMERICAL_FEATURES = [
    'ApplicantIncome',
    'CoapplicantIncome',
    'LoanAmount',
    'Loan_Amount_Term',
    'Credit_History'
]

CATEGORICAL_FEATURES = [
    'Gender',
    'Married',
    'Education',
    'Self_Employed',
    'Property_Area'
]

# Preprocessing Configuration
SCALING_METHOD = "standard"  # standard, minmax, robust
ENCODING_METHOD = "onehot"   # onehot, label

# Performance thresholds
MIN_ACCURACY = 0.85
MIN_PRECISION = 0.80
MIN_RECALL = 0.75
MIN_F1_SCORE = 0.80

# Logging
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Create necessary directories
for dir_path in [DATA_RAW_PATH, DATA_PROCESSED_PATH, MODEL_DIR, LOG_DIR]:
    dir_path.mkdir(parents=True, exist_ok=True)
