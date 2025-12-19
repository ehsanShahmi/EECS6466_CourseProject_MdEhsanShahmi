import math
from sympy import isprime
import unittest

def task_func(input_list):
    """
    Filter the prime numbers from the specified list, sort the prime numbers 
    ascending based on their radian value converted to degrees, and return the sorted list.
    
    The function uses the isprime function from the sympy library to determine prime numbers 
    and the degrees function from the math library to sort the numbers based on their degree value.

    Parameters:
    input_list (list[int]): A list of integers to be filtered and sorted.

    Returns:
    list[int]: A sorted list of prime numbers based on their degree value.

    Requirements:
    - math
    - sympy

    Examples:
    >>> task_func([4, 5, 2, 7, 89, 90])
    [2, 5, 7, 89]
    
    >>> task_func([101, 102, 103, 104])
    [101, 103]
    """

    primes = [i for i in input_list if isprime(i)]
    sorted_primes = sorted(primes, key=lambda x: (math.degrees(x), x))
    return sorted_primes

class TestTaskFunc(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(task_func([4, 5, 2, 7, 89, 90]), [2, 5, 7, 89])
        self.assertEqual(task_func([101, 102, 103, 104]), [101, 103])

    def test_no_prime_numbers(self):
        self.assertEqual(task_func([4, 6, 8, 9, 10]), [])

    def test_empty_list(self):
        self.assertEqual(task_func([]), [])

    def test_large_numbers(self):
        self.assertEqual(task_func([100, 101, 102, 103, 104, 105]), [101, 103])

    def test_mixed_numbers(self):
        self.assertEqual(task_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [2, 3, 5, 7])

if __name__ == '__main__':
    unittest.main()