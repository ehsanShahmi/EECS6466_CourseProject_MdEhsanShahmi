import unittest
import pandas as pd
import os

# Here is your prompt:
import collections
import numpy as np


def task_func(file_name):
    """
    Find the most common value in each column of a csv file with column names.

    If some values occur the same number of times, the values are sorted
    alphabetically and the first is considered most common.

    If an empty csv is passed, an empty dictionary is returned. 
    
    Parameters:
    file_name (str): The name of the csv file.
    
    Returns:
    dict: A dictionary with column names as keys and most common values as values.

    Requirements:
    - collections
    - numpy
    
    Example:
    >>> common_values = task_func('sample.csv')
    >>> print(common_values)
    {'Name': 'Simon Velasquez',
    'Age': 21,
    'Fruit': 'Apple',
    'Genre': 'HipHop',
    'Height': 172}
    """

    data = np.genfromtxt(file_name, delimiter=',', names=True,
                         dtype=None, encoding=None)
    common_values = {}

    if len(np.atleast_1d(data)) == 0:
        return {}

    if len(np.atleast_1d(data)) == 1:
        for col in data.dtype.names:
            common_values[col] = data[col].item()

    else:
        for col in data.dtype.names:
            counter = collections.Counter(data[col])
            if counter.most_common(2)[0][1] == counter.most_common(2)[1][1]:
                common_values[col] = sorted(counter.items())[0][0]
            else:
                common_values[col] = counter.most_common(1)[0][0]

    return common_values


class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Create sample CSV files for testing
        self.files = {
            "test_case_1.csv": "Name,Age,Fruit,Genre,Height\nSimon Velasquez,21,Apple,HipHop,172\nSimon Velasquez,22,Banana,HipHop,172",
            "test_case_2.csv": "Name,Age,Fruit,Genre,Height\nAlice,30,Orange,Rock,160\nBob,30,Orange,Rock,165",
            "test_case_3.csv": "Name,Age,Fruit,Genre,Height\nCharlie,25,Grapes,Jazz,180",
            "test_case_4.csv": "Name,Age,Fruit,Genre,Height\n,21,,HipHop,172\n,,Apple,,",
            "test_case_5.csv": ""  # empty csv
        }
        for file_name, content in self.files.items():
            with open(file_name, "w") as f:
                f.write(content)

    def tearDown(self):
        # Remove the test files after tests
        for file_name in self.files.keys():
            os.remove(file_name)

    def test_case_1(self):
        expected = {'Name': 'Simon Velasquez', 'Age': 21, 'Fruit': 'Apple', 'Genre': 'HipHop', 'Height': 172}
        result = task_func('test_case_1.csv')
        self.assertEqual(result, expected)

    def test_case_2(self):
        expected = {'Name': 'Alice', 'Age': 30, 'Fruit': 'Orange', 'Genre': 'Rock', 'Height': 160}
        result = task_func('test_case_2.csv')
        self.assertEqual(result, expected)

    def test_case_3(self):
        expected = {'Name': 'Charlie', 'Age': 25, 'Fruit': 'Grapes', 'Genre': 'Jazz', 'Height': 180}
        result = task_func('test_case_3.csv')
        self.assertEqual(result, expected)

    def test_case_4(self):
        expected = {'Name': '', 'Age': 21, 'Fruit': 'Apple', 'Genre': 'HipHop', 'Height': 172}
        result = task_func('test_case_4.csv')
        self.assertEqual(result, expected)

    def test_case_5(self):
        expected = {}
        result = task_func('test_case_5.csv')
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()