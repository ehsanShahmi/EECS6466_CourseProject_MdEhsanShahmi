import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import unittest

class TestTaskFunc(unittest.TestCase):

    def test_basic_functionality(self):
        # Test with a simple matrix
        skew, kurtosis, ax = task_func([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertIsInstance(ax, plt.Axes)
        self.assertAlmostEqual(round(skew, 2), 0.0)
        self.assertAlmostEqual(round(kurtosis, 2), -1.5)

    def test_empty_matrix(self):
        # Test with an empty matrix
        with self.assertRaises(ValueError):
            task_func([])

    def test_single_row_matrix(self):
        # Test with a matrix that has a single row
        skew, kurtosis, ax = task_func([[1, 2, 3]])
        self.assertIsInstance(ax, plt.Axes)
        self.assertAlmostEqual(round(skew, 2), 0.0)
        self.assertAlmostEqual(round(kurtosis, 2), -1.5)

    def test_uniform_matrix(self):
        # Test with a uniform matrix where all values are the same
        skew, kurtosis, ax = task_func([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        self.assertIsInstance(ax, plt.Axes)
        self.assertAlmostEqual(round(skew, 2), float('nan'))
        self.assertAlmostEqual(round(kurtosis, 2), float('nan'))

    def test_large_matrix(self):
        # Test with a larger matrix
        matrix = np.random.rand(1000, 10).tolist()
        skew, kurtosis, ax = task_func(matrix)
        self.assertIsInstance(ax, plt.Axes)
        self.assertIsInstance(skew, float)
        self.assertIsInstance(kurtosis, float)


if __name__ == '__main__':
    unittest.main()