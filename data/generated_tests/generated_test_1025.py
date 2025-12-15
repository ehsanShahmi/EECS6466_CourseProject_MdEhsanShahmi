import pandas as pd
import matplotlib.pyplot as plt
import unittest
from sklearn.preprocessing import MinMaxScaler

# Constants
PLOT_TITLE = "Scaled Values"

# Here is your prompt:
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.preprocessing import MinMaxScaler

# Constants
# PLOT_TITLE = "Scaled Values"
def task_func(data_dict):
    """
    Scales the values in a given dictionary using MinMaxScaler and plots the scaled data.

    Parameters:
    - data_dict (dict): A dictionary where keys represent column names and values are lists of numerical data.
                        The values may contain missing data (None), which are handled by dropping them before scaling.

    Returns:
    - pandas.DataFrame containing the scaled data.
    - matplotlib Axes object that displays the plot of the scaled data.

    Requirements:
    - pandas
    - scikit-learn
    - matplotlib

    Example:
    >>> data = {'a': [1, 2, None, 4], 'b': [5, None, 7, 8]}
    >>> scaled_df, plot_ax = task_func(data)
    >>> scaled_df
         a    b
    0  0.0  0.0
    1  1.0  1.0
    >>> plot_ax.get_title()
    'Scaled Values'
    """

    df = pd.DataFrame(data_dict).dropna()

    if df.empty:
        ax = plt.gca()
        ax.set_title(PLOT_TITLE)
        return df, ax

    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(df)
    df_scaled = pd.DataFrame(scaled_data, columns=df.columns)

    ax = df_scaled.plot()
    ax.set_title(PLOT_TITLE)

    return df_scaled, ax


class TestTaskFunc(unittest.TestCase):

    def test_scale_with_none_values(self):
        data = {'a': [1, 2, None, 4], 'b': [5, None, 7, 8]}
        scaled_df, plot_ax = task_func(data)
        
        expected_df = pd.DataFrame({'a': [0.0, 0.333333, 1.0], 'b': [0.0, 0.666667, 1.0]})
        pd.testing.assert_frame_equal(scaled_df.reset_index(drop=True), expected_df.reset_index(drop=True))
        self.assertEqual(plot_ax.get_title(), PLOT_TITLE)

    def test_scale_empty_dict(self):
        data = {}
        scaled_df, plot_ax = task_func(data)
        
        expected_df = pd.DataFrame(columns=[])
        pd.testing.assert_frame_equal(scaled_df, expected_df)
        self.assertEqual(plot_ax.get_title(), PLOT_TITLE)

    def test_scale_no_none_values(self):
        data = {'a': [1, 2, 3, 4], 'b': [5, 6, 7, 8]}
        scaled_df, plot_ax = task_func(data)
        
        expected_df = pd.DataFrame({'a': [0.0, 0.333333, 0.666667, 1.0], 'b': [0.0, 0.333333, 0.666667, 1.0]})
        pd.testing.assert_frame_equal(scaled_df.reset_index(drop=True), expected_df.reset_index(drop=True))
        self.assertEqual(plot_ax.get_title(), PLOT_TITLE)

    def test_scale_identical_values(self):
        data = {'a': [1, 1, 1], 'b': [1, 1, 1]}
        scaled_df, plot_ax = task_func(data)
        
        expected_df = pd.DataFrame({'a': [0.0, 0.0, 0.0], 'b': [0.0, 0.0, 0.0]})
        pd.testing.assert_frame_equal(scaled_df.reset_index(drop=True), expected_df.reset_index(drop=True))
        self.assertEqual(plot_ax.get_title(), PLOT_TITLE)

    def test_scale_large_numbers(self):
        data = {'a': [1000, 2000, None, 4000], 'b': [5000, None, 7000, 8000]}
        scaled_df, plot_ax = task_func(data)
        
        expected_df = pd.DataFrame({'a': [0.0, 0.333333, 1.0], 'b': [0.0, 0.666667, 1.0]})
        pd.testing.assert_frame_equal(scaled_df.reset_index(drop=True), expected_df.reset_index(drop=True))
        self.assertEqual(plot_ax.get_title(), PLOT_TITLE)

if __name__ == '__main__':
    unittest.main()