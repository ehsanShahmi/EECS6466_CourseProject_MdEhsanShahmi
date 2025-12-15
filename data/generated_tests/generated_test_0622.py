import unittest
import numpy as np
from scipy.stats import norm
from itertools import chain
import matplotlib.pyplot as plt

# Here is your prompt:
def task_func(L):
    '''
    Convert a list of lists 'L' into a flattened list of integers, then fit a normal distribution to the data 
    and plot a histogram with the fitted normal distribution overlay.

    Requirements:
    - numpy
    - itertools.chain
    - scipy.stats.norm
    - matplotlib.pyplot

    Parameters:
    L (list of lists): A nested list where each inner list contains integers.

    Returns:
    matplotlib.axes._axes.Axes: Axes object with the plotted histogram and normal distribution overlay.

    Example:
    >>> ax = task_func([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    '''

    data = list(chain(*L))
    mu, std = norm.fit(data)

    fig, ax = plt.subplots()
    ax.hist(data, bins=30, density=True, alpha=0.6, color='g')

    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    ax.plot(x, p, 'k', linewidth=2)
    title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
    ax.set_title(title)

    return ax

class TestTaskFunc(unittest.TestCase):

    def test_empty_input(self):
        """Test that the function handles empty input correctly."""
        ax = task_func([])
        self.assertEqual(ax.patches, [], "Expected no histogram for empty input.")

    def test_single_list_input(self):
        """Test function with a single list input."""
        ax = task_func([[1, 2, 3, 4, 5]])
        self.assertIsNotNone(ax, "Expected an Axes object to be returned.")
        self.assertGreater(len(ax.patches), 0, "Expected histogram bars to be created.")

    def test_multiple_list_input(self):
        """Test function with multiple lists input."""
        ax = task_func([[1, 2], [3, 4], [5, 6]])
        self.assertIsNotNone(ax, "Expected an Axes object to be returned.")
        self.assertGreater(len(ax.patches), 0, "Expected histogram bars to be created.")

    def test_fitted_distribution_parameters(self):
        """Test the parameters of the fitted normal distribution."""
        data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        ax = task_func(data)
        flattened_data = list(chain(*data))
        mu, std = norm.fit(flattened_data)
        
        # Check if the fitted mu and std are plausible
        mu_x, std_x = map(float, ax.get_title().split('=')[1:3])
        self.assertAlmostEqual(mu, mu_x, places=2, msg="Fitted mu value does not match the expected value.")
        self.assertAlmostEqual(std, std_x, places=2, msg="Fitted std value does not match the expected value.")
    
    def test_non_integer_input(self):
        """Test for handling non-integer values."""
        with self.assertRaises(TypeError):
            task_func([[1.5, 2.3], [3, 4]])  # Expecting TypeError due to floats in the input lists

if __name__ == '__main__':
    unittest.main()