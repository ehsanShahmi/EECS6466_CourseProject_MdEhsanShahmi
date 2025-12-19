import unittest
import hashlib
import re

# Here is your prompt:
import re
import hashlib

def task_func(input_str):
    """
    Removes all special characters, punctuation marks, and spaces from the input string using a regular expression,
    retaining only alphanumeric characters. Then hashes the cleaned string with SHA256.

    Parameters:
    input_str (str): The input string to be cleaned and hashed.

    Returns:
    str: The SHA256 hash of the cleaned string.

    Requirements:
    - re
    - hashlib

    Example:
    >>> task_func('Special $#! characters   spaces 888323')
    'af30263c4d44d67917a4f0727191a4149e1ab615b772b2aeda859068178b146c'
    """

    cleaned_str = re.sub('[^A-Za-z0-9]+', '', input_str)
    hashed_str = hashlib.sha256(cleaned_str.encode()).hexdigest()

    return hashed_str

class TestTaskFunc(unittest.TestCase):

    def test_basic_string(self):
        self.assertEqual(task_func('Special $#! characters   spaces 888323'),
                         'af30263c4d44d67917a4f0727191a4149e1ab615b772b2aeda859068178b146c')

    def test_empty_string(self):
        self.assertEqual(task_func(''), 
                         'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855')

    def test_string_with_only_special_characters(self):
        self.assertEqual(task_func('!!!@@@###$$$%%%^^^&&&'), 
                         'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855')

    def test_string_with_spaces_only(self):
        self.assertEqual(task_func('     '), 
                         'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855')

    def test_string_with_alphanumeric_and_special_characters(self):
        self.assertEqual(task_func('ABC123!@#def456'), 
                         '90d3b5f98989c1da7dc1a2fadfe4e6ab5bfa7242fc33a1d82cbff72b224d52e9')

if __name__ == '__main__':
    unittest.main()