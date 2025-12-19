import unittest
import pytz
import numpy as np
from dateutil.parser import parse
import math

MOON_PHASES_YEARS = np.array([1987, 1994, 2001, 2008, 2015, 2022])

def task_func(date_str, from_tz, to_tz):
    """
    Calculate the moon phase by the date and time taking into account the lunar phase cycle of 7 years. The 
    function uses a constant array `MOON_PHASES_YEARS` to determine the reference years for the moon phases.

    Parameters:
    date_str (str): The date string in "yyyy-mm-dd hh:mm:ss" format.
    from_tz (str): The timezone of the given date string.
    to_tz (str): The timezone to which the given date and time should be converted.

    Returns:
    float: The moon phase between 0 and 1. A value of 0 indicates a new moon and a value of 1 indicates a full moon.

    Requirements:
    - pytz
    - numpy
    - dateutil.parser
    - math

    Example:
    >>> task_func('1970-01-01 00:00:00', 'UTC', 'America/New_York')
    0.9749279121818237
    """

    from_tz = pytz.timezone(from_tz)
    to_tz = pytz.timezone(to_tz)
    given_date = parse(date_str).replace(tzinfo=from_tz)
    converted_date = given_date.astimezone(to_tz)

    moon_phase_year = MOON_PHASES_YEARS[np.argmin(np.abs(MOON_PHASES_YEARS - converted_date.year))]
    years_since_moon_phase_year = abs(converted_date.year - moon_phase_year)

    moon_phase = math.sin(math.pi * years_since_moon_phase_year / 7)

    return moon_phase

class TestMoonPhase(unittest.TestCase):

    def test_moon_phase_new_moon(self):
        result = task_func('1987-01-01 00:00:00', 'UTC', 'UTC')
        self.assertAlmostEqual(result, 0.0, places=7)

    def test_moon_phase_full_moon(self):
        result = task_func('1994-07-01 00:00:00', 'UTC', 'UTC')
        self.assertAlmostEqual(result, 1.0, places=7)

    def test_moon_phase_transition_year(self):
        result = task_func('2018-01-01 00:00:00', 'UTC', 'UTC')
        expected = math.sin(math.pi * 1 / 7)  # Calculating expected value for the year 2018
        self.assertAlmostEqual(result, expected, places=7)

    def test_moon_phase_different_timezones(self):
        result = task_func('2022-03-01 12:00:00', 'America/New_York', 'UTC')
        expected = task_func('2022-03-01 17:00:00', 'UTC', 'UTC')  # Converting to UTC manually
        self.assertAlmostEqual(result, expected, places=7)

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            task_func('01/01/1987', 'UTC', 'America/New_York')

if __name__ == '__main__':
    unittest.main()