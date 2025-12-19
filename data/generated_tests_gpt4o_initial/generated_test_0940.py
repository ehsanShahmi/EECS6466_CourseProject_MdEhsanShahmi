import re
from nltk import word_tokenize
from collections import Counter
import unittest

def task_func(input_str):
    """
    Remove all special characters, punctuation marks and spaces from a string called "input _ str" using regex and then count the frequency of each word.

    Parameters:
    input_str (str): The input string.

    Returns:
    dict: A dictionary with the frequency of each word.

    Requirements:
    - re
    - nltk.word_tokenize
    - collections.Counter

    Example:
    >>> task_func('Special $#! characters   spaces 888323')
    Counter({'Special': 1, 'characters': 1, 'spaces': 1, '888323': 1})
    """
    
    cleaned_str = re.sub('[^A-Za-z0-9 ]+', '', input_str)
    words = word_tokenize(cleaned_str)
    freq_dict = Counter(words)

    return freq_dict

class TestTaskFunc(unittest.TestCase):
    
    def test_basic_string(self):
        self.assertEqual(task_func('Hello world!'), Counter({'Hello': 1, 'world': 1}))
        
    def test_string_with_numbers(self):
        self.assertEqual(task_func('Test 123 test 123'), Counter({'Test': 1, '123': 2, 'test': 1}))
        
    def test_string_with_special_characters(self):
        self.assertEqual(task_func('Special $#! characters   spaces 888323'), Counter({'Special': 1, 'characters': 1, 'spaces': 1, '888323': 1}))

    def test_empty_string(self):
        self.assertEqual(task_func(''), Counter())
    
    def test_string_with_multiple_spaces(self):
        self.assertEqual(task_func('   multiple    spaces   here   '), Counter({'multiple': 1, 'spaces': 1, 'here': 1}))

if __name__ == '__main__':
    unittest.main()