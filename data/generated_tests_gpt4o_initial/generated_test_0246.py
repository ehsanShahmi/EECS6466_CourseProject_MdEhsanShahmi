import unittest
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

ANGLES = np.arange(0, 2*np.pi, 0.01)

def task_func(n_waves, seed=0):
    """
    Generate a series of n sine waves with increasing frequency with a fidelity of 0.01 radians as 
    provided by the ANGLES array. The amplitude of each wave is 1. The function returns a list of
    numpy arrays with the y values of the sine waves. Additionally, calculate the Fast Fourier Transform
    (FFT) of the mixed signal and plot the histogram of the magnitude of the FFT data. If n_waves is less
    than 1, return an empty list for the sine waves, an empty array for the FFT data, and None for the axes
    object.
    
    Parameters:
    n_waves (int): The number of sine waves in the series.
    seed (int, Optional): The seed for the random number generator. Defaults to 0.
    
    Returns:
    list: A list of numpy arrays with the y values of the sine waves.
    np.array: FFT data.
    plt.Axes: The axes object of the plot.
    
    Requirements:
    - numpy
    - matplotlib.pyplot
    - scipy.fft

    Example:
    >>> sine_waves, fft_data, ax = task_func(5)
    >>> len(sine_waves)
    5
    >>> fft_data.shape
    (629,)
    """

    np.random.seed(seed)
    sine_wave_series = []

    if n_waves < 1:
        return sine_wave_series, np.array([]), None

    for frequency in range(1, n_waves+1):
        wave = np.sin(frequency * ANGLES)
        sine_wave_series.append(wave)

    fft_data = fft(np.sum(sine_wave_series, axis=0))
    _, ax = plt.subplots()
    ax.hist(np.abs(fft_data))

    return sine_wave_series, fft_data, ax


class TestTaskFunc(unittest.TestCase):

    def test_no_waves(self):
        sine_waves, fft_data, ax = task_func(0)
        self.assertEqual(len(sine_waves), 0)
        self.assertTrue(fft_data.size == 0)
        self.assertIsNone(ax)

    def test_one_wave(self):
        sine_waves, fft_data, ax = task_func(1)
        self.assertEqual(len(sine_waves), 1)
        self.assertEqual(sine_waves[0].shape, ANGLES.shape)
        self.assertEqual(fft_data.shape[0], 629)

    def test_multiple_waves(self):
        n_waves = 5
        sine_waves, fft_data, ax = task_func(n_waves)
        self.assertEqual(len(sine_waves), n_waves)
        for i in range(n_waves):
            self.assertEqual(sine_waves[i].shape, ANGLES.shape)
        self.assertEqual(fft_data.shape[0], 629)

    def test_fft_output_shape(self):
        n_waves = 3
        sine_waves, fft_data, ax = task_func(n_waves)
        self.assertEqual(fft_data.shape[0], 629)

    def test_zeros_for_negative_waves(self):
        sine_waves, fft_data, ax = task_func(-1)
        self.assertEqual(len(sine_waves), 0)
        self.assertTrue(fft_data.size == 0)
        self.assertIsNone(ax)


if __name__ == '__main__':
    unittest.main()