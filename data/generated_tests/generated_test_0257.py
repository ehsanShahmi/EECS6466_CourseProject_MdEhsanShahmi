import unittest
import numpy as np
import matplotlib.pyplot as plt

# Here is your prompt:
import numpy as np
import math

def task_func(ax, num_turns):
    """
    Draws a spiral on the polar diagram 'ax' with the specified number of turns 'num_turns'.
    The spiral starts at the center and expands outward with each turn.
    The radial ticks on the plot are positioned at intervals corresponding to the number of turns multiplied by 45 degrees.

    Parameters:
    ax (matplotlib.axes._axes.Axes): The Axes object for plotting the spiral.
    num_turns (int): The number of turns for the spiral.

    Returns:
    matplotlib.axes._axes.Axes: The modified Axes object with the spiral plot.

    Requirements:
    - numpy
    - math

    Example:
    >>> import matplotlib.pyplot as plt
    >>> fig, ax = plt.subplots(subplot_kw={'polar': True})
    >>> ax = task_func(ax, 3)
    >>> ax.get_rlabel_position()
    135.0
    """

class TestTaskFunc(unittest.TestCase):
    
    def test_num_turns_zero(self):
        fig, ax = plt.subplots(subplot_kw={'polar': True})
        ax = task_func(ax, 0)
        self.assertEqual(ax.get_rlabel_position(), 0.0)

    def test_num_turns_one(self):
        fig, ax = plt.subplots(subplot_kw={'polar': True})
        ax = task_func(ax, 1)
        self.assertEqual(ax.get_rlabel_position(), 45.0)
        self.assertEqual(len(ax.lines), 1)  # Check if one line is created

    def test_num_turns_two(self):
        fig, ax = plt.subplots(subplot_kw={'polar': True})
        ax = task_func(ax, 2)
        self.assertEqual(ax.get_rlabel_position(), 90.0)
        self.assertEqual(len(ax.lines), 1)  # Check if one line is created

    def test_num_turns_three(self):
        fig, ax = plt.subplots(subplot_kw={'polar': True})
        ax = task_func(ax, 3)
        self.assertEqual(ax.get_rlabel_position(), 135.0)
        self.assertEqual(len(ax.lines), 1)  # Check if one line is created

    def test_num_turns_negative(self):
        fig, ax = plt.subplots(subplot_kw={'polar': True})
        ax = task_func(ax, -1)
        self.assertEqual(ax.get_rlabel_position(), -45.0)  # Check for negative turns
        self.assertEqual(len(ax.lines), 1)  # Check if one line is created

if __name__ == '__main__':
    unittest.main()