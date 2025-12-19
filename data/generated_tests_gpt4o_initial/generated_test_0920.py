import pandas as pd
import seaborn as sns
import unittest
import matplotlib.pyplot as plt

def task_func(data):
    """
    Draw and return a correlation matrix heatmap for a DataFrame containing numerical columns.
    The title of the heatmap is set to 'Correlation Matrix'.
    
    Parameters:
    df (pandas.DataFrame): The DataFrame containing numerical columns to be used for correlation.

    Returns:
    matplotlib.axes._axes.Axes: The matplotlib Axes object representing the heatmap.

    Requirements:
    - pandas
    - seaborn

    Example:
    >>> data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
    >>> ax = task_func(data)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>

    """
    df = pd.DataFrame(data)
    correlation_matrix = df.corr()
    ax = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    ax.set_title('Correlation Matrix')
    return ax

class TestCorrelationMatrixHeatmap(unittest.TestCase):

    def test_empty_dataframe(self):
        data = {}
        ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)

    def test_single_column_dataframe(self):
        data = {'a': [1, 2, 3]}
        ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)

    def test_two_columns_dataframe(self):
        data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
        ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)

    def test_three_columns_dataframe(self):
        data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
        ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)

    def test_highly_correlated_dataframe(self):
        data = {'a': [1, 2, 3], 'b': [2, 4, 6], 'c': [3, 6, 9]}
        ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)

if __name__ == '__main__':
    unittest.main()