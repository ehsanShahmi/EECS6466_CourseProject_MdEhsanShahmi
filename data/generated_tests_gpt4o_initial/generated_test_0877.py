import unittest
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def task_func(data, n_components=2):
    """
    Perform PCA (Principal Component Analysis) on the provided DataFrame.

    This function takes a pandas DataFrame, scales the data using sklearn 
    StandardScaler, and then applies PCA to reduce 
    the number of dimensions of the data to the number specified by n_components, 
    maintaining as much information as possible.

    Parameters:
    data (DataFrame): A pandas DataFrame containing numerical data. Each column represents a 
                      different variable, and each row represents a different observation.
    n_components (int): The number of principal components to retain after transformation. 
                        Default is 2.

    Returns:
    DataFrame: A new DataFrame with the original data transformed into 'n_components' principal 
               components.

    Raises:
    ValueError: If input data is not a DataFrame or contains non-numeric data.
    ValueError: If n_components is greater than the number of columns in the data.
    ValueError: If input data is empty.
    """
    if not isinstance(data, pd.DataFrame):
        raise ValueError("data should be a DataFrame.")

    if not data.apply(lambda s: pd.to_numeric(s, errors='coerce').notnull().all()).all():
        raise ValueError("DataFrame should only contain numeric values.")
    
    if n_components > len(data.columns):
        raise ValueError("n_components should not be greater than the number of columns in data.")
    
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)
    pca = PCA(n_components=n_components)
    data_reduced = pca.fit_transform(data_scaled)
    return pd.DataFrame(data_reduced)

class TestTaskFunc(unittest.TestCase):
    def test_valid_input(self):
        data = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [6, 7, 8, 9, 10],
            'C': [11, 12, 13, 14, 15],
        })
        result = task_func(data, n_components=2)
        self.assertEqual(result.shape[1], 2)

    def test_pca_with_one_component(self):
        data = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [10, 20, 30, 40, 50],
        })
        result = task_func(data, n_components=1)
        self.assertEqual(result.shape[1], 1)

    def test_non_dataframe_input(self):
        with self.assertRaises(ValueError) as context:
            task_func([[1, 2], [3, 4]], n_components=1)
        self.assertEqual(str(context.exception), "data should be a DataFrame.")

    def test_non_numeric_data(self):
        data = pd.DataFrame({
            'A': [1, 2, 3],
            'B': ['a', 'b', 'c'],
        })
        with self.assertRaises(ValueError) as context:
            task_func(data, n_components=2)
        self.assertEqual(str(context.exception), "DataFrame should only contain numeric values.")

    def test_n_components_greater_than_columns(self):
        data = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6],
        })
        with self.assertRaises(ValueError) as context:
            task_func(data, n_components=3)
        self.assertEqual(str(context.exception), "n_components should not be greater than the number of columns in data.")

if __name__ == '__main__':
    unittest.main()