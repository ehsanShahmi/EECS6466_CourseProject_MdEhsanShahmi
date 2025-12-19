import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import unittest

# Importing the required libraries (as per prompt)
import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords


def task_func(text, n=2):
    """
    Analyzes a text string, removing duplicate consecutive words and stopwords defined by nltk.corpus,
    generates a square co-occurrence matrix of words, and plots this matrix.

    Parameters:
    - text (str): Input text to be analyzed.
    - n (int, optional): Size of n-grams for the co-occurrence matrix. Defaults to 2.

    Returns:
    - tuple:
        - pd.DataFrame: Square co-occurrence matrix of words.
        - matplotlib.axes.Axes: Plot object of the co-occurrence matrix.

    Requirements:
        - re
        - pandas
        - matplotlib.pyplot
        - numpy
        - sklearn.feature_extraction.text
        - nltk.corpus

    Example:
    >>> import matplotlib
    >>> text = "hello hello world world"
    >>> df, ax = task_func(text, n=2)
    >>> df.columns.tolist()
    ['hello world']
    >>> df.index.tolist()
    ['hello world']
    >>> df.iloc[0, 0]
    0
    >>> isinstance(ax, matplotlib.axes.Axes)
    True
    """

    # Pre-processing the text
    # Remove duplicate consecutive words
    text = re.sub(r'\b(\w+)( \1\b)+', r'\1', text)
    stop_words = set(stopwords.words('english'))
    # Remove stopwords
    words_filtered = ' '.join([word for word in text.lower().split() if word not in stop_words])

    # If words_filtered is empty after removing stopwords, return an empty DataFrame
    if not words_filtered.strip():
        empty_df = pd.DataFrame()
        fig, ax = plt.subplots()
        return empty_df, ax

    # Generating co-occurrence matrix and plotting as before
    vectorizer = CountVectorizer(ngram_range=(n, n))
    X = vectorizer.fit_transform([words_filtered])  # Ensure input is treated as a single document
    matrix = (X.T * X).todense()
    np.fill_diagonal(matrix, 0)
    feature_names = vectorizer.get_feature_names_out() if hasattr(vectorizer,
                                                                  'get_feature_names_out') else vectorizer.get_feature_names()
    matrix_df = pd.DataFrame(matrix, index=feature_names, columns=feature_names)

    fig, ax = plt.subplots()
    cax = ax.matshow(matrix_df, cmap='hot')
    fig.colorbar(cax)
    ax.set_xticks(np.arange(len(matrix_df.columns)))
    ax.set_yticks(np.arange(len(matrix_df.index)))
    ax.set_xticklabels(matrix_df.columns, rotation=90)
    ax.set_yticklabels(matrix_df.index)

    return matrix_df, ax


class TestTaskFunc(unittest.TestCase):
    
    def test_no_words(self):
        text = ""
        df, ax = task_func(text, n=2)
        self.assertTrue(df.empty)
        self.assertIsInstance(ax, plt.Axes)

    def test_single_word(self):
        text = "hello"
        df, ax = task_func(text, n=2)
        self.assertEqual(df.shape, (0, 0))
        self.assertIsInstance(ax, plt.Axes)

    def test_consecutive_duplicates(self):
        text = "hello hello world"
        df, ax = task_func(text, n=2)
        self.assertIn('hello world', df.columns)
        self.assertIn('hello world', df.index)
        self.assertEqual(df.iloc[0, 0], 0)

    def test_with_stopwords(self):
        text = "the cat and the hat"
        df, ax = task_func(text, n=2)
        self.assertEqual(df.shape, (0, 0))
        self.assertIsInstance(ax, plt.Axes)

    def test_ngrams_variation(self):
        text = "the quick brown fox jumps over the lazy dog"
        df, ax = task_func(text, n=2)
        self.assertIn('quick brown', df.columns)
        self.assertIn('quick brown', df.index)
        self.assertIsInstance(ax, plt.Axes)

if __name__ == '__main__':
    unittest.main()