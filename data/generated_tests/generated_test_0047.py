import unittest
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt


def task_func(df):
    """
    Standardize numeric columns in a DataFrame and return the heatmap of the correlation matrix. Missing values are replaced by the column's average.

    Parameters:
    - df (pandas.DataFrame): The pandas DataFrame to be standardized.

    Returns:
    - DataFrame: The pandas DataFrame after standardization.
    - Axes: A heatmap of the correlation matrix.

    Requirements:
    - sklearn.preprocessing.StandardScaler
    - seaborn
    - matplotlib.pyplot

    Example:
    >>> import pandas as pd
    >>> import numpy as np
    >>> df = pd.DataFrame([[1,2,3],[4,5,6],[7.0,np.nan,9.0]], columns=["c1","c2","c3"])
    >>> standardized_df, heatmap = task_func(df)
    >>> print(standardized_df)
             c1        c2        c3
    0 -1.224745 -1.224745 -1.224745
    1  0.000000  1.224745  0.000000
    2  1.224745  0.000000  1.224745
    """

    df = df.fillna(df.mean(axis=0))
    scaler = StandardScaler()
    df[df.columns] = scaler.fit_transform(df[df.columns])
    plt.figure(figsize=(10, 5))
    heatmap = sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    return df, heatmap


class TestTaskFunc(unittest.TestCase):

    def test_standardization_no_nan(self):
        df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=["c1", "c2", "c3"])
        standardized_df, _ = task_func(df)
        expected_df = pd.DataFrame([[-1.224745, -1.224745, -1.224745],
                                     [0, 0, 0],
                                     [1.224745, 1.224745, 1.224745]])
        pd.testing.assert_frame_equal(standardized_df.round(6), expected_df)

    def test_standardization_with_nan(self):
        df = pd.DataFrame([[1, 2, 3], [np.nan, 5, 6], [7, 8, np.nan]], columns=["c1", "c2", "c3"])
        standardized_df, _ = task_func(df)
        expected_df = pd.DataFrame([[-1.224745, -1.224745, -1.224745],
                                     [0, 0, 0],
                                     [1.224745, 1.224745, 1.224745]])
        pd.testing.assert_frame_equal(standardized_df.round(6), expected_df)

    def test_empty_dataframe(self):
        df = pd.DataFrame(columns=["c1", "c2", "c3"])
        with self.assertRaises(ValueError):
            task_func(df)

    def test_single_value_column(self):
        df = pd.DataFrame([[1], [1], [1]], columns=["c1"])
        standardized_df, _ = task_func(df)
        expected_df = pd.DataFrame([[0], [0], [0]], columns=["c1"])
        pd.testing.assert_frame_equal(standardized_df, expected_df)

    def test_multiple_columns(self):
        df = pd.DataFrame([[1, 2], [3, np.nan], [5, 6]], columns=["c1", "c2"])
        standardized_df, heatmap = task_func(df)
        self.assertEqual(standardized_df.shape[1], 2)  # Check column count
        self.assertEqual(heatmap.get_title(), "")  # Check if heatmap has a title
        
if __name__ == "__main__":
    unittest.main()