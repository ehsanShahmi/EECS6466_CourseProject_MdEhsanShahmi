import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import unittest
from matplotlib.axes import Axes

def task_func(start_date, end_date, seed=42):
    """
    Generate random sales data for each day between a start and end date, inclusive.
    Returns the data and a plot of sales over time.

    Parameters:
    start_date (datetime): The start date.
    end_date (datetime): The end date.
    seed (int): Seed for the random number generator. Default is 42.

    Returns:
    DataFrame: A pandas DataFrame with columns 'Date' and 'Sales'.
    Axes: A matplotlib Axes object of the plot showing the sales overtime.
    
    sales ranges 0 to 500 and it is an integer

    Requirements:
    - numpy
    - pandas
    - datetime

    Example:
    >>> start_date = datetime(2021, 1, 1)
    >>> end_date = datetime(2021, 12, 31)
    >>> data, plot = task_func(start_date, end_date)
    >>> print(data.head())
            Date  Sales
    0 2021-01-01    102
    1 2021-01-02    435
    2 2021-01-03    348
    3 2021-01-04    270
    4 2021-01-05    106
    """

    np.random.seed(seed)
    data = []
    date = start_date

    while date <= end_date:
        sales = np.random.randint(0, 500)
        data.append([date, sales])
        date += timedelta(days=1)

    df = pd.DataFrame(data, columns=["Date", "Sales"])
    ax = df.plot(x='Date', y='Sales')
    ax.set_ylabel("Sales")

    return df, ax

class TestTaskFunc(unittest.TestCase):

    def test_data_shape(self):
        start_date = datetime(2022, 1, 1)
        end_date = datetime(2022, 1, 10)
        data, _ = task_func(start_date, end_date)
        self.assertEqual(data.shape[0], (end_date - start_date).days + 1)
        self.assertEqual(data.shape[1], 2)

    def test_sales_range(self):
        start_date = datetime(2022, 1, 1)
        end_date = datetime(2022, 1, 10)
        data, _ = task_func(start_date, end_date)
        self.assertTrue((data['Sales'] >= 0).all() and (data['Sales'] < 500).all())

    def test_date_column(self):
        start_date = datetime(2022, 1, 1)
        end_date = datetime(2022, 1, 10)
        data, _ = task_func(start_date, end_date)
        expected_dates = pd.date_range(start=start_date, end=end_date, freq='D')
        pd.testing.assert_series_equal(data['Date'], pd.Series(expected_dates))

    def test_plot_return_type(self):
        start_date = datetime(2022, 1, 1)
        end_date = datetime(2022, 1, 10)
        _, plot = task_func(start_date, end_date)
        self.assertIsInstance(plot, Axes)

    def test_inconsistent_dates(self):
        start_date = datetime(2022, 1, 10)
        end_date = datetime(2022, 1, 1)
        with self.assertRaises(ValueError):
            task_func(start_date, end_date)

if __name__ == "__main__":
    unittest.main()