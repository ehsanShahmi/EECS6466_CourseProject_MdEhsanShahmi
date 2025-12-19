import random
import matplotlib.pyplot as plt
import unittest

# Constants
DISTRIBUTION_SIZE = 1000

def task_func(bins=30):
    """
    Generate a Gaussian distribution and plot its histogram.

    Parameters:
    - bins (int, optional): Number of bins for the histogram. Default is 30.

    Returns:
    - tuple: A tuple containing the distribution list and the Axes patch object of the histogram plot.

    Requirements:
    - random
    - matplotlib.pyplot

    Example:
    >>> random.seed(0)
    >>> distribution, ax = task_func()
    >>> len(ax.patches) == 30
    True
    >>> len(distribution)
    1000
    >>> plt.close()
    """

    distribution = [random.gauss(0, 1) for _ in range(DISTRIBUTION_SIZE)]
    ax = plt.hist(distribution, bins=bins, edgecolor='black')[2]
    return distribution, ax


class TestTaskFunc(unittest.TestCase):

    def test_default_bins(self):
        """Test the default number of bins (30) in the histogram."""
        random.seed(0)
        distribution, ax = task_func()
        self.assertEqual(len(ax.patches), 30)
        plt.close()

    def test_distribution_size(self):
        """Test that the length of the generated distribution is 1000."""
        random.seed(0)
        distribution, _ = task_func()
        self.assertEqual(len(distribution), 1000)

    def test_custom_bins(self):
        """Test the function with a custom number of bins."""
        random.seed(0)
        custom_bins = 50
        distribution, ax = task_func(bins=custom_bins)
        self.assertEqual(len(ax.patches), custom_bins)
        plt.close()

    def test_histogram_edge_colors(self):
        """Test that the histogram bars have the expected edge color."""
        random.seed(0)
        distribution, ax = task_func()
        for patch in ax.patches:
            self.assertEqual(patch.get_edgecolor(), (0.0, 0.0, 0.0, 1.0))  # Check if the edge color is black
        plt.close()

    def test_non_integer_bins(self):
        """Test the function with a non-integer number of bins, expecting it to default to 30."""
        random.seed(0)
        distribution, ax = task_func(bins=25.5)
        self.assertEqual(len(ax.patches), 30)  # Check if it defaults to 30
        plt.close()


if __name__ == '__main__':
    unittest.main()