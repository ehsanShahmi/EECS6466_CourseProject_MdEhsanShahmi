import unittest
from collections import Counter
import re

def task_func(input_str):
    """
    Count the frequency of each alphanumeric character in a given string after removing all non-alphanumeric characters,
    treating uppercase and lowercase letters as the same.

    Requirements:
    - re
    - collections.Counter

    Parameters:
    - input_str (str): The input string containing alphanumeric characters mixed with special characters and/or spaces.

    Returns:
    - dict: A dictionary with characters as keys (all lowercase) and their frequencies in the input string as values.
    
    Examples:
    >>> task_func("Hello, World!")
    Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, 'w': 1, 'r': 1, 'd': 1})
    """

    cleaned_str = re.sub('[^A-Za-z0-9]+', '', input_str).lower()
    freq_dict = Counter(cleaned_str)
    return freq_dict

class TestTaskFunc(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(task_func(""), Counter())

    def test_special_characters(self):
        self.assertEqual(task_func("!!!@@@###"), Counter())

    def test_mixed_case_characters(self):
        self.assertEqual(task_func("aA"), Counter({'a': 2}))

    def test_numerical_characters(self):
        self.assertEqual(task_func("123123"), Counter({'1': 2, '2': 2, '3': 2}))

    def test_alphanumeric_with_spaces(self):
        self.assertEqual(task_func("Hello World 123!"), Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, 'w': 1, 'r': 1, 'd': 1, '1': 1, '2': 1, '3': 1}))

if __name__ == '__main__':
    unittest.main()