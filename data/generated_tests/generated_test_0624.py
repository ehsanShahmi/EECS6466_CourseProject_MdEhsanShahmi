from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
import unittest

# Constants
N_COMPONENTS = 2

# Here is your prompt:
# from sklearn.decomposition import PCA
# import numpy as np
# import matplotlib.pyplot as plt
#
# Constants
# N_COMPONENTS = 2
#
#
# def task_func(L):
#     """
#     Convert a list of lists 'L' into a 2D numeric array, apply PCA to it and return the PCA result and scatter plot.
#
#     Requirements:
#     - numpy
#     - sklearn.decomposition
#     - matplotlib.pyplot
#
#     Parameters:
#     L (list of lists): A list of lists where each sublist contains integers.
#
#     Returns:
#     tuple: A tuple containing the PCA result (numpy array) and the scatter plot (matplotlib Axes object).
#
#     Example:
#     >>> pca_result, plot = task_func([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#     >>> type(pca_result)
#     <class 'numpy.ndarray'>
#     """
#
#                 data = np.array(L)
#
#     pca = PCA(n_components=N_COMPONENTS)
#     pca_result = pca.fit_transform(data)
#
#     fig, ax = plt.subplots()
#     ax.scatter(pca_result[:,0], pca_result[:,1])
#
#     return pca_result, ax

class TestTaskFunc(unittest.TestCase):

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            task_func([])

    def test_single_point(self):
        pca_result, plot = task_func([[1, 2, 3]])
        self.assertEqual(pca_result.shape, (1, N_COMPONENTS))

    def test_two_points(self):
        pca_result, plot = task_func([[1, 2, 3], [4, 5, 6]])
        self.assertEqual(pca_result.shape, (2, N_COMPONENTS))

    def test_multiple_points(self):
        pca_result, plot = task_func([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
        self.assertEqual(pca_result.shape, (4, N_COMPONENTS))

    def test_correct_output_type(self):
        pca_result, plot = task_func([[1, 2], [3, 4], [5, 6]])
        self.assertIsInstance(pca_result, np.ndarray)
        self.assertIsInstance(plot, plt.Axes)

if __name__ == '__main__':
    unittest.main()