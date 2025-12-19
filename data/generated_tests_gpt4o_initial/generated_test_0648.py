from dateutil.parser import parse
from datetime import timedelta
import unittest

def task_func(date_str):
    """
    Get the next business day (Mon-Fri) after a certain date string. Implemented by dateutil.parser and datetime.

    Parameters:
    date_str (str): The date string in "yyyy-mm-dd" format.

    Returns:
    datetime: The datetime object of the next business day.

    Requirements:
    - datetime
    - dateutil.parser

    Example:
    >>> task_func('2022-10-22')
    datetime.datetime(2022, 10, 24, 0, 0)
    >>> task_func('2022-10-28')
    datetime.datetime(2022, 10, 31, 0, 0)
    """

    given_date = parse(date_str)
    next_day = given_date

    while True:
        next_day = next_day + timedelta(days=1)

        # Monday to Friday are business days
        if 0 <= next_day.weekday() < 5:
            break

    return next_day

class TestNextBusinessDay(unittest.TestCase):

    def test_next_business_day_on_saturday(self):
        self.assertEqual(task_func('2022-10-22'), parse('2022-10-24'))  # Saturday should return next Monday

    def test_next_business_day_on_sunday(self):
        self.assertEqual(task_func('2022-10-23'), parse('2022-10-24'))  # Sunday should also return next Monday

    def test_next_business_day_on_friday(self):
        self.assertEqual(task_func('2022-10-28'), parse('2022-10-31'))  # Friday should return next Monday

    def test_next_business_day_on_holiday(self):
        # Assuming that 2022-12-31 (Saturday) is followed by Monday 2023-01-02
        self.assertEqual(task_func('2022-12-31'), parse('2023-01-02'))  # End of the year

    def test_next_business_day_on_weekday(self):
        self.assertEqual(task_func('2022-10-21'), parse('2022-10-24'))  # A random weekday (Friday)

if __name__ == '__main__':
    unittest.main()