import unittest
import random
import matplotlib.pyplot as plt

def task_func(points: int):
    """
    Generate a plot of random numbers such that indices are on the x-axis and generated numbers are on the y-axis.

    Parameters:
    - points (int): Number of random points to generate.

    Returns:
    - Returns a tuple containing:
        - A list of generated random numbers.
        - A matplotlib Axes object representing the plot.
    """
    x = list(range(points))
    y = [random.random() for _ in range(points)]

    _, ax = plt.subplots()
    ax.plot(x, y)

    return y, ax


class TestTaskFunc(unittest.TestCase):

    def test_zero_points(self):
        """Test when no points are generated (points = 0)"""
        y, ax = task_func(0)
        self.assertEqual(y, [])
        self.assertIsInstance(ax, plt.Axes)

    def test_one_point(self):
        """Test when one point is generated (points = 1)"""
        random.seed(0)
        y, ax = task_func(1)
        self.assertEqual(len(y), 1)
        self.assertIsInstance(ax, plt.Axes)

    def test_multiple_points(self):
        """Test when multiple points are generated (points > 1)"""
        random.seed(0)
        y, ax = task_func(5)
        self.assertEqual(len(y), 5)
        self.assertIsInstance(ax, plt.Axes)

    def test_randomness(self):
        """Test that the generated values are random"""
        random.seed(0)
        y1, _ = task_func(5)
        random.seed(0)
        y2, _ = task_func(5)
        self.assertEqual(y1, y2)  # Ensure the same seed produces the same results

    def test_return_type(self):
        """Test return type is tuple containing list and Axes object."""
        y, ax = task_func(10)
        self.assertIsInstance(y, list)
        self.assertIsInstance(ax, plt.Axes)


if __name__ == '__main__':
    unittest.main()