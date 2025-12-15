import collections
import random
import unittest

# Constants from the original prompt
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# The test suite for the task_func
class TestTaskFunc(unittest.TestCase):
    
    def test_empty_input(self):
        """
        Test the function with n_keys = 0 and n_values = 0.
        Expect an empty dictionary output.
        """
        result = task_func(0, 0)
        self.assertEqual(result, {})
    
    def test_single_key_with_multiple_values(self):
        """
        Test the function with n_keys = 1 and n_values = 5.
        Expect a dictionary with one key and a list of 5 integers as the value.
        """
        random.seed(1)  # Set seed for reproducibility
        result = task_func(1, 5)
        self.assertEqual(len(result), 1)
        self.assertTrue(list(result.values())[0] == [1, 2, 3, 4, 5])
        self.assertIn(list(result.keys())[0], LETTERS)

    def test_multiple_keys_with_same_values(self):
        """
        Test the function with n_keys = 3 and n_values = 5.
        Expect three keys where each has the same list of consecutive integers.
        """
        random.seed(2)  # Set seed for reproducibility
        result = task_func(3, 5)
        self.assertEqual(len(result), 3)
        for value in result.values():
            self.assertEqual(value, [1, 2, 3, 4, 5])
    
    def test_key_selection_from_letters(self):
        """
        Test that all generated keys are from the predefined LETTERS list.
        """
        n_keys = 5
        n_values = 3
        random.seed(3)  # Set seed for reproducibility
        result = task_func(n_keys, n_values)
        self.assertTrue(all(key in LETTERS for key in result.keys()))

    def test_nonexistent_key(self):
        """
        Test the case where the number of keys requested exceeds the available unique keys in LETTERS.
        Since LETTERS has 10 unique keys, request for 15 keys should still result in unique keys only.
        """
        n_keys = 15
        n_values = 1
        random.seed(4)  # Set seed for reproducibility
        result = task_func(n_keys, n_values)
        self.assertEqual(len(result), len(set(result.keys())))  # Ensure all keys are unique

# This part allows running the tests if the script is executed directly
if __name__ == '__main__':
    unittest.main()