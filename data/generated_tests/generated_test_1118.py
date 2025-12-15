import json
import csv
import requests
from io import StringIO
import unittest
from unittest.mock import patch, mock_open, MagicMock


# Constants
CSV_URL = 'https://example.com/data.csv'
JSON_FILE = 'data.json'


def task_func(csv_url=CSV_URL, json_file_path=JSON_FILE):
    """
    Downloads a CSV file from a specified URL, converts it to JSON format, and saves it to a specified file path.
    
    Parameters:
    - csv_url (str): The URL from which the CSV data should be downloaded. Defaults to a constant CSV_URL.
    - json_file_path (str): The file path where the JSON data should be saved. Defaults to a constant JSON_FILE.

    Returns:
    str: The path to the saved JSON file.

    Requirements:
    - json
    - csv
    - requests
    - io.StringIO

    Example:
    >>> task_func("https://example.com/sample.csv", "sample.json")
    "sample.json"
    """
    response = requests.get(csv_url)
    csv_data = csv.reader(StringIO(response.text))

    headers = next(csv_data)
    json_data = [dict(zip(headers, row)) for row in csv_data]

    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file)

    return json_file_path


class TestTaskFunc(unittest.TestCase):

    @patch('requests.get')
    @patch('builtins.open', new_callable=mock_open)
    def test_successful_conversion(self, mock_file, mock_get):
        mock_get.return_value = MagicMock(text='name,age\nAlice,30\nBob,25')
        result = task_func()
        self.assertEqual(result, JSON_FILE)
        mock_file().write.assert_called_once_with(json.dumps([{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]))

    @patch('requests.get')
    def test_empty_csv(self, mock_get):
        mock_get.return_value = MagicMock(text='')
        with self.assertRaises(StopIteration):
            task_func()

    @patch('requests.get')
    @patch('builtins.open', new_callable=mock_open)
    def test_invalid_csv_format(self, mock_file, mock_get):
        mock_get.return_value = MagicMock(text='not-a-csv-format')
        with self.assertRaises(ValueError):
            task_func()

    @patch('requests.get')
    @patch('builtins.open', new_callable=mock_open)
    def test_file_creation(self, mock_file, mock_get):
        mock_get.return_value = MagicMock(text='column1,column2\nvalue1,value2')
        json_path = task_func()
        self.assertTrue(mock_file.called)
        self.assertTrue(json_path.endswith('.json'))

    @patch('requests.get')
    def test_url_not_accessible(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Connection Error")
        with self.assertRaises(requests.exceptions.RequestException):
            task_func()


if __name__ == '__main__':
    unittest.main()