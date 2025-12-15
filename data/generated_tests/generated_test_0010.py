import numpy as np
import itertools
import random
import statistics
import unittest

def task_func(T1, RANGE=100):
    """
    Convert elements in 'T1' to integers and create a list of random integers.
    The size of the list is the sum of the integers in `T1`. Calculate and 
    return the mean, median, and mode of the list.
    
    Parameters:
    T1 (tuple of tuples): Each tuple contains string representations of integers which are converted to integers.
    RANGE (int, optional): The upper limit for generating random integers. Default is 100.
    
    Returns:
    tuple: A tuple containing the mean, median, and mode of the generated list of random integers.
           The mean and median are floats, and the mode is an integer. The calculations use the generated
           list whose size is determined by the sum of converted integers from `T1`.
    
    Requirements:
    - numpy
    - itertools
    - random
    - statistics

    Raises:
    statistics.StatisticsError if T1 is empty
    
    Example:
    >>> import random
    >>> random.seed(42)
    >>> T1 = (('13', '17', '18', '21', '32'), ('07', '11', '13', '14', '28'), ('01', '05', '06', '08', '15', '16'))
    >>> stats = task_func(T1)
    >>> print(stats)
    (49.88, 48.0, 20)
    >>> stats = task_func(T1, RANGE=50)
    >>> print(stats)
    (23.773333333333333, 25.0, 15)
    """

class TestTaskFunc(unittest.TestCase):

    def test_mean_median_mode_non_empty(self):
        T1 = (('1', '2', '3'),)
        expected_mean = 1.5  # assuming re-runs yield similar results; means should generally center around 1 to 3 
        expected_median = 2.0  # for generated numbers based on T1
        expected_mode = statistics.mode([0, 1, 2])  # mode should be calculated based on random generation
        result = task_func(T1, RANGE=10)
        self.assertAlmostEqual(result[0], expected_mean, places=1)
        self.assertAlmostEqual(result[1], expected_median, places=1)
        self.assertEqual(result[2], expected_mode)

    def test_empty_input(self):
        T1 = ()
        with self.assertRaises(statistics.StatisticsError):
            task_func(T1)
    
    def test_different_range(self):
        T1 = (('5', '5'),)
        result = task_func(T1, RANGE=50)
        self.assertGreaterEqual(result[0], 0)  # mean should be >= 0
        self.assertLessEqual(result[0], 50)  # mean should be <= 50
        self.assertGreaterEqual(result[2], 0)  # mode should be >= 0

    def test_large_input(self):
        T1 = (('10', '10', '10'),)
        result = task_func(T1)
        self.assertEqual(len(result), 3)  # mean, median, mode
        self.assertIsInstance(result[0], float)  # mean should be float
        self.assertIsInstance(result[1], float)  # median should be float
        self.assertIsInstance(result[2], int)  # mode should be int

    def test_mode_repetition(self):
        T1 = (('5', '5', '5'),)
        result = task_func(T1)
        self.assertEqual(result[2], 0)  # mode should give the most frequent numbers (which could be 5)

if __name__ == '__main__':
    unittest.main()