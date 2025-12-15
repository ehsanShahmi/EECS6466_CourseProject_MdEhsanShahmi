import json
import re
import pandas as pd
import unittest

def task_func(json_str):
    """
    Load a JSON string into a dictionary, normalize the dictionary by doubling the numerical values,
    and then create a Pandas DataFrame from the dictionary.
    
    (Implementation of the function as per the given prompt is omitted.)
    """

class TestTaskFunc(unittest.TestCase):

    def test_basic_case(self):
        json_str = '{"a": [1, 2, 3], "b": 4.9, "c": "5"}'
        expected_df = pd.DataFrame({'a': [2, 4, 6], 'b': [9.8], 'c': [10]})
        result_df = task_func(json_str)
        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_empty_json(self):
        json_str = '{}'
        expected_df = pd.DataFrame()
        result_df = task_func(json_str)
        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_nested_dicts(self):
        json_str = '{"a": [1, 2], "b": {"nested": 3}, "c": 4}'
        expected_df = pd.DataFrame({'a': [2, 4], 'b': [None], 'c': [8]})
        result_df = task_func(json_str)
        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_strings_with_numbers(self):
        json_str = '{"a": ["1", "2", "3"], "b": "4.5", "c": "not_a_number"}'
        expected_df = pd.DataFrame({'a': [2, 4, 6], 'b': [9.0], 'c': ['not_a_number']})
        result_df = task_func(json_str)
        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_non_numeric_values(self):
        json_str = '{"a": [1, 2, "text"], "b": 5}'
        expected_df = pd.DataFrame({'a': [2, 4, 'text'], 'b': [10]})
        result_df = task_func(json_str)
        pd.testing.assert_frame_equal(result_df, expected_df)

if __name__ == '__main__':
    unittest.main()