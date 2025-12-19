from datetime import datetime
import pytz
import unittest

# Constants
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

class TestTaskFunc(unittest.TestCase):

    def test_unix_timestamp_conversion_to_timezone(self):
        unix_timestamp = 1609459200  # This is 2021-01-01 00:00:00 UTC
        target_timezone = 'America/New_York'
        expected_result = '2020-12-31 19:00:00'  # Expected NY time
        self.assertEqual(task_func(unix_timestamp, target_timezone), expected_result)

    def test_unix_timestamp_conversion_to_different_timezone(self):
        unix_timestamp = 1609459200  # This is 2021-01-01 00:00:00 UTC
        target_timezone = 'Europe/London'
        expected_result = '2021-01-01 00:00:00'  # Expected London time
        self.assertEqual(task_func(unix_timestamp, target_timezone), expected_result)

    def test_unix_timestamp_edge_case(self):
        unix_timestamp = 0  # This is 1970-01-01 00:00:00 UTC
        target_timezone = 'Asia/Tokyo'
        expected_result = '1970-01-01 09:00:00'  # Expected Tokyo time
        self.assertEqual(task_func(unix_timestamp, target_timezone), expected_result)

    def test_invalid_timezone(self):
        unix_timestamp = 1609459200  # This is 2021-01-01 00:00:00 UTC
        target_timezone = 'Invalid/Timezone'
        with self.assertRaises(pytz.UnknownTimeZoneError):
            task_func(unix_timestamp, target_timezone)

    def test_negative_unix_timestamp(self):
        unix_timestamp = -3600  # This is 1969-12-31 23:00:00 UTC
        target_timezone = 'America/Los_Angeles'
        expected_result = '1969-12-31 15:00:00'  # Expected Los Angeles time
        self.assertEqual(task_func(unix_timestamp, target_timezone), expected_result)

if __name__ == '__main__':
    unittest.main()