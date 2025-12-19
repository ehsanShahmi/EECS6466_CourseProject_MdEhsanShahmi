import unittest
import itertools
from random import shuffle

def task_func(numbers=list(range(1, 3))):
    """
    Calculates the average of the sums of absolute differences between each pair of consecutive numbers 
    for all permutations of a given list. Each permutation is shuffled before calculating the differences.

    Args:
    - numbers (list): A list of numbers. Default is numbers from 1 to 10.
    
    Returns:
    float: The average of the sums of absolute differences for each shuffled permutation of the list.

    Requirements:
    - itertools
    - random.shuffle

    Example:
    >>> result = task_func([1, 2, 3])
    >>> isinstance(result, float)
    True
    """

    permutations = list(itertools.permutations(numbers))
    sum_diffs = 0

    for perm in permutations:
        perm = list(perm)
        shuffle(perm)
        diffs = [abs(perm[i] - perm[i+1]) for i in range(len(perm)-1)]
        sum_diffs += sum(diffs)

    avg_sum_diffs = sum_diffs / len(permutations)
    
    return avg_sum_diffs

class TestTaskFunc(unittest.TestCase):

    def test_average_for_small_range(self):
        """Test for small range of numbers."""
        result = task_func([1, 2])
        self.assertAlmostEqual(result, 1.0)

    def test_average_for_three_numbers(self):
        """Test for three numbers."""
        result = task_func([1, 2, 3])
        self.assertAlmostEqual(result, 1.3333333333333333)

    def test_average_for_four_numbers(self):
        """Test for four numbers."""
        result = task_func([1, 2, 3, 4])
        self.assertAlmostEqual(result, 2.5)

    def test_average_for_five_numbers(self):
        """Test for five numbers."""
        result = task_func([1, 2, 3, 4, 5])
        self.assertAlmostEqual(result, 4.0)

    def test_average_for_empty_list(self):
        """Test for empty list input. Should handle gracefully."""
        result = task_func([])
        self.assertEqual(result, 0)  # Since there are no numbers to compare, the average should be defined as 0

if __name__ == '__main__':
    unittest.main()