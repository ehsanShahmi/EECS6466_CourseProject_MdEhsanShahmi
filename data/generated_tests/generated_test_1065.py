from scipy import fftpack
import numpy as np
import unittest
from matplotlib import pyplot as plt


def task_func(arr):
    """
    Performs a Fast Fourier Transform (FFT) on the sum of each row in a 2D array and
    plots the absolute values of the FFT coefficients.

    Parameters:
    arr (numpy.ndarray): A 2D numpy array.

    Returns:
    matplotlib.axes.Axes: An Axes object displaying the plot of the absolute values of the FFT coefficients.

    Requirements:
    - scipy.fftpack
    - matplotlib.pyplot

    Example:
    >>> import numpy as np
    >>> arr = np.array([[i + j for i in range(3)] for j in range(5)])
    >>> ax = task_func(arr)
    >>> ax.get_title()
    'Absolute values of FFT coefficients'
    """

    row_sums = arr.sum(axis=1)
    fft_coefficients = fftpack.fft(row_sums)

    _, ax = plt.subplots()
    ax.plot(np.abs(fft_coefficients))
    ax.set_title("Absolute values of FFT coefficients")

    return ax


class TestTaskFunction(unittest.TestCase):
    
    def test_shape(self):
        arr = np.array([[1, 2, 3], [4, 5, 6]])
        ax = task_func(arr)
        self.assertEqual(ax.get_lines()[0].get_xydata().shape[0], 2)  # should match number of row sums
    
    def test_plot_title(self):
        arr = np.array([[1, 2], [3, 4]])
        ax = task_func(arr)
        self.assertEqual(ax.get_title(), "Absolute values of FFT coefficients")
    
    def test_fft_output_length(self):
        arr = np.random.rand(8, 5)
        ax = task_func(arr)
        self.assertEqual(len(ax.get_lines()[0].get_xydata()), 8)  # Length of FFT output should match number of row sums
    
    def test_sum_of_rows(self):
        arr = np.array([[1, 1, 1], [2, 2, 2]])
        ax = task_func(arr)
        row_sums = arr.sum(axis=1)
        fft_coefficients = fftpack.fft(row_sums)
        self.assertTrue(np.allclose(ax.get_lines()[0].get_ydata(), np.abs(fft_coefficients)))
    
    def test_empty_array(self):
        arr = np.empty((0, 0))
        with self.assertRaises(ValueError):
            task_func(arr)


if __name__ == "__main__":
    unittest.main()