import json
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import defaultdict
import unittest


class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Prepare JSON files with test data
        self.test_files = {
            "basic": 'test_basic.json',
            "empty": 'test_empty.json',
            "single_entry": 'test_single_entry.json',
            "multiple_keys": 'test_multiple_keys.json',
            "complex_data": 'test_complex_data.json',
        }

        # Basic data
        with open(self.test_files["basic"], 'w') as f:
            json.dump([{"a": 1, "b": 2}, {"a": 3, "b": 4}], f)

        # Empty data
        with open(self.test_files["empty"], 'w') as f:
            json.dump([], f)

        # Single entry data
        with open(self.test_files["single_entry"], 'w') as f:
            json.dump([{"a": 1}], f)

        # Multiple keys data
        with open(self.test_files["multiple_keys"], 'w') as f:
            json.dump([{"a": 2}, {"b": 3}, {"a": 4}, {"b": 5}], f)

        # Complex data
        with open(self.test_files["complex_data"], 'w') as f:
            json.dump([{"a": 1, "b": 2}, {"a": 100, "b": 200}, {"c": 300}], f)

    def test_basic_case(self):
        results, ax = task_func(self.test_files["basic"])
        self.assertEqual(results, {'a': {'mean': 2.0, 'median': 2.0}, 'b': {'mean': 3.0, 'median': 3.0}})
        self.assertIsInstance(ax, plt.Axes)

    def test_empty_case(self):
        results, ax = task_func(self.test_files["empty"])
        self.assertEqual(results, {})
        self.assertIsInstance(ax, plt.Axes)

    def test_single_entry_case(self):
        results, ax = task_func(self.test_files["single_entry"])
        self.assertEqual(results, {'a': {'mean': 1.0, 'median': 1.0}})
        self.assertIsInstance(ax, plt.Axes)

    def test_multiple_keys_case(self):
        results, ax = task_func(self.test_files["multiple_keys"])
        self.assertEqual(results, {'a': {'mean': 3.0, 'median': 3.0}, 'b': {'mean': 4.0, 'median': 4.0}})
        self.assertIsInstance(ax, plt.Axes)

    def test_complex_data_case(self):
        results, ax = task_func(self.test_files["complex_data"])
        self.assertEqual(results, {'a': {'mean': 50.0, 'median': 50.0}, 'b': {'mean': 100.0, 'median': 100.0}, 'c': {'mean': 300.0, 'median': 300.0}})
        self.assertIsInstance(ax, plt.Axes)

if __name__ == '__main__':
    unittest.main()