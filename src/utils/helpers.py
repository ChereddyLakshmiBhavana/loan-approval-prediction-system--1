"""Helper utility functions"""

import numpy as np
import pandas as pd

def split_features_target(df, target_column):
    """Split features and target from dataframe"""
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return X, y

def get_feature_importance(model, feature_names):
    """Get feature importance from model"""
    if hasattr(model, 'feature_importances_'):
        importance = model.feature_importances_
        feature_import_df = pd.DataFrame({
            'feature': feature_names,
            'importance': importance
        }).sort_values('importance', ascending=False)
        return feature_import_df
    return None

def evaluate_predictions(y_true, y_pred):
    """Detailed prediction evaluation"""
    from sklearn.metrics import (
        confusion_matrix, classification_report, roc_curve, auc
    )
    
    cm = confusion_matrix(y_true, y_pred)
    report = classification_report(y_true, y_pred)
    
    return {
        'confusion_matrix': cm,
        'classification_report': report
    }

def format_prediction_output(prediction, probability):
    """Format prediction for output"""
    return {
        'approved': bool(prediction),
        'approval_probability': float(probability),
        'decision': 'Approved' if prediction else 'Rejected'
    }
