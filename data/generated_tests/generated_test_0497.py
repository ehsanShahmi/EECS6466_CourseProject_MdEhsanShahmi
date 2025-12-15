import unittest
from datetime import datetime
from pytz import UTC

# Here is your prompt:

def task_func(days_in_past=7):
    """
    Get the weekday of the date 'days_in_past' days ago from today.

    This function computes the date that is 'days_in_past' number of days ago from the current
    system time's date in UTC. It then determines the weekday of this target date using calendar
    and returns its name as a string.

    Parameters:
    days_in_past (int): The number of days to go back from the current date to find the weekday.
                        Defaults to 7 (one week ago). Must be a non-negative integer.

    Returns:
    weekday (str)     : The name of the weekday (e.g., 'Monday', 'Tuesday') for the computed date.

    Raises:
    ValueError: If 'days_in_past' is negative.
    
    Requirements:
    - datetime.datetime
    - datetime.timedelta
    - pytz
    - calendar

    Example:
    >>> task_func()
    'Monday'
    >>> task_func(3)
    'Friday'
    """

    if days_in_past < 0:
        raise ValueError("Days in the past cannot be negative")

    date = datetime.now(UTC) - timedelta(days=days_in_past)
    weekday = calendar.day_name[date.weekday()]

    return weekday


class TestTaskFunc(unittest.TestCase):

    def test_default_days_in_past(self):
        # Testing the default value of days_in_past (7 days ago)
        expected_weekday = (datetime.now(UTC) - timedelta(days=7)).strftime('%A')
        self.assertEqual(task_func(), expected_weekday)

    def test_days_in_past_0(self):
        # Testing the value of days_in_past as 0 (today)
        expected_weekday = datetime.now(UTC).strftime('%A')
        self.assertEqual(task_func(0), expected_weekday)

    def test_days_in_past_1(self):
        # Testing the value of days_in_past as 1 (yesterday)
        expected_weekday = (datetime.now(UTC) - timedelta(days=1)).strftime('%A')
        self.assertEqual(task_func(1), expected_weekday)

    def test_days_in_past_3(self):
        # Testing the value of days_in_past as 3 (3 days ago)
        expected_weekday = (datetime.now(UTC) - timedelta(days=3)).strftime('%A')
        self.assertEqual(task_func(3), expected_weekday)
        
    def test_negative_days_in_past(self):
        # Testing the ValueError raised when days_in_past is negative
        with self.assertRaises(ValueError):
            task_func(-1)


if __name__ == '__main__':
    unittest.main()