import pandas as pd
import unittest
import string

def task_func(word):
    """
    Creates a Pandas DataFrame from a single word, where each row contains a letter from the word 
    and its 1-based position in the alphabet.

    Requirements:
    - pandas
    - string
    
    Parameters:
    - word (str): The word to create the DataFrame from. The word should be in lowercase and consist of alphabetic characters only.
    
    Returns:
    - pandas.DataFrame: A DataFrame with two columns: 'Letter' and 'Position', 
      where 'Position' is the letter's position in the English alphabet.
    
    Examples:
    >>> task_func('abc')
      Letter  Position
    0      a         1
    1      b         2
    2      c         3

    >>> task_func('zoo')
      Letter  Position
    0      z        26
    1      o        15
    2      o        15
    
    Raises:
    - ValueError: If the input word is not in lowercase or contains non-alphabetic characters.
    """
    if not word:  # Check if the input word is empty and return an empty DataFrame
        return pd.DataFrame({'Letter': [], 'Position': []})
    elif not word.isalpha() or not word.islower():
        raise ValueError("Input word must be in lowercase alphabetic characters only.")

    alphabet = string.ascii_lowercase
    positions = [alphabet.index(char) + 1 for char in word]
    df = pd.DataFrame({'Letter': list(word), 'Position': positions})

    return df


class TestTaskFunc(unittest.TestCase):
    
    def test_valid_input_abc(self):
        result = task_func('abc')
        expected_df = pd.DataFrame({'Letter': ['a', 'b', 'c'], 'Position': [1, 2, 3]})
        pd.testing.assert_frame_equal(result, expected_df)
    
    def test_valid_input_zoo(self):
        result = task_func('zoo')
        expected_df = pd.DataFrame({'Letter': ['z', 'o', 'o'], 'Position': [26, 15, 15]})
        pd.testing.assert_frame_equal(result, expected_df)
    
    def test_empty_input(self):
        result = task_func('')
        expected_df = pd.DataFrame({'Letter': [], 'Position': []})
        pd.testing.assert_frame_equal(result, expected_df)

    def test_invalid_input_uppercase(self):
        with self.assertRaises(ValueError):
            task_func('ABC')

    def test_invalid_input_numeric(self):
        with self.assertRaises(ValueError):
            task_func('abc1')


if __name__ == '__main__':
    unittest.main()