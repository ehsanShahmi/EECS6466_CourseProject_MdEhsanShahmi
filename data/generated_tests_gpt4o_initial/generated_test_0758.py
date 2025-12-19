import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import unittest

# Here is your prompt:
def task_func(num_samples, countries=['Russia', 'China', 'USA', 'India', 'Brazil'], 
               ages=np.arange(18, 60), genders=['Male', 'Female'], rng_seed=None):
    """
    Generate a demographic dataset with information about people from different countries, their age, and gender. 
    Genders are encoded using sklearn LabelEncoder.
    Datapoints are sampled from the lists using a numpy.random.default_rng with seed: rng_seed.

    Parameters:
    num_samples (int): The number of samples to generate.
    countries (list of str): A list of country names to use in the dataset. Default is ['Russia', 'China', 'USA', 'India', 'Brazil'].
    ages (array of int): An array of ages to use in the dataset. Default is np.arange(18, 60).
    genders (list of str): A list of genders to use in the dataset. Default is ['Male', 'Female'].
    rng_seed: seed for the random number generator
    
    Returns:
    DataFrame: A pandas DataFrame with the demographics data.

    Raises:
    - ValueError: If num_samples is not an integer.

    Requirements:
    - pandas
    - numpy
    - sklearn.preprocessing.LabelEncoder

    Example:
    >>> demographics = task_func(5, rng_seed=31)
    >>> print(demographics)
      Country  Age  Gender
    0     USA   46       0
    1  Brazil   21       1
    2     USA   37       1
    3  Russia   32       1
    4     USA   46       0

    >>> demographics = task_func(5, countries=['Austria', 'Germany'], rng_seed=3)
    >>> print(demographics)
       Country  Age  Gender
    0  Germany   51       1
    1  Austria   54       1
    2  Austria   42       0
    3  Austria   19       1
    4  Austria   21       1
    """

    if not isinstance(num_samples, int):
        raise ValueError("num_samples should be an integer.")

    rng = np.random.default_rng(seed=rng_seed)
    countries = rng.choice(countries, num_samples)
    ages = rng.choice(ages, num_samples)
    genders = rng.choice(genders, num_samples)

    le = LabelEncoder()
    encoded_genders = le.fit_transform(genders)

    demographics = pd.DataFrame({
        'Country': countries,
        'Age': ages,
        'Gender': encoded_genders
    })

    return demographics

class TestTaskFunc(unittest.TestCase):
    def test_output_type(self):
        result = task_func(5)
        self.assertIsInstance(result, pd.DataFrame)

    def test_correct_number_of_samples(self):
        num_samples = 10
        result = task_func(num_samples)
        self.assertEqual(result.shape[0], num_samples)

    def test_age_range(self):
        num_samples = 5
        result = task_func(num_samples)
        self.assertTrue((result['Age'] >= 18).all() and (result['Age'] < 60).all())

    def test_gender_encoding(self):
        num_samples = 5
        result = task_func(num_samples)
        self.assertTrue(set(result['Gender'].unique()).issubset({0, 1}))

    def test_invalid_num_samples(self):
        with self.assertRaises(ValueError):
            task_func("invalid")

# Run the test suite
if __name__ == '__main__':
    unittest.main()