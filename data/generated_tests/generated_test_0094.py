import numpy as np
import matplotlib.pyplot as plt
import unittest
from scipy.stats import norm

# Here is your prompt:
def task_func(mean, std_dev, num_samples):
    """
    Generates a histogram of samples drawn from a normal distribution and overlays
    the probability density function (PDF) of the normal distribution. The plot is titled
    with the fit results, showing the mean and standard deviation used in the generation.
    The function returns both the plot and the samples generated.

    Parameters:
        mean (float): The mean of the normal distribution.
        std_dev (float): The standard deviation of the normal distribution.
        num_samples (int): The number of samples to draw from the distribution.

    Requirements:
    - numpy
    - scipy.stats.norm
    - matplotlib.pyplot

    Notes:
    - The plot title is "Fit results: mean = %.2f, std = %.2f". This title format on the plot displays the mean and standard deviation
        of the normal distribution used to generate the histogram. The values are presented in a format where %.2f
        is replaced by the floating-point numbers corresponding to `mean` and `std_dev` respectively, rounded to two decimal places.
    - The number of bins is set to 30

    Returns:
        tuple: A tuple containing:
            - matplotlib.figure.Figure: The figure object for the plot.
            - numpy.ndarray: An array of samples drawn from the normal distribution.

    Examples:
    >>> import matplotlib
    >>> samples, fig = task_func(0, 1, 1000)
    >>> len(samples)
    1000
    >>> type(samples)
    <class 'numpy.ndarray'>
    >>> isinstance(fig, matplotlib.figure.Figure)
    True

    Note: The actual values in the array depend on the random seed and will vary each time the function is called.
    """

    samples = np.random.normal(mean, std_dev, num_samples)
    fig, ax = plt.subplots()
    ax.hist(samples, bins=30, density=True, alpha=0.6, color='g')

    xmin, xmax = ax.get_xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mean, std_dev)
    ax.plot(x, p, 'k', linewidth=2)
    title = "Fit results: mean = %.2f,  std = %.2f" % (mean, std_dev)
    ax.set_title(title)

    return samples, fig


class TestTaskFunc(unittest.TestCase):

    def test_sample_length(self):
        """Test if the number of generated samples matches the input num_samples."""
        mean = 0
        std_dev = 1
        num_samples = 1000
        samples, _ = task_func(mean, std_dev, num_samples)
        self.assertEqual(len(samples), num_samples)

    def test_sample_type(self):
        """Test if the generated samples are of numpy ndarray type."""
        mean = 0
        std_dev = 1
        num_samples = 1000
        samples, _ = task_func(mean, std_dev, num_samples)
        self.assertIsInstance(samples, np.ndarray)

    def test_figure_type(self):
        """Test if the returned figure is of type matplotlib.figure.Figure."""
        mean = 0
        std_dev = 1
        num_samples = 1000
        _, fig = task_func(mean, std_dev, num_samples)
        self.assertIsInstance(fig, plt.Figure)

    def test_title_format(self):
        """Test if the title of the plot is formatted correctly."""
        mean = 0
        std_dev = 2
        num_samples = 1000
        _, fig = task_func(mean, std_dev, num_samples)
        expected_title = f"Fit results: mean = {mean:.2f},  std = {std_dev:.2f}"
        self.assertEqual(fig.axes[0].title.get_text(), expected_title)

    def test_distribution_properties(self):
        """Test if the samples generated have the expected mean and std deviation."""
        mean = 5
        std_dev = 2
        num_samples = 10000
        samples, _ = task_func(mean, std_dev, num_samples)
        self.assertAlmostEqual(np.mean(samples), mean, delta=0.1)
        self.assertAlmostEqual(np.std(samples), std_dev, delta=0.1)


if __name__ == '__main__':
    unittest.main()