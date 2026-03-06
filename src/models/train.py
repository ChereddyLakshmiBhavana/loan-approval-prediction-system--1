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

def train_model(data_path=None, model_type='neural_network'):
    """Main training function"""
    
    if data_path is None:
        data_path = DATA_PROCESSED_PATH
    
    print(f"Loading data from {data_path}...")
    
    # Load processed data
    X = pd.read_csv(data_path / "X_processed.csv")
    y = pd.read_csv(data_path / "y.csv")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SPLIT, random_state=RANDOM_STATE
    )
    
    X_train, X_val, y_train, y_val = train_test_split(
        X_train, y_train, test_size=VALIDATION_SPLIT, random_state=RANDOM_STATE
    )
    
    print(f"Training set size: {X_train.shape}")
    print(f"Validation set size: {X_val.shape}")
    print(f"Test set size: {X_test.shape}")
    
    if model_type == 'neural_network':
        print("Training Neural Network model...")
        model, history = train_neural_network(
            X_train.values, y_train.values,
            X_val.values, y_val.values
        )
        
        # Save model
        model_path = MODEL_DIR / "loan_approval_nn.h5"
        model.save(str(model_path))
        print(f"Model saved to {model_path}")
        
    elif model_type == 'gradient_boosting':
        print("Training Gradient Boosting model...")
        model = train_gradient_boosting(X_train.values, y_train.values)
        
        # Save model
        import joblib
        model_path = MODEL_DIR / "loan_approval_gb.pkl"
        joblib.dump(model, str(model_path))
        print(f"Model saved to {model_path}")
    
    # Evaluate on test set
    print("\nEvaluating on test set...")
    metrics = model.evaluate(X_test.values, y_test.values.ravel())
    
    print("Test Metrics:")
    for metric, value in metrics.items():
        print(f"  {metric}: {value:.4f}")
    
    return model, metrics

if __name__ == '__main__':
    train_model(model_type='neural_network')
