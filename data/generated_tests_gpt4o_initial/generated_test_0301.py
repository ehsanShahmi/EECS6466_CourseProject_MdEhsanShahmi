import unittest
import pytz
from dateutil.parser import parse
import math

SOLAR_CYCLE_YEARS = np.array([1986, 1996, 2008, 2019])

def task_func(date_str, from_tz, to_tz):
    """
    Calculate solar activity based on the date and time, taking into account the solar cycle of 11 years.

    Parameters:
    date_str (str): The date string in "yyyy-mm-dd hh:mm:ss" format.
    from_tz (str): The timezone of the given date string.
    to_tz (str): The timezone to which the given date and time should be converted.

    Returns:
    float: The solar activity between 0 and 1. The value represents the solar activity 
           calculated using a cosine function based on the years since the closest solar cycle year.
    """
    from_tz = pytz.timezone(from_tz)
    to_tz = pytz.timezone(to_tz)
    given_date = parse(date_str).replace(tzinfo=from_tz)
    converted_date = given_date.astimezone(to_tz)

    solar_cycle_year = SOLAR_CYCLE_YEARS[np.argmin(np.abs(SOLAR_CYCLE_YEARS - converted_date.year))]
    years_since_solar_cycle_year = abs(converted_date.year - solar_cycle_year)

    solar_activity = math.cos(math.pi * years_since_solar_cycle_year / 11)

    return solar_activity

class TestSolarActivity(unittest.TestCase):

    def test_historical_date(self):
        result = task_func('1970-01-01 00:00:00', 'UTC', 'America/New_York')
        self.assertAlmostEqual(result, 0.14231483827328487, places=10)

    def test_near_solar_cycle_year(self):
        result = task_func('1995-12-31 23:59:59', 'UTC', 'America/New_York')
        self.assertAlmostEqual(result, 0.8405982037710357, places=10)

    def test_year_of_peak_activity(self):
        result = task_func('2008-06-01 00:00:00', 'UTC', 'Europe/London')
        self.assertAlmostEqual(result, 1.0, places=10)

    def test_future_date(self):
        result = task_func('2030-01-01 00:00:00', 'UTC', 'Asia/Tokyo')
        self.assertAlmostEqual(result, 0.6548607339452851, places=10)

    def test_time_zone_conversion(self):
        result = task_func('2019-06-01 00:00:00', 'America/New_York', 'UTC')
        self.assertAlmostEqual(result, 0.0, places=10)

if __name__ == '__main__':
    unittest.main()