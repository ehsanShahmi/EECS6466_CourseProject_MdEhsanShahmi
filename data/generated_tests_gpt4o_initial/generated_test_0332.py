import unittest
from collections import Counter
import re
from nltk.corpus import stopwords

# Here is your prompt:
def task_func(text: str) -> dict:
    """
    Count the number of non-stop words in a given text.
    
    Parameters:
    - text (str): The input text for word counting.
    
    Returns:
    dict: A dictionary with the words (as keys) and their counts (as values).
    
    Requirements:
    - re
    - collections.Counter
    
    Example:
    >>> count = task_func("This is a sample text. Some words are repeated.")
    >>> print(count)
    {'sample': 1, 'text': 1, 'words': 1, 'repeated': 1}
    """

    words = re.findall(r'\b\w+\b', text)
    non_stopwords = [word for word in words if word.lower() not in set(stopwords.words('english'))]
    count = dict(Counter(non_stopwords))

    return count

class TestTaskFunc(unittest.TestCase):

    def test_empty_string(self):
        result = task_func("")
        self.assertEqual(result, {})

    def test_no_non_stopwords(self):
        result = task_func("a an the and")
        self.assertEqual(result, {})

    def test_single_non_stopword(self):
        result = task_func("Hello")
        self.assertEqual(result, {'Hello': 1})

    def test_multiple_non_stopwords(self):
        result = task_func("This is a test of the function.")
        self.assertEqual(result, {'test': 1, 'function': 1})

    def test_special_characters(self):
        result = task_func("Good morning! How's everything?")
        self.assertEqual(result, {'Good': 1, 'morning': 1, 'How': 1, 'everything': 1})

if __name__ == '__main__':
    unittest.main()