import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import unittest

# The provided prompt with the function definition
def task_func(length):
    """
    Create a normal distribution with a given length, plot its histogram alongside the 
    probability density function, and return the distribution and the plot.
    
    Parameters:
    - length (int): The length of the distribution to be generated.
    
    Returns:
    - tuple: A tuple containing:
        1. numpy array with the normal distribution.
        2. matplotlib Axes object representing the plot.
    
    Requirements:
    - numpy
    - scipy.stats.norm
    - matplotlib.pyplot
    
    Note:
    - This function use this constant MU (mean): 0, SIGMA (standard deviation): 1
    
    Example:
    >>> np.random.seed(0)
    >>> distribution, ax = task_func(1000)
    >>> print(type(distribution))
    <class 'numpy.ndarray'>
    >>> len(ax.get_lines())
    1
    >>> plt.close()
    """

    MU = 0
    SIGMA = 1
    
    distribution = np.random.normal(MU, SIGMA, length)
    fig, ax = plt.subplots()
    ax.hist(distribution, 30, density=True, label='Histogram')
    ax.plot(np.sort(distribution), norm.pdf(np.sort(distribution), MU, SIGMA), 
            linewidth=2, color='r', label='PDF')
    ax.legend()
    
    return distribution, ax

# Test suite
class TestTaskFunc(unittest.TestCase):
    
    def test_output_type(self):
        """Test the type of the output of the task_func."""
        np.random.seed(0)
        distribution, ax = task_func(1000)
        self.assertIsInstance(distribution, np.ndarray)
        self.assertIsInstance(ax, plt.Axes)
        
    def test_output_length(self):
        """Test that the length of the output distribution matches the input length."""
        np.random.seed(0)
        length = 1500
        distribution, ax = task_func(length)
        self.assertEqual(len(distribution), length)
        
    def test_histogram_bins(self):
        """Test that the histogram has been created with the expected number of bins."""
        np.random.seed(0)
        distribution, ax = task_func(1000)
        # The number of bins is set to 30 in the function
        hist_data = ax.hist(distribution, 30, density=True)
        self.assertEqual(len(hist_data[0]), 30)
        
    def test_pdf_line(self):
        """Test that the probability density function line is present."""
        np.random.seed(0)
        distribution, ax = task_func(1000)
        self.assertEqual(len(ax.get_lines()), 1)  # Checking the number of lines added to the Axes

    def test_distribution_mean_std(self):
        """Test if the mean and standard deviation of the generated distribution are close to the expected values."""
        np.random.seed(0)
        distribution, _ = task_func(10000)
        self.assertAlmostEqual(np.mean(distribution), 0, delta=0.1)
        self.assertAlmostEqual(np.std(distribution), 1, delta=0.1)

# Executing the test suite
if __name__ == '__main__':
    unittest.main()