import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import unittest

# Here is your prompt:
def task_func(df):
    """
    Perform exploratory data analysis on a dataframe. This function converts the 'date' column to an ordinal format,
    creates a correlation matrix, and generates a pair plot of the dataframe.

    Parameters:
        df (pandas.DataFrame): A dataframe with columns 'group', 'date', and 'value'. The 'date' column should be in datetime format.

    Returns:
        matplotlib.figure.Figure: The figure object for the correlation matrix heatmap.
        seaborn.axisgrid.PairGrid: The PairGrid object for the pair plot.

        The title of the plot is 'Correlation Matrix'. 
    Raises:
        ValueError: If the dataframe is empty, if required columns are missing, or if 'date' column is not in datetime format.

    Requirements:
        - pandas
        - matplotlib.pyplot
        - seaborn

    Example:
        >>> df = pd.DataFrame({
        ...     "group": ["A", "A", "A", "B", "B"],
        ...     "date": pd.to_datetime(["2022-01-02", "2022-01-13", "2022-02-01", "2022-02-23", "2022-03-05"]),
        ...     "value": [10, 20, 16, 31, 56],
        ... })
        >>> heatmap_fig, pairplot_grid = task_func(df)
    """

               if df.empty or not all(col in df.columns for col in ['group', 'date', 'value']):
        raise ValueError("DataFrame must be non-empty and contain 'group', 'date', and 'value' columns.")
    
    if not pd.api.types.is_datetime64_any_dtype(df['date']):
        raise ValueError("'date' column must be in datetime format.")

    try:
        df['date'] = df['date'].apply(lambda x: x.toordinal())
        df_numeric = df.drop(columns=['group'])
        correlation_matrix = df_numeric.corr()

        heatmap_fig = plt.figure(figsize=(8, 6))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
        plt.title('Correlation Matrix')

        pairplot_grid = sns.pairplot(df)

        return heatmap_fig, pairplot_grid

    except Exception as e:
        raise ValueError(f"An error occurred: {e}")

class TestTaskFunc(unittest.TestCase):
    def test_empty_dataframe(self):
        df = pd.DataFrame(columns=["group", "date", "value"])
        with self.assertRaises(ValueError) as context:
            task_func(df)
        self.assertEqual(str(context.exception), "DataFrame must be non-empty and contain 'group', 'date', and 'value' columns.")
        
    def test_missing_columns(self):
        df = pd.DataFrame({
            "group": ["A", "B"],
            "date": pd.to_datetime(["2022-01-01", "2022-01-02"]),
        })
        with self.assertRaises(ValueError) as context:
            task_func(df)
        self.assertEqual(str(context.exception), "DataFrame must be non-empty and contain 'group', 'date', and 'value' columns.")
        
    def test_invalid_date_format(self):
        df = pd.DataFrame({
            "group": ["A", "B"],
            "date": ["2022-01-01", "2022-01-02"],  # Dates are strings instead of datetime
            "value": [10, 20]
        })
        with self.assertRaises(ValueError) as context:
            task_func(df)
        self.assertEqual(str(context.exception), "'date' column must be in datetime format.")
        
    def test_valid_dataframe(self):
        df = pd.DataFrame({
            "group": ["A", "A", "B", "B"],
            "date": pd.to_datetime(["2022-01-01", "2022-01-02", "2022-01-03", "2022-01-04"]),
            "value": [10, 20, 30, 40]
        })
        heatmap_fig, pairplot_grid = task_func(df)
        self.assertIsInstance(heatmap_fig, plt.Figure)
        self.assertIsInstance(pairplot_grid, sns.axisgrid.PairGrid)

    def test_correlational_heatmap(self):
        df = pd.DataFrame({
            "group": ["A", "A", "B", "B"],
            "date": pd.to_datetime(["2022-01-01", "2022-01-02", "2022-01-03", "2022-01-04"]),
            "value": [10, 20, 30, 40]
        })
        heatmap_fig, _ = task_func(df)
        axes = heatmap_fig.get_axes()
        self.assertTrue(len(axes) > 0)  # Ensure that the heatmap has been created

if __name__ == '__main__':
    unittest.main()