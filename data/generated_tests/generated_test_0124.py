import unittest
from random import randint

class TestTaskFunction(unittest.TestCase):

    def test_invalid_type_for_my_list(self):
        with self.assertRaises(TypeError):
            task_func("not_a_list")

    def test_invalid_elements_in_my_list(self):
        with self.assertRaises(ValueError):
            task_func([1, 2, "three"])

    def test_empty_list(self):
        time_taken, ax = task_func([])
        self.assertIsInstance(time_taken, float)
        self.assertEqual(ax.get_title(), 'Histogram of Random Numbers')

    def test_list_with_numeric_elements(self):
        my_list = [1, 2, 3]
        time_taken, ax = task_func(my_list)
        self.assertIsInstance(time_taken, float)
        self.assertTrue(1 <= len(ax.patches) <= 20)  # Checking bar count for histogram

    def test_size_limit_exceedance(self):
        my_list = [30] * 10  # This would sum to 300
        time_taken, ax = task_func(my_list, size=100)
        self.assertIsInstance(time_taken, float)
        self.assertTrue(len(ax.patches) <= 20)  # Maximum histogram bars should be within limit

if __name__ == '__main__':
    unittest.main()