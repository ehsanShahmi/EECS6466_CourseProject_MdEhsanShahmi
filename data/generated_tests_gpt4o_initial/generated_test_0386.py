import numpy as np
import pandas as pd
import unittest

# Constants
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

# Here is your prompt:
# import numpy as np
# import pandas as pd

# Constants
# COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

# def task_func(length, min_value = 0, max_value = 100):
#     ...
#     return df

class TestTaskFunc(unittest.TestCase):
    
    def test_output_shape(self):
        """Test if the output DataFrame shape is correct"""
        length = 100
        output = task_func(length)
        self.assertEqual(output.shape, (101, len(COLUMNS)), "Output shape should be (101, 5)")

    def test_column_names(self):
        """Test if the output DataFrame has the correct column names"""
        length = 50
        output = task_func(length)
        self.assertListEqual(list(output.columns), COLUMNS, "Output DataFrame should have the correct column names")

    def test_min_value(self):
        """Test if the minimum value in the output DataFrame is correct"""
        length = 100
        min_value = 0
        output = task_func(length, min_value)
        self.assertTrue((output.min().min() >= min_value), f"Minimum value should be at least {min_value}")

    def test_max_value(self):
        """Test if the maximum value in the output DataFrame is correct"""
        length = 100
        max_value = 100
        output = task_func(length, 0, max_value)
        self.assertTrue((output.max().max() <= max_value), f"Maximum value should not exceed {max_value}")

    def test_empty_input(self):
        """Test if the function handles an empty DataFrame length correctly"""
        length = 0
        output = task_func(length)
        self.assertEqual(output.shape, (1, len(COLUMNS)), "Output shape for length 0 should be (1, 5)")

if __name__ == '__main__':
    unittest.main()