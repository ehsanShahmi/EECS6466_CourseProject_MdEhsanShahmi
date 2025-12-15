import unittest
import pandas as pd
from sklearn.exceptions import NotFittedError
import matplotlib.pyplot as plt

# Here is your prompt:
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def task_func(data_dict, data_keys):
    """
    Normalize data specified by keys in a dictionary using MinMax scaling and plot the results. This function is
    useful for preprocessing data for machine learning models where data scaling can impact performance.

    Parameters:
    data_dict (dict): A dictionary where keys map to lists of numeric values.
    data_keys (list): Keys within the dictionary whose corresponding values are to be normalized.

    Returns:
    tuple: A tuple containing a DataFrame of normalized values and a matplotlib Axes object representing a plot of the
    normalized data.

    Requirements:
    - pandas
    - sklearn

    Raises:
    ValueError: If no keys in `data_keys` are found in `data_dict`.

    Example:
    >>> data_dict = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    >>> data_keys = ['A', 'B']
    >>> normalized_df, ax = task_func(data_dict, data_keys)
    >>> print(normalized_df.to_string(index=False))
      A   B
    0.0 0.0
    0.5 0.5
    1.0 1.0
    """

    # Extract and transform the data for the specified keys
    data_for_keys = {key: data_dict[key] for key in data_keys if key in data_dict}
    df = pd.DataFrame(data_for_keys)

    # Check if DataFrame is empty (i.e., no keys matched)
    if df.empty:
        raise ValueError("No matching keys found in data dictionary, or keys list is empty.")

    # Apply MinMax normalization
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(df)
    normalized_df = pd.DataFrame(normalized_data, columns=data_keys)

    # Plot the normalized data
    ax = normalized_df.plot(kind='line')
    ax.set_title('Normalized Data')
    ax.set_ylabel('Normalized Value')
    ax.set_xlabel('Index')

    return normalized_df, ax

# Test Suite
class TestTaskFunc(unittest.TestCase):

    def test_normalization_of_data(self):
        data_dict = {'A': [1, 2, 3], 'B': [4, 5, 6]}
        data_keys = ['A', 'B']
        expected_df = pd.DataFrame({'A': [0.0, 0.5, 1.0], 'B': [0.0, 0.5, 1.0]})

        normalized_df, ax = task_func(data_dict, data_keys)
        
        pd.testing.assert_frame_equal(normalized_df, expected_df)

    def test_single_key_normalization(self):
        data_dict = {'A': [10, 20, 30]}
        data_keys = ['A']
        expected_df = pd.DataFrame({'A': [0.0, 0.5, 1.0]})

        normalized_df, ax = task_func(data_dict, data_keys)
        
        pd.testing.assert_frame_equal(normalized_df, expected_df)

    def test_no_matching_keys(self):
        data_dict = {'A': [1, 2, 3]}
        data_keys = ['B']  # no matching keys

        with self.assertRaises(ValueError) as context:
            task_func(data_dict, data_keys)
        
        self.assertEqual(str(context.exception), "No matching keys found in data dictionary, or keys list is empty.")

    def test_empty_data_dict(self):
        data_dict = {}
        data_keys = ['A']

        with self.assertRaises(ValueError) as context:
            task_func(data_dict, data_keys)
        
        self.assertEqual(str(context.exception), "No matching keys found in data dictionary, or keys list is empty.")

    def test_empty_data_keys(self):
        data_dict = {'A': [1, 2, 3]}
        data_keys = []  # empty keys

        with self.assertRaises(ValueError) as context:
            task_func(data_dict, data_keys)
        
        self.assertEqual(str(context.exception), "No matching keys found in data dictionary, or keys list is empty.")

if __name__ == '__main__':
    unittest.main()