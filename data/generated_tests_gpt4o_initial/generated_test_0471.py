from collections import Counter
import pandas as pd
import unittest

def task_func(myList):
    """
    Count the frequency of each word in a list and return a DataFrame of words and their number.

    Parameters:
    myList (list): List of strings. Each string is considered a word regardless of its content,
                                    however the function is case insensitive, and it removes
                                    leading and trailing whitespaces. If empty, function returns
                                    a DataFrame with a Count column that is otherwise empty.

    Returns:
    DataFrame: A pandas DataFrame with words and their counts.

    Requirements:
    - collections.Counter
    - pandas

    Example:
    >>> myList = ['apple', 'banana', 'apple', 'cherry', 'banana', 'banana']
    >>> task_func(myList)
            Count
    apple       2
    banana      3
    cherry      1
    """
    
    words = [w.lower().strip() for w in myList]
    word_counts = dict(Counter(words))
    report_df = pd.DataFrame.from_dict(word_counts, orient="index", columns=["Count"])

    return report_df

class TestTaskFunction(unittest.TestCase):

    def test_basic_functionality(self):
        myList = ['apple', 'banana', 'apple', 'cherry', 'banana', 'banana']
        expected_df = pd.DataFrame({'Count': [2, 3, 1]}, index=['apple', 'banana', 'cherry'])
        expected_df.index.name = ''
        result_df = task_func(myList)
        pd.testing.assert_frame_equal(result_df, expected_df)
    
    def test_case_insensitivity(self):
        myList = ['Apple', 'banana', 'apple', 'Cherry']
        expected_df = pd.DataFrame({'Count': [2, 1, 1]}, index=['apple', 'banana', 'cherry'])
        expected_df.index.name = ''
        result_df = task_func(myList)
        pd.testing.assert_frame_equal(result_df, expected_df)
    
    def test_leading_trailing_whitespace(self):
        myList = ['  apple  ', 'banana', '  apple  ']
        expected_df = pd.DataFrame({'Count': [2, 1]}, index=['apple', 'banana'])
        expected_df.index.name = ''
        result_df = task_func(myList)
        pd.testing.assert_frame_equal(result_df, expected_df)
    
    def test_empty_list(self):
        myList = []
        expected_df = pd.DataFrame({'Count': []})
        expected_df.index.name = ''
        result_df = task_func(myList)
        pd.testing.assert_frame_equal(result_df, expected_df)
    
    def test_single_word(self):
        myList = ['banana']
        expected_df = pd.DataFrame({'Count': [1]}, index=['banana'])
        expected_df.index.name = ''
        result_df = task_func(myList)
        pd.testing.assert_frame_equal(result_df, expected_df)

if __name__ == '__main__':
    unittest.main()