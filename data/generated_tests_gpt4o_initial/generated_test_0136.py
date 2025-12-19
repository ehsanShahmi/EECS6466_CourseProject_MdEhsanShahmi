import unittest
import pandas as pd
import numpy as np
from task_module import task_func  # Assuming the function is in task_module.py

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Create sample data for testing."""
        self.valid_df = pd.DataFrame(np.random.rand(100, 4), columns=list('ABCD'))
        self.empty_df = pd.DataFrame()
        self.invalid_df = None

    def test_valid_input(self):
        """Test with valid DataFrame."""
        pca_df, ax = task_func(self.valid_df)
        self.assertIsInstance(pca_df, pd.DataFrame)
        self.assertEqual(pca_df.shape[1], 2)
        self.assertIn('Principal Component 1', pca_df.columns)
        self.assertIn('Principal Component 2', pca_df.columns)

    def test_empty_dataframe(self):
        """Test with an empty DataFrame."""
        with self.assertRaises(ValueError) as context:
            task_func(self.empty_df)
        self.assertEqual(str(context.exception), "DataFrame is empty")

    def test_invalid_dataframe_type(self):
        """Test with invalid type (None)."""
        with self.assertRaises(ValueError) as context:
            task_func(self.invalid_df)
        self.assertEqual(str(context.exception), "Input must be a DataFrame")

    def test_invalid_dataframe_shape(self):
        """Test with a DataFrame with a single column."""
        single_column_df = pd.DataFrame(np.random.rand(100, 1), columns=['A'])
        with self.assertRaises(ValueError):
            task_func(single_column_df)  # Expecting to handle PCA issues if possible

    def test_plot_attributes(self):
        """Test attributes of the plot generated."""
        pca_df, ax = task_func(self.valid_df)
        self.assertEqual(ax.get_title(), '2 Component PCA')
        self.assertEqual(ax.get_xlabel(), 'Principal Component 1')
        self.assertEqual(ax.get_ylabel(), 'Principal Component 2')

if __name__ == '__main__':
    unittest.main()