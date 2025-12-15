import re
import unittest
from string import punctuation

# Predefined list of common stopwords
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
    Clean the specified text by removing URLs, stopwords, and punctuation.

    Parameters:
    text (str): The text to be cleaned.

    Returns:
    str: The cleaned text with URLs, predefined stopwords, and punctuation removed.
    """
    
    # Constants
    PUNCTUATION = set(punctuation)

    # Remove URLs
    text = re.sub('http[s]?://\S+', '', text)

    # Remove punctuation
    text = re.sub('[{}]'.format(re.escape(''.join(PUNCTUATION))), '', text)

    # Tokenize the text
    words = text.split()

    # Remove stopwords
    cleaned_words = [word for word in words if word.lower() not in PREDEFINED_STOPWORDS]

    return ' '.join(cleaned_words)

class TestTaskFunc(unittest.TestCase):

    def test_basic_functionality(self):
        result = task_func('Visit https://www.python.org for more info. I love to eat apples.')
        self.assertEqual(result, 'Visit info love eat apples')

    def test_removal_of_punctuation(self):
        result = task_func('Hello, world! This is a test.')
        self.assertEqual(result, 'Hello world This test')

    def test_removal_of_stopwords(self):
        result = task_func('I am going to the store.')
        self.assertEqual(result, 'going store')

    def test_removal_of_url(self):
        result = task_func('Check out my website at http://example.com.')
        self.assertEqual(result, 'Check out my website at')

    def test_edge_case_empty_string(self):
        result = task_func('')
        self.assertEqual(result, '')

if __name__ == '__main__':
    unittest.main()