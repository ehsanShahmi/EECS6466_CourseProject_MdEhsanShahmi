import pandas as pd
import unittest
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Constants
COLUMNS = ['Date', 'Value']

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Set up the initial DataFrame for testing."""
        self.valid_df = pd.DataFrame({
            'Date': ['2021-01-01', '2021-01-02'],
            'Value': [[8, 10, 12], [7, 9, 11]]
        })
        
        self.empty_df = pd.DataFrame(columns=COLUMNS)
        
        self.invalid_value_df = pd.DataFrame({
            'Date': ['2021-01-01', '2021-01-02'],
            'Value': ['not a list', [7, 9, 11]]
        })

        self.single_row_df = pd.DataFrame({
            'Date': ['2021-01-01'],
            'Value': [[1, 2, 3]]
        })
        
        self.df_with_nan = pd.DataFrame({
            'Date': ['2021-01-01', '2021-01-02'],
            'Value': [[1, 2, np.nan], [4, 5, 6]]
        })

    def test_valid_input(self):
        """Test valid DataFrame returns correlation DataFrame."""
        corr_df = task_func(self.valid_df)
        self.assertIsInstance(corr_df, pd.DataFrame)
        self.assertEqual(corr_df.shape, (2, 2))  # 2 variables with correlation

    def test_empty_dataframe(self):
        """Test that ValueError is raised for an empty DataFrame."""
        with self.assertRaises(ValueError):
            task_func(self.empty_df)

    def test_invalid_value_column(self):
        """Test that ValueError is raised when 'Value' contains non-list items."""
        with self.assertRaises(ValueError):
            task_func(self.invalid_value_df)

    def test_single_row_dataframe(self):
        """Test valid single row DataFrame returns correlation DataFrame."""
        corr_df = task_func(self.single_row_df)
        self.assertIsInstance(corr_df, pd.DataFrame)
        self.assertEqual(corr_df.shape, (1, 1))  # Only one variable, correlation with itself

    def test_dataframe_with_nan(self):
        """Test that the correlation calculation handles NaN values appropriately."""
        corr_df = task_func(self.df_with_nan)
        self.assertIsInstance(corr_df, pd.DataFrame)
        self.assertTrue(np.isnan(corr_df.iloc[0, 1]))  # Check correlation involving NaN

if __name__ == '__main__':
    unittest.main()