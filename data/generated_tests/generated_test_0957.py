import unittest
import string
import re

def task_func(text: str) -> tuple:
    """
    Counts the number of words, characters, and unique characters in a given text.

    Parameters:
    - text (str): The input text to be analyzed.

    Returns:
    - tuple: A tuple containing three integers: the number of words,
                                                the number of characters,
                                                the number of unique characters.

    Requirements:
    - string
    - re

    Note:
    - This function considers whitespace-separated substrings as words.
    - When counting characters, this function excludes whitespace and special
      characters (i.e. string.punctuation).

    Example:
    >>> task_func('Hello, world!')
    (2, 10, 7)
    >>> task_func('Python is  awesome!  ')
    (3, 15, 12)
    """
    words = text.split()
    chars = re.sub("\s", "", re.sub(f"[{string.punctuation}]", "", text))
    return len(words), len(chars), len(set(chars))

class TestTaskFunc(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(task_func(""), (0, 0, 0))

    def test_single_word(self):
        self.assertEqual(task_func("Hello!"), (1, 5, 4))

    def test_multiple_words_with_punctuation(self):
        self.assertEqual(task_func("Hello, world! How are you?"), (6, 24, 17))

    def test_words_with_numbers(self):
        self.assertEqual(task_func("Python 3 is better than 2."), (6, 26, 15))
    
    def test_unique_characters(self):
        self.assertEqual(task_func("aa bB cC!!"), (3, 7, 3))

if __name__ == '__main__':
    unittest.main()