import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import unittest
from scipy.stats import skew

# Here is your prompt:
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew


def task_func(data_matrix):
    """
    Calculate the skew of each row in a 2D data matrix and plot the distribution.

    Parameters:
    - data_matrix (numpy.array): The 2D data matrix.

    Returns:
    pandas.DataFrame: A DataFrame containing the skewness of each row. The skweness is stored in a new column which name is 'Skewness'.
    matplotlib.axes.Axes: The Axes object of the plotted distribution.

    Requirements:
    - pandas
    - matplotlib.pyplot
    - scipy.stats.skew

    Example:
    >>> import numpy as np
    >>> data = np.array([[6, 8, 1, 3, 4], [-1, 0, 3, 5, 1]])
    >>> df, ax = task_func(data)
    >>> print(df)
       Skewness
    0  0.122440
    1  0.403407
    """

    skewness = skew(data_matrix, axis=1)
    df = pd.DataFrame(skewness, columns=["Skewness"])
    plt.figure(figsize=(10, 5))
    df["Skewness"].plot(kind="hist", title="Distribution of Skewness")
    return df, plt.gca()

# UnitTest Class
class TestTaskFunc(unittest.TestCase):

    def test_shape_of_output(self):
        data = np.array([[1, 2, 3], [4, 5, 6]])
        df, ax = task_func(data)
        self.assertEqual(df.shape[0], data.shape[0], "Output DataFrame should have the same number of rows as input data.")

    def test_skewness_type(self):
        data = np.array([[1, 2, 3], [4, 5, 6]])
        df, ax = task_func(data)
        self.assertIsInstance(df, pd.DataFrame, "Output should be a pandas DataFrame.")
        self.assertIn("Skewness", df.columns, "DataFrame should contain a 'Skewness' column.")

    def test_skewness_values(self):
        data = np.array([[1, 2, 3], [4, 5, 6]])
        df, ax = task_func(data)
        self.assertAlmostEqual(df["Skewness"][0], 0.0, places=5, msg="Skewness of the first row should be close to 0.")
        self.assertAlmostEqual(df["Skewness"][1], 0.0, places=5, msg="Skewness of the second row should be close to 0.")

    def test_empty_input(self):
        data = np.array([[]])
        df, ax = task_func(data)
        self.assertEqual(df.shape[0], 1, "Output should have one row for an empty input.")

    def test_plot_generated(self):
        data = np.array([[1, 1, 1], [2, 2, 2]])
        df, ax = task_func(data)
        self.assertIsNotNone(ax, "The plot should be generated and Axes object should not be None.")

# Run the test suite
if __name__ == '__main__':
    unittest.main()