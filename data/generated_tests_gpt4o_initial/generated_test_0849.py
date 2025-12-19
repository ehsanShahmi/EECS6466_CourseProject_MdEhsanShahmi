import re
from nltk.corpus import stopwords
from collections import Counter
import unittest

STOPWORDS = set(stopwords.words('english'))

def task_func(input_string):
    """
    Divide a multi-line string into individual lines, remove stopwords, and count the frequency of each word.

    Parameters:
    - input_string (str): The multi-line string.

    Returns:
    - dict: A dictionary with word frequencies where each key is a unique word and the value is its frequency.

    Requirements:
    - re
    - nltk.corpus
    - collections

    Example:
    >>> task_func('line a\\nfollows by line b\\n...bye\\n')
    {'line': 2, 'follows': 1, 'b': 1, 'bye': 1}
    """

    lines = input_string.split('\n')
    word_count = Counter()
    for line in lines:
        words = re.findall(r'\b\w+\b', line)
        words = [word for word in words if word not in STOPWORDS]
        word_count.update(words)
    return dict(word_count)

class TestTaskFunc(unittest.TestCase):

    def test_basic_functionality(self):
        result = task_func('line a\nfollows by line b\n...bye\n')
        expected = {'line': 2, 'follows': 1, 'b': 1, 'bye': 1}
        self.assertEqual(result, expected)

    def test_multiple_lines(self):
        result = task_func('hello world\nhello again\ngoodbye world\n')
        expected = {'hello': 2, 'world': 2, 'again': 1, 'goodbye': 1}
        self.assertEqual(result, expected)

    def test_with_stopwords(self):
        result = task_func('the quick brown fox jumps over the lazy dog\n')
        expected = {'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'lazy': 1, 'dog': 1}
        self.assertEqual(result, expected)

    def test_empty_string(self):
        result = task_func('')
        expected = {}
        self.assertEqual(result, expected)

    def test_string_with_only_stopwords(self):
        result = task_func('the and or\nbut if\n')
        expected = {}
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()