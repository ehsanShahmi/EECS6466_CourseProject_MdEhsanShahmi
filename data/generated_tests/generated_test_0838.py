import re
import pandas as pd
from nltk.stem import PorterStemmer
import unittest

def task_func(text_series):
    """
    Process a pandas Series of text data by lowercasing all letters, removing non-alphanumeric 
    characters (except spaces), removing punctuation, and stemming each word to its root form.
    
    Stemming is done using the NLTK's PorterStemmer, which applies a series of rules to find the stem of each word.
    
    Parameters:
    - text_series (pandas.Series): A Series object containing string entries representing text data.

    Requirements:
    - re
    - nltk

    Returns:
    - pandas.Series: A Series where each string has been processed to remove non-alphanumeric characters,
      punctuation, converted to lowercase, and where each word has been stemmed.
    
    Examples:
    >>> input_series = pd.Series(["This is a sample text.", "Another example!"])
    >>> output_series = task_func(input_series)
    >>> print(output_series.iloc[0])
    thi is a sampl text
    >>> print(output_series.iloc[1])
    anoth exampl

    """

    stemmer = PorterStemmer()

    def process_text(text):
        # Remove non-alphanumeric characters (except spaces)
        text = re.sub('[^\sa-zA-Z0-9]', '', text).lower().strip()
        # Stem each word in the text
        text = " ".join([stemmer.stem(word) for word in text.split()])

        return text

    # Apply the processing to each entry in the Series
    return text_series.apply(process_text)


class TestTaskFunc(unittest.TestCase):

    def test_basic_processing(self):
        input_series = pd.Series(["This is a sample text.", "Another example!"])
        expected_output = pd.Series(["thi is a sampl text", "anoth exampl"])
        result = task_func(input_series)
        pd.testing.assert_series_equal(result, expected_output)

    def test_numerical_text(self):
        input_series = pd.Series(["Text with numbers 123 and punctuation!!!"])
        expected_output = pd.Series(["text with number 123 and punctuat"])
        result = task_func(input_series)
        pd.testing.assert_series_equal(result, expected_output)

    def test_empty_string(self):
        input_series = pd.Series(["", "   "])
        expected_output = pd.Series(["", ""])
        result = task_func(input_series)
        pd.testing.assert_series_equal(result, expected_output)

    def test_single_word(self):
        input_series = pd.Series(["running!", "Jumped"])
        expected_output = pd.Series(["run", "jump"])
        result = task_func(input_series)
        pd.testing.assert_series_equal(result, expected_output)

    def test_special_characters(self):
        input_series = pd.Series(["@Special #Characters &test!"])
        expected_output = pd.Series(["special character test"])
        result = task_func(input_series)
        pd.testing.assert_series_equal(result, expected_output)


if __name__ == '__main__':
    unittest.main()