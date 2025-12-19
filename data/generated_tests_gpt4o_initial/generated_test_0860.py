import re
import random
import string
import unittest

def task_func(n, pattern, seed=None):
    """
    Generate a random string of length 'n' and find all non-overlapping matches
    of the regex 'pattern'.

    The function generates a random string of ASCII Letters and Digits using 
    the random module. By providing a seed the results are reproducible.
    Non overlapping matches of the provided pattern are then found using the re
    module.
    
    Parameters:
    n (int): The length of the random string to be generated.
    pattern (str): The regex pattern to search for in the random string.
    seed (int, optional): A seed parameter for the random number generator for reproducible results. Defaults to None.

    Returns:
    list: A list of all non-overlapping matches of the regex pattern in the generated string.
    """

    if seed is not None:
        random.seed(seed)
    rand_str = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(n))
    matches = re.findall(pattern, rand_str)
    return matches

class TestTaskFunc(unittest.TestCase):

    def test_length_of_matches(self):
        result = task_func(100, r'[A-Za-z]{5}', seed=12345)
        self.assertEqual(len(result), 12)

    def test_non_overlapping_matches(self):
        result = task_func(100, r'[A-Za-z]{5}', seed=12345)
        # Check if any match occurs more than once
        self.assertEqual(len(result), len(set(result)))

    def test_seed_reproducibility(self):
        result1 = task_func(100, r'[0-9]{2}', seed=42)
        result2 = task_func(100, r'[0-9]{2}', seed=42)
        self.assertEqual(result1, result2)

    def test_empty_result_for_no_matches(self):
        result = task_func(10, r'[A-Za-z]{5}', seed=54)
        # Since the length is small, the regex may not match anything
        self.assertTrue(all(len(match) < 5 for match in result))

    def test_pattern_with_digits(self):
        result = task_func(1000, r'[1-9]{2}', seed=1)
        # Check that there aren't any matches with '0' in it
        for match in result:
            self.assertNotIn('0', match)

if __name__ == '__main__':
    unittest.main()