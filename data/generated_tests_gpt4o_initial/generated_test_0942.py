import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import unittest

# Constants
START_DATE = '2016-01-01'
PERIODS = 13
FREQ = 'WOM-2FRI'
CATEGORIES = ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']

# The function defined in the prompt is not included here as per the instructions.

class TestSalesReport(unittest.TestCase):

    def test_default_parameters(self):
        df, ax = task_func()
        self.assertEqual(df.shape[0], 65)  # 13 periods * 5 categories
        self.assertEqual(list(df.columns), ['Date', 'Category', 'Sales'])

    def test_custom_parameters(self):
        df, ax = task_func(start_date='2020-01-01', periods=5, freq='W-MON', categories=['Electronics'])
        self.assertEqual(df.shape[0], 5)  # 5 periods * 1 category
        self.assertTrue((df['Category'] == 'Electronics').all())

    def test_sales_range(self):
        df, ax = task_func()
        self.assertTrue((df['Sales'] >= 100).all() and (df['Sales'] < 500).all())

    def test_date_range(self):
        df, ax = task_func(start_date='2020-01-01', periods=3, freq='W-MON')
        expected_dates = pd.date_range(start='2020-01-01', periods=3, freq='W-MON')
        self.assertTrue(df['Date'].equals(expected_dates))

    def test_category_inclusion(self):
        df, ax = task_func(categories=['Electronics', 'Fashion'])
        self.assertTrue(set(['Electronics', 'Fashion']).issubset(df['Category'].unique()))
        self.assertEqual(len(df['Category'].unique()), 2)  # Check only 2 categories in the result

if __name__ == '__main__':
    unittest.main()