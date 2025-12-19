import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import unittest

# Here is your prompt:
def task_func(num_labels=5, data_range=(0, 1)):
    """
    Generate random numeric data across a specified range for a given number of categories and visualize it with
     a stacked bar chart.

    Parameters:
    num_labels (int): Specifies the number of distinct categories or labels to generate data for. Defaults to 5.
    data_range (tuple): Defines the lower and upper bounds for the random data values. Defaults to (0, 1).

    Returns:
    matplotlib.figure.Figure: A Figure object containing the stacked bar chart of the generated data.

    Requirements:
    - pandas
    - matplotlib
    - numpy

    Example:
    >>> fig = task_func()
    >>> fig.show()  # This will display the figure with default parameters

    >>> fig = task_func(num_labels=3, data_range=(1, 10))
    >>> fig.show()  # This will display the figure with three labels and data range from 1 to 10
    """

    np.random.seed(0)
    columns = [f'Label{i + 1}' for i in range(num_labels)]
    data = pd.DataFrame(np.random.uniform(data_range[0], data_range[1], size=(num_labels, num_labels)), columns=columns)

    fig, ax = plt.subplots()

    data.plot(kind='bar', stacked=True, ax=ax)

    return fig

class TestTaskFunction(unittest.TestCase):

    def test_default_parameters(self):
        fig = task_func()
        self.assertIsInstance(fig, plt.Figure)

    def test_number_of_bars(self):
        num_labels = 4
        fig = task_func(num_labels=num_labels)
        ax = fig.get_axes()[0]
        bars = ax.patches
        self.assertEqual(len(bars), num_labels * (num_labels + 1) / 2)

    def test_data_range(self):
        fig = task_func(num_labels=5, data_range=(1, 10))
        ax = fig.get_axes()[0]
        for bar in ax.patches:
            self.assertTrue(1 <= bar.get_height() <= 10)

    def test_invalid_num_labels(self):
        with self.assertRaises(ValueError):
            task_func(num_labels=-1)

    def test_invalid_data_range(self):
        with self.assertRaises(ValueError):
            task_func(data_range=(1, -1))


if __name__ == '__main__':
    unittest.main()