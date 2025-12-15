import sys
import json
from datetime import datetime
import unittest
from unittest.mock import patch, mock_open

# Here is your prompt:
import sys
import json
from datetime import datetime

# Constants
PATH_TO_APPEND = '/path/to/whatever'
JSON_FILE = '/path/to/json_file.json'

def task_func(path_to_append=PATH_TO_APPEND, json_file=JSON_FILE):
    """
    Add a specific path to sys.path and update a JSON file with the current date and time.
    This function appends a given path to Python's sys.path and updates a JSON file with the current date and time under the key 'last_updated'.
    
    Parameters:
    - path_to_append (str): The path to append to sys.path. Default is '/path/to/whatever'.
    - json_file (str): The path to the JSON file to update. Default is '/path/to/json_file.json'. The file should exist before running the function.

    Returns:
    - json_data (dict): The updated JSON data. The dictionary will contain a 'last_updated' key with the current datetime as its value.

    Requirements:
    - sys
    - json
    - datetime.datetime

    Example:
    >>> task_func('/path/to/new_directory', '/path/to/new_json_file.json')
    {'last_updated': '2023-08-28 12:34:56'}
    """

    sys.path.append(path_to_append)

    with open(json_file, 'r+') as file:
        json_data = json.load(file)
        json_data['last_updated'] = str(datetime.now())
        file.seek(0)
        json.dump(json_data, file, indent=4)
        file.truncate()

    return json_data


class TestTaskFunc(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data=json.dumps({"last_updated": "2023-08-28 12:34:56"}))
    @patch('sys.path', append=['/path/to/new_directory'])
    def test_append_path(self, mock_sys_path):
        task_func('/path/to/new_directory', '/path/to/json_file.json')
        self.assertIn('/path/to/new_directory', sys.path)

    @patch('builtins.open', new_callable=mock_open, read_data=json.dumps({"last_updated": "2023-08-28 12:34:56"}))
    def test_update_json_file_timestamp(self, mock_file):
        with patch('datetime.datetime') as mock_datetime:
            mock_datetime.now.return_value = datetime(2023, 9, 1, 15, 30, 0)
            result = task_func('/path/to/new_directory', '/path/to/json_file.json')
        expected_result = {'last_updated': '2023-09-01 15:30:00'}
        self.assertEqual(result, expected_result)

    @patch('builtins.open', new_callable=mock_open, read_data=json.dumps({"last_updated": "2023-08-28 12:34:56"}))
    def test_overwrite_json_file(self, mock_file):
        task_func('/path/to/new_directory', '/path/to/json_file.json')
        mock_file().write.assert_called()  # Check if write was invoked

    @patch('builtins.open', new_callable=mock_open)
    def test_file_not_found(self, mock_file):
        mock_file.side_effect = FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            task_func('/path/to/new_directory', '/invalid/path')

    @patch('builtins.open', new_callable=mock_open, read_data=json.dumps({"last_updated": "2023-08-28 12:34:56"}))
    def test_json_format_after_update(self, mock_file):
        with patch('datetime.datetime') as mock_datetime:
            mock_datetime.now.return_value = datetime(2023, 9, 1, 15, 30, 0)
            task_func('/path/to/new_directory', '/path/to/json_file.json')
            # Read the file again to check if the format is correct
            mock_file().read()
            updated_json_data = json.loads(mock_file().read().strip())
            self.assertIn('last_updated', updated_json_data)
            self.assertEqual(updated_json_data['last_updated'], '2023-09-01 15:30:00')


if __name__ == '__main__':
    unittest.main()