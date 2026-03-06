"""Model training script"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from config.config import (
    DATA_PROCESSED_PATH, MODEL_DIR, BATCH_SIZE, 
    EPOCHS, TEST_SPLIT, VALIDATION_SPLIT, RANDOM_STATE
)
from src.models.model import LoanApprovalModel, GradientBoostingModel

def train_neural_network(X_train, y_train, X_val=None, y_val=None):
    """Train a neural network model"""
    
    # Determine input shape
    input_shape = (X_train.shape[1],)
    
    # Create and train model
    model = LoanApprovalModel(input_shape=input_shape, output_classes=2)
    
    history = model.train(
        X_train, y_train,
        X_val=X_val,
        y_val=y_val,
        epochs=EPOCHS,
        batch_size=BATCH_SIZE
    )
    
    return model, history

def train_gradient_boosting(X_train, y_train):
    """Train a gradient boosting model"""
    model = GradientBoostingModel()
    model.train(X_train, y_train)
    return model

"""Model training script"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from config.config import (
    DATASET_FILENAME, MODEL_DIR, BATCH_SIZE, 
    EPOCHS, TEST_SPLIT, VALIDATION_SPLIT, RANDOM_STATE,
    TARGET_COLUMN
)
from data.loader import DataLoader
from data.preprocessing import DataPreprocessor
from models.model import LoanApprovalModel, GradientBoostingModel

def train_neural_network(X_train, y_train, X_val=None, y_val=None):
    """Train a neural network model"""
    
    # Determine input shape
    input_shape = (X_train.shape[1],)
    
    # Create and train model
    model = LoanApprovalModel(input_shape=input_shape, output_classes=2)
    
    history = model.train(
        X_train, y_train,
        X_val=X_val,
        y_val=y_val,
        epochs=EPOCHS,
        batch_size=BATCH_SIZE
    )
    
    return model, history

def train_gradient_boosting(X_train, y_train):
    """Train a gradient boosting model"""
    model = GradientBoostingModel()
    model.train(X_train, y_train)
    return model

def prepare_data_for_training(df_processed):
    """
    Prepare processed dataframe for model training
    
    Args:
        df_processed: Preprocessed dataframe from DataPreprocessor
        
    Returns:
        X, y: Features and target arrays
    """
    # Drop loan_id and target column to get features
    feature_cols = [col for col in df_processed.columns 
                   if col not in ['loan_id', TARGET_COLUMN]]
    
    X = df_processed[feature_cols].values
    y = df_processed[TARGET_COLUMN].values
    
    return X, y

def train_model(data_filename=None, model_type='neural_network'):
    """Main training function"""
    
    if data_filename is None:
        data_filename = DATASET_FILENAME
    
    print("Starting model training pipeline...")
    print("=" * 50)
    
    # Initialize components
    loader = DataLoader()
    preprocessor = DataPreprocessor()
    
    try:
        # Step 1: Load raw data
        print("1. Loading raw dataset...")
        df_raw = loader.load_loan_approval_dataset(data_filename)
        print(f"✓ Loaded {df_raw.shape[0]} records")
        
        # Step 2: Preprocess data
        print("\n2. Preprocessing data...")
        df_processed = preprocessor.preprocess_loan_dataset(df_raw)
        print(f"✓ Preprocessing completed: {df_processed.shape}")
        
        # Step 3: Prepare features and target
        print("\n3. Preparing features and target...")
        X, y = prepare_data_for_training(df_processed)
        print(f"✓ Features shape: {X.shape}, Target shape: {y.shape}")
        
        # Step 4: Split data
        print("\n4. Splitting data into train/validation/test sets...")
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=TEST_SPLIT, random_state=RANDOM_STATE, stratify=y
        )
        
        X_train, X_val, y_train, y_val = train_test_split(
            X_train, y_train, test_size=VALIDATION_SPLIT, 
            random_state=RANDOM_STATE, stratify=y_train
        )
        
        print(f"✓ Training set: {X_train.shape[0]} samples")
        print(f"✓ Validation set: {X_val.shape[0]} samples")
        print(f"✓ Test set: {X_test.shape[0]} samples")
        
        # Step 5: Train model
        print(f"\n5. Training {model_type} model...")
        if model_type == 'neural_network':
            model, history = train_neural_network(
                X_train, y_train,
                X_val, y_val
            )
            
            # Save model
            model_path = MODEL_DIR / "loan_approval_nn.h5"
            model.save(str(model_path))
            print(f"✓ Neural network model saved to {model_path}")
            
        elif model_type == 'gradient_boosting':
            model = train_gradient_boosting(X_train, y_train)
            
            # Save model
            import joblib
            model_path = MODEL_DIR / "loan_approval_gb.pkl"
            joblib.dump(model, str(model_path))
            print(f"✓ Gradient boosting model saved to {model_path}")
        
        # Step 6: Evaluate on test set
        print("\n6. Evaluating on test set...")
        metrics = model.evaluate(X_test, y_test)
        
        print("Test Metrics:")
        for metric, value in metrics.items():
            print(f"  {metric}: {value:.4f}")
        
        # Step 7: Save processed data for future use
        print("\n7. Saving processed data...")
        loader.save_processed_data(df_processed, "loan_approval_processed.csv")
        
        print("\n" + "=" * 50)
        print("✓ Training pipeline completed successfully!")
        
        return model, metrics
        
    except Exception as e:
        print(f"\n❌ Error in training pipeline: {str(e)}")
        raise

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Train loan approval prediction model')
    parser.add_argument('--model', choices=['neural_network', 'gradient_boosting'], 
                       default='neural_network', help='Model type to train')
    parser.add_argument('--data', default=None, help='Path to dataset file')
    
    args = parser.parse_args()
    
    train_model(data_filename=args.data, model_type=args.model)
