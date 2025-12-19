import random
import math
import unittest

def task_func(LETTERS=[chr(i) for i in range(97, 123)]):
    random_dict = {k: [random.randint(0, 100) for _ in range(random.randint(1, 10))] for k in LETTERS}
    sd_dict = {
        k: math.sqrt(sum((i - sum(v) / len(v)) ** 2 for i in v) / len(v))
        for k, v in random_dict.items()
    }
    return sd_dict

class TestTaskFunc(unittest.TestCase):

    def test_return_type(self):
        result = task_func()
        self.assertIsInstance(result, dict, "The result should be a dictionary.")

    def test_keys_length(self):
        result = task_func()
        self.assertEqual(len(result), 26, "The dictionary should have 26 keys for letters a-z.")

    def test_values_type(self):
        result = task_func()
        for key, value in result.items():
            self.assertIsInstance(value, float, f"The value for key '{key}' should be a float.")

    def test_non_negative_standard_deviation(self):
        result = task_func()
        for key, sd in result.items():
            self.assertGreaterEqual(sd, 0, f"The standard deviation for key '{key}' should be non-negative.")

    def test_bound_standard_deviation(self):
        random.seed(42)  # Seed for reproducibility
        result = task_func()
        for key, sd in result.items():
            self.assertLessEqual(sd, 100, f"The standard deviation for key '{key}' should not exceed 100.")

if __name__ == '__main__':
    unittest.main()