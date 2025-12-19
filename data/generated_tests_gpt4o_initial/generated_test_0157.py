import unittest
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

class TestTaskFunction(unittest.TestCase):

    def test_valid_input(self):
        """Test with a valid 2D numpy array."""
        data = np.array([[1, 2, 3], [4, 5, 6]])
        df, ax = task_func(data)
        self.assertEqual(df.shape[0], 2)
        self.assertIn('Average', df.columns)
        self.assertAlmostEqual(df['Average'][0], 2.0)
        self.assertAlmostEqual(df['Average'][1], 5.0)

    def test_non_numeric_data(self):
        """Test with a 2D array containing non-numeric data."""
        data = np.array([[1, 2, 'a'], [4, 5, 6]])
        with self.assertRaises(ValueError):
            task_func(data)

    def test_non_2d_array(self):
        """Test with a non-2D array input."""
        data = np.array([1, 2, 3])
        with self.assertRaises(ValueError):
            task_func(data)

    def test_empty_array(self):
        """Test with an empty 2D array."""
        data = np.array([[], []])
        with self.assertRaises(ValueError):
            task_func(data)

    def test_large_array(self):
        """Test with a large 2D numpy array."""
        data = np.random.rand(100, 10)  # 100 rows, 10 columns
        df, ax = task_func(data)
        self.assertEqual(df.shape[0], 100)
        self.assertIn('Average', df.columns)
        self.assertEqual(df['Average'].shape[0], 100)

if __name__ == '__main__':
    unittest.main()