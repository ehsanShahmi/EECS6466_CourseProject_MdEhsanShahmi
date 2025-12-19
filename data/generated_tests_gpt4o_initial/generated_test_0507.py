import pandas as pd
import numpy as np
import unittest

# Here is your prompt:
import pandas as pd
import numpy as np


def task_func(column, data):
    """
    Analyzes a list of stock data and calculates the sum, mean, minimum, and maximum
    values for a specified column.

    Parameters:
    - column (str): The name of the column to analyze. Valid options are 'Date', 'Open', 'High',
                    'Low', 'Close', and 'Volume'.
    - data (list of lists): A list where each element is a list representing stock data for a single day.
                            Each inner list should contain values in the following order:
                            'Date', 'Open', 'High', 'Low', 'Close', 'Volume'.
    Returns:
    - dict: A dictionary containing the calculated 'sum', 'mean', 'min' (minimum), and 'max' (maximum)
            for the specified column. If the input data is empty, 'sum' will be 0, and 'mean', 'min', and
            'max' will be NaN.

    Requirements:
    - pandas
    - numpy

    Raises:
    - ValueError: If the specified column name is not valid.
    
    Example:
    >>> data = [[datetime(2022, 1, 1), 100, 105, 95, 102, 10000]]
    >>> results = task_func('Open', data)
    >>> results
    {'sum': 100, 'mean': 100.0, 'min': 100, 'max': 100}
    >>> type(results)
    <class 'dict'>
    """
    
class TestTaskFunc(unittest.TestCase):

    def test_valid_data_open_column(self):
        data = [['2022-01-01', 100, 105, 95, 102, 10000], 
                ['2022-01-02', 110, 115, 105, 112, 11000]]
        results = task_func('Open', data)
        self.assertEqual(results['sum'], 210)
        self.assertEqual(results['mean'], 105.0)
        self.assertEqual(results['min'], 100)
        self.assertEqual(results['max'], 110)

    def test_valid_data_close_column(self):
        data = [['2022-01-01', 100, 105, 95, 102, 10000], 
                ['2022-01-02', 110, 115, 105, 112, 11000]]
        results = task_func('Close', data)
        self.assertEqual(results['sum'], 214)
        self.assertEqual(results['mean'], 107.0)
        self.assertEqual(results['min'], 102)
        self.assertEqual(results['max'], 112)

    def test_empty_data(self):
        data = []
        results = task_func('Open', data)
        self.assertEqual(results['sum'], 0)
        self.assertTrue(np.isnan(results['mean']))
        self.assertTrue(np.isnan(results['min']))
        self.assertTrue(np.isnan(results['max']))

    def test_invalid_column_name(self):
        data = [['2022-01-01', 100, 105, 95, 102, 10000]]
        with self.assertRaises(ValueError) as context:
            task_func('InvalidColumn', data)
        self.assertEqual(str(context.exception), "Invalid column name.")
    
    def test_invalid_data_format(self):
        data = [['2022-01-01', 100, 105]]
        with self.assertRaises(ValueError) as context:
            task_func('Open', data)
        self.assertEqual(str(context.exception), "Data must be a list of lists, with each inner list matching the length of the column names.")

if __name__ == '__main__':
    unittest.main()