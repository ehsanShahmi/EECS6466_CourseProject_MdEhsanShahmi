import unittest
import pandas as pd
import seaborn as sns
from scipy.stats import chi2_contingency

# Here is your prompt:
def task_func(df1, df2, column1="feature1", column2="feature2"):
    """
    Merge two dataframes based on the 'id' column, perform a chi-square independence test on the merged dataframe,
    and draw a heatmap of the contingency table created from the features in column1, column2.

    Parameters:
    - df1 (DataFrame): Left dataframe to merge. Must contain columns 'id' and one matching column1.
    - df2 (DataFrame): Right dataframe to merge from. Must contain columns 'id' and one matching column2.
    - column1   (str): Name of column containing features in df1. Defaults to 'feature1'.
    - column2   (str): Name of column containing features in df2. Defaults to 'feature2'.

    Returns:
    tuple: A tuple containing:
        - p (float): The p-value of the Chi-Squared test.
        - heatmap (matplotlib.pyplot.Axes): Seaborn heatmap of the contingency table.

    Requirements:
    - seaborn
    - scipy.stats.chi2_contingency

    Example:
    >>> import pandas as pd
    >>> df1 = pd.DataFrame({'id': [1, 2, 3], 'feature1': ['A', 'B', 'A']})
    >>> df2 = pd.DataFrame({'id': [1, 2, 3], 'feature2': ['X', 'Y', 'X']})
    >>> p_value, heatmap = task_func(df1, df2)
    >>> p_value
    0.6650055421020291
    >>> heatmap
    <Axes: xlabel='feature2', ylabel='feature1'>
    """
    df = pd.merge(df1, df2, on="id")
    contingency_table = pd.crosstab(df[column1], df[column2])
    heatmap = sns.heatmap(contingency_table)
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    return p, heatmap

class TestTaskFunc(unittest.TestCase):

    def test_basic_functionality(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'feature1': ['A', 'B', 'A']})
        df2 = pd.DataFrame({'id': [1, 2, 3], 'feature2': ['X', 'Y', 'X']})
        p_value, heatmap = task_func(df1, df2)
        self.assertIsInstance(p_value, float)
        self.assertIsNotNone(heatmap)

    def test_no_common_ids(self):
        df1 = pd.DataFrame({'id': [1, 2], 'feature1': ['A', 'B']})
        df2 = pd.DataFrame({'id': [3, 4], 'feature2': ['Y', 'Z']})
        with self.assertRaises(ValueError):
            task_func(df1, df2)

    def test_missing_feature_columns(self):
        df1 = pd.DataFrame({'id': [1, 2, 3]})
        df2 = pd.DataFrame({'id': [1, 2, 3]})
        with self.assertRaises(KeyError):
            task_func(df1, df2)

    def test_custom_column_names(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'custom_feature1': ['C', 'D', 'C']})
        df2 = pd.DataFrame({'id': [1, 2, 3], 'custom_feature2': ['W', 'X', 'W']})
        p_value, heatmap = task_func(df1, df2, column1="custom_feature1", column2="custom_feature2")
        self.assertIsInstance(p_value, float)
        self.assertIsNotNone(heatmap)

    def test_unequal_row_numbers(self):
        df1 = pd.DataFrame({'id': [1, 2], 'feature1': ['A', 'B']})
        df2 = pd.DataFrame({'id': [1, 2, 3], 'feature2': ['X', 'Y', 'Z']})
        p_value, heatmap = task_func(df1, df2)
        self.assertIsInstance(p_value, float)
        self.assertIsNotNone(heatmap)

if __name__ == '__main__':
    unittest.main()