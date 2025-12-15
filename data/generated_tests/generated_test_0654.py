import unittest
import numpy as np

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        self.valid_array = np.array([[1, 2], [1, 3], [1, 4], [2, 5], [2, 6]])
        self.valid_target = 1
        self.invalid_array = np.array([[2, 2], [2, 3]])
        self.zero_target = 0
        self.large_array = np.array([[1, i] for i in range(10)] + [[2, i] for i in range(10, 20)])

    def test_parameters_length(self):
        """Test if the returned parameters have the correct length when valid input is given."""
        params, _ = task_func(self.valid_array, self.valid_target)
        self.assertEqual(len(params), 3)

    def test_fitting_with_insufficient_data(self):
        """Test that a ValueError is raised when there are not enough data points."""
        with self.assertRaises(ValueError):
            task_func(self.invalid_array, 2)

    def test_plotting_functionality(self):
        """Test that the function returns a matplotlib Axes object."""
        _, ax = task_func(self.valid_array, self.valid_target)
        self.assertIsInstance(ax, plt.Axes)

    def test_large_data_set(self):
        """Test the function with a larger data set to ensure it can handle more complex inputs."""
        params, _ = task_func(self.large_array, 1)
        self.assertEqual(len(params), 3)

    def test_invalid_target_value(self):
        """Test that a ValueError is raised when the target value is not present in the first column."""
        with self.assertRaises(ValueError):
            task_func(self.valid_array, self.zero_target)

if __name__ == '__main__':
    unittest.main()