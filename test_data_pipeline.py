#!/usr/bin/env python3
"""
Test script for data loading and preprocessing pipeline
Run this after placing the loan_approval_dataset.csv in data/raw/
"""

import sys
import pandas as pd
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from data.loader import DataLoader
from data.preprocessing import DataPreprocessor
from config.config import DATASET_FILENAME, TARGET_COLUMN

def test_data_pipeline():
    """Test the complete data loading and preprocessing pipeline"""
    print("Testing Loan Approval Data Pipeline")
    print("=" * 50)

    # Initialize components
    loader = DataLoader()
    preprocessor = DataPreprocessor()

    try:
        # Step 1: Load the dataset
        print("1. Loading dataset...")
        df = loader.load_loan_approval_dataset(DATASET_FILENAME)
        print(f"✓ Dataset loaded successfully: {df.shape[0]} rows, {df.shape[1]} columns")

        # Step 2: Get dataset info
        print("\n2. Dataset information:")
        info = loader.get_dataset_info(df)
        print(f"   Shape: {info['shape']}")
        print(f"   Target distribution: {info['target_distribution']}")

        # Step 3: Split features and target
        print("\n3. Splitting features and target...")
        features, target = loader.split_features_target(df, TARGET_COLUMN)
        print(f"✓ Features shape: {features.shape}, Target shape: {target.shape}")

        # Step 4: Preprocess the data
        print("\n4. Preprocessing data...")
        df_processed = preprocessor.preprocess_loan_dataset(df)
        print(f"✓ Preprocessing completed: {df_processed.shape[0]} rows, {df_processed.shape[1]} columns")

        # Step 5: Verify preprocessing results
        print("\n5. Verification:")
        print(f"   - No missing values: {df_processed.isnull().sum().sum() == 0}")
        print(f"   - Target encoded: {df_processed[TARGET_COLUMN].dtype}")
        print(f"   - New features created: {'total_assets_value' in df_processed.columns and 'debt_to_income_ratio' in df_processed.columns}")

        # Step 6: Save processed data
        print("\n6. Saving processed data...")
        loader.save_processed_data(df_processed, "loan_approval_processed.csv")

        print("\n" + "=" * 50)
        print("✓ All tests passed! Data pipeline is working correctly.")
        print("Processed data saved to data/processed/loan_approval_processed.csv")

        return True

    except Exception as e:
        print(f"\n❌ Error in data pipeline: {str(e)}")
        print("\nTroubleshooting:")
        print("1. Ensure loan_approval_dataset.csv is in data/raw/")
        print("2. Check that the CSV has the expected columns")
        print("3. Verify the file is not corrupted")
        return False

if __name__ == "__main__":
    success = test_data_pipeline()
    sys.exit(0 if success else 1)