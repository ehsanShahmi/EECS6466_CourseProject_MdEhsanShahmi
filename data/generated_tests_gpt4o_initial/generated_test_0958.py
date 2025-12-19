import unittest
import random
import re

def task_func(text, seed=None):
    """
    Scramble the letters in each word of a given text, keeping the first and last letters of each word intact.

    Parameters:
    text (str): The text to be scrambled.
    seed (int, optional): A seed for the random number generator to ensure reproducible results.
                          Defaults to None (not set).

    Returns:
    str: The scrambled text.

    Requirements:
    - random
    - re

    Notes:
    - Words are determined by regex word boundaries.
    - The scrambling only affects words longer than three characters, leaving shorter words unchanged.

    Examples:
    >>> task_func('Hello, world!', 0)
    'Hello, wlrod!'
    >>> task_func("Programming is fun, isn't it?", 42)
    "Prmiangmrog is fun, isn't it?"
    """

    if seed is not None:
        random.seed(seed)

    def scramble_word(match):
        word = match.group(0)
        if len(word) > 3:
            middle = list(word[1:-1])
            random.shuffle(middle)
            return word[0] + "".join(middle) + word[-1]
        else:
            return word

    pattern = r"\b\w+\b"
    scrambled_text = re.sub(pattern, scramble_word, text)

    return scrambled_text

class TestTaskFunc(unittest.TestCase):

    def test_scramble_words(self):
        self.assertNotEqual(task_func('Hello world!', 0), 'Hello world!')
        self.assertNotEqual(task_func('Scrambling words is fun.', 1), 'Scrambling words is fun.')

    def test_preserve_short_words(self):
        self.assertEqual(task_func('I am fine.', None), 'I am fine.')
        self.assertEqual(task_func('A B C.', None), 'A B C.')

    def test_reproducibility(self):
        result1 = task_func('Scramble this', 42)
        result2 = task_func('Scramble this', 42)
        self.assertEqual(result1, result2)

    def test_empty_string(self):
        self.assertEqual(task_func('', None), '')

    def test_ignore_non_alphabetic_characters(self):
        self.assertEqual(task_func('How are you today? 1234!!!', 0), 'How are you tdoay? 1234!!!')

if __name__ == '__main__':
    unittest.main()