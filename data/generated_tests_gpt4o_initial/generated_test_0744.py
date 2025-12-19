import unittest
import pandas as pd

# Here is your prompt:
import nltk
from string import punctuation
import pandas as pd


def task_func(text):
    """
    Finds all words in a text, that are seperated by whitespace, 
    beginning with the "$" character and computes their number of occurences.

    Parameters:
    text (str): The input text.

    Returns:
    DataFrame: A pandas DataFrame with two columns: "Word" and "Frequency". 
               "Word" contains the '$' prefixed words, and "Frequency" contains their occurrences.

               
    Raises:
    ValueError: if text is not a string
    
    Requirements:
    - nltk
    - string
    - pandas

    Note:
    The function ignores words that are entirely made up of punctuation, even if they start with a '$'.

    Example:
    >>> text = "$abc def $efg $hij klm $ $abc $abc $hij $hij"
    >>> task_func(text)
       Word  Frequency
    0  $abc          3
    1  $efg          1
    2  $hij          3

    >>> text = "$hello this i$s a $test $test $test"
    >>> task_func(text)
         Word  Frequency
    0  $hello          1
    1   $test          3
    """

               if not isinstance(text, str):
        raise ValueError("The input should be a string.")

    tk = nltk.WhitespaceTokenizer()
    words = tk.tokenize(text)    
    dollar_words = [word for word in words if word.startswith('$') and not all(c in set(punctuation) for c in word)]
    freq = nltk.FreqDist(dollar_words)
    df = pd.DataFrame(list(freq.items()), columns=["Word", "Frequency"])
    return df


class TestTaskFunc(unittest.TestCase):
    
    def test_basic_functionality(self):
        text = "$abc def $efg $hij klm $ $abc $abc $hij $hij"
        expected_output = pd.DataFrame({
            "Word": ["$abc", "$efg", "$hij"],
            "Frequency": [3, 1, 3]
        })
        result = task_func(text).reset_index(drop=True)
        expected_output = expected_output.reset_index(drop=True)
        pd.testing.assert_frame_equal(result, expected_output)

    def test_multiple_same_word(self):
        text = "$hello this is a $test $test $test"
        expected_output = pd.DataFrame({
            "Word": ["$hello", "$test"],
            "Frequency": [1, 3]
        })
        result = task_func(text).reset_index(drop=True)
        expected_output = expected_output.reset_index(drop=True)
        pd.testing.assert_frame_equal(result, expected_output)

    def test_no_dollar_words(self):
        text = "Just a simple text."
        expected_output = pd.DataFrame(columns=["Word", "Frequency"])
        result = task_func(text).reset_index(drop=True)
        expected_output = expected_output.reset_index(drop=True)
        pd.testing.assert_frame_equal(result, expected_output)

    def test_empty_string(self):
        text = ""
        expected_output = pd.DataFrame(columns=["Word", "Frequency"])
        result = task_func(text).reset_index(drop=True)
        expected_output = expected_output.reset_index(drop=True)
        pd.testing.assert_frame_equal(result, expected_output)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            task_func(12345)  # Passing an integer instead of a string

if __name__ == '__main__':
    unittest.main()