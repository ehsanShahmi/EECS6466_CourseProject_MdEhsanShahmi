import collections
from itertools import zip_longest
from random import choices
import unittest

def task_func(l1, l2, K=10):
    """
    Combine two lists by alternating their elements, even if they are of different lengths. 
    Elements from the longer list without a counterpart in the shorter one will be included on their own.
    Then, create a random sample of size K from the combined list, and calculate the frequency of 
    each element in the sample.

    Parameters:
    l1 (list): The first list containing any hashable types.
    l2 (list): The second list containing any hashable types.
    K (int): the size of the random sample from the combined list. Default to 10.

    Returns:
    collections.Counter: An object that counts the frequency of each element in the sample.

    Requirements:
    - collections
    - itertools.zip_longest
    - random.choices
    """

    combined = [val for pair in zip_longest(l1, l2) for val in pair if val is not None]
    sample = choices(combined, k=K)
    freq = collections.Counter(sample)
    return freq

class TestTaskFunc(unittest.TestCase):
    
    def test_same_length_lists(self):
        l1 = [1, 2, 3]
        l2 = [4, 5, 6]
        freq = task_func(l1, l2, K=5)
        self.assertGreaterEqual(sum(freq.values()), 1)
        self.assertLessEqual(len(freq), 6)

    def test_different_length_lists(self):
        l1 = [1, 2, 3, 4]
        l2 = [5, 6]
        freq = task_func(l1, l2, K=10)
        self.assertGreaterEqual(sum(freq.values()), 1)
        self.assertLessEqual(len(freq), 6)

    def test_empty_lists(self):
        l1 = []
        l2 = []
        freq = task_func(l1, l2, K=10)
        self.assertEqual(freq, collections.Counter())

    def test_varied_data_types(self):
        l1 = [1, 'a', 2.5]
        l2 = ['b', None, 3]
        freq = task_func(l1, l2, K=10)
        self.assertGreaterEqual(sum(freq.values()), 1)
        self.assertLessEqual(len(freq), 6)

    def test_large_k_value(self):
        l1 = [1, 2]
        l2 = [3, 4]
        freq = task_func(l1, l2, K=1000)
        self.assertGreaterEqual(sum(freq.values()), 1)
        self.assertLessEqual(len(freq), 4)

if __name__ == '__main__':
    unittest.main()