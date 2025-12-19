import random
import bisect
import statistics
import matplotlib.pyplot as plt
import unittest

def task_func(n, value):
    """
    Generates 'n' random numbers between 0 and 1, finds those greater than their average,
    and counts how many are greater than or equal to a specified value, then plots 
    the sorted numbers.

    Parameters:
        n (int): The number of random numbers to generate.
        value (float): The value to compare against the random numbers.

    Returns:
        list: Numbers greater than the average of all generated numbers.
        int: The count of numbers greater than or equal to the specified value.

    Requirements:
    - random
    - bisect
    - statistics
    - matplotlib.pyplot

    Examples:
    >>> greater_avg, count = task_func(10, 0.5)
    >>> isinstance(greater_avg, list) and isinstance(count, int)
    True
    >>> len(greater_avg) <= 10
    True
    """

    if n < 1:  # Handle case where n is 0 or less
        return [], 0

    numbers = [random.random() for _ in range(n)]
    avg = statistics.mean(numbers)
    greater_avg = [x for x in numbers if x > avg]

    numbers.sort()
    bpoint = bisect.bisect_right(numbers, value)
    num_greater_value = len(numbers) - bpoint

    plt.plot(numbers)
    plt.show()

    return greater_avg, num_greater_value


class TestTaskFunc(unittest.TestCase):

    def test_zero_elements(self):
        """Test when n is 0, should return empty list and count 0."""
        greater_avg, count = task_func(0, 0.5)
        self.assertEqual(greater_avg, [])
        self.assertEqual(count, 0)

    def test_negative_elements(self):
        """Test when n is negative, should return empty list and count 0."""
        greater_avg, count = task_func(-5, 0.5)
        self.assertEqual(greater_avg, [])
        self.assertEqual(count, 0)

    def test_single_element(self):
        """Test when n is 1, should return an empty list and count 0."""
        greater_avg, count = task_func(1, 0.5)
        self.assertEqual(greater_avg, [])
        self.assertEqual(count, 0)

    def test_multiple_elements(self):
        """Test with multiple elements, should return a list and count."""
        greater_avg, count = task_func(10, 0.5)
        self.assertTrue(isinstance(greater_avg, list))
        self.assertTrue(isinstance(count, int))
        self.assertLessEqual(len(greater_avg), 10)

    def test_value_boundaries(self):
        """Test with value equal to boundaries 0 and 1."""
        greater_avg_low, count_low = task_func(10, 0)
        greater_avg_high, count_high = task_func(10, 1)

        self.assertTrue(count_low >= 0)  # Should count values > average, thus ≥ 0
        self.assertEqual(count_high, 0)   # No values should be ≥ 1 (random numbers are in 0-1 range)  

if __name__ == '__main__':
    unittest.main()