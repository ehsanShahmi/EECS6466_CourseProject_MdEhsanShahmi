import pandas as pd
import re
import numpy as np
import unittest

# Constants
PATTERN = r"([a-fA-F\d]{32})"

def task_func(df, column):
    """
    Find all matches of the regex pattern '([a-fA-F\ d] {32})' in a Pandas DataFrame column and count the occurrence of any unique match in the data.

    Parameters:
    df (DataFrame): The pandas DataFrame.
    column (str): The column in which to find the pattern.

    Returns:
    Series: A pandas Series with counts of each unique match.

    Requirements:
    - pandas
    - re
    - numpy

    Raises:
    - The function will raise KeyError if the "column" does not exist in input "df"

    Example:
    >>> data = pd.DataFrame({"text": ["6f96cfdfe5ccc627cadf24b41725caa4 gorilla", "6f96cfdfe5ccc627cadf24b41725caa4 banana", "1234567890abcdef1234567890abcdef apple"]})
    >>> counts = task_func(data, "text")
    >>> print(counts.index[0])
    6f96cfdfe5ccc627cadf24b41725caa4
    """

    matches = df[column].apply(lambda x: re.findall(PATTERN, x))
    flattened_matches = np.concatenate(matches.values)
    counts = pd.Series(flattened_matches).value_counts()
    
    return counts

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.df_valid = pd.DataFrame({
            "text": [
                "6f96cfdfe5ccc627cadf24b41725caa4 gorilla", 
                "6f96cfdfe5ccc627cadf24b41725caa4 banana", 
                "1234567890abcdef1234567890abcdef apple"
            ]
        })
        
        self.df_invalid_column = pd.DataFrame({
            "other": ["6f96cfdfe5ccc627cadf24b41725caa4 gorilla"]
        })

    def test_valid_counts(self):
        counts = task_func(self.df_valid, "text")
        expected_counts = pd.Series({
            "6f96cfdfe5ccc627cadf24b41725caa4": 2, 
            "1234567890abcdef1234567890abcdef": 1
        })
        pd.testing.assert_series_equal(counts, expected_counts)

    def test_empty_dataframe(self):
        df_empty = pd.DataFrame({"text": []})
        counts = task_func(df_empty, "text")
        expected_counts = pd.Series(dtype='int')
        pd.testing.assert_series_equal(counts, expected_counts)

    def test_no_matches(self):
        df_no_matches = pd.DataFrame({"text": ["no_matches_here", "another_line"]})
        counts = task_func(df_no_matches, "text")
        expected_counts = pd.Series(dtype='int')
        pd.testing.assert_series_equal(counts, expected_counts)

    def test_nonexistent_column(self):
        with self.assertRaises(KeyError):
            task_func(self.df_invalid_column, "text")

    def test_mixed_content(self):
        df_mixed = pd.DataFrame({
            "text": [
                "valid: 6f96cfdfe5ccc627cadf24b41725caa4", 
                "invalid: not_a_hash", 
                "another valid: 1234567890abcdef1234567890abcdef"
            ]
        })
        counts = task_func(df_mixed, "text")
        expected_counts = pd.Series({
            "6f96cfdfe5ccc627cadf24b41725caa4": 1, 
            "1234567890abcdef1234567890abcdef": 1
        })
        pd.testing.assert_series_equal(counts, expected_counts)

if __name__ == "__main__":
    unittest.main()