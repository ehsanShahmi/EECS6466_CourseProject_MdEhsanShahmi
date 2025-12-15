import unittest
import pytz
from dateutil.parser import parse

# Constants
TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"

class TestTaskFunc(unittest.TestCase):

    def test_basic_conversion(self):
        """Test conversion from UTC to America/New_York."""
        result = task_func('30/03/09 16:31:32.123', 'UTC', 'America/New_York')
        self.assertEqual(result, '30/03/09 12:31:32.123000')

    def test_conversion_with_daylight_saving(self):
        """Test conversion from America/New_York to Europe/London during daylight saving time."""
        result = task_func('30/07/20 15:00:00.000', 'America/New_York', 'Europe/London')
        self.assertEqual(result, '30/07/20 20:00:00.000000')  # NYC is UTC-4 during DST

    def test_crossing_midnight(self):
        """Test conversion that crosses midnight."""
        result = task_func('31/12/20 23:59:59.999', 'Europe/London', 'Asia/Tokyo')
        self.assertEqual(result, '01/01/21 08:59:59.999000')  # London is UTC during winter

    def test_invalid_timezone(self):
        """Test handling of an invalid timezone."""
        with self.assertRaises(pytz.UnknownTimeZoneError):
            task_func('30/03/09 16:31:32.123', 'UTC', 'Invalid/Timezone')

    def test_formatting_of_output(self):
        """Test output format of the converted time string."""
        result = task_func('01/01/21 00:00:00.000', 'Asia/Tokyo', 'UTC')
        self.assertEqual(result, '31/12/20 15:00:00.000000')  # Tokyo is UTC+9

if __name__ == '__main__':
    unittest.main()