import unittest
import pandas as pd
import matplotlib.pyplot as plt
from your_module import task_func  # replace 'your_module' with the actual name of your module if necessary

class TestTaskFunction(unittest.TestCase):

    def test_zero_rows(self):
        df, ax = task_func(0)
        self.assertEqual(df.shape[0], 0, "DataFrame should have 0 rows when input is 0")
        self.assertEqual(ax.title.get_text(), 'Non-Zero Value Counts', "Title should match for zero rows")

    def test_negative_rows(self):
        df, ax = task_func(-5)
        self.assertEqual(df.shape[0], 0, "DataFrame should have 0 rows for negative input")
        self.assertEqual(ax.title.get_text(), 'Non-Zero Value Counts', "Title should match for negative rows")

    def test_positive_rows(self):
        df, ax = task_func(10)
        self.assertEqual(df.shape[0], 10, "DataFrame should have the correct number of rows (10)")
        self.assertEqual(ax.title.get_text(), 'Non-Zero Value Counts', "Title should be correct for positive rows")
        self.assertEqual(set(df.columns), set(['Column1', 'Column2', 'Column3', 'Column4', 'Column5']), 
                         "DataFrame column names should match the predefined columns")

    def test_data_non_zero_counts(self):
        df, ax = task_func(100)
        counts = df.astype(bool).sum(axis=0)
        bars = [bar.get_height() for bar in ax.patches]
        self.assertEqual(bars, list(counts), "Bar heights should match the non-zero counts in DataFrame")

    def test_data_frame_dtype(self):
        df, ax = task_func(50)
        self.assertTrue(pd.api.types.is_integer_dtype(df['Column1']), "Column1 should be of integer data type")
        self.assertTrue(pd.api.types.is_integer_dtype(df['Column2']), "Column2 should be of integer data type")
        self.assertTrue(pd.api.types.is_integer_dtype(df['Column3']), "Column3 should be of integer data type")
        self.assertTrue(pd.api.types.is_integer_dtype(df['Column4']), "Column4 should be of integer data type")
        self.assertTrue(pd.api.types.is_integer_dtype(df['Column5']), "Column5 should be of integer data type")

if __name__ == '__main__':
    unittest.main()