import pandas as pd
import matplotlib.pyplot as plt
import unittest

# Here is your prompt:

def task_func(df, bins=20):
    """
    Draw a histogram of the last column of the DataFrame and return the plot.

    Parameters:
    - df (DataFrame): The input DataFrame, which must contain at least one column.
    - bins (int, optional): Number of bins for the histogram. Defaults to 20.

    Returns:
    - Axes: A Matplotlib Axes object representing the histogram of the last column. The histogram includes:
      - Title: 'Histogram of ' followed by the name of the last column.
      - X-axis label: 'Value'
      - Y-axis label: 'Frequency'

    Raises:
    - ValueError: If the input is not a DataFrame, or if the DataFrame is empty.

    Requirements:
    - pandas
    - matplotlib.pyplot

    Example:
    >>> df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
    >>> ax = task_func(df)
    >>> plt.show()
    """
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("The input must be a non-empty pandas DataFrame.")

    last_col_name = df.columns[-1]
    fig, ax = plt.subplots()
    ax.hist(df[last_col_name], bins=bins)
    ax.set_title(f'Histogram of {last_col_name}')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    plt.show()
    return ax


class TestTaskFunc(unittest.TestCase):

    def test_valid_dataframe(self):
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        ax = task_func(df)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), 'Histogram of C')
    
    def test_empty_dataframe(self):
        df = pd.DataFrame()
        with self.assertRaises(ValueError) as context:
            task_func(df)
        self.assertEqual(str(context.exception), "The input must be a non-empty pandas DataFrame.")
    
    def test_non_dataframe_input(self):
        with self.assertRaises(ValueError) as context:
            task_func("not a dataframe")
        self.assertEqual(str(context.exception), "The input must be a non-empty pandas DataFrame.")
    
    def test_histogram_bins(self):
        df = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
        ax = task_func(df, bins=5)
        # Check if the histogram has the right number of bins
        self.assertEqual(len(ax.patches), 5)
    
    def test_histogram_labels(self):
        df = pd.DataFrame({'A': [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]})
        ax = task_func(df)
        self.assertEqual(ax.get_xlabel(), 'Value')
        self.assertEqual(ax.get_ylabel(), 'Frequency')

if __name__ == '__main__':
    unittest.main()