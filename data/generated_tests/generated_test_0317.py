import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import unittest

def task_func(example_str):
    """
    Extract all texts not enclosed in square brackets into a string and calculate the TF-IDF values
    which are returned as a dictionary.

    Parameters:
    example_str (str): The input string.

    Returns:
    dict: A dictionary with words as keys and TF-IDF scores as values.

    Requirements:
    - sklearn.feature_extraction.text.TfidfVectorizer
    - numpy
    - re

    Example:
    >>> tfidf_scores = task_func("Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003] Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]")
    >>> print(tfidf_scores)
    {'dog': 0.3779644730092272, 'josie': 0.3779644730092272, 'mugsy': 0.3779644730092272, 'smith': 0.7559289460184544}
    """

    pattern = r'\[.*?\]'
    text = re.sub(pattern, '', example_str)
    if not text.strip():
        return {}

    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([text])
    feature_names = tfidf_vectorizer.get_feature_names_out()
    tfidf_scores = dict(zip(feature_names, np.squeeze(tfidf_matrix.toarray())))

    return tfidf_scores

class TestTaskFunc(unittest.TestCase):

    def test_basic_case(self):
        result = task_func("Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003] Mugsy Dog")
        expected_keys = {'josie', 'smith', 'mugsy', 'dog'}
        self.assertTrue(expected_keys.issubset(result.keys()))
        self.assertEqual(len(result), len(expected_keys))

    def test_empty_string(self):
        result = task_func("")
        self.assertEqual(result, {})

    def test_no_text_outside_brackets(self):
        result = task_func("[some text inside brackets]")
        self.assertEqual(result, {})

    def test_multiple_spaces(self):
        result = task_func("   Josie   Smith   [address here]  Mugsy")
        expected_keys = {'josie', 'smith', 'mugsy'}
        self.assertTrue(expected_keys.issubset(result.keys()))
        self.assertEqual(len(result), len(expected_keys))

    def test_special_characters(self):
        result = task_func("Hello! This is a test string. [Ignored message] @123 #test")
        expected_keys = {'hello', 'this', 'is', 'a', 'test', 'string'}
        self.assertTrue(expected_keys.issubset(result.keys()))
        self.assertEqual(len(result), len(expected_keys))

if __name__ == '__main__':
    unittest.main()