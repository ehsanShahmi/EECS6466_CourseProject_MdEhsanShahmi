import unittest
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class TestTaskFunc(unittest.TestCase):

    def test_remove_column_and_generate_heatmap(self):
        data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
        ax = task_func(data, column='c')
        self.assertIsNotNone(ax)
        self.assertTrue(isinstance(ax, plt.Axes))

    def test_no_numeric_columns(self):
        data = {'a': ["foo", "bar"], 'b': ["baz", "qux"]}
        result = task_func(data, column='c')
        self.assertIsNone(result)

    def test_empty_data(self):
        data = {}
        result = task_func(data, column='c')
        self.assertIsNone(result)

    def test_all_columns_removed(self):
        data = {'a': [7, 8, 9], 'c': [1, 2, 3]}
        result = task_func(data, column='a')
        self.assertIsNone(result)

    def test_heatmap_with_only_one_numeric_column(self):
        data = {'a': [1, 2, 3], 'b': ['x', 'y', 'z'], 'c': [4, 5, 6]}
        ax = task_func(data, column='b')
        self.assertIsNotNone(ax)
        self.assertTrue(isinstance(ax, plt.Axes))

if __name__ == "__main__":
    unittest.main()