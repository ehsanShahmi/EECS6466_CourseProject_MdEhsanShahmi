import unittest
from collections import Counter
import itertools
import operator


def task_func(list_of_menuitems):
    """
    Faced with a nested list of menu items, flatten the list and return the most common menu item.

    Parameters:
    - list_of_menuitems (list): A nested list of menu items.

    Returns:
    - str: The most common menu item.

    Requirements:
    - collections
    - itertools
    - operator

    Example:
    >>> task_func([['Pizza', 'Burger'], ['Pizza', 'Coke'], ['Pasta', 'Coke']])
    'Pizza'
    """
    flat_list = list(itertools.chain(*list_of_menuitems))
    counter = Counter(flat_list)
    return max(counter.items(), key=operator.itemgetter(1))[0]


class TestTaskFunc(unittest.TestCase):

    def test_single_nested_list(self):
        self.assertEqual(task_func([['Pizza', 'Burger'], ['Pizza', 'Coke'], ['Pasta', 'Coke']]), 'Pizza')

    def test_multiple_same_items(self):
        self.assertEqual(task_func([['Coke', 'Coke'], ['Pizza', 'Burger'], ['Coke', 'Pasta']]), 'Coke')

    def test_empty_list(self):
        self.assertEqual(task_func([[], []]), None)

    def test_all_unique_items(self):
        self.assertEqual(task_func([['Salad'], ['Burger'], ['Pizza']]), 'Salad')

    def test_tie_case(self):
        self.assertIn(task_func([['Coke', 'Pepsi'], ['Coke'], ['Pepsi']]), ['Coke', 'Pepsi'])


if __name__ == '__main__':
    unittest.main()