import unittest
import pytz
from datetime import datetime
from dateutil.parser import parse

# Here is your prompt:
def task_func(date_str, from_tz, to_tz):
    """
    Convert a date string from one time zone to another and return the time difference in seconds to the current time
    in the destination time zone.

    Parameters:
    date_str (str): The date string in "yyyy-mm-dd hh:mm:ss" format.
    from_tz (str): The timezone of the given date string.
    to_tz (str): The timezone to which the date string should be converted.

    Returns:
    int: The time difference in seconds.

    Requirements:
    - pytz
    - dateutil.parser
    Example:
    >>> type(task_func('2022-10-22 11:59:59', 'UTC', 'America/Chicago'))
    <class 'int'>
    """

    # Get timezone objects for the source and destination timezones
    from_tz_obj = pytz.timezone(from_tz)
    to_tz_obj = pytz.timezone(to_tz)

    # Parse the given date string and localize it to the source timezone
    given_date_naive = parse(date_str)
    given_date = from_tz_obj.localize(given_date_naive)

    # Convert the given date to the destination timezone
    given_date_in_to_tz = given_date.astimezone(to_tz_obj)

    # Get the current time in the destination timezone
    current_date_in_to_tz = datetime.now(pytz.utc).astimezone(to_tz_obj)

    # Calculate the time difference in seconds
    time_difference = current_date_in_to_tz - given_date_in_to_tz

    return int(time_difference.total_seconds())


class TestTaskFunc(unittest.TestCase):

    def test_conversion_utc_to_central(self):
        result = task_func('2022-10-22 11:59:59', 'UTC', 'America/Chicago')
        self.assertIsInstance(result, int)

    def test_conversion_pst_to_est(self):
        result = task_func('2022-10-22 11:59:59', 'America/Los_Angeles', 'America/New_York')
        self.assertIsInstance(result, int)

    def test_conversion_in_future(self):
        result = task_func('2023-11-22 11:59:59', 'UTC', 'America/New_York')
        self.assertIsInstance(result, int)
        self.assertLess(result, 0)  # This is a future date, so the difference should be negative

    def test_conversion_in_past(self):
        result = task_func('2020-10-22 11:59:59', 'UTC', 'America/Chicago')
        self.assertIsInstance(result, int)
        self.assertGreater(result, 0)  # This is a past date, so the difference should be positive

    def test_invalid_timezones(self):
        with self.assertRaises(pytz.UnknownTimeZoneError):
            task_func('2022-10-22 11:59:59', 'Invalid/Timezone', 'America/Chicago')


if __name__ == '__main__':
    unittest.main()