import re
import string
import unittest

# Constants
PUNCTUATION = string.punctuation

def task_func(text):
    """
    Divide a string into words, remove punctuation marks and convert them to lowercase letters.

    Parameters:
    - text (str): The input string.

    Returns:
    - cleaned_words (list): A list of cleaned words.

    Requirements:
    - re
    - string

    Example:
    >>> task_func("Hello, world! This is a test.")
    ['hello', 'world', 'this', 'is', 'a', 'test']
    """

    words = re.split(r'\s+', text)
    cleaned_words = [re.sub(f'[{PUNCTUATION}]', '', word).lower() for word in words]

    return cleaned_words

class TestTaskFunction(unittest.TestCase):

    def test_normal_sentence(self):
        self.assertEqual(task_func("Hello, world! This is a test."), ['hello', 'world', 'this', 'is', 'a', 'test'])

    def test_sentence_with_multiple_spaces(self):
        self.assertEqual(task_func("Hello,   world!   This   is   a   test."), ['hello', 'world', 'this', 'is', 'a', 'test'])

    def test_sentence_with_no_punctuation(self):
        self.assertEqual(task_func("Hello world This is a test"), ['hello', 'world', 'this', 'is', 'a', 'test'])

    def test_empty_string(self):
        self.assertEqual(task_func(""), [])

    def test_sentence_with_only_punctuation(self):
        self.assertEqual(task_func("!!!???"), [])

if __name__ == '__main__':
    unittest.main()