import numpy as np
import pandas as pd
import unittest
from scipy import stats
import matplotlib.pyplot as plt

TARGET_VALUES = np.array([1, 3, 4])

def task_func(df):
    """
    Replace all elements in DataFrame columns that do not exist in the TARGET_VALUES array with zeros, then perform a Box-Cox transformation on each column (if data is not constant, add 1 to account for zeros) and display the resulting KDE plots.

    Parameters:
        - df (pandas.DataFrame): The input pandas DataFrame with positive values.

    Returns:
        - pandas.DataFrame: The transformed DataFrame after Box-Cox transformation.
        - matplotlib.figure.Figure: Figure containing KDE plots of the transformed columns.
    """
    # Ensure the DataFrame contains only positive values
    if (df <= 0).any().any():
        raise ValueError("Input DataFrame should contain only positive values.")

    df = df.applymap(lambda x: x if x in TARGET_VALUES else 0)

    transformed_df = pd.DataFrame()
    fig, ax = plt.subplots()

    for column in df.columns:
        # Check if data is constant
        if df[column].nunique() == 1:
            transformed_df[column] = df[column]
        else:
            transformed_data, _ = stats.boxcox(
                df[column] + 1
            )  # Add 1 since the are some null values
            transformed_df[column] = transformed_data
            
            # Using matplotlib's kde method to plot the KDE
            kde = stats.gaussian_kde(transformed_df[column])
            x_vals = np.linspace(
                min(transformed_df[column]), max(transformed_df[column]), 1000
            )
            ax.plot(x_vals, kde(x_vals), label=column)

    ax.legend()
    plt.show()
    return transformed_df, fig

class TestTaskFunc(unittest.TestCase):

    def test_positive_values(self):
        df = pd.DataFrame({
            'A': [1, 3, 4, 1, 3],
            'B': [4, 1, 4, 3, 1],
            'C': [3, 3, 4, 3, 1]
        })
        transformed_df, _ = task_func(df)
        self.assertTrue((transformed_df >= 0).all().all(), "All values should be non-negative after transformation.")

    def test_values_outside_target(self):
        df = pd.DataFrame({
            'A': [1, 2, 5, 1, 8],
            'B': [0, -1, 2, 9, 3]
        })
        transformed_df, _ = task_func(df)
        expected_df = pd.DataFrame({
            'A': [0.0, 0.0, 0.0, 0.0, 0.0],
            'B': [0.0, 0.0, 0.0, 0.0, 0.0]
        })
        pd.testing.assert_frame_equal(transformed_df, expected_df, check_dtype=False)

    def test_boxcox_transformation(self):
        df = pd.DataFrame({
            'A': [3, 3, 4, 3, 1],
            'B': [1, 1, 1, 1, 1]
        })
        transformed_df, _ = task_func(df)
        self.assertEqual(transformed_df['A'].nunique(), 4, "Box-Cox transformation should change data if not constant")
        self.assertEqual(transformed_df['B'].nunique(), 1, "Column with constant values should not transform")

    def test_empty_dataframe(self):
        df = pd.DataFrame(columns=['A', 'B'])
        transformed_df, _ = task_func(df)
        pd.testing.assert_frame_equal(transformed_df, df, check_dtype=False)

    def test_invalid_values(self):
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [-1, 0, 1]
        })
        with self.assertRaises(ValueError):
            task_func(df)

if __name__ == '__main__':
    unittest.main()