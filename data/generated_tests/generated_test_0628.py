import math
from random import randint
import matplotlib.pyplot as plt
import unittest

def task_func():
    """
    Create and draw a sine wave with random frequency, amplitude and phase shift. The return ax object
    has 'Random Sine Wave' title, 'Time' on the x axis and 'Amplitude' on the y axis.

    Parameters:
    None

    Returns:
    ax (matplotlib.axes._axes.Axes): The axis object of the generated sine wave plot.

    Requirements:
    - math
    - random
    - matplotlib.pyplot

    Example:
    >>> ax = task_func()
    """

    x = [i/100 for i in range(1000)]
    frequency = randint(1, 5)
    amplitude = randint(1, 5)
    phase_shift = randint(0, 360)

    y = [amplitude * math.sin(2 * math.pi * frequency * (xi + phase_shift)) for xi in x]

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title('Random Sine Wave')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.grid(True)
    
    return ax  # Return the axis object for testing

class TestTaskFunc(unittest.TestCase):
    def test_return_type(self):
        """Test that the function returns a matplotlib axes object."""
        ax = task_func()
        self.assertIsInstance(ax, plt.Axes)

    def test_title(self):
        """Test that the title of the plot is 'Random Sine Wave'."""
        ax = task_func()
        self.assertEqual(ax.get_title(), 'Random Sine Wave')

    def test_x_label(self):
        """Test that the x-axis label is 'Time'."""
        ax = task_func()
        self.assertEqual(ax.get_xlabel(), 'Time')

    def test_y_label(self):
        """Test that the y-axis label is 'Amplitude'."""
        ax = task_func()
        self.assertEqual(ax.get_ylabel(), 'Amplitude')

    def test_grid_enabled(self):
        """Test that the grid is enabled for the plot."""
        ax = task_func()
        self.assertTrue(ax._axis3d.has_data(), "Grid should be enabled on the plot.")

if __name__ == '__main__':
    unittest.main()