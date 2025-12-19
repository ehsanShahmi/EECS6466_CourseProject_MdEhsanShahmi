import unittest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime

# Here is your prompt:
def task_func(start_time, end_time, step, amplitude, period, seed=0):
    """
    Generate a time series with a given seasonality from the start UTC time to the end UTC time
    with a given step, and plot the time series with the seasonality.

    Parameters:
    - start_time (int): The start epoch time in milliseconds.
    = end_time (int): The end epoch time in milliseconds.
    - step (int): The step in milliseconds between each data point. Must be at least 1.
    - amplitude (float): The amplitude of the seasonality.
    - period (int): The period of the seasonality in milliseconds. Must be at least 0.
    - seed (int): Random seed for reproducibility. Defaults to 0.

    Returns:
    matplotlib.pyplot.Axes: A plot of the generated 'Time Series with Seasonality',
              with 'Timestamp' on x-axis and 'Value' on y-axis.

    Requirements:
    - datetime.datetime
    - pandas
    - numpy
    """

    np.random.seed(seed)

    if period <= 0 or step < 1:
        raise ValueError("Invalid input values")

    COLUMNS = ["Timestamp", "Value"]

    timestamps = np.arange(start_time, end_time, step)
    df = pd.DataFrame(columns=COLUMNS)

    if amplitude == 0:
        values = [0] * len(timestamps)
    else:
        values = np.random.normal(size=len(timestamps))

    data = []
    for i, ts in enumerate(timestamps):
        dt = datetime.utcfromtimestamp(ts / 1000).strftime("%Y-%m-%d %H:%M:%S.%f")
        value = values[i] + amplitude * np.sin(2 * np.pi * ts / period)
        data.append([dt, value])

    df = pd.DataFrame(data, columns=COLUMNS)

    ax = df.plot(x="Timestamp", y="Value", title="Time Series with Seasonality")
    ax.set_ylabel("Value")
    return ax


class TestTaskFunc(unittest.TestCase):
    
    def test_output_type(self):
        """Test if the output is of type matplotlib.axes.Axes"""
        ax = task_func(0, 10000, 100, 1, 1000)
        self.assertIsInstance(ax, plt.Axes)

    def test_empty_data(self):
        """Test for a case where the amplitude is zero, ensuring all values are zero."""
        ax = task_func(0, 10000, 100, 0, 1000)
        data = ax.lines[0].get_ydata()
        np.testing.assert_array_equal(data, np.zeros(len(data)))

    def test_invalid_step(self):
        """Test that ValueError is raised for invalid step."""
        with self.assertRaises(ValueError):
            task_func(0, 10000, 0, 1, 1000)

    def test_invalid_period(self):
        """Test that ValueError is raised for invalid period."""
        with self.assertRaises(ValueError):
            task_func(0, 10000, 100, 1, -1)

    def test_timestamps_correctness(self):
        """Test if the timestamps generated are correct."""
        start_time = 0
        end_time = 10000
        step = 100
        ax = task_func(start_time, end_time, step, 1, 1000)
        timestamps = [datetime.utcfromtimestamp(ts / 1000).strftime("%Y-%m-%d %H:%M:%S.%f") 
                      for ts in range(start_time, end_time, step)]
        self.assertEqual(len(ax.lines[0].get_xdata()), len(timestamps))


if __name__ == '__main__':
    unittest.main()