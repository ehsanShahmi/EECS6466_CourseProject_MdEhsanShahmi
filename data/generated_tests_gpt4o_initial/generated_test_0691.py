import unittest
import pandas as pd
import numpy as np
from sklearn.utils.validation import check_is_fitted
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Here is your prompt:
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def task_func(df):
    """
    Given a pandas DataFrame with random numeric values, run KMeans clusters on the data and return the labels.

    Parameters:
    - df (DataFrame): The DataFrame to use.

    Returns:
    - labels (np.array): The labels from the KMeans clustering.

    Requirements:
    - pandas
    - sklearn

    Example:
    >>> import numpy as np
    >>> np.random.seed(42)
    >>> df = pd.DataFrame(np.random.rand(500, 2) * 100, columns=['A', 'B']) 
    >>> labels = task_func(df)
    >>> print(labels)
    [0 2 1 0 2 0 2 1 0 1 1 1 0 0 ...]
    """
    # Perform clustering
    scaler = StandardScaler()
    df_std = scaler.fit_transform(df.values)
    
    # Convert standardized values back to a DataFrame using pd
    df_std = pd.DataFrame(df_std, columns=df.columns)
    
    # Perform clustering with sklearn's KMeans
    kmeans = KMeans(n_clusters=3, random_state=0).fit(df_std)
    labels = kmeans.labels_  # The labels are directly a numpy array
    
    return labels

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Set a random seed for reproducibility
        np.random.seed(0)

    def test_output_shape(self):
        df = pd.DataFrame(np.random.rand(500, 2) * 100, columns=['A', 'B'])
        labels = task_func(df)
        self.assertEqual(labels.shape, (500,), "Output labels should have 500 elements.")

    def test_unique_labels(self):
        df = pd.DataFrame(np.random.rand(100, 2) * 100, columns=['A', 'B'])
        labels = task_func(df)
        unique_labels = np.unique(labels)
        self.assertTrue(set(unique_labels).issubset({0, 1, 2}), "Labels should be in the range of 0 to 2.")

    def test_is_instance_labels(self):
        df = pd.DataFrame(np.random.rand(250, 2) * 100, columns=['A', 'B'])
        labels = task_func(df)
        self.assertIsInstance(labels, np.ndarray, "Output labels should be of type numpy.ndarray.")

    def test_output_on_different_data_sizes(self):
        for size in [10, 100, 1000]:
            df = pd.DataFrame(np.random.rand(size, 2) * 100, columns=['A', 'B'])
            labels = task_func(df)
            self.assertEqual(labels.shape[0], size, f"Output labels should have {size} elements for input size {size}.")

    def test_output_for_identical_points(self):
        # Create a DataFrame with identical points
        df = pd.DataFrame([[1, 1], [1, 1], [1, 1], [1, 1]], columns=['A', 'B'])
        labels = task_func(df)
        self.assertEqual(len(set(labels)), 1, "All identical points should fall into the same cluster.")

# The following code is necessary to run the tests
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)