import pandas as pd
from datetime import datetime
import holidays
import unittest

def task_func(start_date=datetime(2023, 1, 1), end_date=datetime(2023, 12, 31), country='US'):
    """
    Create a list of business days between two dates, excluding weekends and specified country's public holidays.

    Parameters:
    start_date (datetime): The start date. Default is January 1, 2023.
    end_date (datetime): The end date. Default is December 31, 2023.
    country (str): ISO country code to determine public holidays. Default is 'US'.

    Returns:
    list[datetime]: A list of business days (as datetime objects). The start date and end date is included to process.

    Raises:
    ValueError: If start_date is not a datetime object or is after end_date.
    ValueError: If end_date is not a datetime object or is before start_date.

    Requirements:
    - pandas
    - datetime
    - holidays

    Note:
    - The function depends on the 'holidays' package for fetching public holidays.
    - Ensure 'pandas' and 'holidays' packages are installed.

    Example:
    >>> business_days = task_func()
    >>> print(business_days[0])
    2023-01-03 00:00:00
    """

    if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
        raise ValueError("start_date and end_date must be datetime objects.")
    if start_date > end_date:
        raise ValueError("start_date must not be after end_date.")

    country_holidays = holidays.CountryHoliday(country)
    dates = pd.date_range(start_date, end_date)
    business_days = [date for date in dates if date.weekday() < 5 and date not in country_holidays]

    return business_days

class TestTaskFunc(unittest.TestCase):

    def test_valid_business_days(self):
        """ Test for a standard range of business days """
        result = task_func(datetime(2023, 1, 1), datetime(2023, 1, 10))
        self.assertTrue(all(date.weekday() < 5 for date in result))  # Check if all days are weekdays
        self.assertFalse(any(date in holidays.US() for date in result))  # Check if no holidays are in result

    def test_start_date_after_end_date(self):
        """ Test for ValueError when start_date is after end_date """
        with self.assertRaises(ValueError):
            task_func(datetime(2023, 1, 10), datetime(2023, 1, 1))

    def test_non_datetime_start_date(self):
        """ Test for ValueError when start_date is not a datetime object """
        with self.assertRaises(ValueError):
            task_func("2023-01-01", datetime(2023, 1, 10))

    def test_non_datetime_end_date(self):
        """ Test for ValueError when end_date is not a datetime object """
        with self.assertRaises(ValueError):
            task_func(datetime(2023, 1, 1), "2023-01-10")

    def test_no_business_days(self):
        """ Test for a range with no business days (only weekends) """
        result = task_func(datetime(2023, 1, 7), datetime(2023, 1, 8))
        self.assertEqual(result, [])  # Expect no business days in the weekend

if __name__ == '__main__':
    unittest.main()