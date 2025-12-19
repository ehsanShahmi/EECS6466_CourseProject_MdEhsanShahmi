import numpy as np
import matplotlib.pyplot as plt
import unittest

# Constants
BAR_COLOR = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black']

def task_func(data_size):
    """
    Generates random numeric data and creates a histogram of the data.
    The color of the histogram bars is randomly selected from a predefined list.

    Parameters:
    data_size (int): The number of data points to generate.

    Returns:
    tuple:
        - ndarray: The array of randomly generated data.
        - str: The color used for the histogram bars.

    Requirements:
    - numpy
    - matplotlib
    """
    np.random.seed(0)
    data = np.random.randn(data_size)
    color = np.random.choice(BAR_COLOR)
    plt.hist(data, bins=np.arange(-3, 4, 0.5), color=color, edgecolor='black')
    return data, color

class TestTaskFunc(unittest.TestCase):
    def test_data_size(self):
        """Test if the generated data has the correct size."""
        data_size = 10
        data, _ = task_func(data_size)
        self.assertEqual(data.shape[0], data_size)

    def test_color_choice(self):
        """Test if the generated color is from the predefined list."""
        data_size = 5
        _, color = task_func(data_size)
        self.assertIn(color, BAR_COLOR)

    def test_negative_data_size(self):
        """Test if a negative data size raises a ValueError."""
        data_size = -5
        with self.assertRaises(ValueError):
            task_func(data_size)

    def test_zero_data_size(self):
        """Test if a data size of zero returns an empty array."""
        data_size = 0
        data, _ = task_func(data_size)
        self.assertEqual(data.shape[0], 0)

    def test_plot_creation(self):
        """Test if a histogram plot is created without errors."""
        data_size = 20
        try:
            task_func(data_size)
            plt.close()  # Close the figure to prevent display during testing
        except Exception as e:
            self.fail(f"task_func raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()