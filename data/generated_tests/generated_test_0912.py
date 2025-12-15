from collections import Counter
import itertools
import unittest

def task_func(letters: list, repetitions: int) -> dict:
    """
    Count the frequency of each letter in a list after repeating it a given number of times.

    Parameters:
    - letters (list): A list of single-character strings representing letters.
    - repetitions (int): The number of times to repeat the list.

    Returns:
    Returns a dictionary where the keys are the letters and the values are their frequencies.

    Requirements:
    - collections.Counter
    - itertools

    Example:
    >>> task_func(['A', 'B', 'C'], 2)
    {'A': 2, 'B': 2, 'C': 2}
    >>> task_func(['A', 'B'], 3)
    {'A': 3, 'B': 3}
    """
    flattened_list = list(itertools.chain(*[letters for _ in range(repetitions)]))
    counts = dict(Counter(flattened_list))
    return counts

class TestTaskFunc(unittest.TestCase):
    
    def test_repeating_letters(self):
        result = task_func(['A', 'B', 'C'], 2)
        expected = {'A': 2, 'B': 2, 'C': 2}
        self.assertEqual(result, expected)

    def test_multiple_repetitions(self):
        result = task_func(['A', 'B'], 3)
        expected = {'A': 3, 'B': 3}
        self.assertEqual(result, expected)

    def test_empty_list(self):
        result = task_func([], 5)
        expected = {}
        self.assertEqual(result, expected)

    def test_single_letter(self):
        result = task_func(['A'], 4)
        expected = {'A': 4}
        self.assertEqual(result, expected)

    def test_varied_characters(self):
        result = task_func(['A', 'B', 'C', 'D'], 1)
        expected = {'A': 1, 'B': 1, 'C': 1, 'D': 1}
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()