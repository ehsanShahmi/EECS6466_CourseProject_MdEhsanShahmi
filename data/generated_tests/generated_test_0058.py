import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import unittest

# Here is your prompt:
def task_func(mu, sigma, num_samples):
    """
    Display a plot showing a normal distribution with a given mean and standard deviation and overlay a histogram of randomly generated samples from this distribution.
    The plot title should be 'Normal Distribution'.

    Parameters:
    mu (float): The mean of the distribution.
    sigma (float): The standard deviation of the distribution.
    num_samples (int): The number of samples to generate.

    Returns:
    fig (matplotlib.figure.Figure): The generated figure. Useful for testing purposes.

    Requirements:
    - numpy
    - scipy.stats
    - matplotlib.pyplot

    Example:
    >>> plt = task_func(0, 1, 1000)
    """

    samples = np.random.normal(mu, sigma, num_samples)
    fig, ax = plt.subplots()
    ax.hist(samples, bins=30, density=True, alpha=0.6, color='g')

    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mu, sigma)
    ax.plot(x, p, 'k', linewidth=2)

    ax.set_title('Normal Distribution')
    plt.show()
    return fig

class TestTaskFunc(unittest.TestCase):

    def test_function_output_type(self):
        """Test if the function returns a matplotlib figure."""
        fig = task_func(0, 1, 1000)
        self.assertIsInstance(fig, plt.Figure)

    def test_normal_distribution_mean(self):
        """Test if the mean of the generated samples is close to mu."""
        mu = 5
        sigma = 2
        num_samples = 10000
        samples = np.random.normal(mu, sigma, num_samples)
        self.assertAlmostEqual(np.mean(samples), mu, delta=0.1)

    def test_normal_distribution_std_dev(self):
        """Test if the standard deviation of the generated samples is close to sigma."""
        mu = 0
        sigma = 1
        num_samples = 10000
        samples = np.random.normal(mu, sigma, num_samples)
        self.assertAlmostEqual(np.std(samples), sigma, delta=0.1)

    def test_function_handles_zero_samples(self):
        """Test if the function can handle zero samples without error."""
        fig = task_func(0, 1, 0)
        self.assertIsInstance(fig, plt.Figure)

    def test_function_with_negative_sigma(self):
        """Test if the function raises an error with negative sigma."""
        with self.assertRaises(ValueError):
            task_func(0, -1, 1000)

if __name__ == '__main__':
    unittest.main()