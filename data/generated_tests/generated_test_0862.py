import random
import string
from collections import defaultdict
import unittest

def task_func(n, seed=None):
    """
    Generate a dictionary with lists of random lowercase english letters. 
    
    Each key in the dictionary  represents a unique letter from the alphabet,
    and the associated value is a list, containing randomly generated instances
    of that letter based on a seed.

    The function randomly selects 'n' letters from the alphabet (a-z) and places each 
    occurrence in the corresponding list within the dictionary. The randomness is based
    on the provided seed value; the same seed will produce the same distribution of letters.

    The dictionary has only those keys for which a letter was generated.

    Parameters:
    n (int): The number of random letters to generate.
    seed (int, optional): A seed value for the random number generator. If None, the randomness
                          is based on system time or the OS's randomness source.

    Returns:
    defaultdict: A dictionary where the keys are characters ('a' to 'z') and the values 
                 are lists of randomly generated letters. Each list may have 0 to 'n' occurrences of 
                 its associated letter, depending on the randomness and seed.

    Requirements:
    - collections.defaultdict
    - random
    - string

    Example:
    >>> task_func(5, seed=123)
    defaultdict(<class 'list'>, {'b': ['b'], 'i': ['i'], 'c': ['c'], 'y': ['y'], 'n': ['n']})

    >>> task_func(30, seed=1)
    defaultdict(<class 'list'>, {'e': ['e'], 's': ['s'], 'z': ['z', 'z', 'z'], 'y': ['y', 'y', 'y', 'y'], 'c': ['c'], 'i': ['i', 'i'], 'd': ['d', 'd'], 'p': ['p', 'p', 'p'], 'o': ['o', 'o'], 'u': ['u'], 'm': ['m', 'm'], 'g': ['g'], 'a': ['a', 'a'], 'n': ['n'], 't': ['t'], 'w': ['w'], 'x': ['x'], 'h': ['h']})
    """

    LETTERS = string.ascii_lowercase
    random.seed(seed)
    letter_dict = defaultdict(list)
    for _ in range(n):
        letter = random.choice(LETTERS)
        letter_dict[letter].append(letter)
    return letter_dict


class TestTaskFunc(unittest.TestCase):

    def test_empty_case(self):
        result = task_func(0)
        self.assertEqual(result, defaultdict(list), "Should return an empty defaultdict when n is 0")

    def test_single_letter_case(self):
        result = task_func(1, seed=42)
        self.assertIn(result.keys(), string.ascii_lowercase, "The keys of the result should be lowercase letters")
        self.assertEqual(sum(len(v) for v in result.values()), 1, "The total number of letters should equal 1")

    def test_random_case_with_fixed_seed(self):
        result = task_func(5, seed=123)
        expected_output = defaultdict(list, {'b': ['b'], 'i': ['i'], 'c': ['c'], 'y': ['y'], 'n': ['n']})
        self.assertEqual(result, expected_output, "The output should match the expected output with the same seed")

    def test_large_n_case(self):
        result = task_func(100, seed=1)
        total_letters = sum(len(v) for v in result.values())
        self.assertEqual(total_letters, 100, "The total number of letters should equal 100")

    def test_case_with_no_seed(self):
        result = task_func(10)
        self.assertTrue(isinstance(result, defaultdict), "Result should be a defaultdict")
        self.assertGreaterEqual(len(result), 1, "There should be at least one key in the result")

if __name__ == '__main__':
    unittest.main()