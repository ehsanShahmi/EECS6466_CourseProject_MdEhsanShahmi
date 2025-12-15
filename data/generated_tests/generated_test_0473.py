import numpy as np
import matplotlib.pyplot as plt
import itertools
import unittest

# Here is your prompt:
def task_func(n_walks, n_steps, seed=None):
    """
    Create and plot `n_walks` number of random walks, each with `n_steps` steps.

    The function checks for valid n_walks and n_steps, then generates walks via numpy.
    Each walk is plotted in a different color cycling through a predefined set of colors:
    ['b', 'g', 'r', 'c', 'm', 'y', 'k'].

    Parameters:
    - n_walks (int): The number of random walks to be generated and plotted.
    - n_steps (int): The number of steps in each random walk.
    - seed (int, optional): Seed for random number generation. Default is None.

    Returns:
    - ax (plt.Axes): A Matplotlib Axes containing the plotted random walks.

    Requirements:
    - numpy
    - matplotlib
    - itertools

    Example:
    >>> ax = task_func(5, 100, seed=42)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    >>> ax.get_xticklabels()
    [Text(-20.0, 0, '−20'), Text(0.0, 0, '0'), Text(20.0, 0, '20'), Text(40.0, 0, '40'), Text(60.0, 0, '60'), Text(80.0, 0, '80'), Text(100.0, 0, '100'), Text(120.0, 0, '120')]
    """

    if n_walks < 0 or n_steps < 0:
        raise ValueError("Walks and steps cannot be negative.")
    np.random.seed(seed)
    COLORS = ["b", "g", "r", "c", "m", "y", "k"]
    color_cycle = itertools.cycle(COLORS)
    fig, ax = plt.subplots()
    for _ in range(n_walks):
        walk = np.random.choice([-1, 1], size=n_steps)
        walk = np.cumsum(walk)
        ax.plot(walk, next(color_cycle))
    return ax

class TestRandomWalks(unittest.TestCase):

    def test_valid_walks_and_steps(self):
        """Test that the function returns an Axes object for valid inputs."""
        ax = task_func(5, 100)
        self.assertIsInstance(ax, plt.Axes)

    def test_zero_walks(self):
        """Test that zero walks result in an empty Axes."""
        ax = task_func(0, 100)
        # Check that no lines have been plotted
        lines = ax.get_lines()
        self.assertEqual(len(lines), 0)

    def test_negative_walks(self):
        """Test that a ValueError is raised for negative walks."""
        with self.assertRaises(ValueError):
            task_func(-1, 100)

    def test_negative_steps(self):
        """Test that a ValueError is raised for negative steps."""
        with self.assertRaises(ValueError):
            task_func(5, -1)

    def test_seed_functionality(self):
        """Test that using a seed produces consistent results."""
        np.random.seed(42)  # Same seed for consistent random behavior
        ax1 = task_func(5, 100, seed=42)
        np.random.seed(42)  # Reset the seed to repeat the sequence
        ax2 = task_func(5, 100, seed=42)

        # We can check if the x and y values are the same for both plots
        lines1 = ax1.get_lines()
        lines2 = ax2.get_lines()

        for line1, line2 in zip(lines1, lines2):
            np.testing.assert_array_equal(line1.get_xdata(), line2.get_xdata())
            np.testing.assert_array_equal(line1.get_ydata(), line2.get_ydata())

# Running the test suite
if __name__ == '__main__':
    unittest.main()