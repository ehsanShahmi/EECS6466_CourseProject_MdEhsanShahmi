import pandas as pd
import re
import unittest

# Function to replace acronyms in DataFrame
def task_func(data, mapping):
    """
    Replace all acronyms in a DataFrame with their full words according to a provided dictionary.
    
    Requirements:
    - pandas
    - re

    Parameters:
    - data (dict): A dictionary where keys are column names and values are lists of strings.
    - mapping (dict): A dictionary where keys are acronyms and values are the full words.
    
    Returns:
    - pd.DataFrame: A DataFrame where all acronyms in string cells have been replaced with their full words.
    
    Examples:
    >>> data = {'text': ['NASA is great', 'I live in the USA']}
    >>> mapping = {'NASA': 'National Aeronautics and Space Administration', 'USA': 'United States of America'}
    >>> print(task_func(data, mapping))
                                                    text
    0  National Aeronautics and Space Administration ...
    1             I live in the United States of America
    """

    df = pd.DataFrame(data)
    pattern = re.compile(r'\b[A-Z]+\b')
    
    def replace_match(match):
        return mapping.get(match.group(0), match.group(0))

    df = df.applymap(lambda x: pattern.sub(replace_match, x) if isinstance(x, str) else x)

    return df


class TestTaskFunc(unittest.TestCase):

    def test_basic_replacement(self):
        data = {'text': ['NASA is great', 'I live in the USA']}
        mapping = {'NASA': 'National Aeronautics and Space Administration', 'USA': 'United States of America'}
        expected_output = pd.DataFrame({
            'text': [
                'National Aeronautics and Space Administration is great',
                'I live in the United States of America'
            ]
        })
        result = task_func(data, mapping)
        pd.testing.assert_frame_equal(result, expected_output)

    def test_no_replacement_needed(self):
        data = {'text': ['This is a test', 'Nothing to replace here']}
        mapping = {'NASA': 'National Aeronautics and Space Administration'}
        expected_output = pd.DataFrame({
            'text': ['This is a test', 'Nothing to replace here']
        })
        result = task_func(data, mapping)
        pd.testing.assert_frame_equal(result, expected_output)

    def test_partial_replacement(self):
        data = {'text': ['I love NASA and the USA', 'NASA is cool']}
        mapping = {'NASA': 'National Aeronautics and Space Administration'}
        expected_output = pd.DataFrame({
            'text': [
                'I love National Aeronautics and Space Administration and the USA',
                'National Aeronautics and Space Administration is cool'
            ]
        })
        result = task_func(data, mapping)
        pd.testing.assert_frame_equal(result, expected_output)

    def test_empty_dataframe(self):
        data = {'text': []}
        mapping = {}
        expected_output = pd.DataFrame({'text': []})
        result = task_func(data, mapping)
        pd.testing.assert_frame_equal(result, expected_output)

    def test_empty_mapping(self):
        data = {'text': ['This is an example']}
        mapping = {}
        expected_output = pd.DataFrame({'text': ['This is an example']})
        result = task_func(data, mapping)
        pd.testing.assert_frame_equal(result, expected_output)


if __name__ == '__main__':
    unittest.main()