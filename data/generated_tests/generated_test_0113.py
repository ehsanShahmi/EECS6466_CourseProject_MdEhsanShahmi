import json
from collections import Counter
import random
import unittest
import os

def task_func(my_dict, keys):
    """
    Updates a given dictionary by adding 10 random elements based on the 'keys' parameter,
    with values as random integers from 1 to 100. It saves the JSON representation of the
    updated dictionary to a file and the counts of each key to a separate text file.

    Parameters:
        my_dict (dict): The dictionary to be updated.
        keys (list of str): A list of keys to be added to the dictionary.

    Returns:
        tuple: The dictionary, path to the JSON file, and path to the text file.

    Raises:
        ValueError: If 'keys' does not contain exactly 10 unique elements.

    Note:
        This function modifies the input dictionary in place.
        The filename of the json is 'updated_dictionary.json'
        The filename of the txt file is 'key_frequencies.txt'

    Requirements:
    - json
    - collections.Counter
    - random

    Examples:
    >>> result, json_path, txt_path = task_func({'first_key': 1, 'second_key': 2}, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
    >>> isinstance(result, dict)
    True
    >>> len(result) > 2  # Checking if more keys have been added
    True
    """
    
    if len(set(keys)) != 10:
        raise ValueError("keys parameter must contain exactly 10 unique elements")

    for key in keys:
        my_dict[key] = random.randint(1, 100)

    json_filename = "updated_dictionary.json"
    txt_filename = "key_frequencies.txt"

    with open(json_filename, 'w') as json_file:
        json.dump(my_dict, json_file, indent=4)

    key_counts = Counter(my_dict.keys())
    with open(txt_filename, 'w') as txt_file:
        for key, count in key_counts.items():
            txt_file.write(f"{key}: {count}\n")

    return my_dict, json_filename, txt_filename

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.test_dict = {'initial_key': 1}
        self.valid_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        self.invalid_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    def tearDown(self):
        try:
            os.remove("updated_dictionary.json")
            os.remove("key_frequencies.txt")
        except OSError:
            pass  # Ignore if files do not exist.

    def test_function_updates_dict(self):
        result, json_path, txt_path = task_func(self.test_dict, self.valid_keys)
        self.assertEqual(len(result), len(self.test_dict) + 10)
        self.assertIn('a', result)
        self.assertIn('j', result)

    def test_function_creates_json_file(self):
        _, json_path, _ = task_func(self.test_dict, self.valid_keys)
        self.assertTrue(os.path.exists(json_path))

    def test_function_creates_txt_file(self):
        _, _, txt_path = task_func(self.test_dict, self.valid_keys)
        self.assertTrue(os.path.exists(txt_path))

    def test_invalid_keys_raise_error(self):
        with self.assertRaises(ValueError):
            task_func(self.test_dict, self.invalid_keys)

    def test_function_saves_correct_key_counts(self):
        _, _, txt_path = task_func(self.test_dict, self.valid_keys)
        with open(txt_path, 'r') as file:
            contents = file.read()
            for key in self.valid_keys:
                self.assertIn(f"{key}: 1", contents)

if __name__ == '__main__':
    unittest.main()