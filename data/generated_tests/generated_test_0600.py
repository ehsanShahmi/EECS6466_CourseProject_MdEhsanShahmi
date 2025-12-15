import numpy as np
import pandas as pd
import unittest

def task_func(df, letter):
    """
    This function converts an input dictionary into a DataFrame, filters rows where 'Word' column values start with a
    specified letter, calculates the lengths of these words, and returns basic statistics (mean, median, mode) of the
    word lengths.

    Parameters:
    df (dict of list): A dictionary where the key 'Word' maps to a list of strings.
    letter (str): The letter to filter the 'Word' column.

    Returns:
    dict: A dictionary of mean, median, and mode of word lengths.
    
    Requirements:
    - pandas
    - numpy
    """
    
    df = pd.DataFrame(df)
    regex = '^' + letter
    filtered_df = df[df['Word'].str.contains(regex, regex=True)]
    word_lengths = filtered_df['Word'].str.len()
    statistics = {'mean': np.mean(word_lengths), 'median': np.median(word_lengths), 'mode': word_lengths.mode().values[0]}
    
    return statistics

class TestTaskFunc(unittest.TestCase):

    def test_empty_dataframe(self):
        df = {'Word': []}
        result = task_func(df, 'a')
        self.assertEqual(result['mean'], 0)
        self.assertEqual(result['median'], 0)
        with self.assertRaises(IndexError):
            _ = result['mode']

    def test_no_matching_words(self):
        df = {'Word': ['banana', 'berry', 'grape']}
        result = task_func(df, 'a')
        self.assertEqual(result['mean'], 0)
        self.assertEqual(result['median'], 0)
        with self.assertRaises(IndexError):
            _ = result['mode']

    def test_single_letter_match(self):
        df = {'Word': ['apple', 'banana', 'avocado']}
        result = task_func(df, 'a')
        self.assertAlmostEqual(result['mean'], 5.0)
        self.assertEqual(result['median'], 5)
        self.assertEqual(result['mode'], 5)

    def test_multiple_matches(self):
        df = {'Word': ['ant', 'apple', 'banana', 'apricot']}
        result = task_func(df, 'a')
        self.assertAlmostEqual(result['mean'], 5.0)
        self.assertEqual(result['median'], 5)
        self.assertEqual(result['mode'], 3)

    def test_case_insensitive_matching(self):
        df = {'Word': ['Apple', 'apricot', 'Avocado', 'banana']}
        result = task_func(df, 'a')
        self.assertAlmostEqual(result['mean'], 5.666666666666667)  # Mean of lengths: 5, 7, 7
        self.assertEqual(result['median'], 7)
        self.assertEqual(result['mode'], 5)

if __name__ == '__main__':
    unittest.main()