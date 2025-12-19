import unittest
import numpy as np
from scipy.stats import skew, kurtosis

# Constants
TARGET_VALUE = '332'
ARRAY = np.array([['0', '1', '2'], ['a', 'bb', 'ccc'], ['332', '33', '2'], ['33', '22', '332']])


def task_func(target_value=TARGET_VALUE, array=ARRAY):
    indices = np.where(array[:, 0] == target_value)[0]

    # Check if statistical analysis is possible
    if len(indices) < 2:
        plt.hist(indices, bins='auto')  # Plotting can still occur
        plt.show()
        return (np.mean(indices), 'N/A', 'N/A', 'N/A') if indices.size else ('N/A', 'N/A', 'N/A', 'N/A')

    # Perform statistical analysis
    mean = np.mean(indices)
    variance = np.var(indices)
    skewness = stats.skew(indices)
    kurtosis = stats.kurtosis(indices)

    # Plot the distribution
    plt.hist(indices, bins='auto')
    plt.title('Distribution of Indices')
    plt.xlabel('Indices')
    plt.ylabel('Frequency')
    plt.show()

    return mean, variance, skewness, kurtosis


class TestTaskFunc(unittest.TestCase):

    def test_target_value_found_multiple(self):
        result = task_func()
        self.assertEqual(result[0], 2.0)  # Mean index when multiple indices found
        self.assertIsInstance(result[1], float)  # Variance should be a float
        self.assertIsInstance(result[2], float)  # Skewness should be a float
        self.assertIsInstance(result[3], float)  # Kurtosis should be a float

    def test_target_value_found_single(self):
        result = task_func(target_value='0')
        self.assertEqual(result[0], 0.0)  # Mean index is 0 for single index found
        self.assertEqual(result[1], 'N/A')  # Variance should return 'N/A'
        self.assertEqual(result[2], 'N/A')  # Skewness should return 'N/A'
        self.assertEqual(result[3], 'N/A')  # Kurtosis should return 'N/A'

    def test_target_value_not_found(self):
        result = task_func(target_value='999')
        self.assertEqual(result, ('N/A', 'N/A', 'N/A', 'N/A'))  # Check when value not found

    def test_empty_array(self):
        empty_array = np.array([[], []])
        result = task_func(array=empty_array)
        self.assertEqual(result, ('N/A', 'N/A', 'N/A', 'N/A'))  # No data to analyze

    def test_invalid_target_type(self):
        with self.assertRaises(TypeError):
            task_func(target_value=332)  # Passing an integer instead of a string


if __name__ == '__main__':
    unittest.main()