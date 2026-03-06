"""Data loading and I/O operations"""

import pandas as pd
import numpy as np
from pathlib import Path
import sys

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

def load_training_data(csv_path):
    """Load training dataset"""
    df = pd.read_csv(csv_path)
    return df

def load_test_data(csv_path):
    """Load test dataset"""
    df = pd.read_csv(csv_path)
    return df
