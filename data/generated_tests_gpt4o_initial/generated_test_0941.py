import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import unittest

def task_func(start_date: str, periods: int, freq: str, random_seed: int = 0) -> (pd.DataFrame, plt.Axes):
    # Function code provided in the prompt; not modified.

class TestTaskFunc(unittest.TestCase):

    def test_valid_input(self):
        df, ax = task_func('2021-01-01', 5, 'WOM-2FRI')
        self.assertEqual(df.shape, (5, 1))
        self.assertEqual(list(df.columns), ['Sales'])

    def test_correct_dates(self):
        df, ax = task_func('2022-01-01', 3, 'M')
        expected_dates = pd.date_range('2022-01-31', periods=3, freq='M')
        pd.testing.assert_index_equal(df.index, expected_dates)

    def test_random_seed_reproducibility(self):
        df1, _ = task_func('2020-01-01', 5, 'W', random_seed=42)
        df2, _ = task_func('2020-01-01', 5, 'W', random_seed=42)
        pd.testing.assert_frame_equal(df1, df2)

    def test_sales_value_range(self):
        df, ax = task_func('2021-01-01', 10, 'M', random_seed=1)
        self.assertTrue((df['Sales'] >= 100).all() and (df['Sales'] < 500).all())
    
    def test_plot_axes(self):
        df, ax = task_func('2021-01-01', 5, 'M')
        self.assertIsInstance(ax, plt.Axes)
        self.assertIn('Sales Forecast', ax.get_title())
        self.assertEqual(ax.get_xlabel(), 'Date')
        self.assertEqual(ax.get_ylabel(), 'Sales')

if __name__ == '__main__':
    unittest.main()