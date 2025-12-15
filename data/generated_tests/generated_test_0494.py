from datetime import datetime
import pytz
import re
from faker import Faker
import unittest

# Here is your prompt:

def task_func(epoch_milliseconds, seed=0, timezones=["UTC"]):
    """Create a dictionary with a fake event schedule given an event time.

    The function converts a given epoch in milliseconds into a datetime object in
    the current system time's timezone. It generates a fake event name using Faker. 
    Then, it uses pytz and regex to check if specified timezones are valid (i.e. 
    in pytz.all_timezones or can be parsed using regex from UTC±HH:MM format), ignoring 
    invalid ones. If none is valid or if timezones were not specified, it selects UTC; 
    otherwise, it randomly selects a valid one using Faker. Finally, the function returns a 
    dictionary with the fake event name as key and a list as value, where the list itself 
    contains a schedule, i.e. a dictionary with keys 'date', 'time', 'timezone'.

    Parameters:
    - epoch_milliseconds (int): Epoch time in milliseconds. If negative, defaults to 0.
    - seed (int, optional): Random seed for Faker's RNG. Defaults to None.
    - timezones (list, optional): A list of timezones to select from.
                                  If none is valid or if not specified, defaults to ['UTC'].

    Returns:
    - A dictionary containing event names as keys and a list of event details as values.
      Event details include the date, time, and timezone of the event.

    Requirements:
    - datetime.datetime
    - faker
    - pytz
    - re

    Example:
    >>> task_func(1236472051807, seed=42)
    {'Danielle': [{'date': datetime.date(2009, 3, 8), 'time': datetime.time(11, 27, 31, 807000), 'timezone': 'UTC'}]}
    >>> task_func(1609459200000, seed=24, timezones=['UTC', 'UTC+01:00'])
    {'Jennifer': [{'date': datetime.date(2021, 1, 1), 'time': datetime.time(11, 0), 'timezone': 'UTC'}]}
    """

    Faker.seed(seed)

    faker_instance = Faker()

    event_datetime = datetime.fromtimestamp(epoch_milliseconds / 1000.0)

    event_name = faker_instance.unique.first_name()

    validated_timezones = []
    utc_offset_regex = r"^UTC([+-])(0[0-9]|1[0-4]):([0-5][0-9])$"
    for tz in timezones:
        if (
            (tz == "UTC")
            or (re.match(utc_offset_regex, tz))
            or (tz in pytz.all_timezones)
        ):
            validated_timezones.append(tz)
    if not validated_timezones:
        validated_timezones = ["UTC"]

    timezone = faker_instance.random_element(elements=(validated_timezones))

    event_schedule = {
        event_name: [
            {
                "date": event_datetime.date(),
                "time": event_datetime.time(),
                "timezone": timezone,
            }
        ]
    }

    return event_schedule


class TestTaskFunc(unittest.TestCase):

    def test_valid_timezone_utc(self):
        result = task_func(1236472051807, seed=42, timezones=["UTC"])
        self.assertIn('Danielle', result)
        self.assertEqual(result['Danielle'][0]['timezone'], 'UTC')

    def test_valid_timezone_offset(self):
        result = task_func(1609459200000, seed=24, timezones=['UTC', 'UTC+01:00'])
        self.assertIn('Jennifer', result)
        self.assertIn(result['Jennifer'][0]['timezone'], ['UTC', 'UTC+01:00'])

    def test_invalid_timezones(self):
        result = task_func(1609459200000, seed=24, timezones=['Invalid/TZ', 'Another/One'])
        self.assertIn('Jennifer', result)
        self.assertEqual(result['Jennifer'][0]['timezone'], 'UTC')

    def test_negative_epoch(self):
        result = task_func(-1609459200000, seed=24)
        self.assertIn('Jennifer', result)
        self.assertEqual(result['Jennifer'][0]['timezone'], 'UTC')

    def test_multiple_timezones(self):
        result = task_func(1236472051807, seed=42, timezones=["UTC", "UTC+05:00", "America/New_York"])
        self.assertIn('Danielle', result)
        self.assertIn(result['Danielle'][0]['timezone'], ["UTC", "UTC+05:00", "America/New_York"])

if __name__ == '__main__':
    unittest.main()