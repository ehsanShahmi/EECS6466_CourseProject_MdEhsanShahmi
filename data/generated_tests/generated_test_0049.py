from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import unittest

# Constants
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Provided function (for context, do not modify)
def task_func(timestamps):
    """
    Convert a list of Unix timestamps to date objects, create a Pandas DataFrame, and draw a histogram.
    - The date format should be as DATE_FORMAT.
    - The DataFrame should have 'Timestamp' and 'Datetime' as column names.
    - If the list of timestamps is empty, raise a ValueError with the message "Input list of timestamps is empty".

    Parameters:
    - timestamps (list): The list of Unix timestamps.

    Returns:
    - pandas.DataFrame: A pandas DataFrame containing the original Unix timestamps and the converted datetime objects.
    - Axes: The Axes object of the histogram plot. The histogram will have 10 bins by default, representing the distribution of the datetime objects.

    Raises:
    - ValueError("Input list of timestamps is empty."): If the list of timestamps is empty.

    Requirements:
    - datetime
    - pandas
    - matplotlib.pyplot

    Examples:
    >>> df, ax = task_func([1347517370, 1475153730, 1602737300])
    >>> print(df)
        Timestamp             Datetime
    0  1347517370  2012-09-13 02:22:50
    1  1475153730  2016-09-29 08:55:30
    2  1602737300  2020-10-15 00:48:20
    """
    if not timestamps:
        raise ValueError("Input list of timestamps is empty.")
    datetimes = [datetime.fromtimestamp(t).strftime(DATE_FORMAT) for t in timestamps]
    df = pd.DataFrame({"Timestamp": timestamps, "Datetime": datetimes})
    ax = plt.hist(pd.to_datetime(df["Datetime"]))
    plt.close()
    return df, ax

class TestTaskFunc(unittest.TestCase):

    def test_empty_timestamps(self):
        with self.assertRaises(ValueError) as context:
            task_func([])
        self.assertEqual(str(context.exception), "Input list of timestamps is empty.")

    def test_single_timestamp(self):
        df, _ = task_func([1347517370])
        expected_df = pd.DataFrame({
            "Timestamp": [1347517370],
            "Datetime": [datetime.fromtimestamp(1347517370).strftime(DATE_FORMAT)]
        })
        pd.testing.assert_frame_equal(df, expected_df)

    def test_multiple_timestamps(self):
        timestamps = [1347517370, 1475153730, 1602737300]
        df, _ = task_func(timestamps)
        expected_df = pd.DataFrame({
            "Timestamp": timestamps,
            "Datetime": [
                datetime.fromtimestamp(1347517370).strftime(DATE_FORMAT),
                datetime.fromtimestamp(1475153730).strftime(DATE_FORMAT),
                datetime.fromtimestamp(1602737300).strftime(DATE_FORMAT)
            ]
        })
        pd.testing.assert_frame_equal(df, expected_df)

    def test_histogram_output(self):
        _, ax = task_func([1347517370, 1475153730, 1602737300])
        self.assertIsNotNone(ax)

    def test_correct_bins_in_histogram(self):
        _, ax = task_func([1347517370, 1475153730, 1602737300])
        self.assertEqual(len(ax[0]), 10)  # Default number of bins should be 10

if __name__ == '__main__':
    unittest.main()