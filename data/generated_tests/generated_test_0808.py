import re
import nltk
import unittest
from nltk.corpus import stopwords
from textblob import TextBlob

# Constants
STOPWORDS = set(stopwords.words('english'))

def task_func(text):
    """
    Remove duplicate and stopwords from a string "text."
    Then, analyze the sentiment of the text using TextBlob.

    Parameters:
    - text (str): The text string to analyze.

    Returns:
    - Sentiment: The sentiment of the text.

    Requirements:
    - re
    - nltk.corpus.stopwords
    - textblob.TextBlob

    Example:
    >>> text = "The quick brown fox jumps over the lazy dog and the dog was not that quick to respond."
    >>> sentiment = task_func(text)
    >>> print(sentiment)
    Sentiment(polarity=0.13888888888888887, subjectivity=0.6666666666666666)
    """
    text = re.sub(r'\b(\w+)( \1\b)+', r'\1', text)
    words = [word for word in re.findall(r'\b\w+\b', text.lower()) if word not in STOPWORDS]
    text = ' '.join(words)
    blob = TextBlob(text)
    
    return blob.sentiment

class TestTaskFunc(unittest.TestCase):
    def test_simple_text(self):
        text = "I love programming programming and Python Python is great."
        sentiment = task_func(text)
        self.assertIsNotNone(sentiment)
        self.assertIsInstance(sentiment, type(TextBlob('').sentiment))

    def test_text_with_stopwords(self):
        text = "The quick brown fox jumps over the lazy dog."
        sentiment = task_func(text)
        self.assertIsNotNone(sentiment)
        self.assertGreaterEqual(sentiment.polarity, -1)
        self.assertLessEqual(sentiment.polarity, 1)

    def test_empty_string(self):
        text = ""
        sentiment = task_func(text)
        self.assertIsNotNone(sentiment)
        self.assertEqual(sentiment.polarity, 0)
        self.assertEqual(sentiment.subjectivity, 0)

    def test_duplicate_words(self):
        text = "Wow Wow this is a test test for for duplicates."
        sentiment = task_func(text)
        self.assertIsNotNone(sentiment)
        self.assertIn(sentiment.polarity, [-1.0, 0.0, 1.0])  # Check for valid polarity values

    def test_no_valid_words(self):
        text = "the the the a an and"
        sentiment = task_func(text)
        self.assertIsNotNone(sentiment)
        self.assertEqual(sentiment.polarity, 0)
        self.assertEqual(sentiment.subjectivity, 0)

if __name__ == '__main__':
    unittest.main()