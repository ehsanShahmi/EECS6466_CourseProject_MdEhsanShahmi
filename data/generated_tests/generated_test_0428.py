import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import unittest

def task_func(df1, df2):
    """
    Merge two dataframes on the 'id' column and then scale the numeric features.

    This function merges two dataframes via outer join on the 'id' column, and scales the merged dataframe's
    numeric features from df1 to have a mean of 0 and standard deviation of 1. It also returns a pair plot of
    the scaled features from df1.

    Parameters:
    - df1 (pd.DataFrame): Left dataframe to merge into.
    - df2 (pd.DataFrame): Right dataframe to merge from.

    Returns:
    - merged_df (pd.DataFrame): The partially scaled and merged dataframe.
    - pair_plot (seaborn.axisgrid.PairGrid): Pair plot of the scaled dataframe.

    Requirements:
    - pandas
    - sklearn
    - seaborn

    Example:
    >>> df1 = pd.DataFrame({'id': [1, 2, 3], 'feature1': [1.2, 3.4, 5.6], 'feature2': [2.3, 4.5, 6.7]})
    >>> df2 = pd.DataFrame({'id': [1, 2, 3], 'feature4': [4.5, 6.7, 8.9], 'feature5': [5.6, 7.8, 9.0]})
    >>> scaled_df, plot = task_func(df1, df2)
    >>> scaled_df
       id  feature1  feature2  feature4  feature5
    0   1 -1.224745 -1.224745       4.5       5.6
    1   2  0.000000  0.000000       6.7       7.8
    2   3  1.224745  1.224745       8.9       9.0
    >>> type(scaled_df)
    <class 'pandas.core.frame.DataFrame'>
    >>> type(plot)
    <class 'seaborn.axisgrid.PairGrid'>
    """

    merged_df = pd.merge(df1, df2, on="id", how="outer")

    # Select only numeric columns from df1 (excluding 'id')
    numeric_features_df1 = df1.select_dtypes(
        include=["float64", "int64"]
    ).columns.tolist()
    if "id" in numeric_features_df1:
        numeric_features_df1.remove("id")

    # Scale only the numeric features of df1
    if not merged_df.empty and numeric_features_df1:
        scaler = StandardScaler()
        merged_df[numeric_features_df1] = scaler.fit_transform(
            merged_df[numeric_features_df1]
        )

    # Pair plot only for the numeric features of df1
    pair_plot = None
    if numeric_features_df1:
        pair_plot = sns.pairplot(merged_df[numeric_features_df1])

    return merged_df, pair_plot

class TestTaskFunc(unittest.TestCase):

    def test_merge_and_scale(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'feature1': [1.2, 3.4, 5.6], 'feature2': [2.3, 4.5, 6.7]})
        df2 = pd.DataFrame({'id': [1, 2, 3], 'feature4': [4.5, 6.7, 8.9], 'feature5': [5.6, 7.8, 9.0]})
        scaled_df, plot = task_func(df1, df2)
        self.assertEqual(scaled_df.shape, (3, 5))  # Expecting 3 rows, 5 columns
        self.assertEqual(plot.__class__, sns.axisgrid.PairGrid)  # Check type of pair plot

    def test_empty_dataframes(self):
        df1 = pd.DataFrame(columns=['id', 'feature1', 'feature2'])
        df2 = pd.DataFrame(columns=['id', 'feature4', 'feature5'])
        scaled_df, plot = task_func(df1, df2)
        self.assertTrue(scaled_df.empty)  # Expecting merged dataframe to be empty
        self.assertIsNone(plot)  # Expecting pair plot to be None

    def test_no_numeric_columns(self):
        df1 = pd.DataFrame({'id': [1, 2], 'featureA': ['a', 'b'], 'featureB': ['c', 'd']})
        df2 = pd.DataFrame({'id': [1, 2], 'feature4': [4.5, 6.7], 'feature5': [5.6, 7.8]})
        scaled_df, plot = task_func(df1, df2)
        self.assertFalse(scaled_df.empty)  # Merged df should not be empty
        self.assertIsNone(plot)  # No numeric columns to plot

    def test_partial_dataframes(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'feature1': [1.2, 3.4, 5.6]})
        df2 = pd.DataFrame({'id': [1, 4], 'feature4': [4.5, 6.7]})
        scaled_df, plot = task_func(df1, df2)
        self.assertEqual(scaled_df.shape, (3, 3))  # Expecting 3 rows, 3 columns
        self.assertEqual(sorted(scaled_df['id'].unique()), [1, 2, 3])  # Check ids after the merge

    def test_identical_dataframes(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'feature1': [1.2, 3.4, 5.6]})
        df2 = df1.copy()
        scaled_df, plot = task_func(df1, df2)
        self.assertEqual(scaled_df.shape, (3, 4))  # Expecting 3 rows, 4 columns after merge
        self.assertAlmostEqual(scaled_df['feature1'].mean(), 0, places=5)  # Mean should be 0 after scaling

if __name__ == '__main__':
    unittest.main()