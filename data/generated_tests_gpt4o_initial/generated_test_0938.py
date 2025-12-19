import re
import pandas as pd
import unittest

def task_func(input_df):
    """
    Cleans the text in a pandas DataFrame column named 'text' by removing all special characters, punctuation marks, and spaces, then calculates the length of the cleaned text.

    Requirements:
    - re
    - pandas

    Parameters:
    - input_df (pandas.DataFrame): DataFrame with a column 'text' containing strings with alphanumeric and/or special characters.

    Returns:
    - pandas.DataFrame: A DataFrame with two new columns 'clean_text' and 'text_length', where 'clean_text' is the cleaned text and 'text_length' is its length.

    Examples:
    >>> df = pd.DataFrame({'text': ['Special $#! characters   spaces 888323']})
    >>> print(task_func(df))
                          clean_text  text_length
    0  Specialcharactersspaces888323           29
    >>> df = pd.DataFrame({'text': ['Hello, World!']})
    >>> print(task_func(df))
       clean_text  text_length
    0  HelloWorld           10
    """

    def clean_text_and_calculate_length(row):
        if pd.isnull(row['text']):
            return pd.Series(['', 0], index=['clean_text', 'text_length'])
        cleaned_text = re.sub('[^A-Za-z0-9]+', '', str(row['text']))
        return pd.Series([cleaned_text, len(cleaned_text)], index=['clean_text', 'text_length'])

    return input_df.apply(clean_text_and_calculate_length, axis=1)

class TestTaskFunc(unittest.TestCase):

    def test_single_special_characters(self):
        df = pd.DataFrame({'text': ['Special $#! characters   spaces 888323']})
        result = task_func(df)
        expected_result = pd.DataFrame({'clean_text': ['Specialcharactersspaces888323'], 'text_length': [29]})
        pd.testing.assert_frame_equal(result, expected_result)

    def test_simple_phrase(self):
        df = pd.DataFrame({'text': ['Hello, World!']})
        result = task_func(df)
        expected_result = pd.DataFrame({'clean_text': ['HelloWorld'], 'text_length': [10]})
        pd.testing.assert_frame_equal(result, expected_result)

    def test_empty_string(self):
        df = pd.DataFrame({'text': ['']})
        result = task_func(df)
        expected_result = pd.DataFrame({'clean_text': [''], 'text_length': [0]})
        pd.testing.assert_frame_equal(result, expected_result)

    def test_null_value(self):
        df = pd.DataFrame({'text': [None]})
        result = task_func(df)
        expected_result = pd.DataFrame({'clean_text': [''], 'text_length': [0]})
        pd.testing.assert_frame_equal(result, expected_result)

    def test_numeric_string(self):
        df = pd.DataFrame({'text': ['12345!@#']})
        result = task_func(df)
        expected_result = pd.DataFrame({'clean_text': ['12345'], 'text_length': [5]})
        pd.testing.assert_frame_equal(result, expected_result)

if __name__ == '__main__':
    unittest.main()