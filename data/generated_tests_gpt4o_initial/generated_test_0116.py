import numpy as np
import matplotlib.pyplot as plt
import unittest

# Here is your prompt:
import numpy as np
import matplotlib.pyplot as plt

def task_func(mu, sigma, sample_size):
    """
    Generates a numpy array of random samples drawn from a normal distribution
    and plots the histogram of these samples. This function specifies the mean (mu), 
    standard deviation (sigma), and sample size (sample_size), making it useful 
    for simulating data, conducting statistical experiments, or initializing 
    algorithms that require normally distributed data with visualization.

    Parameters:
        mu (float): The mean of the normal distribution.
        sigma (float): The standard deviation of the normal distribution.
        sample_size (int): The number of samples to draw from the distribution.

    Returns:
        ndarray: A numpy array of shape (sample_size,) containing samples drawn from the
                 specified normal distribution.

    Notes:
        Plots a histogram of the generated samples to show the distribution. The histogram
        features:
        - X-axis labeled "Sample values", representing the value of the samples.
        - Y-axis labeled "Frequency", showing how often each value occurs.
        - Title "Histogram of Generated Samples", describing the content of the graph.
        - Number of bins set to 30, to discretize the sample data into 30 intervals.
        - Alpha value of 0.75 for bin transparency, making the histogram semi-transparent.
        - Color 'blue', giving the histogram a blue color.

    Requirements:
    - numpy
    - matplotlib.pyplot

    Examples:
    >>> data = task_func(0, 1, 1000)
    >>> len(data)
    1000
    >>> isinstance(data, np.ndarray)
    True
    """

    samples = np.random.normal(mu, sigma, sample_size)

    # Plotting the histogram of the samples
    plt.hist(samples, bins=30, alpha=0.75, color='blue')
    plt.title('Histogram of Generated Samples')
    plt.xlabel('Sample values')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

    return samples


class TestTaskFunc(unittest.TestCase):

    def test_output_shape(self):
        """Test that the output is of the correct shape."""
        mu = 0
        sigma = 1
        sample_size = 1000
        result = task_func(mu, sigma, sample_size)
        self.assertEqual(result.shape, (sample_size,), "Output shape is incorrect.")

    def test_output_type(self):
        """Test that the output is a numpy array."""
        mu = 0
        sigma = 1
        sample_size = 1000
        result = task_func(mu, sigma, sample_size)
        self.assertIsInstance(result, np.ndarray, "Output is not a numpy array.")

    def test_sample_size(self):
        """Test that the number of samples generated is correct."""
        mu = 0
        sigma = 1
        sample_size = 500
        result = task_func(mu, sigma, sample_size)
        self.assertEqual(len(result), sample_size, "Number of samples generated is incorrect.")

    def test_mean_of_samples(self):
        """Test that the mean of the samples is approximately equal to mu."""
        mu = 5
        sigma = 2
        sample_size = 10000
        result = task_func(mu, sigma, sample_size)
        self.assertAlmostEqual(np.mean(result), mu, delta=0.1, msg="Mean of samples is not close to mu.")

    def test_std_of_samples(self):
        """Test that the standard deviation of samples is approximately equal to sigma."""
        mu = 0
        sigma = 1
        sample_size = 10000
        result = task_func(mu, sigma, sample_size)
        self.assertAlmostEqual(np.std(result), sigma, delta=0.1, msg="Standard deviation of samples is not close to sigma.")


if __name__ == '__main__':
    unittest.main()