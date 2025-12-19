import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import unittest


class TestTaskFunc(unittest.TestCase):

    def test_default_parameters(self):
        ax, mean, std = task_func()
        self.assertIsInstance(ax, plt.Axes)
        self.assertAlmostEqual(mean, 0, delta=0.1)
        self.assertAlmostEqual(std, 1, delta=0.1)

    def test_custom_parameters(self):
        mu = 5
        sigma = 2
        sample_size = 500
        ax, mean, std = task_func(mu, sigma, sample_size)
        self.assertIsInstance(ax, plt.Axes)
        self.assertAlmostEqual(mean, mu, delta=0.1)
        self.assertAlmostEqual(std, sigma, delta=0.1)

    def test_sample_size_zero(self):
        with self.assertRaises(ValueError):
            task_func(sample_size=0)

    def test_negative_sigma(self):
        with self.assertRaises(ValueError):
            task_func(sigma=-1)

    def test_fixed_seed_reproducibility(self):
        seed = 123
        mu = 2
        sigma = 3
        ax1, mean1, std1 = task_func(mu, sigma, seed=seed)
        ax2, mean2, std2 = task_func(mu, sigma, seed=seed)
        np.testing.assert_array_equal(ax1.patches, ax2.patches)
        self.assertAlmostEqual(mean1, mean2, delta=0.01)
        self.assertAlmostEqual(std1, std2, delta=0.01)


if __name__ == '__main__':
    unittest.main()