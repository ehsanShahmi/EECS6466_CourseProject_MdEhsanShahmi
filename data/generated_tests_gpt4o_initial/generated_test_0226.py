import unittest
import numpy as np
import math
import matplotlib.pyplot as plt

# Here is your prompt:
def task_func(range_start=0, range_end=10, step=0.1):
    """
    Create a generator object that generates a sequence of tuples.
    Each tuple contains x and e^x values. Plot the exponential function using these values.

    Returns:
    tuple: 
        - A generator object that yields tuples of (x, e^x).
        - The plotted Axes object of the exponential function.

    Requirements:
    - numpy
    - math
    - matplotlib.pyplot

    Example:
    >>> data, ax = task_func()
    >>> print(next(data))
    (0.0, 1.0)
    >>> ax.get_title()  # Returns the title of the plot
    'Exponential Function Plot'
    """

    x_values = np.arange(range_start, range_end, step)
    data = ((x, math.exp(x)) for x in x_values)
    _, ax = plt.subplots()
    for x, exp_x in data:
        ax.scatter(x, exp_x, color='b')
    ax.set_title("Exponential Function Plot")
    ax.set_xlabel("x")
    ax.set_ylabel("e^x")
    data = ((x, math.exp(x)) for x in x_values)
    return data, ax

class TestTaskFunc(unittest.TestCase):

    def test_generator_start(self):
        data, _ = task_func()
        self.assertEqual(next(data), (0.0, 1.0))

    def test_exponential_values(self):
        data, _ = task_func()
        for x in np.arange(0, 0.2, 0.1):
            self.assertEqual(next(data), (x, math.exp(x)))

    def test_range_end(self):
        data, _ = task_func(0, 1, 0.5)
        expected_values = [(0.0, 1.0), (0.5, math.exp(0.5))]
        for expected in expected_values:
            self.assertEqual(next(data), expected)

    def test_step_size(self):
        data, _ = task_func(0, 1, 0.1)
        self.assertEqual(next(data), (0.0, 1.0))
        self.assertEqual(next(data), (0.1, math.exp(0.1)))

    def test_plot_title(self):
        _, ax = task_func()
        self.assertEqual(ax.get_title(), "Exponential Function Plot")

if __name__ == '__main__':
    unittest.main()