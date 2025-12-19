import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore
import unittest

def task_func(df, z_threshold=2):
    df['Z_score'] = zscore(df['closing_price'])
    outliers = df[np.abs(df['Z_score']) > z_threshold]
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df['closing_price'], color='blue', label='Normal')
    ax.plot(outliers['closing_price'], linestyle='none', marker='X', color='red', markersize=12, label='Outlier')
    ax.set_xlabel('Index')
    ax.set_ylabel('Closing Price')
    ax.set_title('Outliers in Closing Prices')
    ax.legend(loc='best')
    return outliers, ax

class TestTaskFunc(unittest.TestCase):

    def test_no_outliers(self):
        df = pd.DataFrame({'closing_price': [100, 101, 102, 103, 104]})
        outliers, _ = task_func(df)
        self.assertTrue(outliers.empty, "Expected no outliers")

    def test_single_outlier(self):
        df = pd.DataFrame({'closing_price': [100, 101, 150, 103, 104]})
        outliers, _ = task_func(df)
        self.assertEqual(len(outliers), 1, "Expected one outlier")
        self.assertEqual(outliers['closing_price'].values[0], 150)

    def test_multiple_outliers(self):
        df = pd.DataFrame({'closing_price': [100, 200, 150, 300, 400]})
        outliers, _ = task_func(df)
        self.assertGreater(len(outliers), 1, "Expected multiple outliers")

    def test_custom_z_threshold(self):
        df = pd.DataFrame({'closing_price': [10, 20, 30, 40, 100]})
        outliers, _ = task_func(df, z_threshold=1.5)
        self.assertEqual(len(outliers), 1, "Expected one outlier with custom Z-threshold")

    def test_empty_dataframe(self):
        df = pd.DataFrame(columns=['closing_price'])
        outliers, _ = task_func(df)
        self.assertTrue(outliers.empty, "Expected no outliers for empty DataFrame")

if __name__ == '__main__':
    unittest.main()