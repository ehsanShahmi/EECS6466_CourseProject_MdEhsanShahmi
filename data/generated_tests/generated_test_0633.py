import re
from nltk.corpus import stopwords
import unittest

def task_func(text: str) -> dict:
    """
    Analyzes a given text string by removing duplicate words and stopwords defined by nltk.corpus ,
    and then returns a frequency distribution of the remaining words.

    Parameters:
    - text (str): The text string to analyze.

    Returns:
    - dict: The frequency distribution of the words in the text after filtering.

    Requirements:
    - re
    - nltk.corpus

    Note:
    - A manually defined set of common English stopwords is used for filtering.

    Examples:
    >>> task_func("The quick brown fox jumps over the lazy dog and the dog was not that quick to respond.")
    {'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'lazy': 1, 'dog': 1, 'respond': 1}

    >>> task_func("hello hello world")
    {'hello': 1, 'world': 1}
    """
    # Remove duplicate words
    stop_words = set(stopwords.words('english'))
    text = ' '.join(sorted(set(text.split()), key=text.index))
    # Tokenize and remove stopwords
    words = [word for word in re.findall(r'\b\w+\b', text.lower()) if word not in stop_words]
    
    # Create frequency distribution
    freq_dist = {}
    for word in words:
        freq_dist[word] = freq_dist.get(word, 0) + 1
    
    return freq_dist

class TestTaskFunc(unittest.TestCase):

    def test_empty_string(self):
        result = task_func("")
        self.assertEqual(result, {})

    def test_no_stopwords(self):
        result = task_func("Python programming language")
        self.assertEqual(result, {'python': 1, 'programming': 1, 'language': 1})

    def test_with_stopwords(self):
        result = task_func("The quick brown fox jumps over the lazy dog")
        self.assertEqual(result, {'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'lazy': 1, 'dog': 1})

    def test_duplicate_words(self):
        result = task_func("hello hello world")
        self.assertEqual(result, {'hello': 1, 'world': 1})

    def test_combined_case_with_varied_capitalization(self):
        result = task_func("The the Quick BROWN brown Fox")
        self.assertEqual(result, {'quick': 1, 'brown': 2, 'fox': 1})

if __name__ == '__main__':
    unittest.main()