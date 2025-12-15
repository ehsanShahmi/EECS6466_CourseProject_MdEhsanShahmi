import unittest
from random import randint
import numpy as np
import matplotlib.pyplot as plt

from your_module_name import task_func  # Replace 'your_module_name' with the actual module name where task_func is defined.

class TestTaskFunc(unittest.TestCase):

    def test_default_array_length(self):
        ax = task_func()
        self.assertIsInstance(ax, plt.Axes)

    def test_custom_array_length(self):
        custom_length = 50
        ax = task_func(custom_length)
        self.assertIsInstance(ax, plt.Axes)
        
        # Check if the length of the max_values is equal to the custom_length
        array1 = np.array([randint(1, 100) for _ in range(custom_length)])
        array2 = np.array([randint(1, 100) for _ in range(custom_length)])
        max_values = np.maximum(array1, array2)
        self.assertEqual(len(ax.lines[0].get_xdata()), custom_length)

    def test_randomness(self):
        array_length = 100
        ax1 = task_func(array_length)
        ax2 = task_func(array_length)
        # The plots should not be identical due to randomness
        self.assertFalse(np.array_equal(ax1.lines[0].get_ydata(), ax2.lines[0].get_ydata()))

    def test_y_axis_label(self):
        ax = task_func()
        self.assertEqual(ax.get_ylabel(), 'Maximum Values')

    def test_data_type_in_max_values(self):
        custom_length = 100
        ax = task_func(custom_length)
        max_values = ax.lines[0].get_ydata()

        # Check if max_values is a numpy array of floats
        self.assertTrue(isinstance(max_values, np.ndarray))
        self.assertTrue(np.issubdtype(max_values.dtype, np.number))

if __name__ == '__main__':
    unittest.main()