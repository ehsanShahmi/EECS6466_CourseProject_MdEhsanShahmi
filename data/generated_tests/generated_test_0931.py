import unittest
from collections import defaultdict
import re

def task_func(word: str) -> dict:
    """
    Find the occurrences of each two-letter combination in the sanitized word,
    where only alphabetic characters are considered.

    Requirements:
    - collections.defaultdict
    - re
    
    Parameters:
    word (str): The input string.

    Returns:
    collections.defaultdict: A dictionary with keys as two-letter combinations and values as their counts in the sanitized word.

    Example:
    >>> task_func('abcdef')
    defaultdict(<class 'int'>, {'ab': 1, 'bc': 1, 'cd': 1, 'de': 1, 'ef': 1})
    >>> task_func('aabbcc')
    defaultdict(<class 'int'>, {'aa': 1, 'ab': 1, 'bb': 1, 'bc': 1, 'cc': 1})
    >>> task_func('a1!b@c#d$')
    defaultdict(<class 'int'>, {'ab': 1, 'bc': 1, 'cd': 1})
    """

    sanitized_word = re.sub('[^A-Za-z]', '', word)
    occurrences = defaultdict(int)
    pairs = [''.join(x) for x in zip(sanitized_word, sanitized_word[1:])]

    for pair in pairs:
        occurrences[pair] += 1

    return occurrences


class TestTaskFunction(unittest.TestCase):
    
    def test_single_word(self):
        result = task_func('abcdef')
        expected = defaultdict(int, {'ab': 1, 'bc': 1, 'cd': 1, 'de': 1, 'ef': 1})
        self.assertEqual(result, expected)

    def test_repeated_characters(self):
        result = task_func('aabbcc')
        expected = defaultdict(int, {'aa': 1, 'ab': 1, 'bb': 1, 'bc': 1, 'cc': 1})
        self.assertEqual(result, expected)
    
    def test_ignore_non_alpha(self):
        result = task_func('a1!b@c#d$')
        expected = defaultdict(int, {'ab': 1, 'bc': 1, 'cd': 1})
        self.assertEqual(result, expected)

    def test_empty_string(self):
        result = task_func('')
        expected = defaultdict(int)
        self.assertEqual(result, expected)

    def test_single_character(self):
        result = task_func('a')
        expected = defaultdict(int)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()