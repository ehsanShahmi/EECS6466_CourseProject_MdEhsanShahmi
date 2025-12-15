import unittest
import os
import tempfile
import json
import csv

# Here is your prompt:
# import csv
# import json
# import os

# def task_func(file_name):
#     """
#     Convert a csv file to a json file.
#     
#     Parameters:
#     file_name (str): The name of the csv file.
#     
#     Returns:
#     str: The file name of the created json file.
#
#     Requirements:
#     - csv
#     - json
#     - os
#
#     Raises:
#     FileNotFoundError: If the file does not exist.
#     
#     Example:
#     >>> import tempfile
#     >>> FILE_NAME = tempfile.NamedTemporaryFile(prefix='report_', suffix='.csv', dir='/tmp').name
#     >>> with open(FILE_NAME, 'w', newline='') as csvfile:
#     ...     fieldnames = ['id', 'name', 'age']
#     ...     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     ...     _ = writer.writeheader()
#     ...     _ = writer.writerow({'id': '1', 'name': 'John', 'age': '25'})
#     ...     _ = writer.writerow({'id': '2', 'name': 'Doe', 'age': '30'})
#     >>> json_file = task_func(FILE_NAME)
#     >>> print(json_file.startswith('/tmp/report_') and json_file.endswith('.json'))
#     True
#     """

#                 if not os.path.exists(file_name):
#         raise FileNotFoundError("File does not exist.")

#     data = []

#     with open(file_name, 'r') as f:
#         csv_reader = csv.DictReader(f)
#         for row in csv_reader:
#             data.append(row)

#     json_file_name = file_name.split('.')[0] + '.json'

#     with open(json_file_name, 'w') as f:
#         json.dump(data, f)

#     return json_file_name

class TestTaskFunction(unittest.TestCase):

    def setUp(self):
        """Create a temporary CSV file for the tests."""
        self.temp_csv_file = tempfile.NamedTemporaryFile(prefix='test_', suffix='.csv', delete=False)
        self.temp_json_file = self.temp_csv_file.name.replace('.csv', '.json')
        with open(self.temp_csv_file.name, 'w', newline='') as csvfile:
            fieldnames = ['id', 'name', 'age']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'id': '1', 'name': 'Alice', 'age': '30'})
            writer.writerow({'id': '2', 'name': 'Bob', 'age': '25'})

    def tearDown(self):
        """Remove the temporary files after tests."""
        if os.path.exists(self.temp_csv_file.name):
            os.remove(self.temp_csv_file.name)
        if os.path.exists(self.temp_json_file):
            os.remove(self.temp_json_file)

    def test_convert_csv_to_json(self):
        """Test if CSV file is converted to JSON correctly."""
        json_file = task_func(self.temp_csv_file.name)
        self.assertEqual(json_file, self.temp_json_file)
        self.assertTrue(os.path.exists(json_file))
        with open(json_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(len(data), 2)
            self.assertEqual(data[0], {'id': '1', 'name': 'Alice', 'age': '30'})
            self.assertEqual(data[1], {'id': '2', 'name': 'Bob', 'age': '25'})

    def test_file_not_found(self):
        """Test if FileNotFoundError is raised for a non-existing file."""
        with self.assertRaises(FileNotFoundError):
            task_func('non_existing_file.csv')

    def test_empty_csv_file(self):
        """Test conversion of an empty CSV file."""
        empty_csv = tempfile.NamedTemporaryFile(prefix='empty_', suffix='.csv', delete=False)
        empty_json = empty_csv.name.replace('.csv', '.json')
        empty_csv.close()  # Close the file to allow it to be used
        json_file = task_func(empty_csv.name)
        self.assertEqual(json_file, empty_json)
        self.assertTrue(os.path.exists(json_file))
        with open(json_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(data, [])
        os.remove(empty_csv.name)
        os.remove(empty_json)

    def test_json_file_creation(self):
        """Test that a JSON file is created after conversion."""
        json_file = task_func(self.temp_csv_file.name)
        self.assertTrue(os.path.exists(json_file))

if __name__ == '__main__':
    unittest.main()