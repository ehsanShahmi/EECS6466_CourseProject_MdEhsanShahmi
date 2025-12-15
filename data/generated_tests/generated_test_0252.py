import unittest
import matplotlib.pyplot as plt
from itertools import zip_longest


# Constants
COLORS = ['red', 'green', 'blue', 'yellow', 'purple']

def task_func(data, labels):
    """    
    Plot a list of data with different colors. If there are more data series than the predefined colors, 
    the function cycles through the colors. In case of even more series than colors + labels, 'black' is used.
    
    Parameters:
    data (list): A list of lists, each representing a series of data.
    labels (list): A list of labels for the data series.
    
    Returns:
    matplotlib.axes.Axes: The Axes object of the plot.
    """
    fig, ax = plt.subplots()
    for series, label, color in zip_longest(data, labels, COLORS, fillvalue='black'):
        ax.plot(series, label=label, color=color)
        
    ax.legend()
    return ax


class TestTaskFunc(unittest.TestCase):

    def test_plot_with_two_series(self):
        data = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
        labels = ['Series 1', 'Series 2']
        ax = task_func(data, labels)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines), 2)

    def test_plot_with_five_series(self):
        data = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]
        labels = ['Series 1', 'Series 2', 'Series 3', 'Series 4', 'Series 5']
        ax = task_func(data, labels)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines), 5)

    def test_plot_with_more_series_than_colors(self):
        data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
        labels = ['Series 1', 'Series 2', 'Series 3', 'Series 4', 'Series 5', 'Series 6']
        ax = task_func(data, labels)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines), 6)

    def test_plot_without_labels(self):
        data = [[1, 2, 3], [4, 5, 6]]
        labels = []
        ax = task_func(data, labels)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines), 2)

    def test_plot_with_empty_data(self):
        data = []
        labels = []
        ax = task_func(data, labels)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines), 0)


if __name__ == '__main__':
    unittest.main()