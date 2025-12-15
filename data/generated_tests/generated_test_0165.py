import pandas as pd
import matplotlib.pyplot as plt
from random import randint
import unittest

def task_func(num_rows=5, rand_range=(0, 100)):
    """
    Create a DataFrame containing random integer values within a specified range for categories 'A' through 'E',
    and visualize this data with a stacked bar chart.

    Parameters:
    num_rows (int): Specifies the number of rows in the DataFrame.
    rand_range (tuple): Defines the lower and upper bounds for the random number generation, inclusive.

    Returns:
    matplotlib.figure.Figure: The matplotlib Figure object containing the plotted data.

    Requirements:
    - pandas
    - matplotlib
    - random

    Example:
    >>> fig = task_func(num_rows=3, rand_range=(10, 50))
    >>> type(fig)
    <class 'matplotlib.figure.Figure'>
    """

    labels = ['A', 'B', 'C', 'D', 'E']
    data = pd.DataFrame({label: [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)] for label in labels})

    fig, ax = plt.subplots()

    data.plot(kind='bar', stacked=True, ax=ax)

    return fig

class TestTaskFunc(unittest.TestCase):

    def test_return_type(self):
        fig = task_func(num_rows=3, rand_range=(10, 50))
        self.assertIsInstance(fig, plt.Figure)

    def test_dataframe_shape(self):
        num_rows = 4
        fig = task_func(num_rows=num_rows, rand_range=(0, 100))
        data = fig.axes[0].containers[0].get_array()
        self.assertEqual(data.shape[0], num_rows)
        self.assertEqual(data.shape[1], 5)  # There are 5 categories A to E

    def test_random_range(self):
        rand_range = (10, 20)
        num_rows = 5
        fig = task_func(num_rows=num_rows, rand_range=rand_range)
        for bar_container in fig.axes[0].containers:
            for value in bar_container.get_array():
                self.assertGreaterEqual(value, rand_range[0])
                self.assertLessEqual(value, rand_range[1])

    def test_visualization_created(self):
        fig = task_func(num_rows=2, rand_range=(0, 50))
        self.assertIsNotNone(fig.axes)
        self.assertGreater(len(fig.axes), 0)

    def test_default_parameters(self):
        fig = task_func()
        self.assertIsInstance(fig, plt.Figure)
        data = fig.axes[0].containers[0].get_array()
        self.assertEqual(data.shape[0], 5)  # Default is 5 rows
        self.assertEqual(data.shape[1], 5)  # 5 categories A to E

if __name__ == '__main__':
    unittest.main()