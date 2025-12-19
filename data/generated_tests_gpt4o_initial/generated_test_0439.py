import unittest
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class TestTaskFunction(unittest.TestCase):

    def test_product_shape(self):
        P = np.array([[1, 2, 3], [4, 5, 6]])
        T = np.random.rand(3, 3, 3)
        product, heatmap = task_func(P, T)
        self.assertEqual(product.shape, (2, 3, 3), "Product shape should be (2, 3, 3)")

    def test_type_error_on_invalid_P(self):
        P = [[1, 2, 3], [4, 5, 6]]  # List instead of ndarray
        T = np.random.rand(3, 3, 3)
        with self.assertRaises(TypeError):
            task_func(P, T)

    def test_type_error_on_invalid_T(self):
        P = np.array([[1, 2, 3], [4, 5, 6]])
        T = "invalid"  # String instead of ndarray
        with self.assertRaises(TypeError):
            task_func(P, T)

    def test_heatmap_output_type(self):
        P = np.array([[1, 2, 3], [4, 5, 6]])
        T = np.random.rand(3, 3, 3)
        product, heatmap = task_func(P, T)
        self.assertIsInstance(heatmap, plt.Axes, "The heatmap output should be a matplotlib Axes object")

    def test_heatmap_visualization(self):
        P = np.array([[1, 2, 3], [4, 5, 6]])
        T = np.random.rand(3, 3, 3)
        product, heatmap = task_func(P, T)
        plt.close()  # Close the plot after visualizing to avoid displaying during tests

if __name__ == '__main__':
    unittest.main()