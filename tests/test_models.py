"""Tests for model training and prediction"""

import unittest
import numpy as np
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.models.model import LoanApprovalModel, GradientBoostingModel

class TestLoanApprovalModel(unittest.TestCase):
    """Test neural network model"""
    
    def setUp(self):
        self.model = LoanApprovalModel(input_shape=(10,), output_classes=2)
    
    def test_model_creation(self):
        """Test model creation"""
        self.assertIsNotNone(self.model.model)
    
    def test_prediction_shape(self):
        """Test prediction output shape"""
        X = np.random.randn(5, 10)
        predictions = self.model.predict(X)
        self.assertEqual(predictions.shape, (5,))
    
    def test_probability_shape(self):
        """Test probability output shape"""
        X = np.random.randn(5, 10)
        proba = self.model.predict_proba(X)
        self.assertEqual(proba.shape, (5, 2))

class TestGradientBoostingModel(unittest.TestCase):
    """Test gradient boosting model"""
    
    def setUp(self):
        self.model = GradientBoostingModel()
    
    def test_training(self):
        """Test model training"""
        X = np.random.randn(100, 10)
        y = np.random.randint(0, 2, 100)
        
        self.model.train(X, y)
        self.assertIsNotNone(self.model.model)
    
    def test_prediction(self):
        """Test model prediction"""
        X_train = np.random.randn(100, 10)
        y_train = np.random.randint(0, 2, 100)
        
        self.model.train(X_train, y_train)
        
        X_test = np.random.randn(10, 10)
        predictions = self.model.predict(X_test)
        
        self.assertEqual(predictions.shape, (10,))

if __name__ == '__main__':
    unittest.main()
