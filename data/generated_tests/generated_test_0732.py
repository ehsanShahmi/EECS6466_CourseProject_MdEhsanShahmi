import re
import string
from nltk.stem import PorterStemmer
from collections import Counter
import unittest

STEMMER = PorterStemmer()

def task_func(content):
    """
    Stem every word in a sentence, except the last, and count the frequency of each stem.

    Parameters:
    content (str): The sentence to stem and count.

    Returns:
    dict: A dictionary with stemmed words as keys and their frequency as values.

    Requirements:
    - re
    - string
    - nltk.stem
    - collections.Counter

    Example:
    >>> task_func('running runner run')
    {'run': 1, 'runner': 1}
    """
    content = content.split(' ')[:-1]
    words = [word.strip(string.punctuation).lower() for word in re.split('\W+', ' '.join(content))]
    stemmed_words = [STEMMER.stem(word) for word in words]
    word_counts = Counter(stemmed_words)

    return dict(word_counts)


class TestTaskFunc(unittest.TestCase):

    def test_mixed_case_words(self):
        result = task_func('Running Runner RUN')
        expected = {'run': 1, 'runner': 1}
        self.assertEqual(result, expected)

    def test_punctuation_handling(self):
        result = task_func('Hello, world! This is a test sentence.')
        expected = {'hello': 1, 'world': 1, 'thi': 1, 'is': 1, 'a': 1, 'test': 1, 'sentenc': 1}
        self.assertEqual(result, expected)

    def test_empty_string(self):
        result = task_func('')
        expected = {}
        self.assertEqual(result, expected)

    def test_single_word(self):
        result = task_func('OnlyOneWord ')
        expected = {}
        self.assertEqual(result, expected)

    def test_numerical_words(self):
        result = task_func('I have 2 apples and 3 oranges.')
        expected = {'i': 1, 'have': 1, 'appl': 1, 'and': 1, 'orang': 1}
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()