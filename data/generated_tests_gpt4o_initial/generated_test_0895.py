import numpy as np
import matplotlib.pyplot as plt
import unittest

# Constants
ARRAY_SIZE = 10000

def task_func():
    """
    Create a numeric array of random integers, calculate the mean and standard deviation, and draw a histogram of the distribution.

    Returns:
    Tuple: A tuple containing the array, mean, standard deviation, and the histogram plot (Axes).
    """
    array = np.random.randint(1, 500, size=ARRAY_SIZE)
    mean = np.mean(array)
    std = np.std(array)

    fig, ax = plt.subplots()
    ax.hist(array, bins='auto')
    ax.set_title('Histogram of Random Values')
    ax.set_xlabel('Val')
    ax.set_ylabel('Freq')
    return array, mean, std, ax

class TestTaskFunc(unittest.TestCase):

    def test_array_size(self):
        """Test if the generated array has the correct size."""
        array, mean, std, ax = task_func()
        self.assertEqual(array.size, ARRAY_SIZE)

    def test_mean_value_range(self):
        """Test if the mean is within the expected range of the generated random integers."""
        array, mean, std, ax = task_func()
        self.assertGreaterEqual(mean, 1)
        self.assertLessEqual(mean, 500)

    def test_std_value_non_negative(self):
        """Test that the standard deviation is non-negative."""
        array, mean, std, ax = task_func()
        self.assertGreaterEqual(std, 0)

    def test_histogram_title(self):
        """Test if the histogram title is correctly set."""
        array, mean, std, ax = task_func()
        self.assertEqual(ax.get_title(), 'Histogram of Random Values')

    def test_axes_labels(self):
        """Test if the axes labels are correctly set."""
        array, mean, std, ax = task_func()
        self.assertEqual(ax.get_xlabel(), 'Val')
        self.assertEqual(ax.get_ylabel(), 'Freq')

if __name__ == '__main__':
    unittest.main()