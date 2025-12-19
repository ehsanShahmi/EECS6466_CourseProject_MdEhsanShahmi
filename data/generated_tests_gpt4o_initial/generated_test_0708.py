import unittest
import os
import json
import base64

# Here is your prompt:
import json
import csv
import os
import base64

def task_func(raw_string, filename, output_dir):
    """
    Processes a base64-encoded JSON string, stores the data in a CSV file, and returns the path of the file.

    Parameters:
    - raw_string (str): The base64 encoded JSON string.
    - filename (str): The name of the file to which the data should be saved (without extension).
    - output_dir (str): The path of the directory in which the file should be saved.

    Returns:
    - file_path (str): The path of the file.

    Requirements:
    - json
    - csv
    - os
    - base64

    Example:
    >>> task_func('eyJrZXkiOiAiVmFsdWUifQ==', 'data', './output')
    './output/data.csv'
    """

               # Decode the string and load the data
    decoded_string = base64.b64decode(raw_string).decode('utf-8')
    data = json.loads(decoded_string)

    # Prepare the output directory
    os.makedirs(output_dir, exist_ok=True)

    # Prepare the file path
    file_path = os.path.join(output_dir, f'{filename}.csv')

    # Save the data to the file
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        for key, value in data.items():
            writer.writerow([key, value])

    return file_path

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        """Create a temporary output directory for tests."""
        self.output_dir = './test_output'
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def tearDown(self):
        """Remove the output directory after tests."""
        if os.path.exists(self.output_dir):
            for file in os.listdir(self.output_dir):
                os.remove(os.path.join(self.output_dir, file))
            os.rmdir(self.output_dir)
    
    def test_valid_input(self):
        """Test task_func with valid base64 encoded JSON."""
        raw_string = base64.b64encode(json.dumps({'key': 'value'}).encode()).decode()
        filename = 'test_data'
        expected_file_path = os.path.join(self.output_dir, f'{filename}.csv')
        
        result = task_func(raw_string, filename, self.output_dir)
        self.assertEqual(result, expected_file_path)
        self.assertTrue(os.path.exists(expected_file_path))

    def test_empty_json(self):
        """Test task_func with empty JSON."""
        raw_string = base64.b64encode(json.dumps({}).encode()).decode()
        filename = 'empty_data'
        expected_file_path = os.path.join(self.output_dir, f'{filename}.csv')
        
        result = task_func(raw_string, filename, self.output_dir)
        self.assertEqual(result, expected_file_path)
        self.assertTrue(os.path.exists(expected_file_path))

        with open(expected_file_path, 'r') as f:
            content = f.read()
            self.assertEqual(content, '')

    def test_invalid_base64(self):
        """Test task_func with invalid base64 string."""
        with self.assertRaises(Exception):
            task_func('invalid_base64_string', 'test', self.output_dir)

    def test_invalid_json(self):
        """Test task_func with base64 encoded invalid JSON."""
        raw_string = base64.b64encode('{"key": "value"'.encode()).decode()  # Invalid JSON
        with self.assertRaises(Exception):
            task_func(raw_string, 'test', self.output_dir)

if __name__ == '__main__':
    unittest.main()