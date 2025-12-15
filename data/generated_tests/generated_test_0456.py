import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
import unittest

# Here is your prompt:
def task_func(data: pd.DataFrame) -> (pd.DataFrame, plt.Axes):
    """
    Normalize the data and visualize it using a heatmap.

    This function takes a pandas DataFrame, normalizes the data to a range [0, 1], and then visualizes this
    normalized data using a seaborn heatmap.  The heatmap uses the "YlGnBu" colormap to represent normalized
    values and includes a color bar labeled "Normalized Value" to indicate the range of data values.
    It returns both the normalized data and the heatmap plot.

    Parameters:
    - data (pd.DataFrame): The input data with multiple features in columns.

    Returns:
    - pd.DataFrame: Normalized data.
    - plt.Axes: Heatmap plot of the normalized data.

    Requirements:
    - pandas
    - numpy
    - matplotlib.pyplot
    - seaborn
    
    Example:
    >>> df = pd.DataFrame([[1,1,1], [2,2,2], [3,3,3]], columns=['Feature1', 'Feature2', 'Feature3'])
    >>> normalized_df, _ = task_func(df)
    >>> type(normalized_df)
    <class 'pandas.core.frame.DataFrame'>
    >>> normalized_df['Feature1'].iloc[0]  # Returns a normalized value between 0 and 1
    0.0
    """

    # Normalizing the data
    scaler = MinMaxScaler()
    normalized_data = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)

    # Plotting heatmap
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(
        normalized_data, cmap="YlGnBu", cbar_kws={"label": "Normalized Value"}
    )

    return normalized_data, ax


class TestTaskFunc(unittest.TestCase):

    def test_normalization_range(self):
        df = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['A', 'B'])
        normalized_df, _ = task_func(df)
        self.assertTrue((normalized_df.min() >= 0).all())
        self.assertTrue((normalized_df.max() <= 1).all())

    def test_shape_of_normalized_output(self):
        df = pd.DataFrame([[10, 20], [30, 40], [50, 60]], columns=['X', 'Y'])
        normalized_df, _ = task_func(df)
        self.assertEqual(normalized_df.shape, df.shape)

    def test_column_names_preserved(self):
        df = pd.DataFrame([[5, 10], [15, 20]], columns=['Feature_A', 'Feature_B'])
        normalized_df, _ = task_func(df)
        self.assertListEqual(normalized_df.columns.tolist(), df.columns.tolist())

    def test_heatmap_axes(self):
        df = pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])
        _, ax = task_func(df)
        self.assertIsInstance(ax, plt.Axes)

    def test_empty_dataframe(self):
        df = pd.DataFrame(columns=['A', 'B'])
        normalized_df, _ = task_func(df)
        self.assertTrue(normalized_df.empty)

        
if __name__ == '__main__':
    unittest.main()