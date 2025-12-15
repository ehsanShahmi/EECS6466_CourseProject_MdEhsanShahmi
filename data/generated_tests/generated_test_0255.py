import unittest
import matplotlib.pyplot as plt
import numpy as np

# Provided prompt code
import matplotlib
import numpy as np

FUNCTIONS = [np.sin, np.cos, np.tan]

def task_func(ax, func_index):
    """
    Draw a mathematical function (sine, cosine, or tangent) on a polar diagram 'ax'.
    The radial ticks are placed at a position corresponding to the index of the function multiplied by 45 degrees.

    Parameters:
    ax (matplotlib.axes._axes.Axes): The ax to plot on.
    func_index (int): The index of the function in the FUNCTIONS list (0 for sine, 1 for cosine, 2 for tangent).

    Returns:
    matplotlib.axes._axes.Axes: The modified ax with the plotted function.
    
    Raises:
    - This function will raise a ValueError if the input ax is not and Axes.
    
    Requirements:
    - matplotlib
    - numpy

    Example:
    >>> import matplotlib.pyplot as plt
    >>> fig = plt.figure()
    >>> ax = fig.add_subplot(111, polar=True)
    >>> ax_up = task_func(ax, 1)
    <class 'matplotlib.projections.polar.PolarAxes'>
    >>> ax_up.lines[0].get_ydata()[0]
    1.0
    >>> plt.close()
    """

    print(type(ax))
    if not isinstance(ax, matplotlib.axes.Axes):
        raise ValueError("The input is not an axes")
    x = np.linspace(0, 2 * np.pi, 1000)
    y = FUNCTIONS[func_index](x)

    ax.plot(x, y)
    ax.set_rlabel_position(func_index * 45)
    return ax

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, polar=True)

    def test_valid_function_index_sine(self):
        """Test with valid index for sine function (0)."""
        result_ax = task_func(self.ax, 0)
        self.assertIsInstance(result_ax, matplotlib.projections.polar.PolarAxes)
        self.assertEqual(len(result_ax.lines), 1)
        self.assertAlmostEqual(result_ax.lines[0].get_ydata()[0], 0.0)

    def test_valid_function_index_cosine(self):
        """Test with valid index for cosine function (1)."""
        result_ax = task_func(self.ax, 1)
        self.assertIsInstance(result_ax, matplotlib.projections.polar.PolarAxes)
        self.assertEqual(len(result_ax.lines), 1)
        self.assertAlmostEqual(result_ax.lines[0].get_ydata()[0], 1.0)

    def test_valid_function_index_tangent(self):
        """Test with valid index for tangent function (2)."""
        result_ax = task_func(self.ax, 2)
        self.assertIsInstance(result_ax, matplotlib.projections.polar.PolarAxes)
        self.assertEqual(len(result_ax.lines), 1)
        # Check for y-value at pi/4 where tan(pi/4) = 1
        self.assertAlmostEqual(result_ax.lines[0].get_ydata()[250], 1.0, places=1)

    def test_invalid_function_index(self):
        """Test raising error with invalid function index."""
        with self.assertRaises(IndexError):
            task_func(self.ax, 3)  # Invalid index

    def test_invalid_ax_type(self):
        """Test raising error with invalid ax type."""
        with self.assertRaises(ValueError):
            task_func(None, 1)  # None is not an Axes instance

# To run the tests
if __name__ == '__main__':
    unittest.main()