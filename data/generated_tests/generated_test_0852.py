import random
import string
import unittest

def task_func(max_length, n_samples, seed=None):
    """Generate a list containing random strings of lowercase letters. Each string's length varies from 1 to `max_length`.
    An optional seed can be set for the random number generator for reproducible results.

    Note:
    The function utilizes the `random.choices` function to generate random strings and combines them into a list.

    Parameters:
    max_length (int): The maximum length of the strings.
    n_samples (int): The number of strings to return.
    seed (int, optional): A seed for the random number generator. If None, the generator is initialized without a seed.

    Returns:
    list: A list containing random strings. Each string is a random combination of lowercase letters, 
    and their lengths will vary from 1 to `max_length`.

    Requirements:
    - random
    - string

    Raises:
    ValueError: If max_length is smaller than 1.

    Example:
    >>> task_func(3, 12, seed=12)
    ['gn', 'da', 'mq', 'rp', 'aqz', 'ex', 'o', 'b', 'vru', 'a', 'v', 'ncz']
    >>> task_func(5, n_samples=8, seed=1)
    ['ou', 'g', 'tmjf', 'avlt', 's', 'sfy', 'aao', 'rzsn']

    """

    if max_length < 1:
        raise ValueError("max_length must be larger than or equal to 1.")

    LETTERS = string.ascii_lowercase

    if seed is not None:
        random.seed(seed)

    all_combinations = []

    for i in range(n_samples):
        random_length = random.randint(1, max_length)
        combination = ''.join(random.choices(LETTERS, k=random_length))
        all_combinations.append(combination)

    return all_combinations


class TestTaskFunction(unittest.TestCase):
    
    def test_return_type(self):
        result = task_func(5, 10)
        self.assertIsInstance(result, list, "The result should be a list.")
    
    def test_length_of_strings(self):
        max_length = 3
        n_samples = 10
        result = task_func(max_length, n_samples)
        for string in result:
            self.assertLessEqual(len(string), max_length, "Each string should not exceed max_length.")

    def test_min_length_string(self):
        max_length = 5
        n_samples = 10
        result = task_func(max_length, n_samples)
        for string in result:
            self.assertGreaterEqual(len(string), 1, "Each string should have a minimum length of 1.")

    def test_value_error_on_negative_max_length(self):
        with self.assertRaises(ValueError):
            task_func(0, 5)

    def test_consistent_output_with_seed(self):
        max_length = 5
        n_samples = 10
        seed = 42
        result1 = task_func(max_length, n_samples, seed)
        result2 = task_func(max_length, n_samples, seed)
        self.assertEqual(result1, result2, "Output should be consistent when using the same seed.")

if __name__ == '__main__':
    unittest.main()