import unittest
import numpy as np
import pandas as pd

PRODUCTS = ['Product' + str(i) for i in range(1, 6)]
MONTHS = ['Month' + str(i) for i in range(1, 13)]

class TestTaskFunc(unittest.TestCase):

    def test_dataframe_shape(self):
        df = task_func()
        self.assertEqual(df.shape, (12, 5), "DataFrame should have 12 rows and 5 columns.")

    def test_dataframe_columns(self):
        df = task_func()
        self.assertTrue(all(df.columns == PRODUCTS), "DataFrame columns should be named after PRODUCTS.")

    def test_dataframe_index(self):
        df = task_func()
        self.assertTrue(all(df.index == MONTHS), "DataFrame index should be named after MONTHS.")

    def test_dataframe_values_range(self):
        df = task_func()
        self.assertTrue((df.values >= 100).all() and (df.values <= 1000).all(), 
                        "All sales figures should be between 100 and 1000.")

    def test_sales_visualizations(self):
        df = task_func()
        # Check if the visualizations were created without errors (this is implicit testing)
        self.assertIsNotNone(df.plot)  # Check if the plot function exists
        self.assertIsNotNone(df.sum())  # Ensure that summation was possible, indicating data integrity

if __name__ == '__main__':
    unittest.main()