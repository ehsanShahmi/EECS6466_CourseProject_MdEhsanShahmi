import unittest
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

# Here is your prompt:
def task_func(a, b):
    """
    Calculate the Pearson correlation coefficient of two lists, generate a Pandas DataFrame from these lists, and then draw a scatter plot with a regression line.

    Parameters:
    a (list): A list of numbers.
    b (list): Another list of numbers.

    Requirements:
    - numpy
    - pandas
    - scipy
    - matplotlib.pyplot

    Returns:
    - tuple: Contains two elements:
        - float: The Pearson correlation coefficient.
        - matplotlib.axes.Axes: The Axes object of the plotted scatter plot with a regression line.

    Example:
    >>> correlation, ax = task_func([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
    >>> isinstance(correlation, float) and isinstance(ax, matplotlib.axes.Axes)
    True
    >>> round(correlation, 1)
    1.0
    """
    correlation, _ = stats.pearsonr(a, b)
    df = pd.DataFrame({'A': a, 'B': b})

    plt.scatter(df['A'], df['B'])
    plt.plot(np.unique(df['A']), np.poly1d(np.polyfit(df['A'], df['B'], 1))(np.unique(df['A'])), color='red')
    plt.show()
    return correlation, plt.gca()

class TestTaskFunc(unittest.TestCase):

    def test_positive_correlation(self):
        correlation, ax = task_func([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
        self.assertIsInstance(correlation, float)
        self.assertAlmostEqual(correlation, 1.0)

    def test_no_correlation(self):
        correlation, ax = task_func([1, 2, 3, 4], [5, 5, 5, 5])
        self.assertIsInstance(correlation, float)
        self.assertAlmostEqual(correlation, 0.0)

    def test_negative_correlation(self):
        correlation, ax = task_func([1, 2, 3, 4, 5], [10, 8, 6, 4, 2])
        self.assertIsInstance(correlation, float)
        self.assertAlmostEqual(correlation, -1.0)

    def test_identical_lists(self):
        correlation, ax = task_func([5, 5, 5, 5], [5, 5, 5, 5])
        self.assertIsInstance(correlation, float)
        # Correlation is undefined for identical lists
        self.assertTrue(np.isnan(correlation))

    def test_large_numbers(self):
        correlation, ax = task_func([1000, 2000, 3000], [2000, 4000, 6000])
        self.assertIsInstance(correlation, float)
        self.assertAlmostEqual(correlation, 1.0)

if __name__ == '__main__':
    unittest.main()