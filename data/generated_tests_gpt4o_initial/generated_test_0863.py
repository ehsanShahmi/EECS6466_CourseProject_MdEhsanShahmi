import unittest
import numpy as np
import math

# Constants
POSSIBLE_NUMBERS = np.arange(1, 11)

# The function to test is assumed to already exist as described in the prompt.
# Thus we will define our test cases solely based on the provided function description.

class TestTaskFunc(unittest.TestCase):

    def test_empty_input(self):
        result = task_func([])
        self.assertEqual(result, [])

    def test_one_empty_list(self):
        result = task_func([[]])
        self.assertEqual(result, [0.0])

    def test_single_list_with_three_elements(self):
        result = task_func([[1, 2, 3]])
        self.assertEqual(result, [14.0])  # 1^2 + 2^2 + 3^2 = 1 + 4 + 9

    def test_multiple_lists_of_incrementing_length(self):
        result = task_func([[1], [1, 2], [1, 2, 3], [1, 2, 3, 4]])
        self.assertEqual(result, [1.0, 5.0, 14.0, 30.0])  # 1, 1^2 + 2^2, 1^2 + 2^2 + 3^2, 1^2 + 2^2 + 3^2 + 4^2

    def test_lists_with_more_elements_than_possible_numbers(self):
        result = task_func([[1, 2, 3], [4, 5, 6, 7, 8, 9, 10]])
        self.assertEqual(result, [14.0, 385.0])  # The first part is from 1 to 3, 2nd from 1 to 10 (all)

if __name__ == '__main__':
    unittest.main()