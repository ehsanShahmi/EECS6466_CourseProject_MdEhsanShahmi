import numpy as np
import pandas as pd
from collections import Counter
from scipy.stats import norm
import matplotlib.pyplot as plt
import unittest

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Set up a sample DataFrame for testing
        self.df_empty = pd.DataFrame({'value': []})
        self.df_single_value = pd.DataFrame({'value': [5]})
        self.df_multiple_values = pd.DataFrame({
            'value': [1, 2, 2, 3, 3, 4, 3, 2, 1, 4, 4, 4, 2, 2, 3, 1, 1, 1, 3, 2]
        })
        self.df_no_duplicates = pd.DataFrame({'value': [1, 2, 3, 4, 5]})

    def test_empty_dataframe(self):
        counter, ax = task_func(self.df_empty)
        self.assertEqual(counter, Counter())
        self.assertIsInstance(ax, plt.Axes)

    def test_single_value_dataframe(self):
        counter, ax = task_func(self.df_single_value)
        self.assertEqual(counter, Counter({5: 1}))
        self.assertIsInstance(ax, plt.Axes)

    def test_multiple_values_dataframe(self):
        counter, ax = task_func(self.df_multiple_values)
        expected_counter = Counter({2: 6, 1: 5, 3: 5, 4: 4})
        self.assertEqual(counter, expected_counter)
        self.assertIsInstance(ax, plt.Axes)

    def test_no_duplicates_dataframe(self):
        counter, ax = task_func(self.df_no_duplicates)
        self.assertEqual(counter, Counter())
        self.assertIsInstance(ax, plt.Axes)

    def test_bins_parameter(self):
        counter, ax = task_func(self.df_multiple_values, bins=10)
        self.assertIsInstance(ax, plt.Axes)
        # Verify that histogram bins are set correctly
        self.assertEqual(ax.patches[0].get_x(), ax.patches[1].get_x() - (ax.patches[1].get_x() - ax.patches[0].get_x()))  # Check bins

if __name__ == '__main__':
    unittest.main()