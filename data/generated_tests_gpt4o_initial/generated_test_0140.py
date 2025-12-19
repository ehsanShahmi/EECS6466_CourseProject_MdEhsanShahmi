import unittest
import pandas as pd
import numpy as np

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        # Set up a standard DataFrame for testing
        np.random.seed(0)
        self.df = pd.DataFrame({
            'A': np.random.normal(0, 1, 1000),
            'B': np.random.exponential(1, 1000),
            'C': np.random.uniform(0, 1, 1000)
        })

    def test_standardize_valid_columns(self):
        """Test standardizing valid columns."""
        standardized_df = task_func(self.df, ['A', 'B'])
        self.assertAlmostEqual(standardized_df['A'].mean(), 0, delta=0.1)
        self.assertAlmostEqual(standardized_df['B'].mean(), 0, delta=0.1)
        self.assertAlmostEqual(standardized_df['A'].std(), 1, delta=0.1)
        self.assertAlmostEqual(standardized_df['B'].std(), 1, delta=0.1)

    def test_standardize_single_column(self):
        """Test standardizing a single valid column."""
        standardized_df = task_func(self.df, ['C'])
        self.assertAlmostEqual(standardized_df['C'].mean(), 0, delta=0.1)
        self.assertAlmostEqual(standardized_df['C'].std(), 1, delta=0.1)

    def test_invalid_dataframe(self):
        """Test if ValueError is raised when df is not a DataFrame."""
        with self.assertRaises(ValueError):
            task_func([], ['A'])  # Passing a list instead of DataFrame

    def test_invalid_columns_type(self):
        """Test if ValueError is raised when cols is not a list."""
        with self.assertRaises(ValueError):
            task_func(self.df, 'A')  # Passing a string instead of a list

    def test_non_existing_column(self):
        """Test if ValueError is raised when columns in cols do not exist in df."""
        with self.assertRaises(ValueError):
            task_func(self.df, ['A', 'D'])  # 'D' does not exist in df

if __name__ == '__main__':
    unittest.main()