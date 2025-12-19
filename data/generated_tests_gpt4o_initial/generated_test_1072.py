import pandas as pd
import numpy as np
import unittest

def task_func(list_of_lists):
    series_list = []
    for sublist in list_of_lists:
        values = np.arange(1, len(sublist) + 1)
        np.random.shuffle(values)
        s = pd.Series(values, index=sublist)
        series_list.append(s)
    return series_list

class TestTaskFunc(unittest.TestCase):
    
    def test_empty_input(self):
        result = task_func([])
        self.assertEqual(result, [])

    def test_single_sublist(self):
        result = task_func([['a', 'b', 'c']])
        self.assertEqual(len(result), 1)
        self.assertTrue(all(index in ['a', 'b', 'c'] for index in result[0].index))
        self.assertTrue(all(value in [1, 2, 3] for value in result[0].values))

    def test_multiple_sublist(self):
        result = task_func([['x', 'y'], ['a', 'b', 'c']])
        self.assertEqual(len(result), 2)
        self.assertTrue(all(index in ['x', 'y'] for index in result[0].index))
        self.assertTrue(all(value in [1, 2] for value in result[0].values))
        self.assertTrue(all(index in ['a', 'b', 'c'] for index in result[1].index))
        self.assertTrue(all(value in [1, 2, 3] for value in result[1].values))

    def test_unique_values(self):
        result = task_func([['a', 'b', 'c'], ['x', 'y', 'z']])
        for series in result:
            unique_values = set(series.values)
            self.assertEqual(len(unique_values), len(series.values))

    def test_randomness(self):
        np.random.seed(1)
        result1 = task_func([['a', 'b', 'c']])
        np.random.seed(1)
        result2 = task_func([['a', 'b', 'c']])
        pd.testing.assert_series_equal(result1[0], result2[0])

if __name__ == '__main__':
    unittest.main()