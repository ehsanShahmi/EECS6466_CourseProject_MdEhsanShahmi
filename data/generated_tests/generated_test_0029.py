import unittest
import numpy as np
import base64
from sklearn.preprocessing import StandardScaler

# Here is your prompt:
def task_func(data):
    """
    Standardize a numeric array using sklearn's StandardScaler and encode the standardized data in base64 format as an ASCII string.
    
    Parameters:
    - data (numpy.ndarray): The numpy array to standardize and encode.
    
    Returns:
    - str: The base64-encoded ASCII string representation of the standardized data.
    
    Requirements:
    - sklearn.preprocessing.StandardScaler
    - numpy
    - base64
    
    Example:
    >>> data = np.array([[0, 0], [0, 0], [1, 1], [1, 1]])
    >>> encoded_data = task_func(data)
    >>> print(encoded_data)
    W1stMS4gLTEuXQogWy0xLiAtMS5dCiBbIDEuICAxLl0KIFsgMS4gIDEuXV0KIFsgMS4gMS4gMS41TQ==
    """

    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(data)
    standardized_data_str = np.array2string(standardized_data)
    encoded_data = base64.b64encode(standardized_data_str.encode('ascii')).decode('ascii')
    
    return encoded_data


class TestTaskFunc(unittest.TestCase):
    
    def test_standardize_two_dimensional_data(self):
        data = np.array([[0, 0], [0, 0], [1, 1], [1, 1]])
        expected_encoded_data = base64.b64encode(np.array2string(np.array([[0, 0], [0, 0], [1, 1], [1, 1]])).encode('ascii')).decode('ascii')
        self.assertEqual(task_func(data), expected_encoded_data)

    def test_standardize_positive_numbers(self):
        data = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
        expected_encoded_data = base64.b64encode(np.array2string(np.array([[-1.34164079, -1.34164079],
                                                                          [0.4472136, 0.4472136],
                                                                          [1.34164079, 1.34164079],
                                                                          [2.23606798, 2.23606798]])).encode('ascii')).decode('ascii')
        self.assertEqual(task_func(data), expected_encoded_data)

    def test_standardize_negative_numbers(self):
        data = np.array([[-1, -2], [-3, -4], [-5, -6], [-7, -8]])
        expected_encoded_data = base64.b64encode(np.array2string(np.array([[1.34164079, 1.34164079],
                                                                          [0.4472136, 0.4472136],
                                                                          [-0.4472136, -0.4472136],
                                                                          [-1.34164079, -1.34164079]])).encode('ascii')).decode('ascii')
        self.assertEqual(task_func(data), expected_encoded_data)

    def test_standardize_mixed_numbers(self):
        data = np.array([[1, -2], [-3, 4], [5, -6], [-7, 8]])
        expected_encoded_data = base64.b64encode(np.array2string(np.array([[0.0, 0.0],
                                                                          [-1.34164079, 1.34164079],
                                                                          [2.23606798, -2.23606798],
                                                                          [-0.89442719, -0.4472136]])).encode('ascii')).decode('ascii')
        self.assertEqual(task_func(data), expected_encoded_data)

    def test_standardize_single_value(self):
        data = np.array([[0]])
        expected_encoded_data = base64.b64encode(np.array2string(np.array([[0]])).encode('ascii')).decode('ascii')
        self.assertEqual(task_func(data), expected_encoded_data)


if __name__ == '__main__':
    unittest.main()