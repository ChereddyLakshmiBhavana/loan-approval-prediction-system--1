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
        
"""Data preprocessing and cleaning operations"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from typing import List, Dict, Any

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
    
    def preprocess_loan_dataset(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Preprocess the loan approval dataset with loan-specific transformations
        
        Args:
            df: Raw loan approval dataframe
            
        Returns:
            Preprocessed dataframe ready for modeling
        """
        df_processed = df.copy()
        
        # 1. Handle missing values
        df_processed = self.handle_missing_values(df_processed)
        
        # 2. Remove duplicates
        df_processed = self.remove_duplicates(df_processed)
        
        # 3. Encode categorical variables
        categorical_cols = ['education', 'self_employed']
        df_processed = self.encode_categorical(df_processed, categorical_cols)
        
        # 4. Encode target variable (loan_status)
        if 'loan_status' in df_processed.columns:
            df_processed['loan_status'] = df_processed['loan_status'].map({'Approved': 1, 'Rejected': 0})
        
        # 5. Feature engineering - combine assets into total assets
        asset_cols = ['residential_assets_value', 'commercial_assets_value', 
                     'luxury_assets_value', 'bank_asset_value']
        df_processed['total_assets_value'] = df_processed[asset_cols].sum(axis=1)
        
        # 6. Create debt-to-income ratio
        df_processed['debt_to_income_ratio'] = df_processed['loan_amount'] / (df_processed['income_annum'] + 1)  # +1 to avoid division by zero
        
        # 7. Scale numeric features
        numeric_cols_to_scale = [
            'no_of_dependents', 'income_annum', 'loan_amount', 'loan_term', 
            'cibil_score', 'total_assets_value', 'debt_to_income_ratio'
        ]
        df_processed = self.scale_features(df_processed, numeric_cols_to_scale)
        
        print(f"Preprocessing completed. Shape: {df_processed.shape}")
        print(f"Target distribution: {df_processed['loan_status'].value_counts().to_dict()}")
        
        return df_processed
    
    def get_feature_importance_columns(self) -> Dict[str, List[str]]:
        """
        Get column groupings for feature importance analysis
        
        Returns:
            Dictionary with different feature categories
        """
        return {
            'personal_info': ['no_of_dependents', 'education', 'self_employed'],
            'financial_info': ['income_annum', 'loan_amount', 'loan_term'],
            'credit_info': ['cibil_score'],
            'assets': ['residential_assets_value', 'commercial_assets_value', 
                      'luxury_assets_value', 'bank_asset_value', 'total_assets_value'],
            'ratios': ['debt_to_income_ratio']
        }
    
    def preprocess(self, df, numeric_cols, categorical_cols):
        """Complete preprocessing pipeline"""
        df = self.handle_missing_values(df)
        df = self.remove_duplicates(df)
        df = self.scale_features(df, numeric_cols)
        df = self.encode_categorical(df, categorical_cols)
        return df
