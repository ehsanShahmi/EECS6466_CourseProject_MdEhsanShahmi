import unittest
from itertools import combinations
import math

def task_func(seq, letter_weight_dict):
    """
    Find the subsequence in a string that has the maximum total weight based on the weights given for each character. 
    The weights are assigned randomly and a subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.

    Parameters:
    - seq (str): The input string.
    - letter_weight_dict (dict): A dictionary with the weights for each character.

    Returns:
    - str: The subsequence with the highest weight.

    Requirements:
    - itertools
    - math

    Example:
    >>> task_func('abc', {'a': 1, 'b': 2, 'c': 3})
    'abc'
    >>> task_func('aabc', {'a': 10, 'b': -5, 'c': 3})
    'aac'
    """

    max_weight = -math.inf
    max_subseq = ''

    for r in range(1, len(seq) + 1):
        for subseq in combinations(seq, r):
            weight = sum(letter_weight_dict[c] for c in subseq)
            if weight > max_weight:
                max_weight = weight
                max_subseq = ''.join(subseq)

    return max_subseq

class TestTaskFunc(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(task_func('abc', {'a': 1, 'b': 2, 'c': 3}), 'abc')

    def test_case_with_negative_weights(self):
        self.assertEqual(task_func('aabc', {'a': 10, 'b': -5, 'c': 3}), 'aac')

    def test_empty_string(self):
        self.assertEqual(task_func('', {'a': 1, 'b': 2, 'c': 3}), '')

    def test_all_negative_weights(self):
        self.assertEqual(task_func('abc', {'a': -1, 'b': -2, 'c': -3}), '')

    def test_case_with_unweighted_characters(self):
        self.assertEqual(task_func('xyz', {'x': 5, 'y': 0, 'z': 2}), 'xz')

if __name__ == '__main__':
    unittest.main()