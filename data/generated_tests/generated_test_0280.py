import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
import unittest

# Here is your prompt:
def task_func(signal, precision=2, seed=777):
    np.random.seed(seed)
    transformed_signal = fft(signal)
    transformed_signal_rounded = np.round(transformed_signal, precision).tolist()

    fig, ax = plt.subplots(2, 1)
    ax[0].plot(signal)
    ax[0].set_title('Original Signal')
    ax[1].plot(transformed_signal_rounded)
    ax[1].set_title('Transformed Signal')
    plt.tight_layout()  # Adjust layout to avoid overlap

    return np.array(transformed_signal_rounded), ax

class TestTaskFunc(unittest.TestCase):

    def test_basic_signal(self):
        signal = np.array([0., 1., 0., -1.])
        transformed_signal, _ = task_func(signal)
        expected_result = np.array([0.-0.j, 0.-2.j, 0.-0.j, 0.+2.j])
        np.testing.assert_array_almost_equal(transformed_signal, expected_result, decimal=2)

    def test_signal_with_precision(self):
        signal = np.array([1., 2., 3., 4.])
        transformed_signal, _ = task_func(signal, precision=1)
        expected_result = np.round(fft(signal), 1).tolist()
        np.testing.assert_array_almost_equal(transformed_signal, expected_result)

    def test_empty_signal(self):
        signal = np.array([])
        transformed_signal, _ = task_func(signal)
        expected_result = np.array([])
        np.testing.assert_array_equal(transformed_signal, expected_result)

    def test_random_signal(self):
        np.random.seed(777)
        signal = np.random.rand(10)
        transformed_signal, _ = task_func(signal)
        transformed_expected = fft(signal)
        np.testing.assert_array_almost_equal(transformed_signal, np.round(transformed_expected, 2))

    def test_signal_with_different_seed(self):
        signal = np.array([1., 0., -1., 0.])
        transformed_signal1, _ = task_func(signal, seed=777)
        transformed_signal2, _ = task_func(signal, seed=888)
        np.testing.assert_array_equal(transformed_signal1, transformed_signal2)

if __name__ == '__main__':
    unittest.main()