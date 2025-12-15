import math
import itertools
from functools import reduce
import unittest

def task_func(numbers):
    """
    Generates all possible combinations of the provided numbers in a given list for
    each possible length. For each combination, it computes the product of the numbers
    in the combination. It then computes the logarithm of each product and sums these
    logarithms to produce the final result.

    Parameters:
        numbers (list of int): A list of integers for which combinations are formed.

    Requirements:
    - math
    - itertools
    - functools

    Returns:
        float: The sum of the logarithms of the products of all combinations of numbers.
    """
    sum_log_products = 0

    for r in range(1, len(numbers) + 1):
        combinations = itertools.combinations(numbers, r)
        for combination in combinations:
            product = reduce(lambda x, y: x * y, combination)
            sum_log_products += math.log(product)

    return sum_log_products

class TestTaskFunc(unittest.TestCase):

    def test_empty_list(self):
        """Test with an empty list, should return 0.0 as there are no combinations."""
        self.assertEqual(task_func([]), 0.0)

    def test_single_element(self):
        """Test with a single element list, should return log(element)."""
        self.assertAlmostEqual(task_func([5]), math.log(5))

    def test_two_elements(self):
        """Test with two elements, should return the sum of logs of both products
        (the individual elements and the product of both)."""
        result = task_func([2, 3])
        self.assertAlmostEqual(result, math.log(2) + math.log(3) + math.log(6))

    def test_three_elements(self):
        """Test with three elements, should return sum of logs for all combinations."""
        result = task_func([2, 3, 4])
        expected_result = (math.log(2) + math.log(3) + math.log(4) + 
                           math.log(6) + math.log(8) + math.log(12) + 
                           math.log(24))
        self.assertAlmostEqual(result, expected_result)

    def test_large_numbers(self):
        """Test with larger numbers to ensure proper handling of larger products."""
        result = task_func([100, 200, 300])
        expected_result = (math.log(100) + math.log(200) + math.log(300) + 
                           math.log(20000) + math.log(30000) + 
                           math.log(6000000) + math.log(60000000))
        self.assertAlmostEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()