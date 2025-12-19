import pandas as pd
import unittest
import regex as re
from sklearn.feature_extraction.text import CountVectorizer

# Test suite for the provided prompt
class TestTaskFunc(unittest.TestCase):

    def test_single_sentence(self):
        text = "This is a test."
        expected_columns = ["is", "test", "this"]
        dtm = task_func(text)
        self.assertEqual(list(dtm.columns), expected_columns)
        self.assertEqual(dtm.shape[0], 1)  # should have 1 row

    def test_multiple_sentences(self):
        text = "This is a test. This is only a test."
        expected_columns = ["is", "only", "test", "this"]
        dtm = task_func(text)
        self.assertEqual(list(dtm.columns), expected_columns)
        self.assertEqual(dtm.shape[0], 2)  # should have 2 rows

    def test_empty_sentences(self):
        text = "This is a test.  . Another sentence."
        expected_columns = ["another", "is", "sentence", "test", "this"]
        dtm = task_func(text)
        self.assertEqual(list(dtm.columns), expected_columns)
        self.assertEqual(dtm.shape[0], 2)  # should have 2 rows

    def test_no_sentences(self):
        text = "     "  # Only whitespace
        dtm = task_func(text)
        self.assertTrue(dtm.empty)  # DataFrame should be empty
    
    def test_special_characters(self):
        text = "Hello there! How's it going? This is great."
        expected_columns = ["going", "great", "hello", "how", "is", "it", "there", "this"]
        dtm = task_func(text)
        self.assertEqual(list(dtm.columns), expected_columns)
        self.assertEqual(dtm.shape[0], 3)  # should have 3 rows

if __name__ == '__main__':
    unittest.main()