import unittest
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def task_func(my_dict):
    """
    Updates a dictionary by adding a normalized version of a numpy array found under the 'array' key.
    The normalization is performed using MinMaxScaler, scaling each value to fall between 0 and 1.

    Parameters:
        my_dict (dict): A dictionary containing a key 'array' with a numpy array as its value.

    Returns:
        dict: The dictionary after adding a key 'normalized_array' with the normalized values.

    Notes:
        The function modifies the dictionary in-place and does not create a new dictionary.
        The function assumes that 'array' key exists and its value is a numpy array.

    Raises:
        TypeError if the value of the 'array' key in my_dict is not a numpy array
        
    Requirements:
    - numpy
    - sklearn.preprocessing.MinMaxScaler

    Examples:
    >>> example_dict = {'array': np.array([1, 2, 3, 4, 5])}
    >>> result = task_func(example_dict)
    >>> 'normalized_array' in result
    True
    >>> isinstance(result['normalized_array'], np.ndarray)
    True
    """

    if not isinstance(my_dict["array"], np.ndarray):
        raise TypeError

    SCALER = MinMaxScaler()
    array = my_dict['array'].reshape(-1, 1)
    normalized_array = SCALER.fit_transform(array).reshape(-1)

    my_dict['normalized_array'] = normalized_array

    return my_dict

class TestTaskFunc(unittest.TestCase):

    def test_normalization_includes_key(self):
        example_dict = {'array': np.array([1, 2, 3, 4, 5])}
        result = task_func(example_dict)
        self.assertIn('normalized_array', result)

    def test_normalization_type(self):
        example_dict = {'array': np.array([1, 2, 3, 4, 5])}
        result = task_func(example_dict)
        self.assertIsInstance(result['normalized_array'], np.ndarray)

    def test_normalization_value_range(self):
        example_dict = {'array': np.array([1, 2, 3, 4, 5])}
        result = task_func(example_dict)
        normalized_array = result['normalized_array']
        self.assertTrue(np.all(normalized_array >= 0) and np.all(normalized_array <= 1))

    def test_empty_array(self):
        example_dict = {'array': np.array([])}
        result = task_func(example_dict)
        self.assertEqual(result['normalized_array'].size, 0)

    def test_invalid_type(self):
        example_dict = {'array': [1, 2, 3, 4, 5]}  # List instead of numpy array
        with self.assertRaises(TypeError):
            task_func(example_dict)

if __name__ == '__main__':
    unittest.main()