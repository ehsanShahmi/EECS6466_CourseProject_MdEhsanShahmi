import re
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
import unittest

def task_func(example_str, top_n=30):
    """
    Extract all texts that are not enclosed in square brackets from the given string and plot 
    a frequency distribution of the words. Also return the top_n most common words in the frequency distribution
    as a dictionary.

    Parameters:
    - example_str (str): The input string.
    - top_n (int, Optional): The number of most common words to display in the frequency distribution plot. Default is 30.

    Returns:
    - Axes: A matplotlib Axes object representing the frequency distribution plot.
    - dict: A dictionary containing the top_n most common words and their frequencies.

    Requirements:
    - re
    - nltk.probability.FreqDist
    - matplotlib.pyplot

    Example:
    >>> ax, top_n_words = task_func("Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003] Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]")
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """

    text = ' '.join(re.findall('(.*?)\\[.*?\\]', example_str))
    words = text.split()
    fdist = FreqDist(words)

    if top_n > len(fdist):
        top_n = len(fdist)
    # Initialize a fresh plot for the frequency distribution but do not show it
    plt.figure()
    ax = fdist.plot(top_n, cumulative=False, show=False)
    plt.close()

    top_n_words = dict(fdist.most_common(top_n))
    return ax, top_n_words

class TestTaskFunc(unittest.TestCase):

    def test_basic_functionality(self):
        ax, top_n_words = task_func("Hello world Hello [Ignored text]")
        self.assertIsNotNone(ax)
        self.assertEqual(top_n_words, {'Hello': 2, 'world': 1})

    def test_no_words_outside_brackets(self):
        ax, top_n_words = task_func("[Everything inside brackets]")
        self.assertIsNotNone(ax)
        self.assertEqual(top_n_words, {})

    def test_multiple_brackets(self):
        ax, top_n_words = task_func("Text [ignored] more text [ignored too]")
        self.assertIsNotNone(ax)
        self.assertEqual(top_n_words, {'Text': 1, 'more': 1, 'text': 1})

    def test_empty_string(self):
        ax, top_n_words = task_func("")
        self.assertIsNotNone(ax)
        self.assertEqual(top_n_words, {})

    def test_top_n_limit(self):
        ax, top_n_words = task_func("one two three one two three one two three", top_n=2)
        self.assertIsNotNone(ax)
        self.assertEqual(top_n_words, {'one': 3, 'two': 3})

if __name__ == '__main__':
    unittest.main()