import numpy as np
import unittest

# Here is your prompt:
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def task_func(num_samples=500, noise_strength=1, random_seed=None, test_size=0.2):
    """
    Generate a dataset with a single feature and a target variable. The target
    is computed from the feature using a linear relation.
    In addition some gaussian noise (random samples from normal distributioin), scaled by
    noise_strength, is added to the target. The dataset is split into training
    and test sets. Then a linear regression model is adjusted to the training
    set and the R-squared score is calculated on the test set.

    Parameters:
    - num_samples (int): The number of samples to generate for the dataset.
                   Defaults to 500
    - noise_strength (float): The strength (magnitude) of the noise that is
                              added to the dataset. Defaults to 1
    - random_seed (int): The seed used in generating the dataset, in performing
                   the train test split and in generating the random noise.
                   Defaults to None
    - test_size (float): The fraction of the test split. Defaults to 0.2

    Returns:
    float: The R-squared score of the fitted model on the test set.
    LinearRegression: The trained linear regression model.

    Raises:
    - ValueError: If test set size is smaller than 2.

    Requirements:
    - numpy
    - pandas
    - sklearn.model_selection.train_test_split
    - sklearn.linear_model.LinearRegression

    Example:
    >>> task_func(num_samples=10, noise_strength=23.5, random_seed=24, test_size=0.3)
    (-0.4892453918038726, LinearRegression())
    >>> task_func(noise_strength=0.1)
    (0.9658328575162494, LinearRegression())
    """


class TestTaskFunc(unittest.TestCase):

    def test_return_type(self):
        r_squared, model = task_func(num_samples=100, noise_strength=1, random_seed=42, test_size=0.2)
        self.assertIsInstance(r_squared, float, "R-squared score should be a float")
        self.assertIsInstance(model, LinearRegression, "Returned model should be an instance of LinearRegression")

    def test_r_squared_range(self):
        r_squared, _ = task_func(num_samples=1000, noise_strength=1, random_seed=42, test_size=0.2)
        self.assertGreaterEqual(r_squared, -1, "R-squared score should be greater or equal to -1")
        self.assertLessEqual(r_squared, 1, "R-squared score should be less or equal to 1")

    def test_value_error_on_small_test_size(self):
        with self.assertRaises(ValueError):
            task_func(num_samples=3, noise_strength=1, random_seed=42, test_size=0.8)

    def test_different_noise_strength(self):
        r_squared_1, _ = task_func(num_samples=100, noise_strength=0.1, random_seed=42, test_size=0.2)
        r_squared_2, _ = task_func(num_samples=100, noise_strength=10, random_seed=42, test_size=0.2)
        self.assertNotEqual(r_squared_1, r_squared_2, "Different noise strengths should yield different R-squared values")

    def test_consistent_results_with_fixed_seed(self):
        r_squared_1, _ = task_func(num_samples=100, noise_strength=1, random_seed=42, test_size=0.2)
        r_squared_2, _ = task_func(num_samples=100, noise_strength=1, random_seed=42, test_size=0.2)
        self.assertEqual(r_squared_1, r_squared_2, "Fixed seed should produce consistent results")

if __name__ == '__main__':
    unittest.main()