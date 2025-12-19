import numpy as np
import unittest
from datetime import datetime

def task_func(rows=3, columns=2, start_date=datetime(2021, 1, 1), end_date=datetime(2021, 12, 31), seed=0):
    # Function implementation is omitted as per the instruction.

class TestTaskFunc(unittest.TestCase):

    def test_default_parameters(self):
        """Test the function with default parameters."""
        result = task_func()
        self.assertEqual(result.shape, (3, 2))
        self.assertTrue(np.all(np.diff(result.flatten()) >= np.timedelta64(1, 'D')))

    def test_custom_shape(self):
        """Test the function with custom row and column sizes."""
        result = task_func(rows=2, columns=3)
        self.assertEqual(result.shape, (2, 3))

    def test_date_range(self):
        """Test the function to ensure dates are within the specified range."""
        result = task_func(start_date=datetime(2021, 1, 1), end_date=datetime(2021, 1, 10))
        self.assertTrue(np.all(result >= np.datetime64('2021-01-01')))
        self.assertTrue(np.all(result <= np.datetime64('2021-01-10')))

    def test_unique_dates(self):
        """Test that all dates in the matrix are unique."""
        result = task_func(rows=3, columns=4, seed=42)  # Seed set for reproducibility
        unique_dates = np.unique(result)
        self.assertEqual(unique_dates.shape[0], result.size)

    def test_invalid_parameters(self):
        """Test the function behavior with invalid parameters."""
        with self.assertRaises(ValueError):
            task_func(rows=-1, columns=2)  # Rows cannot be negative
        with self.assertRaises(ValueError):
            task_func(rows=2, columns=0)  # Columns cannot be zero

if __name__ == '__main__':
    unittest.main()