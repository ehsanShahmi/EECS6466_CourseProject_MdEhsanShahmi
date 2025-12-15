import unittest
import matplotlib.pyplot as plt
import numpy as np

def task_func(ax, radius):
    '''
    Draw a circle with a given radius on the polar chart 'ax' and set radial ticks.
    This function manipulates plot data using matplotlib.

    Parameters:
    ax (matplotlib.axes._axes.Axes): The ax to plot on. Must be a polar plot.
    radius (float): The radius of the circle. Must be non-negative.

    Returns:
    matplotlib.axes._axes.Axes: The modified Axes object with the circle plotted.

    Note:
    - If the radius is negative this function will raise ValueError.
    - If 'ax' is not a polar plot this function will raise TypeError.

    Requirements:
    - matplotlib.pyplot
    - numpy

    Example:
    >>> import matplotlib.pyplot as plt
    >>> fig = plt.figure()
    >>> ax = fig.add_subplot(111, polar=True)
    >>> result_ax = task_func(ax, 1.5)
    >>> np.allclose(result_ax.get_lines()[0].get_ydata(), 1.5)
    True
    >>> plt.close()
    '''

    if radius < 0:
        raise ValueError('Radius must be non-negative')
    if not isinstance(ax, plt.PolarAxes):
        raise TypeError('ax must be a polar plot')

    theta = np.linspace(0, 2 * np.pi, 1000)
    ax.plot(theta, radius * np.ones_like(theta))
    ax.set_rlabel_position(radius * 45)
    return ax

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, polar=True)

    def tearDown(self):
        plt.close(self.fig)

    def test_positive_radius(self):
        result_ax = task_func(self.ax, 1.0)
        self.assertEqual(len(result_ax.get_lines()), 1)

    def test_zero_radius(self):
        result_ax = task_func(self.ax, 0.0)
        self.assertEqual(len(result_ax.get_lines()), 1)
        self.assertAlmostEqual(result_ax.get_lines()[0].get_ydata()[0], 0.0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            task_func(self.ax, -1.0)

    def test_non_polar_axes(self):
        non_polar_ax = self.fig.add_subplot(111)
        with self.assertRaises(TypeError):
            task_func(non_polar_ax, 1.0)

    def test_circle_coordinates(self):
        result_ax = task_func(self.ax, 1.5)
        ydata = result_ax.get_lines()[0].get_ydata()
        self.assertTrue(np.allclose(ydata, 1.5 * np.ones_like(ydata)))

if __name__ == '__main__':
    unittest.main()