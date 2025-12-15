import unittest
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

class TestTaskFunc(unittest.TestCase):

    def test_output_type(self):
        df, ax = task_func(100)
        self.assertIsInstance(df, pd.DataFrame, "Output should be a pandas DataFrame.")
        self.assertIsInstance(ax, plt.Axes, "Output should be a matplotlib Axes object.")

    def test_dataframe_shape(self):
        df, ax = task_func(100)
        self.assertEqual(df.shape, (3, 2), "DataFrame should have 3 rows and 2 columns.")

    def test_statistics_values(self):
        df, ax = task_func(100)
        array1 = df['Array1'].values
        array2 = df['Array2'].values

        self.assertAlmostEqual(df.at['Mean', 'Array1'], np.mean(array1), places=5, msg="Mean of Array1 is incorrect.")
        self.assertAlmostEqual(df.at['Median', 'Array1'], np.median(array1), places=5, msg="Median of Array1 is incorrect.")
        self.assertAlmostEqual(df.at['Standard Deviation', 'Array1'], np.std(array1), places=5, msg="Std Dev of Array1 is incorrect.")

        self.assertAlmostEqual(df.at['Mean', 'Array2'], np.mean(array2), places=5, msg="Mean of Array2 is incorrect.")
        self.assertAlmostEqual(df.at['Median', 'Array2'], np.median(array2), places=5, msg="Median of Array2 is incorrect.")
        self.assertAlmostEqual(df.at['Standard Deviation', 'Array2'], np.std(array2), places=5, msg="Std Dev of Array2 is incorrect.")

    def test_default_array_length(self):
        df, ax = task_func()
        self.assertEqual(df.shape[0], 3, "DataFrame should have 3 rows for default array length.")
        self.assertEqual(df.shape[1], 2, "DataFrame should have 2 columns for default array length.")

    def test_non_numeric_array_length(self):
        with self.assertRaises(TypeError):
            task_func("not_a_number")
        with self.assertRaises(TypeError):
            task_func(None)

# To run the tests
if __name__ == '__main__':
    unittest.main()