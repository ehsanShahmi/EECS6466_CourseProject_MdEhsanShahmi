import collections
import random
import string
import unittest

def task_func(length=100):
    """
    Generate a random string of the specified length composed of uppercase and lowercase letters, 
    and then count the occurrence of each character in this string.

    Parameters:
    length (int, optional): The number of characters in the generated string. Default is 100.

    Returns:
    dict: A dictionary where each key is a character from the generated string and the value 
            is the count of how many times that character appears in the string.

    Requirements:
    - collections
    - random
    - string

    Raises:
    ValueError if the length is a negative number

    Example:
    >>> import random
    >>> random.seed(42)  # Ensures reproducibility for demonstration
    >>> task_func(10)
    {'h': 1, 'B': 2, 'O': 1, 'L': 1, 'm': 1, 'j': 1, 'u': 1, 'E': 1, 'V': 1}
    """
    if length < 0:
        raise ValueError
    random_string = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=length))
    char_counts = collections.Counter(random_string)
    return dict(char_counts)

class TestTaskFunc(unittest.TestCase):
    
    def test_default_length(self):
        """ Test with default length of 100 """
        result = task_func()
        self.assertEqual(len(result), 52)  # There are 52 possible characters (26 uppercase + 26 lowercase)

    def test_zero_length(self):
        """ Test with length of 0, should return empty dictionary """
        result = task_func(0)
        self.assertEqual(result, {})

    def test_negative_length(self):
        """ Test with a negative length, should raise ValueError """
        with self.assertRaises(ValueError):
            task_func(-1)

    def test_character_count(self):
        """ Test if the character count reflects the length of string generated """
        length = 50
        result = task_func(length)
        self.assertEqual(sum(result.values()), length)

    def test_distribution_of_characters(self):
        """ Test if character counts does not exceed the random length """
        length = 200
        result = task_func(length)
        for count in result.values():
            self.assertLessEqual(count, length)

if __name__ == '__main__':
    unittest.main()