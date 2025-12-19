import os
import json
import unittest
from collections import Counter

def task_func(json_files_path='./json_files/', key='name'):
    """
    Count the occurrence of a particular key in all json files in a specified directory 
    and return a dictionary with the values of the specified key and their counts.
    
    Parameters:
    - json_files_path (str): The path to the directory containing the JSON files. Default is './json_files/'.
    - key (str): The key in the JSON files whose values need to be counted. Default is 'name'.
    
    Returns:
    dict: A dictionary with values of the key as keys and their counts as values.
    
    Requirements:
    - os
    - json
    - collections.Counter
    """
    key_values = []

    for filename in os.listdir(json_files_path):
        if filename.endswith('.json'):
            file_path = os.path.join(json_files_path, filename)
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                if key in data:
                    key_values.append(data[key])

    return dict(Counter(key_values))

class TestTaskFunc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # setup a temporary directory for testing
        cls.test_dir = './test_json_files/'
        os.makedirs(cls.test_dir, exist_ok=True)

    def tearDown(self):
        # Remove all json files after each test
        for filename in os.listdir(self.test_dir):
            file_path = os.path.join(self.test_dir, filename)
            os.remove(file_path)

    @classmethod
    def tearDownClass(cls):
        # Remove the test directory after all tests are done
        os.rmdir(cls.test_dir)

    def test_empty_directory(self):
        """Test when the directory is empty."""
        result = task_func(json_files_path=self.test_dir)
        self.assertEqual(result, {})

    def test_single_json_file(self):
        """Test with a single JSON file."""
        data = {'name': 'apple'}
        with open(os.path.join(self.test_dir, 'file1.json'), 'w') as f:
            json.dump(data, f)

        result = task_func(json_files_path=self.test_dir, key='name')
        self.assertEqual(result, {'apple': 1})

    def test_multiple_json_files_same_value(self):
        """Test with multiple JSON files containing the same value for the key."""
        data1 = {'name': 'banana'}
        data2 = {'name': 'banana'}
        with open(os.path.join(self.test_dir, 'file1.json'), 'w') as f1:
            json.dump(data1, f1)
        with open(os.path.join(self.test_dir, 'file2.json'), 'w') as f2:
            json.dump(data2, f2)

        result = task_func(json_files_path=self.test_dir, key='name')
        self.assertEqual(result, {'banana': 2})

    def test_multiple_json_files_different_values(self):
        """Test with multiple JSON files containing different values for the key."""
        data1 = {'name': 'apple'}
        data2 = {'name': 'banana'}
        data3 = {'name': 'orange'}
        with open(os.path.join(self.test_dir, 'file1.json'), 'w') as f1:
            json.dump(data1, f1)
        with open(os.path.join(self.test_dir, 'file2.json'), 'w') as f2:
            json.dump(data2, f2)
        with open(os.path.join(self.test_dir, 'file3.json'), 'w') as f3:
            json.dump(data3, f3)

        result = task_func(json_files_path=self.test_dir, key='name')
        self.assertEqual(result, {'apple': 1, 'banana': 1, 'orange': 1})

if __name__ == '__main__':
    unittest.main()