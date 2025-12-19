import unittest
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
import sys

# Here is your prompt:
def task_func(data):
    """
    Combine a list of dictionaries with the same keys (fruit names) into a single pandas dataframe
    where NA/NaN values are filled with 0, then generate a line chart of sales.
    The chart should have title 'Fruit Sales over Time', x-axis 'Time', and y-axis 'Sales Quantity'.

    Parameters:
    - data (list): A list of dictionaries. Each element corresponds to sales quantities at a point in time,
                   where keys are fruit names (str) and values are sales quantities (int). If values
                   are not the expected type, this function raises TypeError.

    Returns:
    - matplotlib.axes._axes.Axes: The generated plot's Axes object.
    
    Requirements:
    - pandas
    - matplotlib.pyplot
    """

    df = pd.DataFrame(data)
    df.fillna(0, inplace=True)
    for fruit in df.columns:
        plt.plot(df[fruit], label=fruit)
    plt.xlabel("Time")
    plt.ylabel("Sales Quantity")
    plt.title("Fruit Sales over Time")
    plt.legend()
    return plt.gca()

class TestTaskFunc(unittest.TestCase):

    def test_single_record(self):
        """Test with a single record of fruit sales."""
        data = [{'apple': 10, 'banana': 15, 'cherry': 12, 'durian': 0}]
        ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)

    def test_multiple_records(self):
        """Test with multiple records of fruit sales."""
        data = [{'apple': 10, 'banana': 15, 'cherry': 12}, 
                {'apple': 12, 'banana': 20, 'cherry': 14}]
        ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)

    def test_nan_values(self):
        """Test with NaN values in the data."""
        data = [{'apple': None, 'banana': 20, 'cherry': None}, 
                {'apple': 25, 'banana': None, 'cherry': 10}]
        ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)

    def test_invalid_data_type(self):
        """Test with invalid data types."""
        data = [{'apple': 10, 'banana': 'fifteen', 'cherry': 12}]
        with self.assertRaises(TypeError):
            task_func(data)

    def test_empty_data(self):
        """Test with empty data."""
        data = []
        ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)

if __name__ == "__main__":
    unittest.main(argv=sys.argv)