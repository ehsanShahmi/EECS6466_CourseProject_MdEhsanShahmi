import unittest
import numpy as np
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA

# Here is your prompt:
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA


def task_func(arr):
    """
    Performs Principal Component Analysis (PCA) on the sum of rows of a 2D numpy array and plots the explained variance ratio.

    Note:
    - The title of the plot is set to "Explained Variance Ratio of Principal Components".

    Parameters:
    - arr (numpy.ndarray): A 2D numpy array. The input data for PCA.

    Returns:
    - ax (matplotlib.axes.Axes): An Axes object from matplotlib.

    Requirements:
    - scikit-learn
    - matplotlib

    Notes:
    - The function assumes that 'arr' is a valid 2D numpy array.
    - Only the first principal component is considered in this analysis.
    - The plot illustrates the proportion of the dataset's variance that lies along the axis of this first principal component.
    
    Example:
    >>> import numpy as np
    >>> arr = np.array([[i+j for i in range(3)] for j in range(5)])
    >>> axes = task_func(arr)
    >>> axes.get_title()
    'Explained Variance Ratio of Principal Components'
    """

    row_sums = arr.sum(axis=1)
    pca = PCA(n_components=1)
    pca.fit(row_sums.reshape(-1, 1))

    # Plotting (requires matplotlib and sklearn)

    _, ax = plt.subplots()
    ax.bar([0], pca.explained_variance_ratio_)
    ax.set_title("Explained Variance Ratio of Principal Components")
    ax.set_xticks([0])
    ax.set_xticklabels(["PC1"])

    return ax


class TestTaskFunc(unittest.TestCase):

    def test_shape_of_input_array(self):
        arr = np.array([[1, 2, 3], [4, 5, 6]])
        self.assertEqual(arr.shape, (2, 3))

    def test_pca_explained_variance_ratio(self):
        arr = np.array([[1, 2, 3], [4, 5, 6]])
        axes = task_func(arr)
        self.assertAlmostEqual(axes.patches[0].get_height(), 1.0)

    def test_plot_title(self):
        arr = np.array([[1, 2], [3, 4]])
        axes = task_func(arr)
        self.assertEqual(axes.get_title(), "Explained Variance Ratio of Principal Components")

    def test_input_with_zeros(self):
        arr = np.array([[0, 0, 0], [0, 0, 0]])
        axes = task_func(arr)
        self.assertAlmostEqual(axes.patches[0].get_height(), 0.0)

    def test_column_sum_input(self):
        arr = np.array([[1, 3, 5], [2, 4, 6]])
        axes = task_func(arr)
        self.assertAlmostEqual(axes.patches[0].get_height(), 1.0)

if __name__ == '__main__':
    unittest.main()