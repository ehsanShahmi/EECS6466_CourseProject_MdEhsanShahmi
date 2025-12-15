import unittest
from collections import Counter
import heapq

# Constants
LETTERS = list('abcdefghijklmnopqrstuvwxyz')

def task_func(my_dict):
    """
    Create a dictionary in which the keys are letters and the values are random integers.
    Find the 3 most common letters in the dictionary.

    Parameters:
    - my_dict (dict): The dictionary to process.

    Returns:
    - most_common_letters (list): The 3 most common letters.

    Requirements:
    - collections
    - heapq

    Example:
    >>> random.seed(43)
    >>> my_dict = {letter: random.randint(1, 100) for letter in LETTERS}
    >>> most_common_letters = task_func(my_dict)
    >>> print(most_common_letters)
    ['d', 'v', 'c']
    """

    letter_counter = Counter(my_dict)
    most_common_letters = heapq.nlargest(3, letter_counter, key=letter_counter.get)

    return most_common_letters

class TestTaskFunc(unittest.TestCase):
    
    def test_normal_case(self):
        my_dict = {'a': 5, 'b': 3, 'c': 7, 'd': 7, 'e': 2}
        expected = ['c', 'd', 'a']
        result = task_func(my_dict)
        self.assertEqual(result, expected)

    def test_all_letters_equal(self):
        my_dict = {letter: 1 for letter in LETTERS}
        expected = ['a', 'b', 'c']
        result = task_func(my_dict)
        self.assertEqual(result, expected)

    def test_empty_dict(self):
        my_dict = {}
        expected = []
        result = task_func(my_dict)
        self.assertEqual(result, expected)

    def test_tie_case(self):
        my_dict = {'a': 10, 'b': 10, 'c': 10, 'd': 5}
        expected = ['a', 'b', 'c']
        result = task_func(my_dict)
        self.assertTrue(set(result).issubset({'a', 'b', 'c'}))

    def test_large_values(self):
        my_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}
        expected = ['e', 'd', 'c']
        result = task_func(my_dict)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()