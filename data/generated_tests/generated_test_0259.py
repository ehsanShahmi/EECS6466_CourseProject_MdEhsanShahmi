import unittest
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

class TestTaskFunction(unittest.TestCase):

    def setUp(self):
        """Set up a figure and polar axis for plotting before each test."""
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, polar=True)

    def tearDown(self):
        """Close the figure after each test."""
        plt.close(self.fig)

    def test_valid_input(self):
        """Test the function with valid inputs."""
        num_points = 100
        ax = task_func(self.ax, num_points)
        self.assertIsInstance(ax, matplotlib.axes.Axes)
        self.assertEqual(len(ax.collections), 1)  # Check if points were plotted

    def test_negative_num_points(self):
        """Test the function raises ValueError with negative num_points."""
        with self.assertRaises(ValueError):
            task_func(self.ax, -10)

    def test_non_axes_input(self):
        """Test the function raises ValueError with non-Axes input."""
        with self.assertRaises(ValueError):
            task_func(None, 10)  # Passing None instead of Axes

    def test_zero_points(self):
        """Test the function with zero points."""
        ax = task_func(self.ax, 0)
        self.assertIsInstance(ax, matplotlib.axes.Axes)
        self.assertEqual(len(ax.collections), 0)  # Check for no points plotted

    def test_check_rlabel_position(self):
        """Test that the radial label position is set correctly."""
        num_points = 50
        ax = task_func(self.ax, num_points)
        self.assertEqual(ax.get_rlabel_position(), num_points / 10)

if __name__ == '__main__':
    unittest.main()