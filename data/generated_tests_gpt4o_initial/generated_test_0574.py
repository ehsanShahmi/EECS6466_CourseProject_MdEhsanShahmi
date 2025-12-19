from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
import unittest

def task_func(array_length=100, noise_level=0.2):
    """
    Create a noisy sine wave of a specified length and adjusts a curve using curve_fit from scipy.optimize to the data.
    
    Parameters:
    - array_length (int): Length of the sine wave array. Defaults to 100.
    - noise_level (float): Level of noise added to the sine wave. Defaults to 0.2.

    Returns:
    - Axes object: A plot showing the noisy sine wave and its adjusted curve.

    Requirements:
    - numpy
    - scipy.optimize
    - matplotlib.pyplot

    Example:
    >>> ax = task_func(100, 0.2)
    """
    x = np.linspace(0, 4*np.pi, array_length)
    y = np.sin(x) + noise_level * np.random.rand(array_length)

    def func(x, a, b):
        return a * np.sin(b * x)

    popt, pcov = curve_fit(func, x, y, p0=[1, 1])

    fig, ax = plt.subplots()
    ax.plot(x, y, 'b-', label='data')
    ax.plot(x, func(x, *popt), 'r-', label='fit: a=%5.3f, b=%5.3f' % tuple(popt))
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    
    return ax

class TestTaskFunc(unittest.TestCase):

    def test_array_length(self):
        """ Test when using a longer array length. """
        ax = task_func(array_length=200, noise_level=0.1)
        self.assertTrue(ax.collections)  # Check if the plot has data plotted

    def test_noise_level_zero(self):
        """ Test when noise level is set to zero. """
        ax = task_func(array_length=100, noise_level=0.0)
        lines = ax.get_lines()
        self.assertEqual(len(lines), 1)  # Only one line should be presented without noise
        
    def test_noise_level_increase(self):
        """ Test if increasing noise level affects the fitting. """
        ax_low_noise = task_func(array_length=100, noise_level=0.1)
        ax_high_noise = task_func(array_length=100, noise_level=1.0)
        
        lines_low = ax_low_noise.get_lines()
        lines_high = ax_high_noise.get_lines()
        
        self.assertNotEqual(lines_low[1].get_ydata().tolist(), lines_high[1].get_ydata().tolist())

    def test_output_type(self):
        """ Test that the output is an Axes object. """
        ax = task_func(array_length=100, noise_level=0.2)
        self.assertIsInstance(ax, plt.Axes)

    def test_fit_parameters(self):
        """ Test checking of fitting parameters to ensure they are reasonable. """
        ax = task_func(array_length=100, noise_level=0.2)
        lines = ax.get_lines()
        fit_line = lines[1]
        
        self.assertTrue(fit_line.get_ydata().mean() >= -1 and fit_line.get_ydata().mean() <= 1)
        self.assertTrue(fit_line.get_ydata().max() >= -1 and fit_line.get_ydata().max() <= 1)
        self.assertTrue(fit_line.get_ydata().min() >= -1 and fit_line.get_ydata().min() <= 1)

if __name__ == '__main__':
    unittest.main()