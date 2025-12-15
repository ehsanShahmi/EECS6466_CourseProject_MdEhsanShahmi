import os
import pandas as pd
import numpy as np
import unittest
from unittest.mock import patch

# Here is your prompt:

def task_func(file_path: str, plot_path: str) -> (float, float, str):
    """
    Processes a CSV file at the given path by reading its contents, cleaning the data,
    performing statistical analysis, and generating a plot, which is saved to the specified path.

    Sets the title of the plot to "Data Visualization".
    Labels the x-axis as "Index" and the y-axis as "Value".
    Saves the generated plot to the file path specified in 'plot_path'.

    Parameters:
    - file_path (str): Path to the CSV input file.
    - plot_path (str): Path where the plot will be saved.

    Returns:
    - tuple: A tuple containing the following elements:
        - Mean (float): The average value of the data. Returns NaN if data is empty or non-numeric.
        - Median (float): The middle value of the data when sorted. Returns NaN if data is empty or non-numeric.
        - Plot Path (str): The path where the plot is saved.

    Raises:
    - FileNotFoundError: If the CSV file at 'file_path' does not exist.

    Requirements:
    - os
    - pandas
    - matplotlib
    - numpy

    Example:
    >>> task_func("sample_data.csv", "output_plot.png")
    (25.5, 23.0, "output_plot.png")
    """

               # Check if file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist.")

    # Load data and handle empty file
    try:
        data = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        return np.nan, np.nan, plot_path

    # Convert data to numeric, coerce errors to NaN
    data = pd.to_numeric(data.squeeze(), errors="coerce")

    # Ensure data is a Pandas Series
    if not isinstance(data, pd.Series):
        data = pd.Series(data)

    # Clean data
    data = data.dropna()

    # Perform analysis
    if data.empty:
        mean = median = np.nan
    else:
        # Calculate mean and median
        mean = float(np.mean(data))
        median = float(np.median(data))

    # Create plot and save it
    plt.figure(figsize=(10, 6))
    plt.plot(data)
    plt.title("Data Visualization")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.savefig(plot_path)
    plt.close()

    return mean, median, plot_path

# Test Suite
class TestTaskFunc(unittest.TestCase):

    @patch("os.path.isfile", return_value=True)
    @patch("pandas.read_csv")
    def test_mean_and_median(self, mock_read_csv, mock_isfile):
        mock_read_csv.return_value = pd.DataFrame([1, 2, 3, 4, 5])
        mean, median, plot_path = task_func("dummy.csv", "output_plot.png")
        self.assertAlmostEqual(mean, 3.0)
        self.assertEqual(median, 3.0)
        self.assertEqual(plot_path, "output_plot.png")

    @patch("os.path.isfile", return_value=True)
    @patch("pandas.read_csv")
    def test_empty_file(self, mock_read_csv, mock_isfile):
        mock_read_csv.side_effect = pd.errors.EmptyDataError
        mean, median, plot_path = task_func("dummy.csv", "output_plot.png")
        self.assertTrue(np.isnan(mean))
        self.assertTrue(np.isnan(median))
        self.assertEqual(plot_path, "output_plot.png")

    @patch("os.path.isfile", return_value=False)
    def test_file_not_found(self, mock_isfile):
        with self.assertRaises(FileNotFoundError):
            task_func("non_existent.csv", "output_plot.png")

    @patch("os.path.isfile", return_value=True)
    @patch("pandas.read_csv")
    def test_non_numeric_data(self, mock_read_csv, mock_isfile):
        mock_read_csv.return_value = pd.DataFrame(["a", "b", "c"])
        mean, median, plot_path = task_func("dummy.csv", "output_plot.png")
        self.assertTrue(np.isnan(mean))
        self.assertTrue(np.isnan(median))
        self.assertEqual(plot_path, "output_plot.png")

    @patch("os.path.isfile", return_value=True)
    @patch("pandas.read_csv")
    @patch("matplotlib.pyplot.savefig")
    def test_plot_saved(self, mock_savefig, mock_read_csv, mock_isfile):
        mock_read_csv.return_value = pd.DataFrame([1, 2, 3])
        task_func("dummy.csv", "output_plot.png")
        mock_savefig.assert_called_once_with("output_plot.png")

if __name__ == "__main__":
    unittest.main()