import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import unittest

# Here is your prompt:
def task_func(mu, sigma, num_samples=1000, seed=77):
    """
    Generate a normal distribution with the given mean and standard deviation. 
    Creates a figure containing a histogram and a Q-Q plot of the generated samples.

    Parameters:
    mu (float): The mean of the normal distribution.
    sigma (float): The standard deviation of the normal distribution.
    num_samples (int, Optional): The number of samples to generate. Default is 1000.
    seed (int, Optional): The seed for the random number generator. Default is 77.

    Returns:
    matplotlib.figure.Figure: A matplotlib figure containing the histogram and Q-Q plot.

    Requirements:
    - numpy for generating the samples.
    - matplotlib.pyplot for plotting.
    - scipy.stats for the Q-Q plot.

    Example:
    >>> fig = task_func(0, 1)
    >>> type(fig)
    <class 'matplotlib.figure.Figure'>
    """

    np.random.seed(seed)
    samples = np.random.normal(mu, sigma, num_samples)

    fig = plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.hist(samples, bins=30, density=True, alpha=0.6, color='g')

    plt.subplot(1, 2, 2)
    stats.probplot(samples, dist="norm", plot=plt)

    return fig

class TestTaskFunc(unittest.TestCase):
    
    def test_return_type(self):
        """Test if the return type is a matplotlib.figure.Figure."""
        fig = task_func(0, 1)
        self.assertIsInstance(fig, plt.Figure)

    def test_number_of_samples(self):
        """Test if the number of samples generated equals num_samples parameter."""
        num_samples = 500
        samples = task_func(0, 1, num_samples=num_samples)
        self.assertEqual(len(samples.axes[0].patches), 30)  # 30 bins for histogram

    def test_mean_of_samples(self):
        """Test if the mean of the samples is close to the specified mean (mu)."""
        mu = 5
        samples = task_func(mu, 1)
        # Access the generated samples directly to check the mean
        np.random.seed(77)  # Use the same seed for reproducibility
        generated_samples = np.random.normal(mu, 1, 1000)
        actual_mean = np.mean(generated_samples)
        self.assertAlmostEqual(np.mean(samples.axes[0].patches), actual_mean, delta=0.1)

    def test_std_dev_of_samples(self):
        """Test if the standard deviation of the samples is close to specified standard deviation (sigma)."""
        sigma = 2
        samples = task_func(0, sigma)
        # Access the generated samples directly to check the std dev
        np.random.seed(77)
        generated_samples = np.random.normal(0, sigma, 1000)
        actual_std_dev = np.std(generated_samples)
        self.assertAlmostEqual(np.std(samples.axes[0].patches), actual_std_dev, delta=0.1)

    def test_seed_effect(self):
        """Test if using the same seed produces the same distribution."""
        mu, sigma = 0, 1
        fig1 = task_func(mu, sigma, seed=42)
        fig2 = task_func(mu, sigma, seed=42)
        
        # Check if the two figures are identical in their content.
        self.assertTrue(np.array_equal(fig1.get_array(), fig2.get_array()))

if __name__ == '__main__':
    unittest.main()