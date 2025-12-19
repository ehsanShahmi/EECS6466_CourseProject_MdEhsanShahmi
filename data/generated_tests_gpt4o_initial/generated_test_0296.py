import unittest
import pandas as pd
import matplotlib.pyplot as plt

# Here is your prompt:
def task_func(df):
    """
    Draw a bar chart of the counts of each unique value in the 'value' column of a pandas DataFrame and return the Axes object.
    Empty DataFrame will return an empty bar chart.
    
    Parameters:
    df (DataFrame): The pandas DataFrame with columns ['id', 'value'].

    Returns:
    Axes: The matplotlib Axes object of the bar chart.

    Raises:
    - The function will raise a ValueError is input df is not a DataFrame.

    Note:
    - This function use "Value Distribution" for the plot title.
    - This function use "Value" and "Count" as the xlabel and ylabel respectively.

    Requirements:
    - pandas
    - matplotlib.pyplot

    Example:
    >>> df = pd.DataFrame({'id': [1, 1, 2, 2, 3, 3],'value': ['A', 'B', 'A', 'B', 'A', 'B']})
    >>> ax = task_func(df)
    >>> len(ax.patches)
    2
    >>> plt.close()
    """

           
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input df is not a DataFrame")
    
    value_counts = df['value'].value_counts()
    ax = plt.bar(value_counts.index, value_counts.values)
    plt.xlabel('Value')
    plt.ylabel('Count')
    plt.title('Value Distribution')
    return plt.gca()

class TestTaskFunc(unittest.TestCase):

    def test_valid_dataframe(self):
        df = pd.DataFrame({'id': [1, 1, 2, 2, 3, 3], 'value': ['A', 'B', 'A', 'B', 'A', 'B']})
        ax = task_func(df)
        self.assertEqual(len(ax.patches), 2)

    def test_empty_dataframe(self):
        df = pd.DataFrame(columns=['id', 'value'])
        ax = task_func(df)
        self.assertEqual(len(ax.patches), 0)

    def test_invalid_dataframe_type(self):
        with self.assertRaises(ValueError):
            task_func(None)

    def test_non_dataframe_input(self):
        with self.assertRaises(ValueError):
            task_func("not a dataframe")

    def test_dataframe_with_single_value(self):
        df = pd.DataFrame({'id': [1], 'value': ['A']})
        ax = task_func(df)
        self.assertEqual(len(ax.patches), 1)

if __name__ == '__main__':
    unittest.main()