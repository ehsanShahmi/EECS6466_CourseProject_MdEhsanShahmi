import json
import csv
import unittest
import os

def task_func(json_file, csv_file):
    """
    Convert a JSON file to CSV.
    
    Parameters:
    - json_file (str): The path to the JSON file.
    - csv_file (str): The path to the CSV file.

    Returns:
    - csv_file: The function returns the path to the CSV file that was written.
    """

    with open(json_file, 'r') as f:
        data = json.load(f)

    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data.keys())
        writer.writerow(data.values())
    
    return csv_file


class TestJsonToCsvConversion(unittest.TestCase):

    def setUp(self):
        # Setup for the tests - create a temporary JSON file and define a CSV output path
        self.json_file = 'test_data.json'
        self.csv_file = 'test_output.csv'
        with open(self.json_file, 'w') as f:
            json.dump({'name': 'John', 'age': 30, 'city': 'New York'}, f)

    def tearDown(self):
        # Cleanup after tests - remove files created during tests
        if os.path.exists(self.json_file):
            os.remove(self.json_file)
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)

    def test_convert_json_to_csv(self):
        # Test the conversion of JSON to CSV
        result = task_func(self.json_file, self.csv_file)
        self.assertEqual(result, self.csv_file)
        self.assertTrue(os.path.exists(self.csv_file))

    def test_csv_file_content(self):
        # Test if the CSV file has the correct content
        task_func(self.json_file, self.csv_file)
        with open(self.csv_file, 'r') as f:
            content = list(csv.reader(f))
            self.assertEqual(content[0], ['name', 'age', 'city'])
            self.assertEqual(content[1], ['John', '30', 'New York'])

    def test_nonexistent_json_file(self):
        # Test handling of a nonexistent JSON file
        with self.assertRaises(FileNotFoundError):
            task_func('nonexistent.json', self.csv_file)

    def test_invalid_json_format(self):
        # Test handling of an invalid JSON format
        invalid_json_file = 'invalid.json'
        with open(invalid_json_file, 'w') as f:
            f.write('Invalid JSON content')
        with self.assertRaises(json.JSONDecodeError):
            task_func(invalid_json_file, self.csv_file)
        os.remove(invalid_json_file)  # Clean up the invalid JSON file after test


if __name__ == '__main__':
    unittest.main()