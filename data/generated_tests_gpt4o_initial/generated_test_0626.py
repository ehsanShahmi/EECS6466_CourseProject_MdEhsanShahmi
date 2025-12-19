import unittest
from random import choice
import pytz
from dateutil.parser import parse

# Constants
TIMEZONES = ['America/New_York', 'Europe/London', 'Asia/Shanghai', 'Asia/Tokyo', 'Australia/Sydney']

# Here is your prompt:

def task_func(date_str, from_tz):
    """
    Converts a datetime string from a given timezone to a datetime string in a randomly chosen timezone.

    Parameters:
    - date_str (str): The datetime string in "yyyy-mm-dd hh:mm:ss" format.
    - from_tz (str): The timezone of the given datetime string.

    Returns:
    - tuple: A tuple containing the converted datetime string and the randomly chosen timezone.
    
    Requirements:
    - pytz
    - dateutil.parser
    - random

    Example:
    >>> date_str, from_tz = '2023-06-15 12:00:00', 'UTC'
    >>> converted_date, to_tz = task_func(date_str, from_tz)
    >>> to_tz in TIMEZONES
    True
    """

    from_tz = pytz.timezone(from_tz)
    to_tz = pytz.timezone(choice(TIMEZONES))
    given_date = parse(date_str).replace(tzinfo=from_tz)
    converted_date = given_date.astimezone(to_tz)

    return converted_date.strftime('%Y-%m-%d %H:%M:%S'), to_tz.zone


class TestTaskFunc(unittest.TestCase):

    def test_valid_conversion(self):
        date_str, from_tz = '2023-06-15 12:00:00', 'UTC'
        converted_date, to_tz = task_func(date_str, from_tz)
        self.assertIn(to_tz, TIMEZONES)
        # Additionally check that the converted date is in the right format
        self.assertRegex(converted_date, r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')

    def test_conversion_to_new_york(self):
        date_str, from_tz = '2023-06-15 12:00:00', 'UTC'
        converted_date, to_tz = task_func(date_str, from_tz)
        # Check if conversion to New York timezone is handled correctly
        # Check if the timezone is one of the TIMEZONES
        self.assertEqual(to_tz, 'America/New_York')

    def test_conversion_with_different_tz(self):
        date_str, from_tz = '2023-06-15 15:00:00', 'Europe/London'
        converted_date, to_tz = task_func(date_str, from_tz)
        self.assertIn(to_tz, TIMEZONES)
        self.assertRegex(converted_date, r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')

    def test_invalid_date_format(self):
        date_str, from_tz = '2023/06/15 12:00', 'UTC'
        with self.assertRaises(ValueError):
            task_func(date_str, from_tz)

    def test_invalid_timezone(self):
        date_str, from_tz = '2023-06-15 12:00:00', 'Invalid/Timezone'
        with self.assertRaises(pytz.UnknownTimeZoneError):
            task_func(date_str, from_tz)


if __name__ == '__main__':
    unittest.main()