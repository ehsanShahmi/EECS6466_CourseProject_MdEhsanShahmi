import unittest
import pandas as pd
import numpy as np
from pandas.errors import EmptyDataError
import matplotlib

class TestTaskFunction(unittest.TestCase):

    def test_standardize_numeric_columns(self):
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        standardized_df, _ = task_func(df)
        expected_df = pd.DataFrame({'A': [-1.224745, 0.0, 1.224745], 
                                     'B': [-1.224745, 0.0, 1.224745]})
        pd.testing.assert_frame_equal(standardized_df.round(6), expected_df)

    def test_no_numeric_columns(self):
        df = pd.DataFrame({'C': ['a', 'b', 'c'], 'D': ['d', 'e', 'f']})
        with self.assertRaises(ValueError) as context:
            task_func(df)
        self.assertEqual(str(context.exception), "No numeric columns present")

    def test_empty_dataframe(self):
        df = pd.DataFrame(columns=['A', 'B'])
        with self.assertRaises(ValueError) as context:
            task_func(df)
        self.assertEqual(str(context.exception), "No numeric columns present")

    def test_single_numeric_column(self):
        df = pd.DataFrame({'A': [1, 2, 3]})
        standardized_df, _ = task_func(df)
        expected_df = pd.DataFrame({'A': [-1.224745, 0.0, 1.224745]})
        pd.testing.assert_frame_equal(standardized_df.round(6), expected_df)

    def test_correlation_heatmap_creation(self):
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        _, fig = task_func(df)
        self.assertIsInstance(fig, matplotlib.figure.Figure)

if __name__ == '__main__':
    unittest.main()