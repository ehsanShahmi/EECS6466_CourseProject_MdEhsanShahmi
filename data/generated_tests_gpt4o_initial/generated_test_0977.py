import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import unittest

def task_func(array, features=None, seed=None):
    # Function implementation remains unmodified.

class TestTaskFunc(unittest.TestCase):

    def test_empty_array(self):
        """Test with an empty array should raise ValueError."""
        with self.assertRaises(ValueError):
            task_func(np.array([]))

    def test_non_2d_array(self):
        """Test with a non-2D array should raise ValueError."""
        with self.assertRaises(ValueError):
            task_func(np.array([1, 2, 3]))

    def test_features_mismatch(self):
        """Test with features list that does not match column count should raise ValueError."""
        array = np.random.rand(2, 3)
        features = ['A', 'B']  # Only 2 features for an array with 3 columns
        with self.assertRaises(ValueError):
            task_func(array, features=features)

    def test_valid_input_with_no_features(self):
        """Test with a valid 2D array and no features should not raise error."""
        array = np.random.rand(2, 5)
        ax = task_func(array)
        self.assertIsInstance(ax, plt.Axes)

    def test_valid_input_with_features(self):
        """Test with a valid 2D array and matching features should not raise error."""
        array = np.random.rand(2, 4)
        features = ['A', 'B', 'C', 'D']
        ax = task_func(array, features=features)
        self.assertIsInstance(ax, plt.Axes)

if __name__ == '__main__':
    unittest.main()