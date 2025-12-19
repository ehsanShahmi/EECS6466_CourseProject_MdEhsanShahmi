import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import numpy as np
import unittest

def task_func(data):
    """
    Normalizes a given dataset using MinMax scaling and calculates the average of each row. This average is then
    added as a new column 'Average' to the resulting DataFrame. The function also visualizes these averages in a plot.

    Parameters:
    data (numpy.array): A 2D array where each row represents a sample and each column a feature, with a
    shape of (n_samples, 8).

    Returns:
    DataFrame: A pandas DataFrame where data is normalized, with an additional column 'Average' representing the
    mean of each row.
    Axes: A matplotlib Axes object showing a bar subplot of the average values across the dataset.

    Requirements:
    - pandas
    - sklearn
    - matplotlib

    Example:
    >>> import numpy as np
    >>> data = np.array([[1, 2, 3, 4, 4, 3, 7, 1], [6, 2, 3, 4, 3, 4, 4, 1]])
    >>> df, ax = task_func(data)
    >>> print(df.round(2))
         A    B    C    D    E    F    G    H  Average
    0  0.0  0.0  0.0  0.0  1.0  0.0  1.0  0.0     0.25
    1  1.0  0.0  0.0  0.0  0.0  1.0  0.0  0.0     0.25
    """

    COLUMN_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(data)

    df = pd.DataFrame(normalized_data, columns=COLUMN_NAMES)
    df['Average'] = df.mean(axis=1)

    fig, ax = plt.subplots()
    df['Average'].plot(ax=ax)

    return df, ax

class TestTaskFunction(unittest.TestCase):

    def test_normalization_shape(self):
        data = np.array([[1, 2, 3, 4, 4, 3, 7, 1]])
        df, ax = task_func(data)
        self.assertEqual(df.shape, (1, 9), "The output DataFrame should have 9 columns.")

    def test_average_column_added(self):
        data = np.array([[1, 2, 3, 4, 4, 3, 7, 1]])
        df, ax = task_func(data)
        self.assertIn('Average', df.columns, "The output DataFrame should have an 'Average' column.")

    def test_average_calculation(self):
        data = np.array([[1, 2, 3, 4, 4, 3, 7, 1], [6, 2, 3, 4, 3, 4, 4, 1]])
        df, ax = task_func(data)
        expected_averages = np.mean(data, axis=1)
        np.testing.assert_array_almost_equal(df['Average'].values, expected_averages, decimal=6, 
                                             err_msg="The 'Average' column must correctly reflect the average of each row.")

    def test_minmax_scaling(self):
        data = np.array([[1, 2, 3, 4, 4, 3, 7, 1], [6, 2, 3, 4, 3, 4, 4, 1]])
        df, ax = task_func(data)
        expected_minmax = np.array([[0, 0, 0, 0, 1, 0, 1, 0], [1, 0, 0, 0, 0, 1, 0, 0]])
        np.testing.assert_array_almost_equal(df.iloc[:, :-1].values, expected_minmax, 
                                             decimal=6, err_msg="Data should be correctly min-max scaled.")

    def test_plot_creation(self):
        data = np.array([[1, 2, 3, 4, 4, 3, 7, 1]])
        df, ax = task_func(data)
        self.assertIsNotNone(ax, "A matplotlib Axes object should be returned.")

if __name__ == '__main__':
    unittest.main()