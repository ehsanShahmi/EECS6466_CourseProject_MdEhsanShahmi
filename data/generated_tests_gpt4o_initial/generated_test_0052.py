import pandas as pd
import regex as re
import unittest

# Constants
STOPWORDS = ["a", "an", "the", "in", "is", "are"]

# Provided prompt's function
def task_func(text):
    """
    Count the frequency of each word in a text after removing specific stopwords.

    Parameters:
    text (str): The text to analyze.

    Returns:
    Series: A pandas Series with word frequencies excluding the words in STOPWORDS list.
    """
    words = re.findall(r"\b\w+\b", text.lower())
    words = [word for word in words if word not in STOPWORDS]
    word_counts = pd.Series(words).value_counts().rename(None)
    return word_counts

# Test suite
class TestWordFrequency(unittest.TestCase):

    def test_word_frequency_basic(self):
        text = "This is a sample text. This text contains sample words."
        expected_counts = pd.Series({'this': 2, 'sample': 2, 'text': 2, 'contains': 1, 'words': 1})
        result = task_func(text)
        pd.testing.assert_series_equal(result.sort_index(), expected_counts.sort_index())

    def test_word_frequency_with_stopwords(self):
        text = "The quick brown fox jumps over the lazy dog."
        expected_counts = pd.Series({'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1})
        result = task_func(text)
        pd.testing.assert_series_equal(result.sort_index(), expected_counts.sort_index())

    def test_word_frequency_case_insensitivity(self):
        text = "Hello hello HeLLo heLLo"
        expected_counts = pd.Series({'hello': 4})
        result = task_func(text)
        pd.testing.assert_series_equal(result.sort_index(), expected_counts.sort_index())

    def test_word_frequency_empty_string(self):
        text = ""
        expected_counts = pd.Series(dtype='int64')
        result = task_func(text)
        pd.testing.assert_series_equal(result, expected_counts)

    def test_word_frequency_only_stopwords(self):
        text = "a an the in is are"
        expected_counts = pd.Series(dtype='int64')
        result = task_func(text)
        pd.testing.assert_series_equal(result, expected_counts)

if __name__ == '__main__':
    unittest.main()