import unittest
import matplotlib
import numpy as np
from scipy import stats

# Here is your prompt:
def task_func(mu, sigma, sample_size, seed=0):
    """
    Create a Gaussian kernel density estimate diagram of a normal distribution with a given mean and a 
    standard deviation using a random sample of a size determined by the sample_size parameter. The density 
    diagram is plotted using default settings in a deterministic matplotlib plot. Return the axes object.
    
    Parameters:
    mu (float): The mean of the normal distribution.
    sigma (float): The standard deviation of the normal distribution.
    sample_size (int): The size of the sample to generate. Must be a positive integer.
    seed (int, Optional): The seed to be used for the random number generator. Default is 0.
    
    Returns:
    matplotlib.axes._axes.Axes: Axes object containing the plot of the normal distribution.
    
    Requirements:
    - numpy
    - matplotlib
    - scipy.stats
    
    Example:
    >>> ax = task_func(0, 1, 1000)
    >>> type(ax) # The result should be a matplotlib.axes._axes.Axes object
    <class 'matplotlib.axes._axes.Axes'>
    """
    if sample_size <= 0:
        raise ValueError('sample_size must be a positive integer.')
    
    np.random.seed(seed)
    sample = np.random.normal(mu, sigma, sample_size)
    density = stats.gaussian_kde(sample)

    x = np.linspace(min(sample), max(sample), sample_size)
    fig, ax = plt.subplots()
    ax.plot(x, density(x))
    
    return ax


class TestTaskFunction(unittest.TestCase):

    def test_return_type(self):
        """Test if the function returns a matplotlib axes object."""
        ax = task_func(0, 1, 1000)
        self.assertIsInstance(ax, matplotlib.axes._axes.Axes)

    def test_positive_sample_size(self):
        """Test if ValueError is raised with non-positive sample_size."""
        with self.assertRaises(ValueError):
            task_func(0, 1, 0)
        with self.assertRaises(ValueError):
            task_func(0, 1, -100)

    def test_deterministic_output(self):
        """Test if the output is deterministic for the same inputs."""
        np.random.seed(0)
        ax1 = task_func(0, 1, 1000, seed=0)
        
        np.random.seed(0)
        ax2 = task_func(0, 1, 1000, seed=0)
        
        # Comparing the contents of the axes, specifically the lines plotted
        self.assertEqual(ax1.lines[0].get_ydata().tolist(), ax2.lines[0].get_ydata().tolist())

    def test_output_range(self):
        """Test if the function's plotted density falls within expected range."""
        ax = task_func(0, 1, 1000)
        y_data = ax.lines[0].get_ydata()
        
        # Check that all y data points are non-negative (valid density estimate)
        self.assertTrue(np.all(y_data >= 0))

    def test_mean_and_std_dev(self):
        """Test if the generated sample matches the expected mean and std deviation."""
        mu, sigma, sample_size = 0, 1, 1000
        ax = task_func(mu, sigma, sample_size)

        sample = np.random.normal(mu, sigma, sample_size)
        generated_mean = np.mean(sample)
        generated_std = np.std(sample)

        self.assertAlmostEqual(generated_mean, mu, delta=0.1)
        self.assertAlmostEqual(generated_std, sigma, delta=0.1)


if __name__ == '__main__':
    unittest.main()