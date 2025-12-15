import pandas as pd
import random
import unittest

# Constants
N_DATA_POINTS = 10000
MIN_VALUE = 0.0
MAX_VALUE = 10.0

# Test Suite
class TestTaskFunc(unittest.TestCase):

    def test_return_type(self):
        """Test if the return type is a pandas DataFrame."""
        result = task_func(20)
        self.assertIsInstance(result, pd.DataFrame)

    def test_column_name(self):
        """Test if the DataFrame has the correct column name."""
        result = task_func(10)
        self.assertIn('Value', result.columns)

    def test_empty_dataframe(self):
        """Test if the function returns an empty DataFrame when n_data_points is 0."""
        result = task_func(0)
        self.assertTrue(result.empty)

    def test_data_point_count(self):
        """Test if the function generates the correct number of data points."""
        num_points = 50
        result = task_func(num_points)
        self.assertEqual(result.shape[0], num_points)

    def test_value_range(self):
        """Test if all generated values are within the specified range."""
        result = task_func(100)
        self.assertTrue((result['Value'] >= MIN_VALUE).all() and (result['Value'] <= MAX_VALUE).all())

if __name__ == '__main__':
    unittest.main()