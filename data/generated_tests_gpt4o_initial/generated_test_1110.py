import unittest
from collections import Counter
from operator import itemgetter
import itertools

def task_func(word_dict):
    """
    Given a dictionary of words as keys and letters as values, count the frequency of each letter in the words.
    
    Parameters:
    word_dict (dict): The dictionary with words as keys and their letters as values.
    
    Returns:
    dict: A dictionary with letters as keys and their frequencies as values.
    
    Requirements:
    - collections.Counter
    - operator.itemgetter
    - itertools
    
    Example:
    >>> word_dict = {'apple': 'a', 'banana': 'b', 'cherry': 'c', 'date': 'd', 'elderberry': 'e', 'fig': 'f', 'grape': 'g', 'honeydew': 'h'}
    >>> counts = task_func(word_dict)
    >>> print(counts)
    {'e': 9, 'a': 6, 'r': 6, 'p': 3, 'n': 3, 'y': 3, 'd': 3, 'l': 2, 'b': 2, 'h': 2, 'g': 2, 'c': 1, 't': 1, 'f': 1, 'i': 1, 'o': 1, 'w': 1}
    """
    letters = list(itertools.chain.from_iterable(word_dict.keys()))
    count_dict = dict(Counter(letters))
    
    sorted_dict = dict(sorted(count_dict.items(), key=itemgetter(1), reverse=True))
    
    return sorted_dict

class TestTaskFunc(unittest.TestCase):
    
    def test_basic_case(self):
        word_dict = {'apple': 'a', 'banana': 'b', 'cherry': 'c'}
        expected = {'a': 2, 'b': 1, 'c': 1, 'e': 1, 'h': 1, 'l': 1, 'n': 1, 'p': 1, 'r': 1, 'y': 1}
        result = task_func(word_dict)
        self.assertEqual(result, expected)

    def test_multiple_occurrences(self):
        word_dict = {'letter': 'a', 'letter': 'b', 'letter': 'c', 'letter': 'd'}
        expected = {'e': 4, 't': 4, 'l': 2, 'r': 2}
        result = task_func(word_dict)
        self.assertEqual(result, expected)

    def test_empty_dict(self):
        word_dict = {}
        expected = {}
        result = task_func(word_dict)
        self.assertEqual(result, expected)

    def test_single_character(self):
        word_dict = {'a': 'a'}
        expected = {'a': 1}
        result = task_func(word_dict)
        self.assertEqual(result, expected)

    def test_all_unique_characters(self):
        word_dict = {'abc': 'a', 'def': 'd'}
        expected = {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1}
        result = task_func(word_dict)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()