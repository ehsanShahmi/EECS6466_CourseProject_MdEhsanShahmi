import unittest
import collections
import heapq

def task_func(x, n):
    """
    Find the n most common letters in a dictionary, x, where the key letters and the values are their frequencies.

    Parameters:
    - x (dict): The dictionary of letter frequencies.
    - n (int): The number of most frequent letters to return.

    Returns:
    - list: The n most frequent letters.

    Requirements:
    - heapq
    - collections

    Example:
    >>> task_func({'a': 1, 'b': 2, 'c': 3}, 2)
    ['c', 'b']
    """

    counter = collections.Counter(x)
    most_frequent = heapq.nlargest(n, counter.keys(), key=counter.get)

    return most_frequent

class TestTaskFunc(unittest.TestCase):

    def test_basic_functionality(self):
        result = task_func({'a': 1, 'b': 2, 'c': 3}, 2)
        self.assertEqual(result, ['c', 'b'])

    def test_more_letters(self):
        result = task_func({'a': 5, 'b': 3, 'c': 8, 'd': 2}, 3)
        self.assertEqual(result, ['c', 'a', 'b'])

    def test_edge_case_n_is_zero(self):
        result = task_func({'a': 1, 'b': 2, 'c': 3}, 0)
        self.assertEqual(result, [])

    def test_n_exceeds_unique_letters(self):
        result = task_func({'a': 2, 'b': 4}, 10)
        self.assertEqual(result, ['b', 'a'])

    def test_single_letter(self):
        result = task_func({'a': 10}, 1)
        self.assertEqual(result, ['a'])

if __name__ == '__main__':
    unittest.main()