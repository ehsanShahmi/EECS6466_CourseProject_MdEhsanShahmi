import re
import math
import unittest

def task_func(s):
    '''
    Count the number of integers and floating-point numbers in a comma-separated string and calculate the sum of their square roots.

    Parameters:
    - s (str): The comma-separated string.

    Returns:
    - count (int): The number of integers and floats in the string.
    - sqrt_sum (float): The sum of the square roots of the integers and floats.
    
    Requirements:
    - re
    - math
    
    Example:
    >>> count, sqrt_sum = task_func('1,2,3.5,abc,4,5.6')
    >>> print(count)  # Ensure this matches exactly with expected output
    5
    >>> print("{:.2f}".format(sqrt_sum))  # Ensure this matches exactly with expected output
    8.65
    '''

    numbers = re.findall(r'\b\d+(?:\.\d+)?\b', s)  # Use non-capturing group for decimals
    count = len(numbers)
    sqrt_sum = sum(math.sqrt(float(num)) for num in numbers if num)  # Ensure conversion to float
    return count, sqrt_sum

class TestTaskFunc(unittest.TestCase):
    
    def test_case_1(self):
        count, sqrt_sum = task_func('1,2,3.5,abc,4,5.6')
        self.assertEqual(count, 5)
        self.assertAlmostEqual(sqrt_sum, 8.65)

    def test_case_2(self):
        count, sqrt_sum = task_func('1, 4, 9, 16')
        self.assertEqual(count, 4)
        self.assertAlmostEqual(sqrt_sum, 10.0)  # √1 + √4 + √9 + √16 = 1 + 2 + 3 + 4

    def test_case_3(self):
        count, sqrt_sum = task_func('10.0, 15.5, abc, 25, 36')
        self.assertEqual(count, 4)
        self.assertAlmostEqual(sqrt_sum, 14.874)  # √10 + √15.5 + √25 + √36

    def test_case_4(self):
        count, sqrt_sum = task_func('1.0, 2.0, 3.0, 4.0')
        self.assertEqual(count, 4)
        self.assertAlmostEqual(sqrt_sum, 4.0)  # √1 + √2 + √3 + √4

    def test_case_5(self):
        count, sqrt_sum = task_func('0.0, -1.0, 4, 16')
        self.assertEqual(count, 3)
        self.assertAlmostEqual(sqrt_sum, 6.0)  # √0 + √4 + √16

if __name__ == '__main__':
    unittest.main()