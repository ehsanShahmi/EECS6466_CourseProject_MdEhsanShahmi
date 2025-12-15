import pandas as pd
import matplotlib.pyplot as plt
import unittest
import os

# Here is your prompt:
def task_func(csv_file_path: str):
    """
    This function reads data from a CSV file, normalizes a specific column named 'column1', and then plots the normalized data.

    - The title is created using Python's string formatting, aligning 'Plot Title' and 'Normalized Column 1' on either side of a 
    colon, each padded to 20 characters.
    - Similarly, the x-label is formatted with 'Index' and 'Normalized Value' on either side of a colon, 
    each padded to 20 characters.
    - The y-label is set in the same manner, with 'Frequency' and 'Normalized Value' on either side of a colon.

    Parameters:
    - csv_file_path (str): Path to the CSV file. The file must contain a column named 'column1'.

    Returns:
    - The matplotlib.axes.Axes object with the plot of the normalized data.

    Requirements:
    - pandas
    - matplotlib

    Example:
    >>> ax = task_func('data.csv')
    >>> ax.get_title()
    "          Plot Title :  Normalized Column 1"
    """

    df = pd.read_csv(csv_file_path)
    mean = df["column1"].mean()
    std = df["column1"].std()
    df["column1_normalized"] = (df["column1"] - mean) / std

    # Creating a figure and axes
    _, ax = plt.subplots()
    # Plotting on the created axes
    ax.plot(df["column1_normalized"])
    title = "%*s : %*s" % (20, "Plot Title", 20, "Normalized Column 1")
    xlabel = "%*s : %*s" % (20, "Index", 20, "Normalized Value")
    ylabel = "%*s : %*s" % (20, "Frequency", 20, "Normalized Value")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # Return the axes object for further manipulation
    return ax

class TestTaskFunc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a temporary CSV file for testing
        cls.test_csv = 'test_data.csv'
        data = {
            'column1': [10, 20, 30, 40, 50]
        }
        df = pd.DataFrame(data)
        df.to_csv(cls.test_csv, index=False)

    @classmethod
    def tearDownClass(cls):
        # Remove the temporary CSV file after tests
        if os.path.exists(cls.test_csv):
            os.remove(cls.test_csv)

    def test_plot_title(self):
        ax = task_func(self.test_csv)
        expected_title = "                    Plot Title :      Normalized Column 1"
        self.assertEqual(ax.get_title(), expected_title)

    def test_x_label(self):
        ax = task_func(self.test_csv)
        expected_xlabel = "                Index :         Normalized Value"
        self.assertEqual(ax.xaxis.get_label_text(), expected_xlabel)

    def test_y_label(self):
        ax = task_func(self.test_csv)
        expected_ylabel = "            Frequency :         Normalized Value"
        self.assertEqual(ax.yaxis.get_label_text(), expected_ylabel)

    def test_normalization(self):
        ax = task_func(self.test_csv)
        df = pd.read_csv(self.test_csv)
        normalized_values = (df['column1'] - df['column1'].mean()) / df['column1'].std()
        plotted_values = ax.lines[0].get_ydata()
        self.assertTrue((plotted_values == normalized_values.tolist()).all())

    def test_data_frame_exists(self):
        df = pd.read_csv(self.test_csv)
        self.assertIn('column1', df.columns)

if __name__ == '__main__':
    unittest.main()