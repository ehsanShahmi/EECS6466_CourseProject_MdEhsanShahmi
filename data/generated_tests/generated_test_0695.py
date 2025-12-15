import unittest
import numpy as np
from sklearn.decomposition import PCA

def task_func(tuples_list, n_components):
    """
    Perform Principal Component Analysis (PCA) on a list of tuples.
    
    Parameters:
    - tuples_list (list): The list of tuples.
    
    Returns:
    - transformed_data (ndarray): The transformed data.
    """
    data = np.array(tuples_list)
    pca = PCA(n_components=n_components)
    transformed_data = pca.fit_transform(data)

    return transformed_data

class TestTaskFunc(unittest.TestCase):

    def test_basic_functionality(self):
        data = task_func([(1, 2), (3, 4), (5, 6)], 1)
        expected_shape = (3, 1)
        self.assertEqual(data.shape, expected_shape)

    def test_max_components(self):
        data = task_func([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 3)
        expected_shape = (3, 3)
        self.assertEqual(data.shape, expected_shape)

    def test_zero_components(self):
        with self.assertRaises(ValueError):
            task_func([(1, 2), (3, 4), (5, 6)], 0)

    def test_negative_components(self):
        with self.assertRaises(ValueError):
            task_func([(1, 2), (3, 4), (5, 6)], -1)

    def test_identical_points(self):
        data = task_func([(1, 1), (1, 1), (1, 1)], 1)
        expected = np.array([[0], [0], [0]])
        np.testing.assert_array_almost_equal(data, expected)

if __name__ == '__main__':
    unittest.main()