import unittest
from itertools import combinations
import math

def task_func(x, w):
    """
    Find the continuous substring of x, which has the maximum total weight, given a dictionary where the keys are characters and the values are their weights.

    Parameters:
    - x (str): The input string.
    - w (dict): The dictionary of character weights.

    Returns:
    - max_substr (str): The continuous substring with the highest weight.

    Requirements:
    - itertools
    - math

    Example:
    >>> task_func('c', {'a': 1, 'b': 2, 'c': 3})
    'c'
    >>> task_func('abc', {'a': 10, 'b': -5, 'c': 3})
    'a'
    """

    max_weight = -math.inf
    max_substr = ''

    for start, end in combinations(range(len(x) + 1), 2):
        substr = x[start:end]
        weight = sum(w.get(c, 0) for c in substr)
        if weight > max_weight:
            max_weight = weight
            max_substr = substr

    return max_substr

class TestTaskFunc(unittest.TestCase):
    
    def test_single_character(self):
        self.assertEqual(task_func('c', {'a': 1, 'b': 2, 'c': 3}), 'c')
        
    def test_mixed_weights(self):
        self.assertEqual(task_func('abc', {'a': 10, 'b': -5, 'c': 3}), 'a')
        
    def test_empty_string(self):
        self.assertEqual(task_func('', {'a': 1, 'b': 1}), '')
        
    def test_all_negative_weights(self):
        self.assertEqual(task_func('abc', {'a': -1, 'b': -2, 'c': -3}), '')
        
    def test_character_weight_zeros(self):
        self.assertEqual(task_func('abc', {'a': 0, 'b': 0, 'c': 0}), '')

if __name__ == '__main__':
    unittest.main()