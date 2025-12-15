import pandas as pd
import numpy as np
import unittest

# Here is your prompt:
def task_func(df):
    """
    Draw and return the daily turnover line chart from a pandas DataFrame.

    Parameters:
    df (DataFrame): A pandas DataFrame with 'Date' and 'Sales' columns.

    Returns:
    Axes: Matplotlib Axes object with the line chart.

    Raises:
    ValueError: If 'df' is not a DataFrame or lacks 'Date' or 'Sales' columns, or has no data to plot.

    Requirements:
    - pandas
    - matplotlib.pyplot

    Example:
    >>> df = pd.DataFrame({
    ...     'Date': pd.date_range(start='1/1/2021', end='12/31/2021'),
    ...     'Sales': np.random.randint(100, 2000, size=365)
    ... })
    >>> ax = task_func(df)
    >>> ax.get_title()  # Expected: 'Daily Turnover'
    'Daily Turnover'
    >>> ax.get_ylabel()  # Expected: 'Sales'
    'Sales'
    """

    if not isinstance(df, pd.DataFrame) or not all(col in df.columns for col in ['Date', 'Sales']):
        raise ValueError("Invalid 'df': must be a DataFrame with 'Date' and 'Sales' columns.")

    df['Date'] = pd.to_datetime(df['Date'])
    df = df.set_index('Date')
    resampled_df = df.resample('D').sum()

    if resampled_df.empty or resampled_df['Sales'].sum() == 0:
        raise ValueError("No data available to plot after resampling.")

    ax = resampled_df.plot(y='Sales')
    ax.set_title('Daily Turnover')
    ax.set_ylabel('Sales')
    plt.show()
    return ax

class TestTaskFunc(unittest.TestCase):

    def test_valid_dataframe(self):
        df = pd.DataFrame({
            'Date': pd.date_range(start='1/1/2021', end='1/10/2021'),
            'Sales': np.random.randint(100, 2000, size=10)
        })
        ax = task_func(df)
        self.assertEqual(ax.get_title(), 'Daily Turnover')
        self.assertEqual(ax.get_ylabel(), 'Sales')

    def test_no_data(self):
        df = pd.DataFrame({'Date': [], 'Sales': []})
        with self.assertRaises(ValueError) as context:
            task_func(df)
        self.assertEqual(str(context.exception), "No data available to plot after resampling.")

    def test_missing_columns(self):
        df = pd.DataFrame({
            'Date': pd.date_range(start='1/1/2021', end='1/10/2021'),
            'OtherColumn': np.random.randint(100, 2000, size=10)
        })
        with self.assertRaises(ValueError) as context:
            task_func(df)
        self.assertEqual(str(context.exception), "Invalid 'df': must be a DataFrame with 'Date' and 'Sales' columns.")

    def test_invalid_dataframe_type(self):
        df = "This is not a DataFrame"
        with self.assertRaises(ValueError) as context:
            task_func(df)
        self.assertEqual(str(context.exception), "Invalid 'df': must be a DataFrame with 'Date' and 'Sales' columns.")

    def test_zero_sales(self):
        df = pd.DataFrame({
            'Date': pd.date_range(start='1/1/2021', end='1/5/2021'),
            'Sales': [0, 0, 0, 0, 0]
        })
        with self.assertRaises(ValueError) as context:
            task_func(df)
        self.assertEqual(str(context.exception), "No data available to plot after resampling.")

if __name__ == '__main__':
    unittest.main()