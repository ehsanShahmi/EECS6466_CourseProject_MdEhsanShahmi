import numpy as np
import pandas as pd
import seaborn as sns
import unittest
from unittest.mock import patch

# Here is your prompt:
def task_func(num_samples=100, num_features=5):
    """
    Generate a Pandas DataFrame with random values, representing a dataset with multiple features. 
    Calculate the correlation between the features and visualize this information using a heatmap.
    
    Parameters:
    - num_samples (int): The number of samples to generate. Default is 100.
    - num_features (int): The number of features to generate. Default is 5.
    
    Returns:
    - DataFrame: The generated DataFrame with random values.
    - Axes: The heatmap visualization of the correlation matrix.

    Requirements:
    - pandas
    - numpy
    - seaborn
    
    Example:
    >>> df, ax = task_func(10, 3)
    >>> ax.figure.show()
    """

    FEATURES = ['Feature' + str(i) for i in range(1, num_features + 1)]
    SAMPLES = ['Sample' + str(i) for i in range(1, num_samples + 1)]
    
    data = np.random.rand(len(SAMPLES), len(FEATURES))
    df = pd.DataFrame(data, index=SAMPLES, columns=FEATURES)
    
    corr_matrix = df.corr()
    ax = sns.heatmap(corr_matrix, annot=True)
    
    return df, ax

class TestTaskFunc(unittest.TestCase):

    def test_default_parameters(self):
        df, ax = task_func()
        self.assertEqual(df.shape, (100, 5))
        self.assertEqual(list(df.columns), ['Feature1', 'Feature2', 'Feature3', 'Feature4', 'Feature5'])

    def test_custom_sample_size(self):
        num_samples = 50
        df, ax = task_func(num_samples=num_samples)
        self.assertEqual(df.shape[0], num_samples)

    def test_custom_feature_size(self):
        num_features = 10
        df, ax = task_func(num_features=num_features)
        self.assertEqual(df.shape[1], num_features)
        self.assertEqual(list(df.columns), [f'Feature{i}' for i in range(1, num_features + 1)])

    def test_non_default_heatmap_annotations(self):
        df, ax = task_func()
        self.assertTrue(ax.collections[0].get_array().min() >= 0)  # Check annotations are there and non-negative
        self.assertTrue(ax.collections[0].get_array().max() <= 1)  # Check correlation values are between -1 and 1

    def test_large_data(self):
        num_samples = 1000
        num_features = 20
        df, ax = task_func(num_samples=num_samples, num_features=num_features)
        self.assertEqual(df.shape, (num_samples, num_features))

if __name__ == '__main__':
    unittest.main()