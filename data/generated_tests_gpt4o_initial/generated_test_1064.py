import unittest
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Here is your prompt:
def task_func(arr):
    """
    Plots a heatmap of a given 2D numerical array and prints the sum of each row.
    The heatmap's color range is set based on the minimum and maximum values in the array.

    Parameters:
    arr (numpy.array): A 2D numpy array of numerical values.

    Returns:
    ax (matplotlib.axes.Axes): The Axes object with the plotted heatmap.

    Requirements:
    - numpy
    - seaborn

    Note:
    The function calculates the sum of each row and prints these values.
    The heatmap is plotted based on the original array with its color range set from the minimum to the maximum value in the array.

    Example:
    >>> arr = np.array([[i + j for i in range(3)] for j in range(5)])
    >>> ax = task_func(arr)
    >>> ax.get_title()
    'Heatmap of the 2D Array'
    """

    row_sums = arr.sum(axis=1)
    vmax = np.max(arr)  # Set vmax to the maximum value in the array
    vmin = np.min(arr)  # Set vmin to the minimum value in the array
    ax = sns.heatmap(
        arr, annot=True, vmax=vmax, vmin=vmin
    )  # Include both vmin and vmax in the heatmap call
    ax.set_title("Heatmap of the 2D Array")

    return ax

class TestTaskFunc(unittest.TestCase):
    def test_shape_of_array(self):
        arr = np.array([[1, 2], [3, 4]])
        ax = task_func(arr)
        self.assertEqual(arr.shape, (2, 2))

    def test_row_sums(self):
        arr = np.array([[1, 2, 3], [4, 5, 6]])
        with self.assertLogs(level='INFO') as log:
            task_func(arr)
            self.assertIn('INFO:root:Row sums: [ 6 15]', log.output)

    def test_vmin_and_vmax(self):
        arr = np.array([[10, 15], [20, 30]])
        ax = task_func(arr)
        self.assertEqual(ax.collections[0].get_clim(), (10, 30))

    def test_plot_title(self):
        arr = np.array([[1, 2], [3, 4]])
        ax = task_func(arr)
        self.assertEqual(ax.get_title(), "Heatmap of the 2D Array")

    def test_heatmap_visualization(self):
        arr = np.array([[1, 1], [1, 1]])
        ax = task_func(arr)
        plt.close()
        self.assertIsInstance(ax, plt.Axes)

if __name__ == '__main__':
    unittest.main()