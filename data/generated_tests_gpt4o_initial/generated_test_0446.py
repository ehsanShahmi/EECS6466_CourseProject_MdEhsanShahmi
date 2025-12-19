import unittest
import numpy as np
import matplotlib.pyplot as plt

# Here is your prompt:
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs


def task_func(n_samples=100, centers=3, n_features=2, random_seed=42):
    """
    Create isotropic Gaussian blobs to form clusters and visualize them.

    Parameters:
    - n_samples (int): The total number of points divided among clusters.
    - centers (int): The number of centers to generate.
    - n_features (int): The number of features for each sample.
    - random_seed (int): The seed for the random number generator.

    Returns:
    tuple: A tuple containing:
        - X (numpy.ndarray): The matrix of blob points.
        - y (numpy.ndarray): The vector of blob labels.
        - ax (matplotlib.axes.Axes): The Axes object with the scatter plot.

    Requirements:
    - matplotlib.pyplot
    - sklearn

    Example:
    >>> X, y, ax = task_func(n_samples=500, centers=5, random_seed=0)
    >>> type(X), type(y), type(ax)
    (<class 'numpy.ndarray'>, <class 'numpy.ndarray'>, <class 'matplotlib.axes._axes.Axes'>)
    >>> ax
    <Axes: >
    """

    X, y = make_blobs(
        n_samples=n_samples,
        centers=centers,
        n_features=n_features,
        random_state=random_seed,
    )

    fig, ax = plt.subplots()
    ax.scatter(X[:, 0], X[:, 1], c=y)

    return X, y, ax

class TestTaskFunc(unittest.TestCase):

    def test_output_types(self):
        X, y, ax = task_func(n_samples=100, centers=3, random_seed=42)
        self.assertIsInstance(X, np.ndarray, "X should be a numpy ndarray")
        self.assertIsInstance(y, np.ndarray, "y should be a numpy ndarray")
        self.assertIsInstance(ax, plt.Axes, "ax should be a matplotlib Axes object")

    def test_shape_of_output(self):
        n_samples = 200
        centers = 4
        X, y, ax = task_func(n_samples=n_samples, centers=centers, random_seed=42)
        
        self.assertEqual(X.shape[0], n_samples, "The number of rows in X should be equal to n_samples")
        self.assertEqual(y.shape[0], n_samples, "The number of elements in y should be equal to n_samples")
        self.assertEqual(X.shape[1], 2, "X should have 2 features for 2D data")

    def test_center_count(self):
        n_samples = 150
        centers = 5
        X, y, ax = task_func(n_samples=n_samples, centers=centers, random_seed=42)
        
        unique_labels = set(y)
        self.assertEqual(len(unique_labels), centers, "The number of unique labels in y should match the number of centers")

    def test_default_parameters(self):
        X, y, ax = task_func()
        self.assertEqual(X.shape[0], 100, "Default n_samples should be 100")
        self.assertEqual(len(set(y)), 3, "Default centers should be 3")

    def test_random_seed(self):
        X1, y1, ax1 = task_func(n_samples=100, centers=3, random_seed=42)
        X2, y2, ax2 = task_func(n_samples=100, centers=3, random_seed=42)
        
        np.testing.assert_array_equal(X1, X2, "X should be the same with the same random seed")
        np.testing.assert_array_equal(y1, y2, "y should be the same with the same random seed")

if __name__ == '__main__':
    unittest.main()