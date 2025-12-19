import unittest
import re
import string

def task_func(text1, text2):
    """
    This function takes two strings, removes any ASCII punctuation using regular expressions, 
    and returns the cleaned strings as a tuple. It targets punctuation characters defined in 
    `string.punctuation`, which includes the following characters:
    '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    Note: This function may not remove non-ASCII or uncommon punctuation symbols.

    Parameters:
    text1, text2 (str): The original texts containing punctuation.

    Returns:
    tuple: A tuple containing the cleaned texts (text1, text2) with punctuation removed.

    Requirements:
    - re
    - string

    Example:
    >>> cleaned_text1, cleaned_text2 = task_func("Hello, world!", "How's it going?")
    >>> print(cleaned_text1, cleaned_text2)
    Hello world Hows it going

    >>> cleaned_text1, cleaned_text2 = task_func("test (with parenthesis []!!)", "And, other; stuff ^_`")
    >>> print(cleaned_text1, cleaned_text2)
    test with parenthesis  And other stuff 
    """

    # Constants
    PUNCTUATION = string.punctuation

    cleaned_texts = []

    # Remove punctuation from each text string
    for text in [text1, text2]:
        cleaned_text = re.sub('[' + re.escape(PUNCTUATION) + ']', '', text)
        cleaned_texts.append(cleaned_text)

    return tuple(cleaned_texts)

class TestTaskFunc(unittest.TestCase):
    
    def test_basic_input(self):
        cleaned_text1, cleaned_text2 = task_func("Hello, world!", "How's it going?")
        self.assertEqual(cleaned_text1, "Hello world")
        self.assertEqual(cleaned_text2, "Hows it going")

    def test_with_parentheses(self):
        cleaned_text1, cleaned_text2 = task_func("test (with parenthesis []!!)", "And, other; stuff ^_`")
        self.assertEqual(cleaned_text1, "test with parenthesis ")
        self.assertEqual(cleaned_text2, "And other stuff ")

    def test_empty_strings(self):
        cleaned_text1, cleaned_text2 = task_func("", "")
        self.assertEqual(cleaned_text1, "")
        self.assertEqual(cleaned_text2, "")

    def test_no_punctuation(self):
        cleaned_text1, cleaned_text2 = task_func("No punctuation here", "Same goes for this")
        self.assertEqual(cleaned_text1, "No punctuation here")
        self.assertEqual(cleaned_text2, "Same goes for this")

    def test_only_punctuation(self):
        cleaned_text1, cleaned_text2 = task_func("!!!???", "....,,,")
        self.assertEqual(cleaned_text1, "")
        self.assertEqual(cleaned_text2, "")

if __name__ == '__main__':
    unittest.main()