import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import unittest

def task_func(data, target_column, test_size=0.2, random_state=0) -> float:
    """
    Train a linear regression model and return the model score of the test set.
    ... (prompt content skipped for brevity)
    """

class TestTaskFunc(unittest.TestCase):

    def test_non_dataframe_input(self):
        with self.assertRaises(ValueError) as context:
            task_func("not a dataframe", "y")
        self.assertEqual(str(context.exception), "data should be a DataFrame.")

    def test_empty_dataframe(self):
        empty_df = pd.DataFrame()
        with self.assertRaises(ValueError) as context:
            task_func(empty_df, "y")
        self.assertEqual(str(context.exception), "data should contain at least one row.")

    def test_target_column_not_in_dataframe(self):
        df = pd.DataFrame({'x1': [1, 2, 3]})
        with self.assertRaises(ValueError) as context:
            task_func(df, "y")
        self.assertEqual(str(context.exception), "target_column should be in the provided DataFrame.")

    def test_non_numeric_data(self):
        df = pd.DataFrame({'x1': [1, 2, 'a'], 'y': [1, 2, 3]})
        with self.assertRaises(ValueError) as context:
            task_func(df, 'y')
        self.assertEqual(str(context.exception), "data values should be numeric only.")

    def test_invalid_test_size(self):
        df = pd.DataFrame({'x1': [1, 2, 3], 'y': [1, 2, 3]})
        with self.assertRaises(ValueError) as context:
            task_func(df, 'y', test_size=1.5)
        self.assertEqual(str(context.exception), "test_size should be between 0 and 1: 0 < test_size < 1")

if __name__ == '__main__':
    unittest.main()