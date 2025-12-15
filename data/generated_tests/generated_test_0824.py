import unittest
import re
import string

# Constants
PUNCTUATION = string.punctuation

def task_func(text):
    """
    Count the number of words and punctuation marks in a string.

    Parameters:
    - text (str): The input string.

    Returns:
    - tuple: A tuple containing the number of words and punctuation marks.

    Requirements:
    - re
    - string

    Example:
    >>> task_func("Hello, world! This is a test.")
    (6, 3)
    """
    words = re.findall(r'\b\w+\b', text)
    punctuation_marks = [char for char in text if char in PUNCTUATION]

    return len(words), len(punctuation_marks)

class TestTaskFunc(unittest.TestCase):

    def test_empty_string(self):
        result = task_func("")
        self.assertEqual(result, (0, 0))
        
    def test_no_words_only_punctuation(self):
        result = task_func("!!!")
        self.assertEqual(result, (0, 3))
    
    def test_only_words_no_punctuation(self):
        result = task_func("This is a test")
        self.assertEqual(result, (4, 0))
    
    def test_mixed_input(self):
        result = task_func("Hello, world! This is a test.")
        self.assertEqual(result, (6, 3))
    
    def test_special_characters(self):
        result = task_func("What? Yes! It's true: 100% sure...")
        self.assertEqual(result, (8, 6))

if __name__ == '__main__':
    unittest.main()