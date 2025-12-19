import re
from collections import Counter
import unittest

def task_func(sentence):
    """
    Count the occurrence of each word in a sentence and return the result as a dictionary.
    This function uses a regular expression to find words and a Counter to count their occurrences.

    Parameters:
    sentence (str): The sentence to count the words in.

    Returns:
    dict: A dictionary where the keys are the words and the values are their counts.

    Requirements:
    - re
    - collections.Counter
    
    Example:
    >>> task_func("apple banana apple orange orange orange")
    {'apple': 2, 'banana': 1, 'orange': 3}
    """

    words = re.findall(r'\b\w+\b', sentence)
    return dict(Counter(words))

class TestTaskFunc(unittest.TestCase):

    def test_basic_counts(self):
        self.assertEqual(task_func("apple banana apple orange orange orange"), {'apple': 2, 'banana': 1, 'orange': 3})

    def test_no_words(self):
        self.assertEqual(task_func(""), {})

    def test_single_word(self):
        self.assertEqual(task_func("word"), {'word': 1})

    def test_mixed_case_words(self):
        self.assertEqual(task_func("Apple apple aPPle"), {'Apple': 1, 'apple': 2, 'aPPle': 1})

    def test_punctuation_in_sentence(self):
        self.assertEqual(task_func("Hello, world! Hello... world?"), {'Hello': 2, 'world': 2})

if __name__ == '__main__':
    unittest.main()