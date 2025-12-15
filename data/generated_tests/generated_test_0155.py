import unittest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Constants
COLUMN_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def task_func(data):
    """
    Computes the average of each row in a provided 2D array and appends these averages as a new column.
    Additionally, it plots the averages against their respective row indices.

    Parameters:
    data (numpy.array): A 2D numpy array with exactly eight columns, corresponding to 'A' through 'H'.

    Returns:
    tuple: A tuple containing:
        - DataFrame: A pandas DataFrame which includes the original data and an additional 'Average' column.
        - Axes: A matplotlib Axes object with the plot of row averages.
    """
    df = pd.DataFrame(data, columns=COLUMN_NAMES)
    df['Average'] = df.mean(axis=1)

    # Creating a new figure and axis for plotting
    fig, ax = plt.subplots()
    df['Average'].plot(ax=ax)
    ax.set_ylabel('Average')  # Setting the Y-axis label to 'Average'

    return df, ax

class TestTaskFunction(unittest.TestCase):

    def test_average_with_integers(self):
        data = np.array([[1, 2, 3, 4, 4, 3, 7, 1], [6, 2, 3, 4, 3, 4, 4, 1]])
        df, ax = task_func(data)
        expected_averages = [3.125, 3.375]
        self.assertTrue(np.allclose(df['Average'].values, expected_averages))

    def test_average_with_floats(self):
        data = np.array([[1.5, 2.5, 3.5, 4.5, 4.5, 3.5, 7.5, 1.5], [6.5, 2.5, 3.5, 4.5, 3.5, 4.5, 4.5, 1.5]])
        df, ax = task_func(data)
        expected_averages = [3.625, 3.875]
        self.assertTrue(np.allclose(df['Average'].values, expected_averages))

    def test_average_shape(self):
        data = np.array([[1, 2, 3, 4, 4, 3, 7, 1], [6, 2, 3, 4, 3, 4, 4, 1]])
        df, ax = task_func(data)
        self.assertEqual(df.shape, (2, 9))  # 2 rows + 8 original columns + 1 average column

    def test_column_names(self):
        data = np.array([[1, 2, 3, 4, 4, 3, 7, 1]])
        df, ax = task_func(data)
        self.assertListEqual(df.columns.tolist(), COLUMN_NAMES + ['Average'])

    def test_plot_axes(self):
        data = np.array([[1, 2, 3, 4, 4, 3, 7, 1], [6, 2, 3, 4, 3, 4, 4, 1]])
        df, ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)

if __name__ == '__main__':
    unittest.main()