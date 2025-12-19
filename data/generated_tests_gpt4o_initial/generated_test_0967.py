import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import unittest

# Here is your prompt:
# import numpy as np
# from scipy import integrate
# import matplotlib.pyplot as plt

# def task_func(func, x_range=(-2, 2), num_points=1000):
#     """
#     Calculates and plots both a given function and its cumulative integral over a specified range,
#     using a linearly spaced range of x-values.
# 
#     Parameters:
#     func (function): A function of a single variable to integrate and plot.
#     x_range (tuple, optional): The range (start, end) over which to evaluate `func`. Defaults to (-2, 2).
#     num_points (int, optional): Number of points to generate in `x_range`. Defaults to 1000.
# 
#     Returns:
#     matplotlib.axes.Axes: The Axes object containing the plots of the function and its integral.
# 
#     Requirements:
#     - numpy
#     - scipy
#     - matplotlib
# 
#     Note:
#     - The plot includes a legend and labels for the x and y axes that include the function's name.
# 
#     Example:
#     >>> ax = task_func(np.sin)
#     >>> type(ax)
#     <class 'matplotlib.axes._axes.Axes'>
#     >>> ax.get_legend_handles_labels()[-1]
#     ['sin(x)', 'Integral of sin(x)']
#     """
# 
#                X = np.linspace(x_range[0], x_range[1], num_points)
#     y = func(X)
#     y_int = integrate.cumulative_trapezoid(y, X, initial=0)
# 
#     fig, ax = plt.subplots()
#     ax.plot(X, y, label=f"{func.__name__}(x)")
#     ax.plot(X, y_int, label=f"Integral of {func.__name__}(x)")
#     ax.legend()
# 
#     return ax

class TestTaskFunc(unittest.TestCase):

    def test_sine_function(self):
        ax = task_func(np.sin)
        self.assertIsInstance(ax, plt.Axes)
        self.assertIn('sin(x)', [label.get_text() for label in ax.get_legend().get_texts()])

    def test_cosine_function(self):
        ax = task_func(np.cos)
        self.assertIsInstance(ax, plt.Axes)
        self.assertIn('cos(x)', [label.get_text() for label in ax.get_legend().get_texts()])

    def test_exponential_function(self):
        ax = task_func(np.exp)
        self.assertIsInstance(ax, plt.Axes)
        self.assertIn('exp(x)', [label.get_text() for label in ax.get_legend().get_texts()])

    def test_custom_range(self):
        ax = task_func(np.sin, x_range=(-1, 1))
        self.assertIsInstance(ax, plt.Axes)
        x_labels = ax.get_xticks()
        self.assertTrue(all(x >= -1 and x <= 1 for x in x_labels))

    def test_number_of_points(self):
        ax = task_func(np.sin, num_points=500)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines), 2)  # There should be 2 lines for function and integral

if __name__ == '__main__':
    unittest.main()