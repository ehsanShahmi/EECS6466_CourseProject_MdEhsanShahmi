import pandas as pd
import seaborn as sns
import unittest

class TestTaskFunc(unittest.TestCase):
    
    def test_valid_data(self):
        data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
        ax = task_func(data)
        self.assertIsNotNone(ax, "The returned Axes object should not be None.")

    def test_empty_data(self):
        data = {}
        with self.assertRaises(ValueError) as context:
            task_func(data)
        self.assertEqual(str(context.exception), "No numeric columns present")

    def test_no_numeric_columns(self):
        data = {'A': ['a', 'b', 'c'], 'B': ['d', 'e', 'f']}
        with self.assertRaises(ValueError) as context:
            task_func(data)
        self.assertEqual(str(context.exception), "No numeric columns present")

    def test_numeric_and_non_numeric_columns(self):
        data = {'A': [1, 2, 3], 'B': ['a', 'b', 'c']}
        ax = task_func(data)
        self.assertIsNotNone(ax, "The returned Axes object should not be None.")
    
    def test_single_numeric_column(self):
        data = {'A': [1, 2, 3]}
        ax = task_func(data)
        self.assertIsNotNone(ax, "The returned Axes object should not be None.")

if __name__ == '__main__':
    unittest.main()