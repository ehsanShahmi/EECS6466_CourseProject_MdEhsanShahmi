import re
import string
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import unittest

nltk.download('vader_lexicon')

# Constants
ALPHANUMERIC = re.compile('[\W_]+')
PUNCTUATIONS = string.punctuation

def task_func(text: str, sia: SentimentIntensityAnalyzer) -> dict:
    """Analyze the sentiment of a text using the provided SentimentIntensityAnalyzer.
    The text is first cleaned by:
    - Removing all non-alphanumeric characters except spaces.
    - Converting to lowercase.
    - Removing punctuation.
    
    Parameters:
    text (str): The string to analyze.
    sia (SentimentIntensityAnalyzer): An instance of the SentimentIntensityAnalyzer for sentiment analysis.
    
    Returns:
    dict: A dictionary with sentiment scores. The dictionary contains four scores:
          - 'compound': The overall sentiment score.
          - 'neg': Negative sentiment score.
          - 'neu': Neutral sentiment score.
          - 'pos': Positive sentiment score.
    """
    text = ALPHANUMERIC.sub(' ', text).lower()
    text = text.translate(str.maketrans('', '', PUNCTUATIONS))
    sentiment_scores = sia.polarity_scores(text)
    return sentiment_scores


class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        """Set up the SentimentIntensityAnalyzer before each test."""
        self.sia = SentimentIntensityAnalyzer()
        
    def test_positive_sentiment(self):
        """Test with a clearly positive sentiment text."""
        result = task_func("I love Python!", self.sia)
        self.assertGreater(result['pos'], result['neg'], "Expected a higher positive score than negative.")

    def test_negative_sentiment(self):
        """Test with a clearly negative sentiment text."""
        result = task_func("I hate bugs.", self.sia)
        self.assertGreater(result['neg'], result['pos'], "Expected a higher negative score than positive.")

    def test_neutral_sentiment(self):
        """Test with a neutral statement."""
        result = task_func("This is a book.", self.sia)
        self.assertAlmostEqual(result['pos'], 0.0, delta=0.01, msg="Expected positive score close to 0.")
        self.assertAlmostEqual(result['neg'], 0.0, delta=0.01, msg="Expected negative score close to 0.")

    def test_mixed_sentiment(self):
        """Test with a mixed sentiment text."""
        result = task_func("I love and hate working late.", self.sia)
        self.assertGreater(result['compound'], 0, "Expected a positive compound score for mixed sentiments.")

    def test_text_with_punctuation(self):
        """Test with text that contains punctuation."""
        result = task_func("Wow!!! This is awesome!!!", self.sia)
        self.assertGreater(result['pos'], 0, "Expected a positive score despite punctuation.")

if __name__ == '__main__':
    unittest.main()