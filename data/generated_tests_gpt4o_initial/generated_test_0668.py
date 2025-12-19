import itertools
import math
import unittest

def task_func(x):
    """
    Find the sub-sequence of a dictionary, x, with the minimum total length, where the keys are letters and the values are their lengths.

    Parameters:
    - x (dict): The dictionary of letter lengths.

    Returns:
    - list: The subsequence with the minimum total length.

    Requirements:
    - itertools
    - math

    Example:
    >>> task_func({'a': 1, 'b': 2, 'c': 3})
    ['a']
    >>> task_func({'a': 1, 'b': -2, 'c': -5, 'd': 4})
    ['b', 'c']
    """

    min_length = math.inf
    min_subseq = []

    for r in range(1, len(x) + 1):
        for subseq in itertools.combinations(x.items(), r):
            length = sum(length for letter, length in subseq)
            if length < min_length:
                min_length = length
                min_subseq = [letter for letter, length in subseq]

    return min_subseq

class TestTaskFunc(unittest.TestCase):
    
    def test_case_1(self):
        self.assertEqual(task_func({'a': 1, 'b': 2, 'c': 3}), ['a'])
    
    def test_case_2(self):
        self.assertEqual(task_func({'a': 1, 'b': -2, 'c': -5, 'd': 4}), ['b', 'c'])
    
    def test_case_3(self):
        self.assertEqual(task_func({'x': 10, 'y': -4, 'z': 3}), ['y', 'z'])
    
    def test_case_4(self):
        self.assertEqual(task_func({'one': 5, 'two': 5, 'three': 5}), ['one'])
    
    def test_case_5(self):
        self.assertEqual(task_func({'a': -1, 'b': -2, 'c': 3, 'd': 4}), ['a', 'b'])

if __name__ == '__main__':
    unittest.main()