import nltk
import unittest
from collections import Counter

# Download necessary NLTK data (if not already present)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def task_func(content):
    """
    Count the Part-of-Speech (POS) tags in a sentence without the last word.

    Parameters:
    - content (str): The sentence to count POS tags from.

    Returns:
    - dict: A dictionary with POS tags as keys and their count as values.

    Requirements:
    - nltk
    - collections.Counter

    Example:
    >>> task_func('this is an example content')
    {'DT': 2, 'VBZ': 1, 'NN': 1}
    """

    words = content.split()[:-1]  # Split and remove the last word
    pos_tags = nltk.pos_tag(words)  # Tokenization is built into pos_tag for simple whitespace tokenization
    pos_counts = Counter(tag for _, tag in pos_tags)
    return dict(pos_counts)

class TestTaskFunc(unittest.TestCase):

    def test_basic_sentence(self):
        result = task_func('this is an example content')
        expected = {'DT': 2, 'VBZ': 1, 'NN': 1}
        self.assertEqual(result, expected)

    def test_empty_string(self):
        result = task_func('')
        expected = {}
        self.assertEqual(result, expected)

    def test_single_word(self):
        result = task_func('running')
        expected = {}
        self.assertEqual(result, expected)

    def test_no_last_word_effect(self):
        result = task_func('The quick brown fox jumps')
        expected = {'DT': 1, 'JJ': 2, 'NN': 1, 'VBZ': 1}
        self.assertEqual(result, expected)

    def test_special_characters(self):
        result = task_func('Hello, world! This is a test -.')
        expected = {'NN': 3, 'DT': 1, 'VBZ': 1, 'JJ': 1}
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()