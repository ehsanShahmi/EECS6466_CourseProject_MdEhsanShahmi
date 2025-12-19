import unittest
import numpy as np
from scipy.fft import fft
from matplotlib import pyplot as plt

def task_func(original):
    arr = np.array([b for (_, b) in original])

    if arr.size == 0:
        fft_data = np.array([])
        return arr, fft_data, None

    fft_data = fft(arr)
    _, ax = plt.subplots()
    ax.hist(np.abs(fft_data))

    return arr, fft_data, ax

class TestTaskFunc(unittest.TestCase):

    def test_empty_list(self):
        original = []
        arr, fft_data, ax = task_func(original)
        self.assertTrue(np.array_equal(arr, np.array([])))
        self.assertTrue(np.array_equal(fft_data, np.array([])))
        self.assertIsNone(ax)

    def test_single_element(self):
        original = [('a', 5)]
        arr, fft_data, ax = task_func(original)
        expected_arr = np.array([5])
        expected_fft_data = np.array([5.-0.j])
        
        self.assertTrue(np.array_equal(arr, expected_arr))
        self.assertTrue(np.array_equal(fft_data, expected_fft_data))

    def test_multiple_elements(self):
        original = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
        arr, fft_data, ax = task_func(original)
        expected_arr = np.array([1, 2, 3, 4])
        expected_fft_data_magnitude = np.array([10., 2.82842712, 2., 2.82842712])
        
        self.assertTrue(np.array_equal(arr, expected_arr))
        self.assertAlmostEqual(np.linalg.norm(fft_data.real), expected_fft_data_magnitude[0])
        self.assertAlmostEqual(np.linalg.norm(fft_data.imag), expected_fft_data_magnitude[1])

    def test_negative_numbers(self):
        original = [('a', -1), ('b', -2), ('c', -3)]
        arr, fft_data, ax = task_func(original)
        expected_arr = np.array([-1, -2, -3])
        
        self.assertTrue(np.array_equal(arr, expected_arr))
        self.assertEqual(len(fft_data), 3)

    def test_varied_data_types(self):
        original = [('a', 3), ('b', 0), ('c', 4.5), ('d', -1)]
        arr, fft_data, ax = task_func(original)
        expected_arr = np.array([3, 0, 4.5, -1])
        
        self.assertTrue(np.array_equal(arr, expected_arr))
        self.assertEqual(len(fft_data), 4)

if __name__ == '__main__':
    unittest.main()