import unittest
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Constants
PLOT_TITLE = 'Square root plot'
X_LABEL = 'x'
Y_LABEL = 'sqrt(x)'
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

# Provided code context may not be modified, so we will only define the test suite below.

class TestTaskFunc(unittest.TestCase):

    def test_basic_functionality(self):
        result = [{"from_user": 16}, {"from_user": 9}]
        square_roots, ax = task_func(result)
        expected_square_roots = np.array([4.0, 3.0])
        np.testing.assert_array_almost_equal(square_roots, expected_square_roots)
        self.assertEqual(ax.get_title(), PLOT_TITLE)
        self.assertEqual(ax.get_xlabel(), X_LABEL)
        self.assertEqual(ax.get_ylabel(), Y_LABEL)

    def test_empty_input(self):
        result = []
        square_roots, ax = task_func(result)
        expected_square_roots = np.array([])
        np.testing.assert_array_almost_equal(square_roots, expected_square_roots)
        self.assertEqual(ax.get_title(), PLOT_TITLE)

    def test_single_entry(self):
        result = [{"from_user": 25}]
        square_roots, ax = task_func(result)
        expected_square_roots = np.array([5.0])
        np.testing.assert_array_almost_equal(square_roots, expected_square_roots)
        self.assertEqual(ax.get_title(), PLOT_TITLE)

    def test_non_numeric_values(self):
        result = [{"from_user": 16}, {"value": "not_a_number"}, {"from_user": 49}]
        square_roots, ax = task_func(result)
        expected_square_roots = np.array([4.0, 7.0])
        np.testing.assert_array_almost_equal(square_roots, expected_square_roots)
        self.assertEqual(ax.get_title(), PLOT_TITLE)

    def test_multiple_entries(self):
        result = [{"from_user": 1}, {"from_user": 4}, {"from_user": 10}, {"from_user": 100}]
        square_roots, ax = task_func(result)
        expected_square_roots = np.array([1.0, 2.0, 3.16, 10.0])
        np.testing.assert_array_almost_equal(square_roots, expected_square_roots)
        self.assertEqual(ax.get_title(), PLOT_TITLE)

if __name__ == '__main__':
    unittest.main()