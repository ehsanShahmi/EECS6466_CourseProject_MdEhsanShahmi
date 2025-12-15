import re
import string
from random import choice
import unittest

def task_func(n, pattern):
    """
    Generates a random string of a specified length that conforms to a given regular expression pattern.
    The function repeatedly generates random strings, using both uppercase and lowercase ASCII letters,
    of the specified length until one matches the pattern.

    Parameters:
    n (int): The length of the string to be generated.
    pattern (str): A regular expression pattern the generated string must match, including start and end anchors.

    Returns:
    str: A randomly generated string that matches the specified pattern.

    Requirements:
    - re
    - string
    - random.choice

    Examples:
    >>> len(task_func(5, '[a-z]*')) == 5
    True

    >>> bool(re.match('^[A-Z]+$', task_func(3, '^[A-Z]+$')))
    True
    """

               while True:
        s = ''.join(choice(string.ascii_letters) for _ in range(n))
        if re.match(pattern, s):
            return s

class TestTaskFunc(unittest.TestCase):

    def test_length(self):
        """Test that the generated string has the correct length"""
        result = task_func(10, '.*')
        self.assertEqual(len(result), 10)

    def test_lowercase_pattern(self):
        """Test that the generated string matches the lowercase pattern"""
        result = task_func(5, '^[a-z]+$')
        self.assertTrue(bool(re.match('^[a-z]+$', result)))

    def test_uppercase_pattern(self):
        """Test that the generated string matches the uppercase pattern"""
        result = task_func(3, '^[A-Z]+$')
        self.assertTrue(bool(re.match('^[A-Z]+$', result)))

    def test_mixed_case_pattern(self):
        """Test that the generated string matches the mixed case pattern"""
        result = task_func(6, '^[A-Za-z]+$')
        self.assertTrue(bool(re.match('^[A-Za-z]+$', result)))

    def test_numeric_pattern(self):
        """Test that the generated string matches the numeric pattern"""
        result = task_func(4, '^[0-9]{4}$')
        self.assertTrue(bool(re.match('^[0-9]{4}$', result)))

if __name__ == '__main__':
    unittest.main()