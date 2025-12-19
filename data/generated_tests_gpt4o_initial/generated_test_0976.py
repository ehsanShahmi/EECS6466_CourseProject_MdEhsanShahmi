import numpy as np
import pandas as pd
import unittest

class TestTaskFunc(unittest.TestCase):

    def test_shape_of_output(self):
        data = np.array([[1, 2, 3], [4, 5, 6]])
        df = task_func(data, random_seed=42)
        self.assertEqual(df.shape, (2, 3))

    def test_output_column_names(self):
        data = np.array([[1, 2, 3], [4, 5, 6]])
        df = task_func(data, random_seed=42)
        self.assertTrue(set(df.columns).issubset({'f1', 'f2', 'f3'}))

    def test_value_error_on_non_2d_input(self):
        data = np.array([1, 2, 3])
        with self.assertRaises(ValueError):
            task_func(data)

    def test_output_means_close_to_zero(self):
        data = np.array([[1, 2, 3], [4, 5, 6]])
        df = task_func(data, random_seed=42)
        self.assertAlmostEqual(df.mean().mean(), 0, delta=0.1)

    def test_output_variance_one(self):
        data = np.array([[1, 2, 3], [4, 5, 6]])
        df = task_func(data, random_seed=42)
        self.assertTrue(all(np.isclose(df.var(), 1, atol=0.1)))

if __name__ == '__main__':
    unittest.main()