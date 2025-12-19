import collections
import matplotlib.pyplot as plt
import pandas as pd
import unittest

# Constants
WORDS = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I']

def task_func(sentences_dict, word_keys):
    """
    Calculate the occurrence of certain words in a collection of sentences and return a bar chart.

    Parameters:
    sentences_dict (dict): The dictionary containing sentences.
    word_keys (list): The list of words.

    Returns:
    - matplotlib.axes._axes.Axes: Axes object of the bar chart displaying the frequencies.

    Requirements:
    - collections
    - matplotlib.pyplot
    - pandas

    Example:
    >>> sentences_dict = {'Sentence1': 'the quick brown fox', 'Sentence2': 'jumps over the lazy dog', 'Sentence3': 'the dog is brown'}
    >>> word_keys = ['the', 'dog']
    >>> type(task_func(sentences_dict, word_keys))
    <class 'matplotlib.axes._axes.Axes'>
    """

               word_counts = collections.Counter(' '.join(sentences_dict.values()).split())
    frequencies = [word_counts[word] for word in word_keys]
    word_series = pd.Series(frequencies, index=word_keys)
    plt.figure()
    word_series.plot(kind='bar')
    return word_series.plot(kind='bar')


class TestTaskFunc(unittest.TestCase):

    def test_empty_sentences_dict(self):
        """Test with an empty sentences_dict"""
        sentences_dict = {}
        word_keys = ['the', 'dog']
        result = task_func(sentences_dict, word_keys)
        self.assertIsInstance(result, plt.Axes)
        self.assertTrue(result.patches)  # Should still create a plot

    def test_no_matching_words(self):
        """Test with no matching words in the sentences"""
        sentences_dict = {'Sentence1': 'quick brown fox', 'Sentence2': 'jumps over lazy dog'}
        word_keys = ['the', 'cat']
        result = task_func(sentences_dict, word_keys)
        self.assertIsInstance(result, plt.Axes)
        # Check if the bars are empty
        for rect in result.patches:
            self.assertEqual(rect.get_height(), 0)

    def test_multiple_sentences_with_some_matching_words(self):
        """Test with multiple sentences having some matching words"""
        sentences_dict = {'Sentence1': 'the quick brown fox', 'Sentence2': 'the lazy dog and the cat'}
        word_keys = ['the', 'dog', 'cat']
        result = task_func(sentences_dict, word_keys)
        self.assertIsInstance(result, plt.Axes)
        self.assertEqual(len(result.patches), len(word_keys))  # Correct number of bars

    def test_case_insensitivity(self):
        """Test to ensure that function is case insensitive"""
        sentences_dict = {'Sentence1': 'The quick brown fox', 'Sentence2': 'jumps over the lazy Dog'}
        word_keys = ['the', 'dog']
        result = task_func(sentences_dict, word_keys)
        self.assertIsInstance(result, plt.Axes)
        # Check if the height of 'the' bar is greater than 0 and 'dog' as well
        self.assertGreater(result.patches[0].get_height(), 0)  # for 'the'
        self.assertGreater(result.patches[1].get_height(), 0)  # for 'dog'

    def test_special_characters(self):
        """Test to ensure the function handles special characters correctly"""
        sentences_dict = {'Sentence1': 'the quick brown fox!', 'Sentence2': 'the lazy dog; and the cat?'}
        word_keys = ['the', 'dog']
        result = task_func(sentences_dict, word_keys)
        self.assertIsInstance(result, plt.Axes)
        self.assertEqual(result.patches[0].get_height(), 3)  # 'the' appears 3 times
        self.assertEqual(result.patches[1].get_height(), 1)  # 'dog' appears 1 time

if __name__ == '__main__':
    unittest.main()