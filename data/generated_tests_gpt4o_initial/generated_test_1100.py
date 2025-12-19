import re
from sklearn.feature_extraction.text import TfidfVectorizer
import unittest

def task_func(texts):
    """
    Processes a collection of text documents to compute the TF-IDF (Term Frequency-Inverse Document Frequency) scores
    for each word, excluding any URLs present in the texts. The TF-IDF scores help to identify the importance of a word
    within a document relative to a collection of documents.

    Parameters:
    texts (list of str): A list containing the text documents to be analyzed.

    Returns:
    tuple of (list of tuples, list of str):
        - The first element is a list of tuples, each tuple representing a document with its words' TF-IDF scores in a
          dense matrix format. Each score in the tuple corresponds to a word's TF-IDF score in the document.
        - The second element is a list of strings, representing the unique words (features) across all documents for
          which TF-IDF scores have been calculated. The order of words in this list matches the order of scores in the
          tuples of the first element.

    Requirements:
    - re
    - sklearn.feature_extraction.text.TfidfVectorizer

    Example:
    >>> task_func(['Visit https://www.python.org for more info.', 'Python is great.', 'I love Python.'])
    ([(0.5, 0.0, 0.5, 0.0, 0.0, 0.5, 0.0, 0.5), (0.0, 0.62276601, 0.0, 0.62276601, 0.0, 0.0, 0.4736296, 0.0), (0.0, 0.0, 0.0, 0.0, 0.79596054, 0.0, 0.60534851, 0.0)], ['for', 'great', 'info', 'is', 'love', 'more', 'python', 'visit'])

    Notes:
    - URLs in the text documents are removed before calculating TF-IDF scores to ensure they do not affect the analysis.
    - The TF-IDF scores are rounded to 8 decimal places for precision.
    """

class TestTaskFunc(unittest.TestCase):
    
    def test_multiple_documents(self):
        result = task_func(['Visit https://www.python.org for more info.', 'Python is great.', 'I love Python.'])
        expected_matrix = [
            (0.5, 0.0, 0.5, 0.0, 0.0, 0.5, 0.0, 0.5),
            (0.0, 0.62276601, 0.0, 0.62276601, 0.0, 0.0, 0.4736296, 0.0),
            (0.0, 0.0, 0.0, 0.0, 0.79596054, 0.0, 0.60534851, 0.0)
        ]
        expected_features = ['for', 'great', 'info', 'is', 'love', 'more', 'python', 'visit']
        self.assertEqual(result[0], expected_matrix)
        self.assertEqual(result[1], expected_features)
    
    def test_single_document(self):
        result = task_func(['Hello world!'])
        expected_matrix = [(1.0)]
        expected_features = ['hello', 'world']
        self.assertEqual(result[0], expected_matrix)
        self.assertEqual(result[1], expected_features)

    def test_empty_document_list(self):
        result = task_func([])
        self.assertEqual(result, ([], []))

    def test_documents_with_only_urls(self):
        result = task_func(['https://example.com', 'http://anotherexample.com'])
        self.assertEqual(result, ([], []))

    def test_mixed_content(self):
        result = task_func(['Check this link: https://domain.com', 'Check out Python and Java!', 'Python is amazing.'])
        expected_matrix = [
            (0.5, 0.5, 0.0, 0.0, 0.5, 0.0),
            (0.0, 0.0, 0.70710678, 0.70710678, 0.0, 0.0),
            (0.0, 0.0, 0.0, 0.0, 0.70710678, 0.70710678)
        ]
        expected_features = ['and', 'check', 'java', 'out', 'python', 'this']
        self.assertEqual(result[0], expected_matrix)
        self.assertEqual(result[1], expected_features)

if __name__ == '__main__':
    unittest.main()