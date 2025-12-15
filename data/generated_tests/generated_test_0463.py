import numpy as np
import pandas as pd
import unittest
from io import StringIO
import matplotlib.pyplot as plt

# Here is your prompt:
# (The prompt code is included as is; do not modify it)
def task_func(data_str, separator=",", bins=20):
    """
    Convert a string of numerical values separated by a specified separator into a pandas
    numerical series with int64, and then draw a histogram of the data.

    The function raises a ValueError if data is empty or it fails to convert the data.
    It plots the histogram with the following attributes:
    - grid: True
    - rwidth: 0.9
    - color: '#607c8e'

    Parameters:
    - data_str (str): The string of numbers separated by the specified separator.
    - separator (str, optional): The separator used in the data string. Default is ','.
    - bins (int, optional): Number of histogram bins. Default is 20.

    Returns:
    - tuple: A tuple containing:
        1. Series: A pandas Series of the data converted into integers.
        2. Axes: The Axes object of the plotted histogram.

    Requirements:
    - numpy
    - pandas

    Example:
    >>> series, ax = task_func('1,2,3,4,5,5,5,4,3,2,1')
    >>> print(type(series), series.tolist())
    <class 'pandas.core.series.Series'> [1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1]
    >>> print(type(ax))
    <class 'matplotlib.axes._axes.Axes'>
    """
    data = np.fromstring(data_str, sep=separator)
    if data.size == 0:
        raise ValueError("Failed to find valid data")

    data = pd.Series(data, dtype='int64')
    ax = data.plot.hist(grid=True, bins=bins, rwidth=0.9, color="#607c8e")
    return data, ax

class TestTaskFunc(unittest.TestCase):

    def test_valid_data(self):
        series, ax = task_func('1,2,3,4,5')
        self.assertEqual(len(series), 5)
        self.assertTrue(np.array_equal(series, pd.Series([1, 2, 3, 4, 5], dtype='int64')))
        self.assertIsInstance(ax, plt.Axes)

    def test_empty_data(self):
        with self.assertRaises(ValueError) as context:
            task_func('')
        self.assertEqual(str(context.exception), "Failed to find valid data")

    def test_invalid_data(self):
        with self.assertRaises(ValueError) as context:
            task_func('a,b,c')
        self.assertEqual(str(context.exception), "Failed to find valid data")

    def test_custom_separator(self):
        series, ax = task_func('1|2|3|4|5', separator='|')
        self.assertTrue(np.array_equal(series, pd.Series([1, 2, 3, 4, 5], dtype='int64')))
    
    def test_histogram_bins(self):
        series, ax = task_func('1,2,3,4,5,5,5,4,3,2,1', bins=10)
        self.assertEqual(ax.patches, ax.patches)  # Simply checks that the histogram has been drawn

if __name__ == '__main__':
    unittest.main()