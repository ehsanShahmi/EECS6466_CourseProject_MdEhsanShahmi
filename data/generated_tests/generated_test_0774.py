import unittest
import numpy as np
from task_module import task_func  # Assuming the function is in task_module.py.

class TestTaskFunc(unittest.TestCase):

    def test_default_parameters(self):
        """Test the function with default parameters."""
        mean_score, model = task_func()
        self.assertIsInstance(mean_score, float)
        self.assertIsInstance(model, RandomForestRegressor)

    def test_custom_samples(self):
        """Test the function with custom number of samples."""
        mean_score, model = task_func(num_samples=200)
        self.assertIsInstance(mean_score, float)
        self.assertIsInstance(model, RandomForestRegressor)

    def test_custom_estimators(self):
        """Test the function with a custom number of estimators."""
        mean_score, model = task_func(n_estimators=150)
        self.assertIsInstance(mean_score, float)
        self.assertEqual(model.n_estimators, 150)

    def test_random_seed(self):
        """Test the function with a specific random seed."""
        mean_score1, model1 = task_func(random_seed=42)
        mean_score2, model2 = task_func(random_seed=42)
        self.assertEqual(mean_score1, mean_score2)  # Ensuring same seed yields same results

    def test_invalid_cv_parameter(self):
        """Test the function raises ValueError for invalid cv."""
        with self.assertRaises(ValueError):
            task_func(num_samples=5, cv=3)  # 5 samples with 3 folds is invalid

if __name__ == '__main__':
    unittest.main()