import unittest
import pytz
from dateutil import parser

# Here is your prompt:
def task_func(date_str, from_tz, to_tz):
    """
    Converts a date time from one timezone to another.

    Parameters:
    date_str (str): The date string in "yyyy-mm-dd hh:mm:ss" format.
    from_tz (str): The timezone of the given date string.
    to_tz (str): The timezone to which the date should be converted.

    Returns:
    str: The converted datetime string in "yyyy-mm-dd hh:mm:ss" format.

    Requirements:
    - pytz
    - dateutil.parser

    Example:
    >>> task_func('2022-03-01 12:00:00', 'UTC', 'America/New_York')
    '2022-03-01 07:00:00'
    """
    from_tz = pytz.timezone(from_tz)
    to_tz = pytz.timezone(to_tz)
    date = parser.parse(date_str).replace(tzinfo=from_tz)
    date = date.astimezone(to_tz)

    return date.strftime('%Y-%m-%d %H:%M:%S')

class TestTaskFunc(unittest.TestCase):

    def test_utc_to_ny(self):
        self.assertEqual(task_func('2022-03-01 12:00:00', 'UTC', 'America/New_York'), '2022-03-01 07:00:00')

    def test_ny_to_utc(self):
        self.assertEqual(task_func('2022-03-01 07:00:00', 'America/New_York', 'UTC'), '2022-03-01 12:00:00')

    def test_utc_to_london(self):
        self.assertEqual(task_func('2022-07-01 12:00:00', 'UTC', 'Europe/London'), '2022-07-01 13:00:00')

    def test_ny_to_london(self):
        self.assertEqual(task_func('2022-03-01 07:00:00', 'America/New_York', 'Europe/London'), '2022-03-01 12:00:00')

    def test_invalid_timezone(self):
        with self.assertRaises(pytz.UnknownTimeZoneError):
            task_func('2022-03-01 12:00:00', 'Invalid/Timezone', 'America/New_York')

if __name__ == '__main__':
    unittest.main()