import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import unittest

def task_func(n_samples=1000, mu=0, sigma=1, random_seed=0):
    # Function implementation as provided in the prompt
    if n_samples <= 0 or sigma <= 0:
        raise ValueError("Invalid n_samples or sigma")
    np.random.seed(random_seed)
    plt.figure()
    samples = np.random.normal(mu, sigma, n_samples)
    _, _, _ = plt.hist(samples, 30, density=True)
    ax = plt.gca()
    ax.plot(
        np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000),
        norm.pdf(np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000), mu, sigma),
        linewidth=2,
        color="r",
    )
    return ax, samples

class TestTaskFunc(unittest.TestCase):

    def test_default_parameters(self):
        ax, samples = task_func()
        self.assertEqual(len(samples), 1000)
        self.assertIsInstance(ax, plt.Axes)

    def test_negative_samples(self):
        with self.assertRaises(ValueError):
            task_func(n_samples=-10)

    def test_zero_samples(self):
        with self.assertRaises(ValueError):
            task_func(n_samples=0)

    def test_invalid_sigma(self):
        with self.assertRaises(ValueError):
            task_func(sigma=0)

    def test_custom_parameters(self):
        mu = 5
        sigma = 2
        n_samples = 1500
        ax, samples = task_func(n_samples=n_samples, mu=mu, sigma=sigma)
        self.assertEqual(len(samples), n_samples)
        self.assertAlmostEqual(np.mean(samples), mu, delta=0.5)
        self.assertAlmostEqual(np.std(samples, ddof=1), sigma, delta=0.5)

if __name__ == '__main__':
    unittest.main()