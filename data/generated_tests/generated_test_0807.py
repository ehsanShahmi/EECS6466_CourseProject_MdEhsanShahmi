import unittest
import numpy as np
from scipy.stats import norm

class TestTaskFunction(unittest.TestCase):
    
    def test_no_outliers(self):
        data = np.array([1, 2, 3, 4, 5])
        outliers, mean, var = task_func(data)
        self.assertEqual(outliers, [])
        self.assertAlmostEqual(mean, 3.0)
        self.assertAlmostEqual(var, 2.0)

    def test_single_outlier(self):
        data = np.array([1, 2, 3, 4, 100])
        outliers, mean, var = task_func(data)
        self.assertEqual(outliers, [4])  # Index of 100
        self.assertAlmostEqual(mean, 22.0)
        self.assertAlmostEqual(var, 898.0)

    def test_multiple_outliers(self):
        data = np.array([-10, 3, 5, 5, 5, 5, 5, 7, 20])
        outliers, mean, var = task_func(data, threshold=4)
        self.assertEqual(outliers, [0, 8])  # Indices of -10 and 20
        self.assertAlmostEqual(mean, 5.0)
        self.assertAlmostEqual(var, 50.888888888888886)

    def test_no_variation(self):
        data = np.array([5, 5, 5, 5])
        outliers, mean, var = task_func(data)
        self.assertEqual(outliers, [])
        self.assertAlmostEqual(mean, 5.0)
        self.assertEqual(var, 0.0)

    def test_float_data_with_outlier(self):
        data = np.array([1.5, 2.5, 2.2, 3.1, 40.0])
        outliers, mean, var = task_func(data)
        self.assertEqual(outliers, [4])  # Index of 40.0
        self.assertAlmostEqual(mean, 9.46)
        self.assertAlmostEqual(var, 563.817)

if __name__ == '__main__':
    unittest.main()