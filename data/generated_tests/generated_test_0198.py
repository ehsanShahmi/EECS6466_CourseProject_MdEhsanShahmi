import numpy as np
import bisect
import statistics
import matplotlib.pyplot as plt
import unittest

def task_func(data, value):
    """
    Analyzes a list of numerical data, identifies values greater than the average,
    and counts how many values are greater than a specified value. Additionally, plots the
    histogram of the sorted numbers.

    Parameters:
        data (list): A list of numerical data.
        value (float): A value to compare against the data.

    Returns:
        numpy.ndarray: An array of values from the data that are greater than the average.
        int: The number of values in the data that are greater than the given value.
    
    Requirements:
    - numpy
    - bisect
    - statistics
    - matplotlib.pyplot
    
    Note:
    - If the data list is empty, the function returns an empty numpy.ndarray and a count of 0. This ensures
      the function's output remains consistent and predictable even with no input data.
    
    Examples:
    >>> greater_avg, count = task_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
    >>> greater_avg.tolist()
    [6, 7, 8, 9, 10]
    >>> count
    5
    """
    if not data:  # Handle empty data list
        return np.array([]), 0

    data = np.array(data)
    avg = statistics.mean(data)
    greater_avg = data[data > avg]

    data.sort()
    bpoint = bisect.bisect_right(data, value)
    num_greater_value = len(data) - bpoint

    plt.hist(data, bins=10)
    plt.show()

    return greater_avg, num_greater_value


class TestTaskFunc(unittest.TestCase):

    def test_empty_data(self):
        greater_avg, count = task_func([], 5)
        self.assertTrue(np.array_equal(greater_avg, np.array([])))
        self.assertEqual(count, 0)

    def test_one_element_data(self):
        greater_avg, count = task_func([10], 5)
        self.assertTrue(np.array_equal(greater_avg, np.array([])))
        self.assertEqual(count, 0)

    def test_multiple_elements_greater_than_avg(self):
        greater_avg, count = task_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
        self.assertTrue(np.array_equal(greater_avg, np.array([6, 7, 8, 9, 10])))
        self.assertEqual(count, 5)

    def test_no_elements_greater_than_value(self):
        greater_avg, count = task_func([1, 2, 3], 10)
        self.assertTrue(np.array_equal(greater_avg, np.array([2, 3])))
        self.assertEqual(count, 0)

    def test_all_elements_greater_than_value(self):
        greater_avg, count = task_func([10, 11, 12], 5)
        self.assertTrue(np.array_equal(greater_avg, np.array([11, 12])))
        self.assertEqual(count, 3)


if __name__ == "__main__":
    unittest.main()