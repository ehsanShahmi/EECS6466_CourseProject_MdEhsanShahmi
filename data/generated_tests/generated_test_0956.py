import unittest
import random
import string
import re

# Here is your prompt:

def task_func(text: str, seed=None) -> str:
    """
    Transforms a given string by removing special characters, normalizing whitespace,
    and randomizing character casing.

    Parameters:
    - text (str): The text string to be preprocessed.
    - seed (int, optional): Random seed for reproducibility. Defaults to None (not set).

    Returns:
    - str: The preprocessed text string.

    Requirements:
    - re
    - string
    - random

    Note:
    - This function considers special characters to be string punctuations.
    - Spaces, tabs, and newlines are replaced with with '_', '__', and '___' respectively.
    - To randomize casing, this function converts characters to uppercase with a 50% probability.

    Example:
    >>> task_func('Hello   World!', 0)
    'HeLlo___WORlD'
    >>> task_func('attention is all you need', 42)
    'ATtENTIOn_IS_ALL_You_Need'
    """

           
    if seed is not None:
        random.seed(seed)

    text = re.sub("[%s]" % re.escape(string.punctuation), "", text)

    REPLACEMENTS = {" ": "_", "\t": "__", "\n": "___"}
    for k, v in REPLACEMENTS.items():
        text = text.replace(k, v)

    text = "".join(random.choice([k.upper(), k]) for k in text)

    return text


class TestTaskFunc(unittest.TestCase):
    
    def test_basic_transform(self):
        result = task_func('Hello   World!', seed=0)
        # Validate that special characters are removed and whitespace is normalized
        self.assertRegex(result, r'^[a-zA-Z_]+$')
        self.assertIn('___', result)

    def test_multiple_spaces(self):
        result = task_func('This is   a  test.', seed=1)
        # Ensure multiple spaces are turned into a single underscore
        self.assertNotIn(' ', result)
        self.assertTrue('_' in result)  # Check underscore is present

    def test_special_characters(self):
        result = task_func('What a *great* day!!', seed=2)
        # Check punctuation is removed
        self.assertNotRegex(result, r'[^\w\s]')  # No special characters

    def test_case_randomization(self):
        result = task_func('Check case!', seed=3)
        # Check that result contains both uppercase and lowercase characters
        upper_count = sum(1 for c in result if c.isupper())
        lower_count = sum(1 for c in result if c.islower())
        self.assertGreater(upper_count, 0)
        self.assertGreater(lower_count, 0)

    def test_seed_reproducibility(self):
        result1 = task_func('Hello World!', seed=42)
        result2 = task_func('Hello World!', seed=42)
        # Ensure that using the same seed produces the same output
        self.assertEqual(result1, result2)


if __name__ == '__main__':
    unittest.main()