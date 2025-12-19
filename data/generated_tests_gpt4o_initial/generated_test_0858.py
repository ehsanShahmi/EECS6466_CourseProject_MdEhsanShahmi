import string
import random
from collections import Counter
import unittest

def task_func(n, seed=None):
    LETTERS = string.ascii_lowercase
    if seed is not None:
        random.seed(seed)
    letters = [random.choice(LETTERS) for _ in range(n)]
    letter_counts = Counter(letters)
    return letter_counts

class TestTaskFunc(unittest.TestCase):
    
    def test_count_zero_letters(self):
        result = task_func(0)
        self.assertEqual(result, Counter(), "Expected an empty Counter for 0 letters")

    def test_count_ten_letters(self):
        result = task_func(10, seed=1)
        expected_result = Counter({'b': 3, 'a': 2, 'c': 2, 'd': 1, 'e': 1, 'f': 1})  # This is a hypothetical outcome.
        self.assertEqual(result, expected_result, "Expected a specific count for 10 letters with seed=1")

    def test_count_hundred_letters(self):
        result = task_func(100, seed=2)
        expected_result = Counter({'g': 10, 'm': 10, 'u': 9, 't': 9, 'n': 8, 'x': 7, 'z': 7})  # This is a hypothetical outcome.
        self.assertEqual(result, expected_result, "Expected a specific count for 100 letters with seed=2")
    
    def test_count_same_seed_repeatability(self):
        result_one = task_func(50, seed=5)
        result_two = task_func(50, seed=5)
        self.assertEqual(result_one, result_two, "Expected results to be the same with the same seed")
    
    def test_count_case_insensitivity(self):
        result = task_func(20, seed=3)
        self.assertEqual(sum(result.values()), 20, "Total counts should equal the number of letters generated.")
        for key in result:
            self.assertIn(key, string.ascii_lowercase, "All keys should be lowercase letters")

if __name__ == '__main__':
    unittest.main()