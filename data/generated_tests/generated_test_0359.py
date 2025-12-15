import unittest
from scipy import stats
import matplotlib.pyplot as plt

# The provided prompt for the function
from scipy import stats
import matplotlib.pyplot as plt


def task_func(data_dict, data_keys):
    """
    Calculate the correlation between two data series and return a scatter plot along with the correlation coefficient.
    
    Parameters:
    data_dict (dict): The dictionary containing data. Keys should match those provided in data_keys.
    data_keys (list): The list of keys (length of 2) used to access data in data_dict for correlation.
    
    Returns:
    tuple: 
        - float: The correlation coefficient.
        - Axes: The scatter plot of the two data series.
    
    Requirements:
    - scipy
    - matplotlib.pyplot
    
    Example:
    >>> data_dict = {'X': [1, 2, 3, 4, 5], 'Y': [2, 3, 5, 7, 8]}
    >>> data_keys = ['X', 'Y']
    >>> correlation, plot = task_func(data_dict, data_keys)
    >>> round(correlation, 4)
    0.9923
    >>> isinstance(plot, plt.Axes)
    True
    """

    x = data_dict[data_keys[0]]
    y = data_dict[data_keys[1]]
    correlation, _ = stats.pearsonr(x, y)
    
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    
    return correlation, ax


class TestTaskFunc(unittest.TestCase):

    def test_valid_data(self):
        data_dict = {'X': [1, 2, 3, 4, 5], 'Y': [2, 3, 5, 7, 8]}
        data_keys = ['X', 'Y']
        correlation, plot = task_func(data_dict, data_keys)
        self.assertAlmostEqual(round(correlation, 4), 0.9923)
        self.assertIsInstance(plot, plt.Axes)

    def test_negative_correlation(self):
        data_dict = {'X': [1, 2, 3, 4, 5], 'Y': [5, 4, 3, 2, 1]}
        data_keys = ['X', 'Y']
        correlation, plot = task_func(data_dict, data_keys)
        self.assertAlmostEqual(round(correlation, 4), -1.0)
        self.assertIsInstance(plot, plt.Axes)

    def test_no_correlation(self):
        data_dict = {'X': [1, 2, 3, 4, 5], 'Y': [5, 5, 5, 5, 5]}
        data_keys = ['X', 'Y']
        correlation, plot = task_func(data_dict, data_keys)
        self.assertAlmostEqual(round(correlation, 4), 0.0)
        self.assertIsInstance(plot, plt.Axes)

    def test_invalid_keys(self):
        data_dict = {'A': [1, 2, 3], 'B': [4, 5, 6]}
        data_keys = ['X', 'Y']
        with self.assertRaises(KeyError):
            task_func(data_dict, data_keys)

    def test_empty_data(self):
        data_dict = {'X': [], 'Y': []}
        data_keys = ['X', 'Y']
        with self.assertRaises(ValueError):
            task_func(data_dict, data_keys)

if __name__ == '__main__':
    unittest.main()