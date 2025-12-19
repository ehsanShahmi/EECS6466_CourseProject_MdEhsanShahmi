import unittest
import pandas as pd
from collections import Counter

from your_module import task_func  # Assuming the function resides in a module named 'your_module'

class TestTaskFunction(unittest.TestCase):

    def test_empty_input(self):
        """Test case for empty input list."""
        result = task_func([])
        expected = pd.DataFrame(columns=['Count'])
        self.assertTrue(result.equals(expected))

    def test_single_menu_item(self):
        """Test case for a list with a single menu item."""
        result = task_func([['Burger']])
        expected = pd.DataFrame({'Count': [1]}, index=['Burger'])
        expected.index.name = 'MenuItem'
        self.assertTrue(result.equals(expected))

    def test_multiple_identical_items(self):
        """Test case for multiple identical menu items."""
        result = task_func([['Pizza', 'Pizza', 'Pizza']])
        expected = pd.DataFrame({'Count': [3]}, index=['Pizza'])
        expected.index.name = 'MenuItem'
        self.assertTrue(result.equals(expected))

    def test_different_items(self):
        """Test case for a list with different menu items."""
        result = task_func([['Pizza', 'Burger'], ['Pasta', 'Coke'], ['Pizza', 'Coke']])
        expected = pd.DataFrame({'Count': [2, 1, 1, 2]}, 
                                index=['Pizza', 'Burger', 'Pasta', 'Coke'])
        expected.index.name = 'MenuItem'
        self.assertTrue(result.equals(expected))

    def test_nested_lists(self):
        """Test case for deeply nested lists of menu items."""
        result = task_func([['Pizza', ['Burger', 'Coke']], ['Pasta'], ['Pizza']])
        expected = pd.DataFrame({'Count': [2, 1, 1, 1]}, 
                                index=['Pizza', 'Burger', 'Coke', 'Pasta'])
        expected.index.name = 'MenuItem'
        self.assertTrue(result.equals(expected))

if __name__ == '__main__':
    unittest.main()