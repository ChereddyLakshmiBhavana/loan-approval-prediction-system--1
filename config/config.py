"""Configuration settings for the Loan Approval Prediction System"""

import os
from pathlib import Path


def _get_bool_env(name: str, default: bool) -> bool:
    """Parse boolean environment variables safely."""
    return os.getenv(name, str(default)).strip().lower() in {"1", "true", "yes", "on"}


def _get_list_env(name: str, default: str = ""):
    """Return a comma-separated env var as a clean list."""
    raw_value = os.getenv(name, default)
    return [item.strip() for item in raw_value.split(",") if item.strip()]

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
DEBUG_MODE = _get_bool_env("DEBUG_MODE", False)
ENVIRONMENT = os.getenv("ENVIRONMENT", "development").strip().lower()

# CORS configuration
ALLOWED_ORIGINS = _get_list_env(
    "ALLOWED_ORIGINS",
    "http://localhost:3000,http://127.0.0.1:3000"
)

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

# Feature Configuration for Loan Approval Dataset
NUMERICAL_FEATURES = [
    'no_of_dependents',
    'income_annum',
    'loan_amount',
    'loan_term',
    'cibil_score',
    'residential_assets_value',
    'commercial_assets_value',
    'luxury_assets_value',
    'bank_asset_value',
    'total_assets_value',  # Engineered feature
    'debt_to_income_ratio'  # Engineered feature
]

CATEGORICAL_FEATURES = [
    'education',
    'self_employed'
]

# Target Configuration
TARGET_COLUMN = 'loan_status'
TARGET_CLASSES = ['Rejected', 'Approved']  # 0 = Rejected, 1 = Approved

# Dataset Configuration
DATASET_FILENAME = 'loan_approval_dataset.csv'
EXPECTED_COLUMNS = [
    'loan_id', 'no_of_dependents', 'education', 'self_employed',
    'income_annum', 'loan_amount', 'loan_term', 'cibil_score',
    'residential_assets_value', 'commercial_assets_value',
    'luxury_assets_value', 'bank_asset_value', 'loan_status'
]

# Model Configuration
INPUT_SHAPE = (None, len(NUMERICAL_FEATURES) + len(CATEGORICAL_FEATURES))  # Adjust based on encoded features

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
