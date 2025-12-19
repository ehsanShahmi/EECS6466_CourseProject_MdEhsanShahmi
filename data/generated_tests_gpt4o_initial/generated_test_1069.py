import pandas as pd
import matplotlib.pyplot as plt
import unittest

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Sets up data for testing."""
        self.data1 = {
            'Category1': ['A', 'A', 'B', 'B', 'C'],
            'Category2': ['X', 'X', 'Y', 'Y', 'Z'],
        }

        self.data2 = {
            'Category1': ['A', 'B', 'A', 'B', 'A', 'B'],
            'Category2': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
        }

        self.data3 = {
            'Category1': ['A', 'A', 'B', 'C'],
            'Category2': ['X', 'Y', 'Z', 'Z'],
        }

        self.data4 = {
            'Category1': ['A', 'B', 'C', 'D', 'E'],
            'Category2': ['W', 'W', 'W', 'W', 'W'],
        }

        self.data5 = {
            'Category1': ['A', 'B', 'C', 'A', 'B'],
            'Category2': ['X', 'Y', 'Z', 'X', 'Y'],
        }

    def test_non_uniform_distributions(self):
        """Test for non-uniform distributions in data1."""
        with self.assertLogs() as log:
            task_func(self.data1)
            self.assertIn("The distribution of values in column", log.output[0])
            self.assertIn("The distribution of values in column", log.output[1])

    def test_uniform_distributions(self):
        """Test for uniform distributions in data2."""
        with self.assertLogs() as log:
            task_func(self.data2)
            self.assertNotIn("The distribution of values in column", log.output)

    def test_mixed_distribution1(self):
        """Test for mixed distributions in data3."""
        with self.assertLogs() as log:
            task_func(self.data3)
            self.assertIn("The distribution of values in column 'Category1'", log.output[0])
            self.assertIn("The distribution of values in column 'Category2'", log.output[1])

    def test_uniform_distribution_in_category2(self):
        """Test to ensure Category2 in data4 has uniform distribution."""
        with self.assertLogs() as log:
            task_func(self.data4)
            self.assertNotIn("The distribution of values in column 'Category1'", log.output)
            self.assertNotIn("The distribution of values in column 'Category2'", log.output)

    def test_non_uniform_category1(self):
        """Test for non-uniform distributions in data5."""
        with self.assertLogs() as log:
            task_func(self.data5)
            self.assertIn("The distribution of values in column 'Category1'", log.output[0])
            self.assertIn("The distribution of values in column 'Category2'", log.output[1])

# To run the tests
if __name__ == '__main__':
    unittest.main()