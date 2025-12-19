import unittest
import matplotlib.pyplot as plt
import pandas as pd

# Provided Prompt
def task_func(d, keys=['x', 'y', 'z']):
    """
    Plot values from a list of dictionaries based on specified keys and return the plot as a Matplotlib Axes object.
    
    Parameters:
    d (list): A list of dictionaries containing numerical data.
    keys (list, optional): A list of string keys to plot. Defaults to ['x', 'y', 'z'].

    Returns:
    Matplotlib Axes object: The plot showing the values of specified keys from the input list of dictionaries.

    Requirements:
    - pandas
    - matplotlib.pyplot

    Example:
    >>> data = [{'x': 1, 'y': 10, 'z': 5}, {'x': 3, 'y': 15, 'z': 6}, {'x': 2, 'y': 1, 'z': 7}]
    >>> ax = task_func(data)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>

    >>> ax = task_func(data, keys=['x', 'y'])
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """

    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(d)

    # Initialize a plot
    fig, ax = plt.subplots()
    
    # Plot the values for the specified keys
    plotted_keys = []
    for key in keys:
        if key in df.columns:
            ax.plot(df[key], label=key)
            plotted_keys.append(key)
    
    # Add a legend if there are any lines plotted
    if plotted_keys:
        ax.legend()
    
    # Return the Axes object
    return ax

class TestTaskFunc(unittest.TestCase):

    def test_with_default_keys(self):
        data = [{'x': 1, 'y': 10, 'z': 5}, {'x': 3, 'y': 15, 'z': 6}, {'x': 2, 'y': 1, 'z': 7}]
        ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.get_lines()), 3)  # x, y, z should be three lines

    def test_with_partial_keys(self):
        data = [{'x': 1, 'y': 10}, {'x': 3, 'y': 15}, {'x': 2, 'y': 1}]
        ax = task_func(data, keys=['x', 'y'])
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.get_lines()), 2)  # x and y should be two lines

    def test_with_no_keys(self):
        data = [{'x': 1, 'y': 10}, {'x': 3, 'y': 15}, {'x': 2, 'y': 1}]
        ax = task_func(data, keys=[])
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.get_lines()), 0)  # no lines should be plotted

    def test_with_missing_key(self):
        data = [{'x': 1, 'z': 5}, {'x': 3, 'z': 6}, {'x': 2, 'z': 7}]
        ax = task_func(data, keys=['x', 'y'])
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.get_lines()), 1)  # only x should be plotted

    def test_empty_data(self):
        data = []
        ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.get_lines()), 0)  # no lines should be plotted

if __name__ == '__main__':
    unittest.main()