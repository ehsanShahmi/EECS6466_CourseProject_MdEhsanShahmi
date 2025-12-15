from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
import unittest

def task_func(l):
    """
    Perform Principal Component Analysis (PCA) on the given array and record the first two main components.

    Parameters:
    l (numpy array): The input array.

    Returns:
    ax (matplotlib.axes._axes.Axes): Axes object of the generated plot

    Note:
    - This function use "PCA Result" as the title of the plot.
    - This function use "First Principal Component" and "Second Principal Component" as the xlabel 
    and ylabel of the plot, respectively.

    Requirements:
    - sklearn.decomposition.PCA
    - matplotlib.pyplot

    Example:
    >>> import numpy as np
    >>> l = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    >>> ax = task_func(l)
    >>> len(ax.collections[0].get_offsets())
    4
    >>> print(ax.get_title())
    PCA Result
    >>> plt.close()
    """
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(l)

    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot(111)
    plt.scatter(principalComponents[:, 0], principalComponents[:, 1])
    plt.xlabel('First Principal Component')
    plt.ylabel('Second Principal Component')
    plt.title('PCA Result')

    return ax

class TestPCAFunction(unittest.TestCase):

    def test_shape_of_output(self):
        l = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
        ax = task_func(l)
        self.assertEqual(len(ax.collections[0].get_offsets()), 4)

    def test_plot_title(self):
        l = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
        ax = task_func(l)
        self.assertEqual(ax.get_title(), 'PCA Result')
    
    def test_xlabel(self):
        l = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
        ax = task_func(l)
        self.assertEqual(ax.get_xlabel(), 'First Principal Component')

    def test_ylabel(self):
        l = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
        ax = task_func(l)
        self.assertEqual(ax.get_ylabel(), 'Second Principal Component')

    def test_pca_output_shape(self):
        l = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
        pca = PCA(n_components=2)
        principalComponents = pca.fit_transform(l)
        self.assertEqual(principalComponents.shape, (4, 2))

if __name__ == '__main__':
    unittest.main()