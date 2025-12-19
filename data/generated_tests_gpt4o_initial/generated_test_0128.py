import unittest
import numpy as np
import matplotlib.pyplot as plt

# Here is your prompt:
import numpy as np
import matplotlib.pyplot as plt
from random import randint
import math

def task_func(POINTS=100):
    """
    Simulates a random walk in a two-dimensional space and draws the path using matplotlib.
    The walk is determined by randomly choosing directions at each step. The function generates
    two numpy arrays representing the x and y coordinates of each step and plots these points
    to visualize the path of the walk.

    Parameters:
        POINTS (int): The number of steps in the random walk. Default is 100.

    Returns:
        A matplotlib figure object representing the plot of the random walk.

    Requirements:
        - numpy
        - matplotlib.pyplot
        - random.randint
        - math

    Examples:
        >>> import matplotlib
        >>> fig = task_func(200)  # Displays a plot of a random walk with 200 steps
        >>> isinstance(fig, matplotlib.figure.Figure)
        True
    """
    x = np.zeros(POINTS)
    y = np.zeros(POINTS)

    for i in range(1, POINTS):
        val = randint(0, 1)
        if val == 1:
            x[i] = x[i - 1] + math.cos(2 * math.pi * val)
            y[i] = y[i - 1] + math.sin(2 * math.pi * val)
        else:
            x[i] = x[i - 1] - math.cos(2 * math.pi * val)
            y[i] = y[i - 1] - math.sin(2 * math.pi * val)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()
    return fig

class TestRandomWalk(unittest.TestCase):

    def test_default_points_type(self):
        fig = task_func()
        self.assertIsInstance(fig, plt.Figure)

    def test_custom_points_type(self):
        fig = task_func(150)
        self.assertIsInstance(fig, plt.Figure)

    def test_points_value(self):
        fig = task_func(0)
        # Should still return a figure even if POINTS=0
        self.assertIsInstance(fig, plt.Figure)

    def test_correct_shape_output(self):
        x, y = np.zeros(100), np.zeros(100)
        for i in range(1, 100):
            val = randint(0, 1)
            if val == 1:
                x[i] = x[i - 1] + math.cos(2 * math.pi * val)
                y[i] = y[i - 1] + math.sin(2 * math.pi * val)
            else:
                x[i] = x[i - 1] - math.cos(2 * math.pi * val)
                y[i] = y[i - 1] - math.sin(2 * math.pi * val)
        
        fig = task_func(100)
        ax = fig.get_axes()[0]
        lines = ax.get_lines()
        self.assertEqual(len(lines), 1)
        self.assertEqual(len(lines[0].get_xdata()), 100)
        self.assertEqual(len(lines[0].get_ydata()), 100)

    def test_non_positive_points(self):
        with self.assertRaises(ValueError):
            task_func(-1)

if __name__ == '__main__':
    unittest.main()