import unittest
import pandas as pd
import numpy as np

class TestTaskFunction(unittest.TestCase):

    def test_output_shape(self):
        df = task_func(10, [1, 3])
        # Check if the number of rows is correct
        self.assertEqual(df.shape[0], 10)
        # Check if the correct number of columns is present after removal (5 - 2 = 3)
        self.assertEqual(df.shape[1], 3)

    def test_columns_reduction(self):
        df = task_func(10, [1, 3])
        # Verify that the columns 'B' and 'D' are removed
        self.assertNotIn('B', df.columns)
        self.assertNotIn('D', df.columns)
        # Verify that the columns 'A', 'C', 'E' exist
        self.assertIn('A', df.columns)
        self.assertIn('C', df.columns)
        self.assertIn('E', df.columns)

    def test_random_seed_stability(self):
        df1 = task_func(5, [1, 3], random_seed=42)
        df2 = task_func(5, [1, 3], random_seed=42)
        # Check if two DataFrames generated with the same seed are identical
        pd.testing.assert_frame_equal(df1, df2)

    def test_empty_dataframe(self):
        df = task_func(0, [0, 1])
        # Check if the dataframe is empty
        self.assertTrue(df.empty)

    def test_custom_columns(self):
        df = task_func(3, [1, 3], columns=['test', 'rem1', 'apple', 'remove'])
        # Verify that the DataFrame has the expected custom columns after dropping
        self.assertNotIn('rem1', df.columns)
        self.assertNotIn('remove', df.columns)
        self.assertIn('test', df.columns)
        self.assertIn('apple', df.columns)

if __name__ == '__main__':
    unittest.main()