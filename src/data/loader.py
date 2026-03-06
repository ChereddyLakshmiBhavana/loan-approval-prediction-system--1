"""Data loading and I/O operations"""

import pandas as pd
import numpy as np
from pathlib import Path
import sys
from typing import Optional, Tuple

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from config.config import DATA_RAW_PATH, DATA_PROCESSED_PATH

class DataLoader:
    """Load data from various sources"""
    
    def __init__(self):
        self.raw_path = DATA_RAW_PATH
        self.processed_path = DATA_PROCESSED_PATH
    
    def load_csv(self, filename, filepath=None):
        """Load data from CSV file"""
        if filepath is None:
            filepath = self.raw_path / filename
        
        return pd.read_csv(filepath)
    
    def save_processed_data(self, df, filename):
        """Save processed data to disk"""
        filepath = self.processed_path / filename
        df.to_csv(filepath, index=False)
        print(f"Data saved to {filepath}")
    
    def load_processed_data(self, filename):
        """Load processed data from disk"""
        filepath = self.processed_path / filename
        return pd.read_csv(filepath)
    
    def load_loan_approval_dataset(self, filename: str = "loan_approval_dataset.csv") -> pd.DataFrame:
        """
        Load the Kaggle loan approval prediction dataset
        
        Expected columns:
        - loan_id: Unique identifier for each loan application
        - no_of_dependents: Number of dependents
        - education: Education level (Graduate/Not Graduate)
        - self_employed: Employment status (Yes/No)
        - income_annum: Annual income
        - loan_amount: Loan amount requested
        - loan_term: Loan term in months
        - cibil_score: Credit score
        - residential_assets_value: Value of residential assets
        - commercial_assets_value: Value of commercial assets
        - luxury_assets_value: Value of luxury assets
        - bank_asset_value: Value of bank assets
        - loan_status: Target variable (Approved/Rejected)
        """
        filepath = self.raw_path / filename
        
        if not filepath.exists():
            raise FileNotFoundError(f"Dataset file not found: {filepath}")
        
        df = pd.read_csv(filepath)
        
        # Validate expected columns
        expected_columns = [
            'loan_id', 'no_of_dependents', 'education', 'self_employed',
            'income_annum', 'loan_amount', 'loan_term', 'cibil_score',
            'residential_assets_value', 'commercial_assets_value',
            'luxury_assets_value', 'bank_asset_value', 'loan_status'
        ]
        
        missing_columns = [col for col in expected_columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Missing expected columns: {missing_columns}")
        
        print(f"Successfully loaded loan approval dataset with {len(df)} records")
        print(f"Columns: {list(df.columns)}")
        
        return df
    
    def split_features_target(self, df: pd.DataFrame, target_col: str = 'loan_status') -> Tuple[pd.DataFrame, pd.Series]:
        """
        Split dataset into features and target variable
        
        Args:
            df: Input dataframe
            target_col: Name of target column
            
        Returns:
            Tuple of (features_df, target_series)
        """
        if target_col not in df.columns:
            raise ValueError(f"Target column '{target_col}' not found in dataframe")
        
        features = df.drop(columns=[target_col])
        target = df[target_col]
        
        return features, target
    
    def get_dataset_info(self, df: pd.DataFrame) -> dict:
        """Get basic information about the dataset"""
        info = {
            'shape': df.shape,
            'columns': list(df.columns),
            'dtypes': df.dtypes.to_dict(),
            'missing_values': df.isnull().sum().to_dict(),
            'target_distribution': df['loan_status'].value_counts().to_dict() if 'loan_status' in df.columns else None
        }
        
        return info

def load_training_data(csv_path):
    """Load training dataset"""
    df = pd.read_csv(csv_path)
    return df

def load_test_data(csv_path):
    """Load test dataset"""
    df = pd.read_csv(csv_path)
    return df
