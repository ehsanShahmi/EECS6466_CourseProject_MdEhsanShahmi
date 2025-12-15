import collections
import json
import os
import unittest
import tempfile

def task_func(data, json_file_name='data.json'):
    """
    Add a new key "a" with the value 1 to the input dictionary, calculate the frequency of its values, and save the updated dictionary along with its frequency distribution to a JSON file. The dictionary is saved under the key 'data' and the frequency distribution under the key 'freq'.

    Parameters:
    data (dict): The input data as a dictionary.
    json_file_name (str): The name of the JSON file to be saved.

    Returns:
    str: The path of the JSON file.

    Requirements:
    - collections
    - re
    - json
    - os

    Example:
    >>> import tempfile
    >>> json_file = tempfile.NamedTemporaryFile(delete=False)
    >>> data = {'key1': 'value1', 'key2': 'value2', 'key3': 'value1'}
    >>> task_func(data, json_file.name) is not None
    True
    """
    
    # Add new key 'a' with value 1
    data['a'] = 1

    # Calculate the frequency of values in `data`
    freq = collections.Counter(data.values())

    # Save the updated `data` and the `freq` into a JSON file
    json_data = {'data': data, 'freq': dict(freq)}
    json_file_path = os.path.join(os.getcwd(), json_file_name)
    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file)

    return json_file_path


class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.data = {'key1': 'value1', 'key2': 'value2'}
        self.temp_json_file = tempfile.NamedTemporaryFile(delete=False)

    def tearDown(self):
        os.remove(self.temp_json_file.name)

    def test_add_key_a(self):
        task_func(self.data, self.temp_json_file.name)
        expected_data = {'key1': 'value1', 'key2': 'value2', 'a': 1}
        with open(self.temp_json_file.name) as json_file:
            result = json.load(json_file)
        self.assertEqual(result['data'], expected_data)

    def test_frequency_count(self):
        self.data['key3'] = 'value1'
        task_func(self.data, self.temp_json_file.name)
        expected_freq = {'value1': 3, 'value2': 1}
        with open(self.temp_json_file.name) as json_file:
            result = json.load(json_file)
        self.assertEqual(result['freq'], expected_freq)

    def test_json_file_saved(self):
        result_path = task_func(self.data, self.temp_json_file.name)
        self.assertTrue(os.path.exists(result_path))

    def test_return_value(self):
        result_path = task_func(self.data, self.temp_json_file.name)
        self.assertEqual(result_path, self.temp_json_file.name)

    def test_empty_data(self):
        empty_data = {}
        task_func(empty_data, self.temp_json_file.name)
        expected_data = {'a': 1}
        with open(self.temp_json_file.name) as json_file:
            result = json.load(json_file)
        self.assertEqual(result['data'], expected_data)


if __name__ == '__main__':
    unittest.main()