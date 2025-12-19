import matplotlib.pyplot as plt
from itertools import cycle
import numpy as np
from random import shuffle
import unittest

COLORS = ["b", "g", "r", "c", "m", "y", "k"]

def task_func(list_of_lists):
    """
    Plots a series of lines for each list in `list_of_lists`. Each line is plotted with shuffled y-values
    and sequential x-values starting from 1. The function shuffles the y-values of each inner list before plotting.
    Each line is plotted with a different color from a predetermined set of colors. The function cycles through 
    these colors for each inner list.

    Parameters:
    - list_of_lists (list of list): A list of lists where each inner
    list represents a set of y-values to be shuffled and plotted. The x-values are automatically
    generated as a sequence starting from 1 up to the length of the inner list.

    Returns:
    - tuple: A tuple containing the figure and axes objects of the plotted graph.

    Requirements:
    - matplotlib
    - itertools
    - numpy
    - random

    Example:
    >>> import random
    >>> random.seed(0)
    >>> fig, ax = task_func([[1, 2, 3], [4, 5, 6]])
    >>> ax.lines[0].get_color()
    (0.0, 0.0, 1.0, 1)

    Note:
    - If an inner list is empty, it will be skipped and no line will be plotted for it.
    - The colors are reused cyclically if there are more inner lists than colors available.
    - The shuffling of y-values is random and different each time the function is called,
      unless a random seed is set externally.
    - The function uses a default set of colors defined in the COLORS constant.
    """
    fig, ax = plt.subplots()
    color_cycle = cycle(COLORS)

    for list_ in list_of_lists:
        if not list_:
            continue
        y_values = np.arange(1, len(list_) + 1)
        shuffle(y_values)
        ax.plot(y_values, next(color_cycle))

    return fig, ax

class TestTaskFunc(unittest.TestCase):

    def test_empty_input(self):
        fig, ax = task_func([])
        self.assertEqual(len(ax.lines), 0, "Expected no lines for empty input")

    def test_single_list_length_one(self):
        fig, ax = task_func([[1]])
        self.assertEqual(len(ax.lines), 1, "Expected one line for single list of length one")
        self.assertEqual(ax.lines[0].get_xydata().shape[0], 1, "Expected one point in the line")

    def test_multiple_lists(self):
        fig, ax = task_func([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(len(ax.lines), 3, "Expected three lines for three lists")

    def test_empty_inner_lists(self):
        fig, ax = task_func([[1, 2], [], [3]])
        self.assertEqual(len(ax.lines), 2, "Expected two lines, one for [1, 2] and one for [3]")

    def test_cyclic_colors(self):
        fig, ax = task_func([[1], [2], [3], [4], [5], [6], [7]])
        self.assertEqual(len(ax.lines), 7, "Expected seven lines for seven inner lists")
        colors_used = [line.get_color() for line in ax.lines]
        self.assertEqual(colors_used[0], colors_used[3], "Expected color cycling to occur after 3 lines")


if __name__ == "__main__":
    unittest.main()