import json
import os
import glob
import unittest

# Constants
KEY = 'mynewkey'
VALUE = 'mynewvalue'

def task_func(directory):
    """
    Add a new key-value pair to all JSON files in a specific directory and save the updated JSON files.
    
    Specifically, the function searches for all JSON files within the provided directory and 
    updates each JSON file by adding a new key-value pair ('mynewkey': 'mynewvalue') if the key 
    doesn't already exist. The function modifies the JSON files in place.

    Parameters:
    directory (str): The directory containing the JSON files.

    Returns:
    int: The number of JSON files updated.

    Requirements:
    - json
    - os
    - glob

    Example:
    >>> task_func('./json_files') # Random test case with no JSON files
    0
    """
    files = glob.glob(os.path.join(directory, '*.json'))
    updated_files = 0

    for file in files:
        with open(file, 'r+') as f:
            data = json.load(f)
            if KEY not in data:
                data[KEY] = VALUE
                f.seek(0)
                f.truncate()
                json.dump(data, f)
                updated_files += 1

    return updated_files

class TestTaskFunc(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = './test_json_files'
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        # Remove the temporary directory after tests
        for f in glob.glob(os.path.join(self.test_dir, '*.json')):
            os.remove(f)
        os.rmdir(self.test_dir)

    def test_no_json_files(self):
        """Test with no JSON files in the directory."""
        result = task_func(self.test_dir)
        self.assertEqual(result, 0)

    def test_update_single_json_file(self):
        """Test update when there is one JSON file without the key."""
        json_data = {'existingkey': 'existingvalue'}
        with open(os.path.join(self.test_dir, 'test1.json'), 'w') as f:
            json.dump(json_data, f)

        result = task_func(self.test_dir)
        self.assertEqual(result, 1)

        with open(os.path.join(self.test_dir, 'test1.json'), 'r') as f:
            updated_data = json.load(f)
            self.assertIn(KEY, updated_data)
            self.assertEqual(updated_data[KEY], VALUE)

    def test_no_update_existing_key(self):
        """Test that existing key is not overwritten."""
        json_data = {KEY: 'oldvalue'}
        with open(os.path.join(self.test_dir, 'test2.json'), 'w') as f:
            json.dump(json_data, f)

        result = task_func(self.test_dir)
        self.assertEqual(result, 0)

        with open(os.path.join(self.test_dir, 'test2.json'), 'r') as f:
            updated_data = json.load(f)
            self.assertEqual(updated_data[KEY], 'oldvalue')

    def test_update_multiple_json_files(self):
        """Test update multiple JSON files without the key."""
        json_data_1 = {'key1': 'value1'}
        json_data_2 = {'key2': 'value2'}
        with open(os.path.join(self.test_dir, 'test3.json'), 'w') as f:
            json.dump(json_data_1, f)
        with open(os.path.join(self.test_dir, 'test4.json'), 'w') as f:
            json.dump(json_data_2, f)

        result = task_func(self.test_dir)
        self.assertEqual(result, 2)

        for filename in ['test3.json', 'test4.json']:
            with open(os.path.join(self.test_dir, filename), 'r') as f:
                updated_data = json.load(f)
                self.assertIn(KEY, updated_data)
                self.assertEqual(updated_data[KEY], VALUE)

if __name__ == '__main__':
    unittest.main()