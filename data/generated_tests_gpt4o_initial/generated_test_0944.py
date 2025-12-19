import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import unittest

def task_func(start_date='2016-01-01', periods=13, freq='WOM-2FRI', seed=0):
    ...
    # Function implementation is not provided as per the instruction

class TestTaskFunc(unittest.TestCase):

    def test_default_values(self):
        df, ax = task_func()
        self.assertEqual(len(df), 13)
        self.assertEqual(df.index[0].strftime('%Y-%m-%d'), '2016-01-01')

    def test_custom_date(self):
        df, ax = task_func(start_date='2020-01-01', periods=5, freq='M', seed=42)
        self.assertEqual(len(df), 5)
        self.assertEqual(df.index[0].strftime('%Y-%m-%d'), '2020-01-01')

    def test_random_seed_reproducibility(self):
        df1, _ = task_func(seed=42)
        df2, _ = task_func(seed=42)
        pd.testing.assert_frame_equal(df1, df2)

    def test_price_range(self):
        df, ax = task_func(freq='M', periods=10)
        self.assertTrue((df['Price'] >= 100).all() and (df['Price'] <= 500).all())

    def test_plot_properties(self):
        _, ax = task_func()
        self.assertEqual(ax.title.get_text(), 'Stock Prices')
        self.assertEqual(ax.get_xlabel(), 'Date')
        self.assertEqual(ax.get_ylabel(), 'Price')

if __name__ == '__main__':
    unittest.main()