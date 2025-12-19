import random
from collections import Counter
import unittest

def task_func(values, weights, n_samples):
    samples = random.choices(values, weights=weights, k=n_samples)
    histogram = dict(Counter(samples))
    return histogram

class TestTaskFunc(unittest.TestCase):
    def test_basic_functionality(self):
        random.seed(42)
        result = task_func([1, 2, 3], [3, 2, 1], 1000)
        expected_result = {1: 480, 2: 342, 3: 178}
        self.assertEqual(result, expected_result)

    def test_zero_samples(self):
        result = task_func([1, 2, 3], [3, 2, 1], 0)
        expected_result = {}
        self.assertEqual(result, expected_result)

    def test_uniform_weights(self):
        random.seed(42)
        result = task_func(['a', 'b', 'c'], [1, 1, 1], 3000)
        self.assertTrue(all(count >= 900 and count <= 1200 for count in result.values()))

    def test_different_value_types(self):
        random.seed(42)
        result = task_func([1.5, 2.5, 3.5], [1, 1, 1], 1000)
        self.assertTrue(set(result.keys()).issubset({1.5, 2.5, 3.5}))

    def test_large_numbers(self):
        random.seed(42)
        values = list(range(1000))
        weights = list(range(1, 1001))
        result = task_func(values, weights, 10000)
        self.assertTrue(all(count >= 0 for count in result.values()))

if __name__ == '__main__':
    unittest.main()