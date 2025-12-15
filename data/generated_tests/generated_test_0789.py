import numpy as np
from sklearn.preprocessing import MinMaxScaler
import unittest

# Constants
ARRAY_LENGTH = 10

def task_func():
    """
    Generate a random array and apply min-max normalization (scaling) to transform the array values into a range between 0 and 1.

    Parameters:
    - None

    Returns:
    - scaled_array (numpy.ndarray): The normalized array.

    Requirements:
    - numpy
    - sklearn
    """
    np.random.seed(42)  # For reproducibility
    array = np.random.randint(0, 10, ARRAY_LENGTH).reshape(-1, 1)
    scaler = MinMaxScaler()
    scaled_array = scaler.fit_transform(array)
    return scaled_array

class TestTaskFunc(unittest.TestCase):

    def test_return_shape(self):
        """Test if the output shape is correct."""
        result = task_func()
        self.assertEqual(result.shape, (ARRAY_LENGTH, 1))

    def test_values_range(self):
        """Test if all values in the output are between 0 and 1."""
        result = task_func()
        self.assertTrue(np.all(result >= 0) and np.all(result <= 1))

    def test_output_type(self):
        """Test if the output is a numpy ndarray."""
        result = task_func()
        self.assertIsInstance(result, np.ndarray)

    def test_min_value(self):
        """Test if the minimum value in the scaled array is 0."""
        result = task_func()
        self.assertEqual(np.min(result), 0)

    def test_max_value(self):
        """Test if the maximum value in the scaled array is 1."""
        result = task_func()
        self.assertEqual(np.max(result), 1)

if __name__ == '__main__':
    unittest.main()