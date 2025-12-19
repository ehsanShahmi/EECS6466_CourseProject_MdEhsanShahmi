import pandas as pd
import json
import unittest
import os

class TestTaskFunc(unittest.TestCase):

    def test_default_output_file(self):
        result = task_func({'a': [1, 2], 'b': [3, 4], 'c': [5, 6]})
        self.assertEqual(result, './default_data_output.json')
        with open(result, 'r') as file:
            data = json.load(file)
        expected_data = {'a': {'0': 1, '1': 2}, 'b': {'0': 3, '1': 4}}
        self.assertEqual(data, expected_data)
        os.remove(result)

    def test_custom_output_file(self):
        result = task_func({'a': [1, 2], 'b': [3, 4], 'c': [5, 6]}, 'custom/path/results.json')
        self.assertEqual(result, 'custom/path/results.json')
        with open(result, 'r') as file:
            data = json.load(file)
        expected_data = {'a': {'0': 1, '1': 2}, 'b': {'0': 3, '1': 4}}
        self.assertEqual(data, expected_data)
        os.remove(result)

    def test_no_c_column(self):
        result = task_func({'a': [1, 2], 'b': [3, 4]})
        self.assertEqual(result, './default_data_output.json')
        with open(result, 'r') as file:
            data = json.load(file)
        expected_data = {'a': {'0': 1, '1': 2}, 'b': {'0': 3, '1': 4}}
        self.assertEqual(data, expected_data)
        os.remove(result)

    def test_empty_data(self):
        result = task_func({})
        self.assertEqual(result, './default_data_output.json')
        with open(result, 'r') as file:
            data = json.load(file)
        expected_data = {}
        self.assertEqual(data, expected_data)
        os.remove(result)

    def test_single_value_in_columns(self):
        result = task_func({'a': [1], 'b': [2], 'c': [3]})
        self.assertEqual(result, './default_data_output.json')
        with open(result, 'r') as file:
            data = json.load(file)
        expected_data = {'a': {'0': 1}, 'b': {'0': 2}}
        self.assertEqual(data, expected_data)
        os.remove(result)

if __name__ == '__main__':
    unittest.main()