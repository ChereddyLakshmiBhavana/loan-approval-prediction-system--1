"""Data preprocessing and cleaning operations"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer

class DataPreprocessor:
    """Handle data preprocessing and cleaning"""
    
    def __init__(self):
        self.scaler = StandardScaler()
        self.label_encoders = {}
    
    def handle_missing_values(self, df, strategy='mean'):
        """Handle missing values in the dataset"""
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        categorical_cols = df.select_dtypes(include=['object']).columns
        
        # Handle numeric columns
        numeric_imputer = SimpleImputer(strategy=strategy)
        df[numeric_cols] = numeric_imputer.fit_transform(df[numeric_cols])
        
        # Handle categorical columns
        if len(categorical_cols) > 0:
            cat_imputer = SimpleImputer(strategy='most_frequent')
            df[categorical_cols] = cat_imputer.fit_transform(df[categorical_cols])
        
        return df
    
    def remove_duplicates(self, df):
        """Remove duplicate rows"""
        return df.drop_duplicates()
    
    def scale_features(self, df, columns):
        """Scale numeric features"""
        df[columns] = self.scaler.fit_transform(df[columns])
        return df
    
    def encode_categorical(self, df, columns):
        """Encode categorical variables"""
        df_encoded = df.copy()
        
        for col in columns:
            if col not in self.label_encoders:
                self.label_encoders[col] = LabelEncoder()
                df_encoded[col] = self.label_encoders[col].fit_transform(df_encoded[col].astype(str))
            else:
                df_encoded[col] = self.label_encoders[col].transform(df_encoded[col].astype(str))
        
        return df_encoded
    
    def preprocess(self, df, numeric_cols, categorical_cols):
        """Complete preprocessing pipeline"""
        df = self.handle_missing_values(df)
        df = self.remove_duplicates(df)
        df = self.scale_features(df, numeric_cols)
        df = self.encode_categorical(df, categorical_cols)
        return df
