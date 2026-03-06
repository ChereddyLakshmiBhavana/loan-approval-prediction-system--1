"""Tests for data loading and preprocessing"""

import unittest
import tempfile
import pandas as pd
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.data.loader import DataLoader
from src.data.preprocessing import DataPreprocessor

class TestDataLoader(unittest.TestCase):
    """Test data loading functionality"""
    
    def setUp(self):
        self.loader = DataLoader()
    
    def test_load_csv(self):
        """Test CSV loading"""
        # Create temporary CSV
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write("col1,col2\n1,2\n3,4\n")
            f.flush()
            
            df = self.loader.load_csv(f.name, filepath=Path(f.name))
            self.assertEqual(df.shape, (2, 2))

class TestDataPreprocessor(unittest.TestCase):
    """Test data preprocessing functionality"""
    
    def setUp(self):
        self.preprocessor = DataPreprocessor()
    
    def test_handle_missing_values(self):
        """Test missing value handling"""
        df = pd.DataFrame({
            'A': [1, 2, None, 4],
            'B': [5, None, None, 8]
        })
        
        result = self.preprocessor.handle_missing_values(df)
        self.assertEqual(result.isnull().sum().sum(), 0)
    
    def test_remove_duplicates(self):
        """Test duplicate removal"""
        df = pd.DataFrame({
            'A': [1, 1, 2, 3],
            'B': [4, 4, 5, 6]
        })
        
        result = self.preprocessor.remove_duplicates(df)
        self.assertEqual(result.shape[0], 3)

if __name__ == '__main__':
    unittest.main()
