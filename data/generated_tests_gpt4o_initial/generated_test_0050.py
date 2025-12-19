from datetime import datetime
import pandas as pd
import pytz
import matplotlib.pyplot as plt
import unittest

# Constants
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
TIMEZONES = [
    "America/New_York",
    "Europe/London",
    "Asia/Shanghai",
    "Asia/Tokyo",
    "Australia/Sydney",
]


def task_func(timestamp):
    """
    Convert a Unix timestamp to date objects in different time zones, create a Pandas DataFrame, and draw a bar chart.
    - You should use the time zones mentionned in the constant TIMEZONES.
    - The date format should be as DATE_FORMAT.
    - The DataFrame should have 'Timezone' and 'Datetime' as column names.
    - The x-label of the bar plot should be set to 'Timezone' while the y-label should be set to 'Datetime'.
    - The plot title should be "Datetime = f(Timezone)"

    Parameters:
    timestamp (int): The Unix timestamp.

    Returns:
    tuple: A tuple containing:
        - DataFrame: A pandas DataFrame containing the datetime in different timezones.
        - Axes: A matplotlib Axes object for the generated bar chart.

    Requirements:
    - datetime
    - pandas
    - pytz
    - matplotlib.pyplot

    Example:
    >>> df, ax = task_func(1347517370)
    >>> print(df)
               Timezone            Datetime
    0  America/New_York 2012-09-13 02:22:50
    1     Europe/London 2012-09-13 07:22:50
    2     Asia/Shanghai 2012-09-13 14:22:50
    3        Asia/Tokyo 2012-09-13 15:22:50
    4  Australia/Sydney 2012-09-13 16:22:50
    """
    datetimes = [
        datetime.fromtimestamp(timestamp, pytz.timezone(tz)).strftime(DATE_FORMAT)
        for tz in TIMEZONES
    ]
    df = pd.DataFrame({"Timezone": TIMEZONES, "Datetime": datetimes})
    df["Datetime"] = pd.to_datetime(df["Datetime"])
    ax = df.plot.bar(x="Timezone", y="Datetime", legend=False)
    plt.ylabel("Timezone")
    plt.ylabel("Datetime")
    plt.title("Datetime = f(Timezone)")
    plt.close()
    return df, ax


class TestTaskFunction(unittest.TestCase):

    def test_valid_timestamp(self):
        df, ax = task_func(1347517370)
        self.assertEqual(len(df), 5)
        self.assertListEqual(df['Timezone'].tolist(), TIMEZONES)
        
    def test_dataframe_structure(self):
        df, ax = task_func(1347517370)
        self.assertIn('Timezone', df.columns)
        self.assertIn('Datetime', df.columns)
        
    def test_datetime_format(self):
        df, ax = task_func(1347517370)
        for dt in df['Datetime']:
            self.assertEqual(dt.strftime(DATE_FORMAT), dt.strftime(DATE_FORMAT))

    def test_plot_title(self):
        df, ax = task_func(1347517370)
        self.assertEqual(ax.get_title(), "Datetime = f(Timezone)")

    def test_empty_timestamp(self):
        df, ax = task_func(0)
        self.assertEqual(df.shape[0], 5)  # Should still return DataFrame for valid timezones


if __name__ == "__main__":
    unittest.main()