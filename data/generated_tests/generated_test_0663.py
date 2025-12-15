import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import unittest

def task_func(x, y, labels):
    """
    Fit an exponential curve to given data points and plot the curves with labels.
    It fits an exponential curve of the form: f(x) = a * exp(-b * x) + c
    to the provided x and y data points for each set of data and plots the fitted curves
    with the corresponding labels on a single matplotlib figure.

    Parameters:
    - x (list of np.ndarray): List of numpy arrays, each representing the x-values of the data points for a dataset.
    - y (list of np.ndarray): List of numpy arrays, each representing the y-values of the data points for a dataset.
    - labels (list of str): List of strings, each representing the label for a dataset.

    Returns:
    - matplotlib.figure.Figure: The figure object that contains the plotted curves.

    Requirements:
    - numpy
    - scipy.optimize
    """

    if not x or not y or not labels:
        raise ValueError("Empty data lists provided.")

    def exponential_func(x, a, b, c):
        """Exponential function model for curve fitting."""
        return a * np.exp(-b * x) + c

    fig, ax = plt.subplots()

    for i in range(len(x)):
        # Fit the exponential model to the data
        popt, _ = curve_fit(exponential_func, x[i], y[i])

        # Plot the fitted curve
        ax.plot(x[i], exponential_func(x[i], *popt), label=labels[i])

    ax.legend()

    return fig

class TestTaskFunction(unittest.TestCase):
    def test_empty_data_lists(self):
        """Test that ValueError is raised with empty input lists."""
        with self.assertRaises(ValueError):
            task_func([], [], [])

    def test_single_dataset(self):
        """Test with a single dataset for correct curve fitting and labels."""
        x_data = [np.array([1, 2, 3])]
        y_data = [np.array([1, 2, 1.5])]
        labels = ['Dataset 1']
        fig = task_func(x_data, y_data, labels)
        self.assertIsNotNone(fig)

    def test_multiple_datasets(self):
        """Test with multiple datasets for correct curve fitting and labels."""
        x_data = [np.array([1, 2, 3]), np.array([1, 4, 6])]
        y_data = [np.array([1, 0.5, 0.1]), np.array([2, 1, 0.5])]
        labels = ['Dataset 1', 'Dataset 2']
        fig = task_func(x_data, y_data, labels)
        self.assertIsNotNone(fig)

    def test_inconsistent_input_lengths(self):
        """Test that ValueError is raised with inconsistent lengths of x, y, and labels."""
        x_data = [np.array([1, 2]), np.array([1, 3, 5])]
        y_data = [np.array([1, 0.5])]
        labels = ['Dataset 1']
        with self.assertRaises(ValueError):
            task_func(x_data, y_data, labels)

    def test_plot_labels(self):
        """Test if the correct labels are on the plot."""
        x_data = [np.array([1, 2, 3])]
        y_data = [np.array([2, 3, 4])]
        labels = ['Test Curve']
        fig = task_func(x_data, y_data, labels)
        ax = fig.gca()
        self.assertIn('Test Curve', [text.get_text() for text in ax.get_legend().get_texts()])

if __name__ == '__main__':
    unittest.main()