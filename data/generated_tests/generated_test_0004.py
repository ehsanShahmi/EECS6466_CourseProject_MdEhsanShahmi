import unittest
from collections import Counter
import itertools

def task_func(d):
    """
    Count the occurrence of each integer in the values of the input dictionary, where each value is a list of integers,
    and return a dictionary with these counts. The resulting dictionary's keys are the integers, and the values are 
    their respective counts across all lists in the input dictionary.

    Parameters:
    d (dict): A dictionary where each key is a string and the value is a list of integers.

    Returns:
    dict: A dictionary where each key is an integer from any of the input lists, and the value is the count of 
            how often that integer appears in all the lists combined.

    Requirements:
    - collections.Counter
    - itertools
    
    Example:
    >>> d = {'a': [1, 2, 3, 1], 'b': [3, 4, 5], 'c': [1, 2]}
    >>> count_dict = task_func(d)
    >>> print(count_dict)
    {1: 3, 2: 2, 3: 2, 4: 1, 5: 1}
    """

    count_dict = Counter(itertools.chain.from_iterable(d.values()))
    return dict(count_dict)

class TestTaskFunc(unittest.TestCase):

    def test_empty_dict(self):
        self.assertEqual(task_func({}), {})

    def test_single_key_multiple_values(self):
        self.assertEqual(task_func({'a': [1, 2, 1]}), {1: 2, 2: 1})

    def test_multiple_keys_unique_values(self):
        self.assertEqual(task_func({'a': [1], 'b': [2], 'c': [3]}), {1: 1, 2: 1, 3: 1})

    def test_multiple_keys_repeated_values(self):
        self.assertEqual(task_func({'a': [1, 1], 'b': [1, 2], 'c': [2, 2]}), {1: 3, 2: 3})

    def test_mixed_values(self):
        self.assertEqual(task_func({'a': [1, 2], 'b': [1, 3, 3], 'c': [2, 4]}), {1: 2, 2: 2, 3: 2, 4: 1})

if __name__ == '__main__':
    unittest.main()