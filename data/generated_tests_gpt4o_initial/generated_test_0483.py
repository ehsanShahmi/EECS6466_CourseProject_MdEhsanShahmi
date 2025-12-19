import re
import pandas as pd
import unittest

def task_func(df: pd.DataFrame, column_name: str, pattern: str) -> pd.DataFrame:
    """
    Reverse the order of words in a specific column of a pandas DataFrame where the words
    match a user-specified regular expression pattern, using a nested helper function.
    Words are considered to be whitespace-separated strings. This function maintains the
    original order of non-matching words.

    Parameters:
    - df (pd.DataFrame): The pandas DataFrame.
    - column_name (str): The name of the column to be modified.
    - pattern (str), the regular expression pattern to match words against.

    Returns:
    - pd.DataFrame: A new pandas DataFrame with the specified column's words reordered
    if they match the pattern, maintaining the original order of words that do not match,
    and returning a copy of the unaltered DataFrame if the pattern is empty.

    Requirements:
    - pandas
    - re

    Example:
    >>> df = pd.DataFrame({'A': ['apple orange', 'red yellow green'], 'B': [1, 2]})
    >>> pattern = r'\b(?:apple|yellow)\b'
    >>> reversed_df = task_func(df, 'A', pattern)
    >>> reversed_df
                      A  B
    0      apple orange  1
    1  red yellow green  2
    >>> df = pd.DataFrame({'A': ['yellow car red', 'green apple yellow'], 'B': [3, 4]})
    >>> pattern = r'\b(?:car|apple|yellow)\b'
    >>> reversed_df = task_func(df, 'A', pattern)
    >>> reversed_df
                        A  B
    0      yellow car red  3
    1  green apple yellow  4
    """

    def reverse_matched_words(text):
        words = text.split()
        matched_words = [word for word in words if re.search(pattern, word)][::-1]
        new_words = [
            matched_words.pop(0) if re.search(pattern, word) else word for word in words
        ]
        return " ".join(new_words)

    new_df = df.copy()
    if not pattern:
        return new_df
    new_df[column_name] = new_df[column_name].apply(reverse_matched_words)
    return new_df

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.df1 = pd.DataFrame({
            'A': ['apple orange', 'red yellow green'],
            'B': [1, 2]
        })

        self.df2 = pd.DataFrame({
            'A': ['yellow car red', 'green apple yellow'],
            'B': [3, 4]
        })

        self.df3 = pd.DataFrame({
            'A': ['hello world', 'foo bar baz'],
            'B': [5, 6]
        })

        self.df4 = pd.DataFrame({
            'A': ['only nonmatching words', 'another sentence'],
            'B': [7, 8]
        })

        self.df5 = pd.DataFrame({
            'A': ['singleword', 'multiple words here', 'testing'],
            'B': [9, 10, 11]
        })

    def test_reverse_matching_words(self):
        pattern = r'\b(?:apple|yellow)\b'
        result = task_func(self.df1, 'A', pattern)
        expected = pd.DataFrame({
            'A': ['apple orange', 'red green yellow'],
            'B': [1, 2]
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_reverse_multiple_matches(self):
        pattern = r'\b(?:car|apple|yellow)\b'
        result = task_func(self.df2, 'A', pattern)
        expected = pd.DataFrame({
            'A': ['yellow car red', 'green yellow apple'],
            'B': [3, 4]
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_no_matches(self):
        pattern = r'\b(?:xyz|abc)\b'
        result = task_func(self.df3, 'A', pattern)
        expected = self.df3.copy()
        pd.testing.assert_frame_equal(result, expected)

    def test_empty_pattern(self):
        pattern = ''
        result = task_func(self.df4, 'A', pattern)
        expected = self.df4.copy()
        pd.testing.assert_frame_equal(result, expected)

    def test_single_word_and_multiple_words(self):
        pattern = r'\b(?:singleword|multiple)\b'
        result = task_func(self.df5, 'A', pattern)
        expected = pd.DataFrame({
            'A': ['singleword', 'here multiple words', 'testing'],
            'B': [9, 10, 11]
        })
        pd.testing.assert_frame_equal(result, expected)

if __name__ == '__main__':
    unittest.main()