import pandas as pd
import re
import unittest

# Constants
STOPWORDS = set([
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
    "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
    "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
    "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
    "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because",
    "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into",
    "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out",
    "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where",
    "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no",
    "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just",
    "don", "should", "now"
])

def task_func(data, column):
    """
    Removes English stopwords from a text column in a DataFrame and returns the modified DataFrame.
    
    Parameters:
    df (pandas.DataFrame): The DataFrame containing the text column to be processed.
    column (str): The name of the text column from which stopwords should be removed.
    
    Returns:
    pandas.DataFrame: A DataFrame with the stopwords removed from the specified column.
    
    Requirements:
    - pandas
    - re
    
    Constants:
    - STOPWORDS: A set containing common English stopwords.
    
    Example:
    >>> data = {'text': ['This is a sample sentence.', 'Another example here.']}
    >>> print(task_func(data, 'text'))
                  text
    0  sample sentence
    1  Another example
    """

    df = pd.DataFrame(data)
    df[column] = df[column].apply(lambda x: ' '.join([word for word in re.findall(r'\b\w+\b', x) if word.lower() not in STOPWORDS]))
    return df

class TestTaskFunc(unittest.TestCase):

    def test_basic_removal(self):
        data = {'text': ['This is a sample sentence.', 'Another example here.']}
        expected = {'text': ['sample sentence', 'Another example']}
        result = task_func(data, 'text')
        expected_df = pd.DataFrame(expected)
        pd.testing.assert_frame_equal(result, expected_df)

    def test_empty_column(self):
        data = {'text': ['']}
        expected = {'text': ['']}
        result = task_func(data, 'text')
        expected_df = pd.DataFrame(expected)
        pd.testing.assert_frame_equal(result, expected_df)

    def test_no_stopwords(self):
        data = {'text': ['Hello World!']}
        expected = {'text': ['Hello World']}
        result = task_func(data, 'text')
        expected_df = pd.DataFrame(expected)
        pd.testing.assert_frame_equal(result, expected_df)

    def test_all_stopwords(self):
        data = {'text': ['I am a test.']}
        expected = {'text': ['test']}
        result = task_func(data, 'text')
        expected_df = pd.DataFrame(expected)
        pd.testing.assert_frame_equal(result, expected_df)

    def test_multiple_stopwords(self):
        data = {'text': ['This text has many stopwords.']}
        expected = {'text': ['text many stopwords']}
        result = task_func(data, 'text')
        expected_df = pd.DataFrame(expected)
        pd.testing.assert_frame_equal(result, expected_df)

if __name__ == '__main__':
    unittest.main()