import re
import nltk
import unittest
from nltk.corpus import stopwords
from collections import Counter

# Constants
STOPWORDS = set(stopwords.words('english'))

# The provided prompt
def task_func(text, n=2):
    """
    Remove duplicate and stopwords from a string "text."
    Then, generate a count of n-grams (default is bigrams) in the text.

    Parameters:
    - text (str): The text string to analyze.
    - n (int): The size of the n-grams.

    Returns:
    - dict: The count of the n-grams in the text.

    Requirements:
    - re
    - nltk.corpus.stopwords
    - collections.Counter

    Example:
    >>> text = "The quick brown fox jumps over the lazy dog and the dog was not that quick to respond."
    >>> ngrams = task_func(text)
    >>> print(ngrams)
    Counter({('quick', 'brown'): 1, ('brown', 'fox'): 1, ('fox', 'jumps'): 1, ('jumps', 'lazy'): 1, ('lazy', 'dog'): 1, ('dog', 'dog'): 1, ('dog', 'quick'): 1, ('quick', 'respond'): 1})
    """

    # Normalize spaces and remove punctuation
    text = re.sub(r'[^\w\s]', '', text)  # Remove all punctuation
    text = re.sub(r'\s+', ' ', text)  # Normalize whitespace

    # Filter out stopwords and split into words
    words = [word.lower() for word in text.split() if word.lower() not in STOPWORDS]

    # Generate n-grams
    ngrams = zip(*[words[i:] for i in range(n)])

    return Counter(ngrams)

class TestTaskFunc(unittest.TestCase):
    
    def test_basic_bigrams(self):
        text = "The quick brown fox jumps"
        expected_output = Counter({('quick', 'brown'): 1, ('brown', 'fox'): 1, ('fox', 'jumps'): 1})
        self.assertEqual(task_func(text, 2), expected_output)
    
    def test_with_stopwords(self):
        text = "The quick brown fox jumps over the lazy dog"
        expected_output = Counter({('quick', 'brown'): 1, ('brown', 'fox'): 1, ('fox', 'jumps'): 1, ('jumps', 'lazy'): 1, ('lazy', 'dog'): 1})
        self.assertEqual(task_func(text), expected_output)
    
    def test_trigrams(self):
        text = "The quick brown fox jumps"
        expected_output = Counter({('quick', 'brown', 'fox'): 1, ('brown', 'fox', 'jumps'): 1})
        self.assertEqual(task_func(text, 3), expected_output)

    def test_empty_string(self):
        text = ""
        expected_output = Counter()
        self.assertEqual(task_func(text), expected_output)

    def test_text_with_only_stopwords(self):
        text = "the and is of that"
        expected_output = Counter()
        self.assertEqual(task_func(text), expected_output)

if __name__ == '__main__':
    unittest.main()