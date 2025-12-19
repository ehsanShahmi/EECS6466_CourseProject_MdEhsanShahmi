import numpy as np
from collections import Counter
import unittest

def task_func(list_of_tuples):
    """
    Computes the sum of numeric values and counts the occurrences of categories in a list of tuples.

    Each tuple in the input list contains a numeric value and a category. This function calculates
    the sum of all the numeric values and also counts how many times each category appears in the list.

    Parameters:
    - list_of_tuples (list of tuple): A list where each tuple contains a numeric value and a category.

    Returns:
    - tuple: A 2-element tuple where the first element is the sum of the numeric values, and the
             second element is a dictionary with categories as keys and their counts as values.

    Requirements:
    - numpy
    - collections.Counter
    """

    numeric_values = [pair[0] for pair in list_of_tuples]
    categories = [pair[1] for pair in list_of_tuples]

    total_sum = np.sum(numeric_values)
    category_counts = Counter(categories)

    return total_sum, dict(category_counts)


class TestTaskFunc(unittest.TestCase):

    def test_multiple_categories(self):
        list_of_tuples = [(5, 'Fruits'), (9, 'Vegetables'), (-1, 'Dairy'), (-2, 'Bakery'), (4, 'Meat')]
        sum_of_values, category_counts = task_func(list_of_tuples)
        self.assertEqual(sum_of_values, 15)
        self.assertEqual(category_counts, {'Fruits': 1, 'Vegetables': 1, 'Dairy': 1, 'Bakery': 1, 'Meat': 1})

    def test_empty_list(self):
        list_of_tuples = []
        sum_of_values, category_counts = task_func(list_of_tuples)
        self.assertEqual(sum_of_values, 0)
        self.assertEqual(category_counts, {})

    def test_negative_values(self):
        list_of_tuples = [(-3, 'Fruits'), (-7, 'Vegetables')]
        sum_of_values, category_counts = task_func(list_of_tuples)
        self.assertEqual(sum_of_values, -10)
        self.assertEqual(category_counts, {'Fruits': 1, 'Vegetables': 1})

    def test_single_category_multiple_entries(self):
        list_of_tuples = [(4, 'Fruits'), (3, 'Fruits'), (2, 'Fruits')]
        sum_of_values, category_counts = task_func(list_of_tuples)
        self.assertEqual(sum_of_values, 9)
        self.assertEqual(category_counts, {'Fruits': 3})

    def test_mixed_categories(self):
        list_of_tuples = [(5, 'Fruits'), (5, 'Fruits'), (-2, 'Dairy'), (4, 'Vegetables')]
        sum_of_values, category_counts = task_func(list_of_tuples)
        self.assertEqual(sum_of_values, 12)
        self.assertEqual(category_counts, {'Fruits': 2, 'Dairy': 1, 'Vegetables': 1})


if __name__ == '__main__':
    unittest.main()