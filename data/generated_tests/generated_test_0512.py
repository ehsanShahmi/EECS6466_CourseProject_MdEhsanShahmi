import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO

# Here is your prompt:
# (the function task_func is not implemented, and this will be tested)

class TestTaskFunc(unittest.TestCase):

    def test_valid_data_total_sales(self):
        data = [['Product A', 100, 10000], ['Product B', 150, 15000], ['Product C', 200, 20000]]
        stats, plot = task_func('Total Sales', data)
        self.assertEqual(stats['sum'], 45000)
        self.assertEqual(stats['mean'], 15000.0)
        self.assertEqual(stats['min'], 10000)
        self.assertEqual(stats['max'], 20000)
        self.assertIsInstance(plot, plt.Axes)

    def test_valid_data_quantity_sold(self):
        data = [['Product A', 100, 10000], ['Product B', 150, 15000], ['Product C', 200, 20000]]
        stats, plot = task_func('Quantity Sold', data)
        self.assertEqual(stats['sum'], 450)
        self.assertEqual(stats['mean'], 150.0)
        self.assertEqual(stats['min'], 100)
        self.assertEqual(stats['max'], 200)
        self.assertIsInstance(plot, plt.Axes)

    def test_invalid_negative_quantity_sold(self):
        data = [['Product A', -100, 10000], ['Product B', 150, 15000]]
        with self.assertRaises(ValueError):
            task_func('Quantity Sold', data)

    def test_invalid_negative_total_sales(self):
        data = [['Product A', 100, -10000], ['Product B', 150, 15000]]
        with self.assertRaises(ValueError):
            task_func('Total Sales', data)

    def test_invalid_column_name(self):
        data = [['Product A', 100, 10000], ['Product B', 150, 15000]]
        with self.assertRaises(KeyError):
            task_func('Invalid Column', data)

if __name__ == "__main__":
    unittest.main()