import re
from collections import Counter
import unittest

# Here is your prompt:
PREDEFINED_STOPWORDS = {
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", 
    "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", 
    "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", 
    "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", 
    "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", 
    "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", 
    "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", 
    "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", 
    "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "more"
}

def task_func(text):
    """
    Count the stopwords found in the text after you have removed URLs.

    Parameters:
    text (str): The text to summarize.

    Returns:
    list: A list of tuples where each tuple contains a word and its frequency.
    """
    # Remove URLs
    text = re.sub('http[s]?://\S+', '', text)
    # Tokenize the text using regex (improved tokenization)
    words = re.findall(r'\b\w+\b', text)
    # Count the frequency of each word
    word_freq = Counter(words)
    result = Counter(words)
    for i in word_freq:
        if i not in PREDEFINED_STOPWORDS:
            del result[i]
    return list(result.items())

class TestTaskFunc(unittest.TestCase):
    
    def test_with_single_stopword(self):
        text = 'Visit https://www.python.org for more info. Python is great.'
        expected_result = [('for', 1), ('more', 1)]
        self.assertEqual(task_func(text), expected_result)

    def test_with_multiple_stopwords(self):
        text = 'Visit https://www.python.org for more info. Python is great, we love Python, and we also love Rust.'
        expected_result = [('for', 1), ('more', 1), ('and', 1)]
        self.assertEqual(task_func(text), expected_result)

    def test_with_no_stopwords(self):
        text = 'This sentence does not contain any stopwords.'
        expected_result = []
        self.assertEqual(task_func(text), expected_result)

    def test_with_only_stopwords(self):
        text = 'I am he and she.'
        expected_result = []
        self.assertEqual(task_func(text), expected_result)

    def test_with_various_capitalizations(self):
        text = 'Visit https://www.example.com. an And and do it now.'
        expected_result = [('do', 1), ('now', 1)]
        self.assertEqual(task_func(text), expected_result)

# This part is necessary to run the tests when this script is executed directly.
if __name__ == '__main__':
    unittest.main()