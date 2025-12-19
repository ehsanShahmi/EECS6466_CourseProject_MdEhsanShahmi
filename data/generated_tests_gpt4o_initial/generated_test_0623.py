import unittest
from itertools import chain
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Here is your prompt:
def task_func(L):
    """
    Convert a list of lists into a list of integers, apply the KMeans clustering, 
    and return a scatter plot 'matplotlib.axes.Axes' with data points color-coded by their cluster.

    Requirements:
    - itertools.chain
    - numpy
    - sklearn.cluster

    Parameters:
    L (list of lists): A list of lists where each sublist contains integers.

    Returns:
    matplotlib.axes.Axes: An Axes object representing the scatter plot.

    Example:
    >>> ax = task_func([[1, 2, 3], [50, 60, 70], [100, 110, 120]])
    """
    # Constants
    N_CLUSTERS = 3

    data = list(chain(*L))
    data = np.array(data).reshape(-1, 1)

    kmeans = KMeans(n_clusters=N_CLUSTERS).fit(data)

    fig, ax = plt.subplots()
    ax.scatter(data, [0]*len(data), c=kmeans.labels_.astype(float))
    
    return ax

class TestTaskFunc(unittest.TestCase):
    
    def test_empty_input(self):
        """Test with empty list of lists."""
        result = task_func([[]])
        self.assertIsInstance(result, plt.Axes)

    def test_single_cluster(self):
        """Test with a list that will clearly form a single cluster."""
        result = task_func([[1, 2, 3]])
        self.assertIsInstance(result, plt.Axes)

    def test_multiple_clusters(self):
        """Test with distinct points to form multiple clusters."""
        result = task_func([[1, 2, 3], [50, 51, 52], [100, 101, 102]])
        self.assertIsInstance(result, plt.Axes)

    def test_non_integer_input(self):
        """Test with non-integer values, expecting to handle them gracefully."""
        with self.assertRaises(ValueError):
            task_func([[1.5, 2.5], ['a', 'b']])

    def test_large_numbers(self):
        """Test with large integer values to check for performance and clustering."""
        result = task_func([[10000, 20000, 30000], [40000, 50000, 60000]])
        self.assertIsInstance(result, plt.Axes)

if __name__ == '__main__':
    unittest.main()