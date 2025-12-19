import unittest
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Here is your prompt:
def task_func(mu=0, sigma=1):
    """
    Draw and return a subplot of a normal distribution with the given mean and standard deviation,
    utilizing numpy's linspace to create an array of 100 linearly spaced numbers between
    `mu - 3*sigma` and `mu + 3*sigma`.

    Parameters:
    mu (float): The mean of the distribution. Default is 0.
    sigma (float): The standard deviation of the distribution. Default is 1.

    Returns:
    matplotlib.axes.Axes: The subplot representing the normal distribution.

    Requirements:
    - numpy
    - matplotlib.pyplot
    - scipy.stats.norm

    Example:
    >>> ax = task_func(mu=5, sigma=2)
    >>> ax
    <Axes: >
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """

    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    y = norm.pdf(x, mu, sigma)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    return ax

class TestTaskFunc(unittest.TestCase):

    def test_default_parameters(self):
        ax = task_func()
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines), 1)  # Check if a line has been plotted

    def test_custom_mean(self):
        mu = 5
        ax = task_func(mu=mu)
        self.assertIsInstance(ax, plt.Axes)
        x_values = ax.lines[0].get_xdata()
        self.assertAlmostEqual(np.mean(x_values), mu, delta=0.1)  # Check mean is approximately mu

    def test_custom_std_dev(self):
        sigma = 2
        ax = task_func(sigma=sigma)
        self.assertIsInstance(ax, plt.Axes)
        y_values = ax.lines[0].get_ydata()
        self.assertTrue(np.all(y_values >= 0))  # Check that all y values are non-negative

    def test_negative_std_dev(self):
        with self.assertRaises(ValueError):
            task_func(sigma=-1)  # Expecting failure for negative std deviation

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            task_func(mu='a')  # Expecting failure for non-numeric mean
        with self.assertRaises(TypeError):
            task_func(sigma='b')  # Expecting failure for non-numeric standard deviation

if __name__ == '__main__':
    unittest.main()