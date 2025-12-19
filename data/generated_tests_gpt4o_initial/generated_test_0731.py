import unittest
import numpy as np
import pickle
import os
from sklearn.datasets import make_classification

# Constants
FILE_NAME = 'save.pkl'
DATA, TARGET = make_classification(n_samples=100, n_features=20, n_informative=2, n_redundant=10, n_classes=2, random_state=1)

def task_func(data, target):
    """
    Save the Sklearn dataset ("Data" and "Destination") in the pickle file "save.pkl" and then read it back for validation.

    Parameters:
    - data (numpy array): The data part of the sklearn dataset.
    - target (numpy array): The target part of the sklearn dataset.

    Returns:
    tuple: The loaded tuple (data, target) from 'save.pkl'.

    Requirements:
    - pickle
    - os
    - sklearn.datasets
    """

    with open(FILE_NAME, 'wb') as file:
        pickle.dump((data, target), file)
    
    with open(FILE_NAME, 'rb') as file:
        loaded_data, loaded_target = pickle.load(file)

    os.remove(FILE_NAME)

    return loaded_data, loaded_target

class TestTaskFunc(unittest.TestCase):

    def test_task_func_correctness(self):
        """Test if the data and target are correctly saved and loaded."""
        data, target = make_classification(n_samples=100, n_features=20, n_informative=2, n_redundant=10, n_classes=2, random_state=1)
        loaded_data, loaded_target = task_func(data, target)
        self.assertTrue(np.array_equal(data, loaded_data), "Loaded data does not match the original data.")
        self.assertTrue(np.array_equal(target, loaded_target), "Loaded target does not match the original target.")

    def test_task_func_data_shape(self):
        """Test if the shapes of loaded data and target are correct."""
        data, target = make_classification(n_samples=100, n_features=20, n_informative=2, n_redundant=10, n_classes=2, random_state=1)
        loaded_data, loaded_target = task_func(data, target)
        self.assertEqual(data.shape, loaded_data.shape, "Loaded data shape is incorrect.")
        self.assertEqual(target.shape, loaded_target.shape, "Loaded target shape is incorrect.")

    def test_task_func_file_removal(self):
        """Test if the pickle file is removed after loading."""
        data, target = make_classification(n_samples=100, n_features=20, n_informative=2, n_redundant=10, n_classes=2, random_state=1)
        task_func(data, target)
        self.assertFalse(os.path.exists(FILE_NAME), "Pickle file was not removed after execution.")

    def test_task_func_empty_input(self):
        """Test if the function handles empty inputs correctly."""
        data = np.array([])
        target = np.array([])
        with self.assertRaises(ValueError):  # Expecting a ValueError because of empty inputs
            task_func(data, target)

    def test_task_func_type_check(self):
        """Test if the function raises an error for invalid input types."""
        with self.assertRaises(TypeError):  # Expecting a TypeError
            task_func("invalid_data", "invalid_target")


if __name__ == '__main__':
    unittest.main()