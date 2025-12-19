import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt
import unittest

def task_func(data):
    """
    Draw a scatter plot of dots and mark the point with the maximum y-value. Return the axes object as
    well as the maximum y-value point. 
    
    Parameters:
    data (list of tuples): A list where each tuple contains two floats representing x and y coordinates.
    
    Returns:
    matplotlib.axes.Axes: Axes object with the scatter plot, with the x-axis labeled 'x', the y-axis labeled 'y', and the title 'Points with Max Y Point Highlighted'.
    tuple: The point with the maximum y-value.
    
    Requirements:
    - numpy
    - operator
    - matplotlib.pyplot

    Example:
    >>> ax, point = task_func([(0.1, 0.2), (0.5, 0.6), (0.3, 0.9)])
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """
    max_y_point = max(data, key=itemgetter(1))
    points = np.array(data)
    x = points[:,0]
    y = points[:,1]

    fig, ax = plt.subplots()
    ax.scatter(x, y, label='Points')
    ax.scatter(*max_y_point, color='red', label='Max Y Point')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Points with Max Y Point Highlighted')
    ax.legend()
    return ax, max_y_point

class TestTaskFunc(unittest.TestCase):

    def test_basic_functionality(self):
        ax, point = task_func([(0.1, 0.2), (0.5, 0.6), (0.3, 0.9)])
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(point, (0.3, 0.9))

    def test_multiple_points_same_max_y(self):
        ax, point = task_func([(1.0, 2.0), (2.0, 2.0), (0.5, 1.5)])
        self.assertIsInstance(ax, plt.Axes)
        self.assertIn(point, [(1.0, 2.0), (2.0, 2.0)])

    def test_negative_coordinates(self):
        ax, point = task_func([(-1.0, -2.0), (-2.0, -1.0), (-0.5, -0.5)])
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(point, (-0.5, -0.5))

    def test_same_y_values(self):
        ax, point = task_func([(0.0, 5.0), (1.0, 5.0), (2.0, 5.0)])
        self.assertIsInstance(ax, plt.Axes)
        self.assertIn(point, [(0.0, 5.0), (1.0, 5.0), (2.0, 5.0)])

    def test_empty_data(self):
        with self.assertRaises(ValueError):
            task_func([])

if __name__ == '__main__':
    unittest.main()