import re
from collections import Counter
import unittest

def task_func(text, top_n):
    """
    Count the N most common words in a text after removing URLs.

    Parameters:
    text (str): The text to analyze.
    top_n (int): The number of top words to return.

    Returns:
    list: A list of tuples where each tuple contains a word and its frequency.

    Requirements:
    - re
    - collections.Counter

    Example:
    >>> task_func('Visit https://www.python.org for more info. Python is great. I love Python.', 2)
    [('Python', 2), ('Visit', 1)]

    Note:
    - Valid url is start with http or https
    """
    # Remove URLs
    text = re.sub('http[s]?://\S+', '', text)

    # Tokenize the text using regex (improved tokenization)
    words = re.findall(r'\b\w+\b', text)

    # Count the frequency of each word
    word_freq = Counter(words)

    return word_freq.most_common(top_n)

class TestTaskFunc(unittest.TestCase):

    def test_basic_functionality(self):
        result = task_func('Visit https://www.python.org for more info. Python is great. I love Python.', 2)
        expected = [('Python', 2), ('Visit', 1)]
        self.assertEqual(result, expected)

    def test_no_urls(self):
        result = task_func('Hello world. This is a test. Hello again.', 2)
        expected = [('Hello', 2), ('world', 1)]
        self.assertEqual(result, expected)

    def test_only_urls(self):
        result = task_func('Check this: https://google.com and http://example.com', 2)
        expected = []
        self.assertEqual(result, expected)

    def test_case_sensitivity(self):
        result = task_func('Same word different cases: hello, Hello, HELLO.', 3)
        expected = [('hello', 1), ('Hello', 1), ('HELLO', 1)]
        self.assertEqual(result, expected)

    def test_empty_string(self):
        result = task_func('', 2)
        expected = []
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()