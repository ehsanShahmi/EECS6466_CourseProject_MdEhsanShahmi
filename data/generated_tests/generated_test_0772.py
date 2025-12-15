import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import unittest


def task_func(num_samples=1000, k=5, d=2, random_seed=None):
    if random_seed is not None:
        np.random.seed(random_seed)
    data = np.random.randn(num_samples, 1) * k + d
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    mse = mean_squared_error(data, scaled_data)

    return mse


class TestTaskFunc(unittest.TestCase):

    def test_default_parameters(self):
        mse = task_func()
        self.assertIsInstance(mse, float)
        self.assertGreaterEqual(mse, 0)

    def test_negative_k(self):
        mse = task_func(k=-6.4, d=12.1, random_seed=2)
        self.assertIsInstance(mse, float)
        self.assertGreaterEqual(mse, 0)

    def test_zero_transformation(self):
        mse = task_func(k=1, d=0)
        self.assertIsInstance(mse, float)
        self.assertAlmostEqual(mse, 0.001, delta=0.01)

    def test_small_sample_size(self):
        mse = task_func(num_samples=10, k=5, d=2)
        self.assertIsInstance(mse, float)
        self.assertGreaterEqual(mse, 0)

    def test_large_sample_size(self):
        mse = task_func(num_samples=100000, k=5, d=2)
        self.assertIsInstance(mse, float)
        self.assertGreaterEqual(mse, 0)


if __name__ == '__main__':
    unittest.main()