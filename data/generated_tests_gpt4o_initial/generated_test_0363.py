import unittest
from multiprocessing import Pool
import math

def calculate_factorial(number: int) -> tuple:
    return number, math.factorial(number)

def task_func(numbers: list) -> dict:
    if not all(isinstance(n, int) and n >= 0 for n in numbers):
        raise ValueError("All elements in the list must be integers")
    with Pool() as pool:
        factorial_dict = dict(pool.starmap(calculate_factorial, [(i,) for i in numbers]))
    return factorial_dict

class TestTaskFunc(unittest.TestCase):

    def test_empty_list(self):
        """Test with an empty list should return an empty dictionary."""
        result = task_func([])
        self.assertEqual(result, {})

    def test_single_number(self):
        """Test with a single number should return the correct factorial."""
        result = task_func([5])
        self.assertEqual(result, {5: 120})

    def test_multiple_numbers(self):
        """Test with multiple numbers should return correct factorials."""
        result = task_func([3, 4, 5])
        self.assertEqual(result, {3: 6, 4: 24, 5: 120})

    def test_invalid_type(self):
        """Test should raise ValueError for non-integer values."""
        with self.assertRaises(ValueError):
            task_func([5, 'non-integer', 7])

    def test_negative_number(self):
        """Test should raise ValueError for negative numbers."""
        with self.assertRaises(ValueError):
            task_func([5, -1, 7])

if __name__ == '__main__':
    unittest.main()