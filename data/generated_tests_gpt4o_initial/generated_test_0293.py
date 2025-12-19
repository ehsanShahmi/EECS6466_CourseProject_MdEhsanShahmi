import itertools
import numpy as np
import matplotlib.pyplot as plt
import unittest

def task_func(elements, subset_size):
    """
    Generate all subsets of a given size from a tuple and draw a histogram of the sums of the subsets. Additionally,
    return the Axes object of the plotted histogram and the combinations of the subsets and their sums.

    Parameters:
    - elements (tuple): A tuple of integers for which subsets will be generated.
    - subset_size (int): Size of the subsets to be generated.

    Returns:
    - matplotlib.axes.Axes: Axes object of the plotted histogram.
    - list: List of all the combinations of subsets.
    - list: List of the sums of all the subsets.

    Requirements:
    - itertools
    - numpy
    - matplotlib

    Example:
    >>> ax, combs, sums = task_func((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 2)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    >>> len(combs)
    45
    >>> len(sums)
    45
    """

    combinations = list(itertools.combinations(elements, subset_size))
    sums = [sum(combination) for combination in combinations]
    ax = plt.hist(sums, bins=np.arange(min(sums), max(sums) + 2) - 0.5, rwidth=0.8, align='left')
    return plt.gca(), combinations, sums

class TestTaskFunc(unittest.TestCase):

    def test_task_func_basic(self):
        ax, combs, sums = task_func((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 2)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(combs), 45)
        self.assertEqual(len(sums), 45)

    def test_task_func_empty_tuple(self):
        ax, combs, sums = task_func((), 2)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(combs), 0)
        self.assertEqual(len(sums), 0)

    def test_task_func_single_element(self):
        ax, combs, sums = task_func((1,), 1)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(combs), 1)
        self.assertEqual(sums[0], 1)

    def test_task_func_large_subset(self):
        ax, combs, sums = task_func((1, 2, 3, 4, 5, 6, 7, 8), 4)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(combs), 70)
        self.assertEqual(len(sums), 70)

    def test_task_func_non_integer_tuple(self):
        with self.assertRaises(TypeError):
            task_func((1.5, 2.5, 3.5), 2)

if __name__ == '__main__':
    unittest.main()