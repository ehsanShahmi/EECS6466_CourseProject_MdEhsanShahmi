import unittest
import numpy as np
import math

def task_func(L):
    """
    Calculate the median of all elements in a nested list 'L'.

    Parameters:
    - L (list): The nested list.

    Returns:
    - median (float): The median.

    Requirements:
    - numpy
    - math

    Example:
    >>> task_func([[1,2,3],[4,5,6]])
    3.5
    """

    def flatten(lst):
        flat_list = []
        for item in lst:
            if isinstance(item, list):
                flat_list.extend(flatten(item))
            else:
                flat_list.append(item)
        return flat_list
    
    flattened = flatten(L)
    
    if not flattened:
        raise ValueError("List is empty")
    
    sorted_flattened = np.sort(flattened)
    n = len(sorted_flattened)
    
    if n % 2 == 0:
        median_index1 = math.ceil(n / 2) - 1
        median_index2 = median_index1 + 1
        median = (sorted_flattened[median_index1] + sorted_flattened[median_index2]) / 2.0
    else:
        median_index = math.ceil(n / 2) - 1
        median = sorted_flattened[median_index]

    return median

class TestTaskFunc(unittest.TestCase):
    
    def test_flat_list_with_even_numbers(self):
        self.assertEqual(task_func([[4, 2, 3], [1, 6, 5]]), 3.5)
    
    def test_flat_list_with_odd_numbers(self):
        self.assertEqual(task_func([[1, 3, 5], [2, 4]]), 3)
    
    def test_flat_list_with_single_element(self):
        self.assertEqual(task_func([[42]]), 42)
    
    def test_flat_list_with_empty_sublist(self):
        self.assertEqual(task_func([[1, 2, 3], [], [4, 5]]), 3)
    
    def test_empty_list(self):
        with self.assertRaises(ValueError) as context:
            task_func([])
        self.assertEqual(str(context.exception), "List is empty")

if __name__ == '__main__':
    unittest.main()