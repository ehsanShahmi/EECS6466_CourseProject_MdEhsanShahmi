import math
import numpy as np
import matplotlib.pyplot as plt
import unittest

def task_func(list_input):
    """
    Sort the given list in ascending order based on the degree value of its elements, calculate the cumulative sum of 
    the sorted list, and draw a line chart of the cumulative sum.

    Parameters:
    list_input (list): The list to be sorted.

    Returns:
    tuple: A tuple containing:
           - numpy array: The cumulative sum of the sorted list.
           - matplotlib.axes._axes.Axes: The Axes object of the plotted line chart.

    Requirements:
    - math
    - numpy
    - matplotlib.pyplot

    Example:
    >>> cumsum, ax = task_func([10, 20, 30])
    >>> print(cumsum)
    [10 30 60]
    >>> ax.get_title()
    'Cumulative Sum Plot'
    """
    sorted_list = sorted(list_input, key=lambda x: (math.degrees(x), x))
    cumsum = np.cumsum(sorted_list)
    
    # Plotting the line chart
    ax = plt.plot(cumsum)[0].axes
    ax.set_title("Cumulative Sum Plot")
    ax.set_xlabel("Index")
    ax.set_ylabel("Cumulative Sum")
    
    return cumsum, ax

class TestTaskFunc(unittest.TestCase):

    def test_regular_integers(self):
        cumsum, ax = task_func([10, 20, 30])
        expected_cumsum = np.array([10, 30, 60])
        self.assertTrue(np.array_equal(cumsum, expected_cumsum))
        self.assertEqual(ax.get_title(), 'Cumulative Sum Plot')

    def test_mixed_integers(self):
        cumsum, ax = task_func([50, 10, 30, 40])
        expected_cumsum = np.array([10, 40, 80, 130])
        self.assertTrue(np.array_equal(cumsum, expected_cumsum))
        self.assertEqual(ax.get_title(), 'Cumulative Sum Plot')

    def test_negative_numbers(self):
        cumsum, ax = task_func([-1, -2, -3])
        expected_cumsum = np.array([-3, -5, -6])
        self.assertTrue(np.array_equal(cumsum, expected_cumsum))
        self.assertEqual(ax.get_title(), 'Cumulative Sum Plot')

    def test_floats(self):
        cumsum, ax = task_func([1.5, 2.5, 3.5])
        expected_cumsum = np.array([1.5, 4.0, 7.5])
        self.assertTrue(np.array_equal(cumsum, expected_cumsum))
        self.assertEqual(ax.get_title(), 'Cumulative Sum Plot')

    def test_empty_list(self):
        cumsum, ax = task_func([])
        expected_cumsum = np.array([])
        self.assertTrue(np.array_equal(cumsum, expected_cumsum))
        self.assertEqual(ax.get_title(), 'Cumulative Sum Plot')

if __name__ == '__main__':
    unittest.main()