import unittest
import pandas as pd
import matplotlib.pyplot as plt

class TestTaskFunc(unittest.TestCase):

    def test_empty_data(self):
        """Test case for empty data list"""
        result = task_func([])
        self.assertIsNone(result)

    def test_single_entry(self):
        """Test case with a single dictionary entry"""
        data = [{'A': 10, 'B': 15}]
        ax = task_func(data)
        self.assertIsNotNone(ax)
        self.assertEqual(ax.get_title(), 'Data over Time')
        self.assertEqual(len(ax.lines), 2)  # One for each key in the dictionary

    def test_multiple_entries(self):
        """Test case with multiple dictionaries"""
        data = [{'A': 10, 'B': 15, 'C': 12},
                {'A': 12, 'B': 20, 'C': 14},
                {'A': 15, 'B': 18, 'C': 15},
                {'A': 11, 'B': 17, 'C': 13}]
        ax = task_func(data)
        self.assertIsNotNone(ax)
        self.assertEqual(ax.get_title(), 'Data over Time')
        self.assertEqual(len(ax.lines), 3)  # One for each key in the dictionary

    def test_missing_keys_in_dictionaries(self):
        """Test case with missing keys in the dictionaries"""
        data = [{'A': 10, 'B': 15},
                {'A': 12, 'C': 14},
                {'B': 18, 'C': 15},
                {'A': 11, 'B': 17}]
        ax = task_func(data)
        self.assertIsNotNone(ax)
        self.assertEqual(ax.get_title(), 'Data over Time')
        self.assertEqual(len(ax.lines), 3)  # Check that it identifies unique keys

    def test_non_numeric_data(self):
        """Test case where data points are not numeric"""
        data = [{'A': '10', 'B': '15'},
                {'A': '12', 'B': '20'},
                {'A': '15', 'B': '18'},
                {'A': '11', 'B': '17'}]
        with self.assertRaises(TypeError):
            task_func(data)

if __name__ == '__main__':
    unittest.main()