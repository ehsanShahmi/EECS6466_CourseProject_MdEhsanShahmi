import unittest
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.docs = [
            'This is the first document.',
            'This document is the second document.',
            'And this is the third one.',
            'Is this the first document?'
        ]

    def test_shape_of_output(self):
        """Test that the output shape is correct."""
        tfidf = task_func(self.docs)
        self.assertEqual(tfidf.shape, (4, 11))

    def test_non_empty_dataframe(self):
        """Test that the output DataFrame is non-empty."""
        tfidf = task_func(self.docs)
        self.assertFalse(tfidf.empty)

    def test_column_count(self):
        """Test that the number of columns matches the expected number of unique words."""
        tfidf = task_func(self.docs)
        expected_columns = len(set(' '.join(self.docs).split()))
        self.assertEqual(tfidf.shape[1], expected_columns)

    def test_dataframe_columns(self):
        """Test that the DataFramecolumns contain expected words."""
        tfidf = task_func(self.docs)
        expected_words = {'this', 'is', 'the', 'first', 'document', 'second', 'and', 'third', 'one'}
        actual_words = set(tfidf.columns)
        self.assertTrue(expected_words.issubset(actual_words))

    def test_tfidf_values(self):
        """Test that TF-IDF values are in the expected range."""
        tfidf = task_func(self.docs)
        for col in tfidf.columns:
            for value in tfidf[col]:
                self.assertGreaterEqual(value, 0)
                self.assertLessEqual(value, 1)

if __name__ == '__main__':
    unittest.main()