import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import unittest

# Test suite for the task_func function
class TestTaskFunc(unittest.TestCase):

    def test_default_random_data(self):
        # Test default behavior (random dataset generation)
        result = task_func()
        self.assertEqual(result.shape, (100, 5))
        self.assertTrue(isinstance(result, pd.DataFrame))

    def test_data_shape(self):
        # Test with specific data shape and check if it's maintained
        data = np.random.rand(50, 3)
        result = task_func(data)
        self.assertEqual(result.shape, (50, 3))

    def test_replacement_of_values(self):
        # Test to check if values less than 0.5 are replaced with zeros
        data = np.array([[0.1, 0.2, 0.6], [0.4, 0.7, 0.3]])
        result = task_func(data)
        self.assertTrue((result.values < 0.5).sum() == 0)

    def test_standardization(self):
        # Test to ensure that the standardized data has a mean of 0 and std of 1
        data = np.array([[1, 2], [3, 4], [5, 6]])
        result = task_func(data)
        self.assertAlmostEqual(result.mean().mean(), 0, delta=0.1)
        self.assertAlmostEqual(result.std().mean(), 1, delta=0.1)

    def test_dataframe_columns(self):
        # Test to ensure that the columns in the result match the input dataframe
        data = np.random.rand(10, 4)
        result = task_func(data)
        self.assertTrue(all(result.columns == range(4)))

# If this script is being run directly, execute the tests
if __name__ == '__main__':
    unittest.main()