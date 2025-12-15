import unittest
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

# Here is your prompt:
def task_func(text_dict, word_keys, top_k=2):
    """
    Calculate the frequency of certain words in a text dictionary and return a bar chart's Axes object and a dictionary
    containing the frequencies of the top_k most common words in text_dict. 
    
    The function takes a dictionary containing word frequencies and a list of words. It calculates the frequency 
    of the provided words in the dictionary and returns the Axes object of the bar chart displaying the frequencies
    along with the top_k most common words and their frequencies as a dictionary. If a word in word_keys is not present 
    in text_dict, its frequency is considered to be 0.
    
    Parameters:
    - text_dict (dict): The dictionary containing word frequencies. Key is the word and value is its frequency.
    - word_keys (list of str): The list of words to consider.
    - top_k (int, Optional): A positive integer denoting the number of most common words to return. Default is 2.
    
    Returns:
    - matplotlib.axes._axes.Axes: Axes object of the bar chart displaying the frequencies.
    - dict: Dictionary containing the frequencies of the top_k most common words. Key is the word and value is 
    its frequency.
    
    Requirements:
    - pandas
    - collections.Counter

    Raises:
    - ValueError: If top_k is a negative integer.
    
    Example:
    >>> import collections
    >>> text_dict = collections.Counter(['the', 'be', 'to', 'the', 'that', 'and', 'a', 'in', 'the', 'that', 'have', 'I'])
    >>> word_keys = ['the', 'and', 'I']
    >>> ax, frequencies = task_func(text_dict, word_keys, 3)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    >>> frequencies
    {'the': 3, 'that': 2, 'be': 1}
    """

               if top_k < 0:
        raise ValueError('top_k must be a positive integer.')
    elif top_k >= len(text_dict):
        top_k = len(text_dict)

    frequencies = [text_dict.get(word, 0) for word in word_keys]
    freq_dict = Counter(text_dict)
    top_k_words = freq_dict.most_common(top_k)
    word_series = pd.Series(frequencies, index=word_keys)
    ax = word_series.plot(kind='bar')
    return ax, dict(top_k_words)

class TestTaskFunc(unittest.TestCase):

    def test_basic_functionality(self):
        text_dict = Counter(['the', 'be', 'to', 'the', 'that', 'and', 'a', 'in', 'the', 'that', 'have', 'I'])
        word_keys = ['the', 'and', 'I']
        ax, frequencies = task_func(text_dict, word_keys, 3)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(frequencies, {'the': 3, 'that': 2, 'be': 1})

    def test_zero_frequency_word(self):
        text_dict = Counter(['the', 'be', 'to', 'the', 'that'])
        word_keys = ['and', 'that', 'the']
        ax, frequencies = task_func(text_dict, word_keys, 2)
        self.assertEqual(frequencies['and'], 0)

    def test_negative_top_k(self):
        text_dict = Counter(['the', 'be', 'to', 'the', 'that'])
        word_keys = ['the', 'be']
        with self.assertRaises(ValueError):
            task_func(text_dict, word_keys, -1)

    def test_top_k_greater_than_dict_size(self):
        text_dict = Counter(['the', 'be', 'to'])
        word_keys = ['the', 'be']
        ax, frequencies = task_func(text_dict, word_keys, 5)  # top_k exceeds the number of unique words
        self.assertEqual(len(frequencies), 2)  # should only return existing words

    def test_empty_text_dict(self):
        text_dict = Counter()
        word_keys = ['the', 'be']
        ax, frequencies = task_func(text_dict, word_keys, 2)
        self.assertEqual(frequencies['the'], 0)
        self.assertEqual(frequencies['be'], 0)

if __name__ == '__main__':
    unittest.main()