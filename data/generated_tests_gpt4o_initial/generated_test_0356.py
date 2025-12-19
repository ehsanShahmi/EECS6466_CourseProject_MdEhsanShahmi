import numpy as np
import matplotlib.pyplot as plt
import cmath
import unittest

def task_func(x, y):
    """
    Draw the phase of a complex function over a range of x and y and return the matplotlib axes object
    along with the 2D array of calculated phase values.
    
    Parameters:
    x (numpy.ndarray): The range of x values.
    y (numpy.ndarray): The range of y values.
    
    Returns:
    tuple: containing
        - matplotlib.axes.Axes: The axes object with the phase plot.
        - numpy.ndarray: The 2D array of calculated phase values.
    
    Raises:
    TypeError: If either `x` or `y` is not a numpy.ndarray.
    ValueError: If `x` and `y` do not have the same length.
    
    Requirements:
    - numpy
    - matplotlib.pyplot
    - cmath
    """
    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray):
        raise TypeError("x and y must be numpy.ndarray")

    if x.size == 0 or y.size == 0:
        print("Empty x or y array provided.")
        return None, np.array([])

    if len(x) != len(y):
        raise ValueError("Mismatched array sizes: x and y must have the same length")

    Z = np.zeros((len(y), len(x)), dtype=float)
    for i in range(len(y)):
        for j in range(len(x)):
            z = complex(x[j], y[i])
            Z[i, j] = cmath.phase(z**2 - 1)

    fig, ax = plt.subplots()
    c = ax.imshow(Z, extent=(np.amin(x), np.amax(x), np.amin(y), np.amax(y)), origin='lower', cmap='hsv')
    fig.colorbar(c, ax=ax, label="Phase (radians)")
    ax.grid()

    return ax, Z

class TestTaskFunc(unittest.TestCase):

    def test_valid_arrays(self):
        ax, Z = task_func(np.array([1, 2, 3]), np.array([1, 2, 3]))
        self.assertIsInstance(ax, plt.Axes)
        self.assertIsInstance(Z, np.ndarray)
        self.assertEqual(Z.shape, (3, 3))

    def test_single_point(self):
        ax, Z = task_func(np.array([0]), np.array([0]))
        self.assertIsInstance(ax, plt.Axes)
        self.assertIsInstance(Z, np.ndarray)
        self.assertEqual(Z.shape, (1, 1))

    def test_empty_x_array(self):
        ax, Z = task_func(np.array([]), np.array([1, 2, 3]))
        self.assertIsNone(ax)
        self.assertEqual(Z.shape, (0,))

    def test_empty_y_array(self):
        ax, Z = task_func(np.array([1, 2, 3]), np.array([]))
        self.assertIsNone(ax)
        self.assertEqual(Z.shape, (0,))

    def test_mismatched_array_sizes(self):
        with self.assertRaises(ValueError):
            task_func(np.array([1, 2]), np.array([1]))

    def test_type_error_on_non_ndarray(self):
        with self.assertRaises(TypeError):
            task_func([1, 2, 3], np.array([1, 2, 3]))
        with self.assertRaises(TypeError):
            task_func(np.array([1, 2, 3]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()