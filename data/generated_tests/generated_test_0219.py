import math
import statistics
import numpy as np
import unittest

def task_func(input_list):
    """
    Sorts the input list in ascending order based on the degree value of its elements, and then 
    calculates the mean, median, and mode of both the sorted list and the same for the magnitude of 
    the fast fourier transform of the degree values upto the nearest integer.

    Parameters:
    input_list (list): A list of numbers to be sorted and analyzed.

    Returns:
    tuple: A tuple containing the rounded mean, median and mode of the sorted list along with those 
    for the magnitude of the fast fourier transform of the degree values.

    Requirements:
    - math
    - statistics
    - numpy

    Example:
    >>> input_list = [30, 45, 60, 90, 180]
    >>> stats = task_func(input_list)
    >>> print(stats)
    (81, 60, 30, 10712, 8460, 8460)
    """

    fft = np.abs(np.fft.fft([math.degrees(x) for x in input_list]))
    sorted_list = sorted(input_list, key=lambda x: (math.degrees(x), x))
    mean = statistics.mean(sorted_list)
    median = statistics.median(sorted_list)
    mode = statistics.mode(sorted_list)
    mean_fft = round(statistics.mean(fft))
    median_fft = round(statistics.median(fft))
    mode_fft = round(statistics.mode(fft))
    return (mean, median, mode, mean_fft, median_fft, mode_fft)


class TestTaskFunc(unittest.TestCase):
    
    def test_sorted_list_stats(self):
        input_list = [30, 45, 60, 90, 180]
        expected = (81, 60, 30, 10712, 8460, 8460)
        result = task_func(input_list)
        self.assertEqual(result, expected)

    def test_empty_list(self):
        input_list = []
        expected = (0, 0, 0, 0, 0, 0)  # Assuming 0 returns for empty case; adjust if behavior changes
        result = task_func(input_list)
        self.assertEqual(result, expected)

    def test_single_element_list(self):
        input_list = [45]
        expected = (45, 45, 45, 0, 0, 0)  # FFT of a single element is always 0, mode is undefined
        result = task_func(input_list)
        self.assertEqual(result, expected)

    def test_identical_elements_list(self):
        input_list = [90, 90, 90, 90]
        expected = (90, 90, 90, 360, 360, 360)  # FFT will result in 0s and repeated values
        result = task_func(input_list)
        self.assertEqual(result, expected)

    def test_large_numbers(self):
        input_list = [300, 450, 600, 900, 1800]
        expected = (810, 600, 300, 116048, 90000, 90000)  # Adjust expected values based on FFT calculation
        result = task_func(input_list)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()