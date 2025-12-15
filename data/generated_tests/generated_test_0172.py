import json
import unittest
from datetime import datetime

def task_func(json_data):
    """
    Determine if the given datetime is a weekend.

    Parameters:
    - json_data (str): JSON string containing the datetime in UTC format.

    Returns:
    bool: True if the date is a weekend (Saturday or Sunday), False otherwise.

    Note:
    - The datetime to be extracted is located in the 'utc_datetime' key in the JSON data.

    Requirements:
    - json
    - datetime

    Example:
    >>> json_data = '{"utc_datetime": "2024-04-19T12:00:00"}'
    >>> task_func(json_data)
    False
    """
    try:
        # Convert JSON string to Python dictionary
        data = json.loads(json_data)

        # Extract datetime string from dictionary
        datetime_str = data['utc_datetime']

        # Convert datetime string to datetime object
        utc_datetime = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S')

        # Check if the day of the week is Saturday (5) or Sunday (6)
        return utc_datetime.weekday() >= 5
    except Exception as e:
        raise e

class TestTaskFunc(unittest.TestCase):

    def test_weekend_saturday(self):
        json_data = '{"utc_datetime": "2024-04-20T12:00:00"}'  # This is a Saturday
        self.assertTrue(task_func(json_data))

    def test_weekend_sunday(self):
        json_data = '{"utc_datetime": "2024-04-21T12:00:00"}'  # This is a Sunday
        self.assertTrue(task_func(json_data))

    def test_weekday_monday(self):
        json_data = '{"utc_datetime": "2024-04-22T12:00:00"}'  # This is a Monday
        self.assertFalse(task_func(json_data))

    def test_weekday_friday(self):
        json_data = '{"utc_datetime": "2024-04-19T12:00:00"}'  # This is a Friday
        self.assertFalse(task_func(json_data))

    def test_invalid_json(self):
        json_data = '{"utc_datetime": "invalid-date"}'  # Invalid date format
        with self.assertRaises(ValueError):
            task_func(json_data)

if __name__ == '__main__':
    unittest.main()