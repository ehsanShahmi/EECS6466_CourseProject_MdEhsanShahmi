from datetime import datetime
import pytz
from dateutil.parser import parse
import unittest

def task_func(date_str, tz_str):
    """
    Determine the time in seconds until the next turn of the year in a certain time zone from a given date string.

    Parameters:
    - date_str (str): The date string in "yyyy-mm-dd hh:mm:ss" format.
    - tz_str (str): The IANA timezone string (e.g., 'America/Chicago').

    Returns:
    - int: The time in seconds until the next New Year in the specified timezone.

    Requirements:
    - datetime
    - dateutil.parser
    - pytz

    Example:
    >>> type(task_func('2022-10-22 11:59:59', 'America/Chicago'))
    <class 'int'>
    """

               tz = pytz.timezone(tz_str)
    given_date = parse(date_str).astimezone(tz)  # Correctly handle timezone conversion

    next_year = given_date.year + 1
    new_year = tz.localize(datetime(next_year, 1, 1, 0, 0, 0))  # Correctly create the New Year moment in the specified timezone

    time_until_new_year = new_year - given_date

    return int(time_until_new_year.total_seconds())

class TestTaskFunc(unittest.TestCase):
    def test_time_until_new_year_january(self):
        self.assertEqual(task_func('2023-01-01 00:00:01', 'America/New_York'), 31535999)

    def test_time_until_new_year_december(self):
        self.assertEqual(task_func('2022-12-31 23:59:59', 'America/Chicago'), 1)

    def test_time_until_new_year_in_different_timezone(self):
        self.assertEqual(task_func('2022-12-31 22:00:00', 'America/Los_Angeles'), 3600)

    def test_time_until_new_year_edge_case(self):
        self.assertEqual(task_func('2022-12-31 00:00:00', 'UTC'), 31536000)

    def test_invalid_date_string(self):
        with self.assertRaises(ValueError):
            task_func('invalid-date', 'America/New_York')

if __name__ == '__main__':
    unittest.main()