import unittest
import random
import string

# Constants
LETTERS = string.ascii_letters

def task_func(num_words, word_length):
    """
    Create a list of random words of a certain length.

    Parameters:
    - num_words (int): The number of words to generate.
    - word_length (int): The length of each word.

    Returns:
    - words (list): A list of random words.

    Requirements:
    - random
    - string

    Raises:
    - ValueError: If num_words or word_length is negative.
    
    Example:
    >>> task_func(5, 3)
    ['Ohb', 'Vrp', 'oiV', 'gRV', 'IfL']
    """

    # Validate input parameters
    if num_words < 0 or word_length < 0:
        raise ValueError("num_words and word_length must be non-negative")

    random.seed(42)
    words = [''.join(random.choice(LETTERS) for _ in range(word_length)) for _ in range(num_words)]
    
    return words

class TestTaskFunc(unittest.TestCase):

    def test_zero_words(self):
        """Test when num_words is 0, should return an empty list."""
        self.assertEqual(task_func(0, 5), [])

    def test_single_word(self):
        """Test when generating a single word of length 6."""
        result = task_func(1, 6)
        self.assertEqual(len(result), 1)
        self.assertEqual(len(result[0]), 6)

    def test_multiple_words(self):
        """Test generating multiple words of length 4."""
        result = task_func(5, 4)
        self.assertEqual(len(result), 5)
        for word in result:
            self.assertEqual(len(word), 4)

    def test_negative_num_words(self):
        """Test when num_words is negative, should raise ValueError."""
        with self.assertRaises(ValueError):
            task_func(-1, 5)

    def test_negative_word_length(self):
        """Test when word_length is negative, should raise ValueError."""
        with self.assertRaises(ValueError):
            task_func(5, -1)

if __name__ == '__main__':
    unittest.main()