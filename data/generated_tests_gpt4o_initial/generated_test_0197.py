import unittest
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt

# The provided prompt (for context). Do not modify this part.
'''
import heapq
import math
import matplotlib.pyplot as plt


def task_func(l1, l2, N=10):
    """ 
    Find the N biggest differences between the respective elements of the list 'l1' and list 'l2', 
    square the differences, take the square root and return the plotted values as a matplotlib Axes object.

    Parameters:
    l1 (list): A list of numbers.
    l2 (list): A list of numbers.
    N (int): Number of largest differences to consider. Default is 10.

    Returns:
    matplotlib.axes._axes.Axes: A matplotlib Axes object with the plotted differences.

    Requirements:
    - heapq
    - math
    - matplotlib.pyplot

    Example:
    >>> l1 = [99, 86, 90, 70, 86, 95, 56, 98, 80, 81]
    >>> l2 = [21, 11, 21, 1, 26, 40, 4, 50, 34, 37]
    >>> ax = task_func(l1, l2)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """
    
    largest_diff_indices = heapq.nlargest(N, range(len(l1)), key=lambda i: abs(l1[i] - l2[i]))
    largest_diffs = [math.sqrt((l1[i] - l2[i])**2) for i in largest_diff_indices]

    fig, ax = plt.subplots()
    ax.plot(largest_diffs)

    return ax
'''

class TestTaskFunc(unittest.TestCase):

    def test_return_type(self):
        l1 = [99, 86, 90, 70, 86, 95, 56, 98, 80, 81]
        l2 = [21, 11, 21, 1, 26, 40, 4, 50, 34, 37]
        ax = task_func(l1, l2)
        self.assertIsInstance(ax, plt.Axes)

    def test_plot_length(self):
        l1 = [99, 86, 90, 70, 86, 95, 56, 98, 80, 81]
        l2 = [21, 11, 21, 1, 26, 40, 4, 50, 34, 37]
        ax = task_func(l1, l2)
        lines = ax.get_lines()
        self.assertEqual(len(lines[0].get_xdata()), 10)  # Expecting 10 points plotted by default

    def test_large_differences(self):
        l1 = [100, 200, 300, 400, 500]
        l2 = [0, 10, 20, 30, 40]
        ax = task_func(l1, l2, N=3)
        lines = ax.get_lines()
        data = lines[0].get_ydata()
        self.assertGreaterEqual(data.max(), 460)  # Check that the largest differences are significant

    def test_empty_lists(self):
        l1 = []
        l2 = []
        with self.assertRaises(ValueError):
            task_func(l1, l2)

    def test_non_numeric_lists(self):
        l1 = ['a', 'b', 'c']
        l2 = [1, 2, 3]
        with self.assertRaises(TypeError):
            task_func(l1, l2)

if __name__ == '__main__':
    unittest.main()