import unittest
import matplotlib.pyplot as plt
import numpy as np

# Here is your prompt:
def task_func(n, seed=0):
    """
    Generates a simple scatter plot with 'n' points.

    Parameters:
    - n (int): The number of points to be plotted.
    - seed (int, optional): The seed for the random number generator. Defaults to None.

    Returns:
    - plot (matplotlib.figure.Figure): The generated plot titled "Scatter plot of random points", with x-axis labeled "X" and y-axis labeled "Y".
    - points (list of tuples): List containing the (x, y) coordinates of the plotted points.

    Requirements:
    - numpy
    - matplotlib.pyplot
    
    Example:
    >>> task_func(5)
    (<Figure size 640x480 with 1 Axes>, [(0.5488135039273248, 0.6458941130666561), (0.7151893663724195, 0.4375872112626925), (0.6027633760716439, 0.8917730007820798), (0.5448831829968969, 0.9636627605010293), (0.4236547993389047, 0.3834415188257777)])
    """

    # Setting the random seed for reproducibility
    np.random.seed(seed)

    # Generating random points
    x = np.random.rand(n)
    y = np.random.rand(n)

    # Plotting
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_title("Scatter plot of random points")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    return fig, list(zip(x, y))


class TestTaskFunc(unittest.TestCase):

    def test_return_type(self):
        fig, points = task_func(10)
        self.assertIsInstance(fig, plt.Figure, "Return value should be a matplotlib Figure.")
        self.assertIsInstance(points, list, "Return points should be in list format.")

    def test_point_count(self):
        n = 20
        _, points = task_func(n)
        self.assertEqual(len(points), n, "The number of points returned should match 'n'.")

    def test_point_coordinates_range(self):
        _, points = task_func(100, seed=42)
        for x, y in points:
            self.assertGreaterEqual(x, 0, "X coordinate should be greater than or equal to 0.")
            self.assertLessEqual(x, 1, "X coordinate should be less than or equal to 1.")
            self.assertGreaterEqual(y, 0, "Y coordinate should be greater than or equal to 0.")
            self.assertLessEqual(y, 1, "Y coordinate should be less than or equal to 1.")

    def test_seed_reproducibility(self):
        _, points_seed_0 = task_func(10, seed=0)
        _, points_seed_1 = task_func(10, seed=0)
        self.assertEqual(points_seed_0, points_seed_1, "The points should be reproducible with the same seed.")

    def test_plot_title_and_labels(self):
        fig, _ = task_func(10)
        ax = fig.axes[0]
        self.assertEqual(ax.get_title(), "Scatter plot of random points", "Plot title is incorrect.")
        self.assertEqual(ax.get_xlabel(), "X", "X-axis label is incorrect.")
        self.assertEqual(ax.get_ylabel(), "Y", "Y-axis label is incorrect.")


if __name__ == '__main__':
    unittest.main()