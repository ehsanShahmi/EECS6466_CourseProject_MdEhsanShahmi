import unittest
import pandas as pd
from collections import Counter
from textblob import TextBlob
from matplotlib import pyplot as plt
import seaborn as sns

# Here is your prompt:
def task_func(text, n, top_k):
    """
    Visualize the uppermost K n-grams in a given text string.

    Parameters:
    text (str): The text string.
    n (int): The value of n for the n-grams.
    top_k (int): The number of top n-grams to visualize.

    Returns:
    None

    Requirements:
    - re
    - pandas
    - seaborn
    - textblob
    - matplotlib

    Example:
    >>> type(task_func('This is a sample text for testing.', 2, 5))
    <class 'matplotlib.axes._axes.Axes'>
    """

    blob = TextBlob(text.lower())
    words_freq = Counter([' '.join(list(span)) for span in blob.ngrams(n=n)])  # Get n-grams and count frequency
    words_freq_filtered = words_freq.most_common(top_k)  # Get top k n-grams
    top_df = pd.DataFrame(words_freq_filtered, columns=['n-gram', 'Frequency'])
    plt.figure()

    return sns.barplot(x='n-gram', y='Frequency', data=top_df)

class TestTaskFunc(unittest.TestCase):

    def test_return_type(self):
        """Test if the task_func returns a matplotlib Axes object."""
        result = task_func('This is a sample text for testing.', 2, 5)
        self.assertIsInstance(result, plt.Axes)
        
    def test_n_grams_capture(self):
        """Test if the function correctly captures n-grams."""
        text = 'test test example example test example'
        n = 2
        expected_ngrams = {'test example': 3, 'example test': 2}
        blob = TextBlob(text.lower())
        words_freq = Counter([' '.join(list(span)) for span in blob.ngrams(n=n)])
        filtered = words_freq.most_common(2)
        result = dict(filtered)
        self.assertEqual(result, expected_ngrams)
        
    def test_top_k_output(self):
        """Test if the top_k parameter correctly limits the output."""
        text = 'one two two three three three four four four four'
        n = 1
        expected_keys = {'three', 'four'}
        result = task_func(text, n, 2)
        
        blob = TextBlob(text.lower())
        words_freq = Counter([' '.join(list(span)) for span in blob.ngrams(n=n)])
        filtered = words_freq.most_common(2)
        output_keys = set([k for k, v in filtered])
        
        self.assertEqual(output_keys, expected_keys)

    def test_empty_text(self):
        """Test the response of the function with an empty string."""
        result = task_func('', 1, 5)
        self.assertIsInstance(result, plt.Axes)  # Should still return an Axes object

    def test_invalid_n_grams(self):
        """Test how the function handles invalid n values."""
        with self.assertRaises(ValueError):
            task_func('Some example text.', 0, 5)  # n cannot be less than 1

if __name__ == '__main__':
    unittest.main()