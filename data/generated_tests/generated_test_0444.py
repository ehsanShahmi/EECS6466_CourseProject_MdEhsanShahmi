import unittest
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Here is your prompt:
def task_func(n_points=100, random_seed=None):
    """
    Generate an array of random 3D dots in the range [0, 1) for each dimension
    and draw them in a 3D scatter plot.

    Parameters:
    n_points (int): The number of points to generate and plot. Default is 100.
    random_seed (int, optional): Seed for the random number generator. Default is None.

    Returns:
    tuple: A tuple containing:
        - points (ndarray): A numpy ndarray of shape (n_points, 3) with the coordinates of the points.
        - plot (Axes3D): A 3D scatter plot of the generated points.

    Requirements:
    - numpy
    - matplotlib.pyplot

    Example:
    >>> points, plot = task_func(200, random_seed=42)
    >>> type(points)
    <class 'numpy.ndarray'>
    >>> type(plot)
    <class 'mpl_toolkits.mplot3d.axes3d.Axes3D'>
    """
    np.random.seed(random_seed)
    points = np.random.random((n_points, 3))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(points[:, 0], points[:, 1], points[:, 2])

    return points, ax

class TestTaskFunc(unittest.TestCase):
    
    def test_return_type(self):
        points, plot = task_func(100)
        self.assertIsInstance(points, np.ndarray)
        self.assertEqual(points.shape, (100, 3))
        self.assertIsInstance(plot, Axes3D)

    def test_points_with_default_seed(self):
        points, _ = task_func(100)
        self.assertTrue(np.all((points >= 0) & (points < 1)))

    def test_random_seed_affects_output(self):
        points1, _ = task_func(100, random_seed=42)
        points2, _ = task_func(100, random_seed=42)
        np.testing.assert_array_equal(points1, points2)

    def test_points_count(self):
        points, _ = task_func(50)
        self.assertEqual(points.shape[0], 50)

    def test_points_range(self):
        points, _ = task_func(100)
        self.assertTrue(np.all(points >= 0))
        self.assertTrue(np.all(points < 1))

if __name__ == '__main__':
    unittest.main()