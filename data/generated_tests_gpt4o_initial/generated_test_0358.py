import itertools
import json
import unittest


def task_func(json_list, r):
    """
    Generate all possible combinations of r elements from a given number list taken from JSON string input.
    
    Parameters:
    json_list (str): JSON string containing the number list.
    r (int): The number of elements in each combination.

    Returns:
    list: A list of tuples, each tuple representing a combination.

    Note:
    - The datetime to be extracted is located in the 'number_list' key in the JSON data.

    Raises:
    - Raise an Exception if the json_list is an invalid JSON, empty, or does not have 'number_list' key.
    
    Requirements:
    - itertools
    - json
    
    Example:
    >>> combinations = task_func('{"number_list": [1, 2, 3, 4, 5]}', 3)
    >>> print(combinations)
    [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]
    """


class TestTaskFunc(unittest.TestCase):

    def test_valid_combinations(self):
        json_input = '{"number_list": [1, 2, 3, 4, 5]}'
        r = 3
        expected_output = [(1, 2, 3), (1, 2, 4), (1, 2, 5), 
                           (1, 3, 4), (1, 3, 5), (1, 4, 5), 
                           (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]
        result = task_func(json_input, r)
        self.assertEqual(result, expected_output)

    def test_empty_json(self):
        json_input = '{}'
        r = 2
        with self.assertRaises(Exception) as context:
            task_func(json_input, r)
        self.assertTrue("Key 'number_list' not found" in str(context.exception))

    def test_invalid_json(self):
        json_input = '{number_list: [1, 2, 3]}'
        r = 2
        with self.assertRaises(json.JSONDecodeError):
            task_func(json_input, r)

    def test_r_greater_than_list_length(self):
        json_input = '{"number_list": [1, 2]}'
        r = 3
        with self.assertRaises(Exception) as context:
            task_func(json_input, r)
        self.assertTrue("r should not be greater than the length of number_list" in str(context.exception))

    def test_non_integer_r(self):
        json_input = '{"number_list": [1, 2, 3]}'
        r = 'a'
        with self.assertRaises(TypeError):
            task_func(json_input, r)


if __name__ == "__main__":
    unittest.main()