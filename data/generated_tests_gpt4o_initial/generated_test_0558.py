import unittest
import pandas as pd
import matplotlib
from task import task_func

class TestTaskFunc(unittest.TestCase):
    
    def test_standardization_with_positive_numbers(self):
        df, ax = task_func([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape[1], 2)
        self.assertEqual(list(df.columns), ['A', 'B'])

    def test_standardization_with_negative_numbers(self):
        df, ax = task_func([-1, -2, -3], [-2, -4, -6])
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape[0], 3)

    def test_standardization_with_empty_first_list(self):
        df, ax = task_func([], [2, 4, 6])
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue(df.empty)

    def test_standardization_with_empty_second_list(self):
        df, ax = task_func([1, 2, 3, 4], [])
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue(df.empty)

    def test_standardization_with_default_columns(self):
        df, ax = task_func([1, 3, 5], [2, 6, 10])
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(list(df.columns), ['A', 'B'])

if __name__ == '__main__':
    unittest.main()