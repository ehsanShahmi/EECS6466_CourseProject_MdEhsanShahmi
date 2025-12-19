import collections
import json
import os
import tempfile
import unittest

def task_func(directory_path: str) -> dict:
    """
    Count the total appearances of all keys in all JSON files in the specified directory and return a dictionary 
    with the keys from the JSON files as keys and their respective counts as values.

    Parameters:
    - directory_path (str): The path to the directory containing the JSON files.

    Returns:
    dict: A dictionary with the keys from the JSON files as keys and their counts as values.
    """
    key_counts = collections.defaultdict(int)

    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                for key in data.keys():
                    key_counts[key] += 1

    return dict(key_counts)

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Create a temporary directory for testing."""
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        """Remove the temporary directory after tests."""
        for filename in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, filename))
        os.rmdir(self.test_dir)

    def test_single_file(self):
        """Test with a single JSON file."""
        data = {'name': 'John', 'age': 25}
        with open(os.path.join(self.test_dir, 'test_1.json'), 'w') as f:
            json.dump(data, f)
        
        result = task_func(self.test_dir)
        expected = {'name': 1, 'age': 1}
        self.assertEqual(result, expected)

    def test_multiple_files(self):
        """Test with multiple JSON files."""
        data1 = {'name': 'John', 'age': 25}
        data2 = {'name': 'Doe', 'age': 30, 'address': '123 Main St'}
        with open(os.path.join(self.test_dir, 'test_1.json'), 'w') as f:
            json.dump(data1, f)
        with open(os.path.join(self.test_dir, 'test_2.json'), 'w') as f:
            json.dump(data2, f)

        result = task_func(self.test_dir)
        expected = {'name': 2, 'age': 2, 'address': 1}
        self.assertEqual(result, expected)

    def test_no_json_files(self):
        """Test when there are no JSON files in the directory."""
        os.mkdir(os.path.join(self.test_dir, 'subdir'))
        result = task_func(self.test_dir)
        expected = {}
        self.assertEqual(result, expected)

    def test_empty_json_file(self):
        """Test with an empty JSON file."""
        with open(os.path.join(self.test_dir, 'empty.json'), 'w') as f:
            json.dump({}, f)

        result = task_func(self.test_dir)
        expected = {}
        self.assertEqual(result, expected)

    def test_mixed_files(self):
        """Test with mixed files (not all JSON)."""
        data = {'name': 'John', 'age': 25}
        with open(os.path.join(self.test_dir, 'test.json'), 'w') as f:
            json.dump(data, f)
        with open(os.path.join(self.test_dir, 'test.txt'), 'w') as f:
            f.write("This is a text file.")

        result = task_func(self.test_dir)
        expected = {'name': 1, 'age': 1}
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()