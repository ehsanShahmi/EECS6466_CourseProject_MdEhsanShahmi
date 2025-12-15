import itertools
import math
from pandas import Series
import unittest

def task_func(elements, subset_size, top_n=2):
    """
    Generate all subsets of a given size from a tuple and calculate the product of the sums of the subsets. Additionally, 
    return the top_n sums of the subsets. If the subset size is larger than the tuple length, return 1. If the subset size is 0,
    return 1.

    Parameters:
    - elements (tuple): A tuple of elements to create subsets from.
    - subset_size (int): The size of the subsets to be generated.
    - top_n (int, Optional): The number of top subsets to return. Defaults to None.

    Returns:
    int: The product of the sums of the subsets.
    list: The top_n sums of the subsets as a pandas Series.
    """
    
    if subset_size > len(elements) or subset_size <= 0:
        return 1, []

    combinations = list(itertools.combinations(elements, subset_size))
    sums = [sum(combination) for combination in combinations if len(combination) != 0]
    product = math.prod(sums)
    top_sums = sorted(sums, reverse=True)[:top_n]
    top_sums = Series(top_sums)
    return product, top_sums

class TestTaskFunc(unittest.TestCase):

    def test_basic_functionality(self):
        prod, sums = task_func((1, 2, 3), 2)
        self.assertEqual(prod, 60)
        self.assertEqual(list(sums), [5, 4])
    
    def test_empty_tuple(self):
        prod, sums = task_func((), 2)
        self.assertEqual(prod, 1)
        self.assertEqual(list(sums), [])

    def test_subset_size_greater_than_tuple_length(self):
        prod, sums = task_func((1, 2), 3)
        self.assertEqual(prod, 1)
        self.assertEqual(list(sums), [])

    def test_zero_subset_size(self):
        prod, sums = task_func((1, 2, 3), 0)
        self.assertEqual(prod, 1)
        self.assertEqual(list(sums), [])

    def test_top_n_greater_than_available_sums(self):
        prod, sums = task_func((1, 2, 3, 4), 2, top_n=5)
        self.assertEqual(prod, 120)
        self.assertEqual(list(sums), [7, 6, 5, 4])

if __name__ == '__main__':
    unittest.main()