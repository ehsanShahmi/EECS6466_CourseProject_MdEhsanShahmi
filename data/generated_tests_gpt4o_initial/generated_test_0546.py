from collections import OrderedDict
from prettytable import PrettyTable
import unittest

def task_func(my_dict):
    """
    Sorts a given dictionary by its keys in ascending order and returns a PrettyTable object displaying the sorted items with the names 'Key' and 'Value'.

    Parameters:
    my_dict (dict): The dictionary to be sorted and displayed.

    Returns:
    PrettyTable: A PrettyTable object representing the sorted dictionary.

    Requirements:
    - collections.OrderedDict
    - prettytable.PrettyTable

    Examples:
    Display a simple dictionary in a sorted table format.
    >>> table = task_func({3: 'apple', 1: 'banana', 2: 'cherry'})
    >>> str(table).startswith('+') and 'banana' in str(table)
    True

    Display an empty dictionary.
    >>> str(task_func({})).startswith('+')
    True
    """

    ordered_dict = OrderedDict(sorted(my_dict.items(), key=lambda t: t[0]))
    table = PrettyTable(['Key', 'Value'])

    for key, value in ordered_dict.items():
        table.add_row([key, value])

    return table

class TestTaskFunc(unittest.TestCase):
    
    def test_sorted_table_with_integers(self):
        table = task_func({3: 'apple', 1: 'banana', 2: 'cherry'})
        self.assertTrue(str(table).startswith('+'))
        self.assertIn('banana', str(table))

    def test_empty_dictionary(self):
        table = task_func({})
        self.assertTrue(str(table).startswith('+'))
        self.assertNotIn('Key', str(table))
        self.assertNotIn('Value', str(table))

    def test_sorted_table_with_strings(self):
        table = task_func({'b': 4, 'c': 2, 'a': 5})
        self.assertTrue(str(table).startswith('+'))
        self.assertIn('4', str(table))
        self.assertIn('5', str(table))

    def test_single_element_dictionary(self):
        table = task_func({1: 'only'})
        self.assertTrue(str(table).startswith('+'))
        self.assertIn('only', str(table))

    def test_table_with_negative_keys(self):
        table = task_func({-1: 'minus', 0: 'zero', 1: 'plus'})
        self.assertTrue(str(table).startswith('+'))
        self.assertIn('minus', str(table))
        self.assertIn('zero', str(table))
        self.assertIn('plus', str(table))

if __name__ == '__main__':
    unittest.main()