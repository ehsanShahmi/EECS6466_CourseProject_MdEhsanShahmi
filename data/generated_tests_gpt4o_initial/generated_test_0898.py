from collections import Counter
import random
import unittest

LETTERS = ['a', 'b', 'c', 'd', 'e']

def task_func(count, seed=0):
    """
    Generate a specific number of random letter pairs, each from a predefined list, and analyze the frequency of each pair.

    Parameters:
    - count (int): The number of letter pairs to generate.
    - seed (int, optional): Seed for the random number generator to ensure reproducibility. Defaults to None.

    Returns:
    - Counter: A Counter object representing the frequency of each generated letter pair.

    Requirements:
    - collections.Counter
    - random

    Examples:
    >>> task_func(5, seed=42)
    Counter({('d', 'a'): 1, ('b', 'b'): 1, ('d', 'd'): 1, ('e', 'a'): 1, ('c', 'a'): 1})
    >>> task_func(0, seed=42)
    Counter()
    """
    random.seed(seed)
    pairs = [tuple(random.choices(LETTERS, k=2)) for _ in range(count)]
    pair_frequency = Counter(pairs)
    return pair_frequency

class TestTaskFunc(unittest.TestCase):

    def test_random_pairs_count(self):
        result = task_func(5, seed=42)
        self.assertEqual(sum(result.values()), 5, "The total count of pairs should match the request count")

    def test_empty_case(self):
        result = task_func(0, seed=42)
        self.assertEqual(result, Counter(), "The result for count 0 should be an empty Counter")

    def test_repeatable_output_with_seed(self):
        result1 = task_func(5, seed=42)
        result2 = task_func(5, seed=42)
        self.assertEqual(result1, result2, "The output should be the same for the same seed")

    def test_letter_pairs(self):
        result = task_func(10, seed=0)
        for pair in result.keys():
            self.assertIn(pair[0], LETTERS, "First letter of pair should be one of the predefined letters")
            self.assertIn(pair[1], LETTERS, "Second letter of pair should be one of the predefined letters")

    def test_varied_count(self):
        result_5 = task_func(5, seed=1)
        result_10 = task_func(10, seed=1)
        self.assertGreater(len(result_10), len(result_5), "The output with a larger count should have more key-value pairs")

if __name__ == '__main__':
    unittest.main()