import pandas as pd
import numpy as np
import itertools
import unittest

def task_func(T1, row_num=50, seed=None):
    np.random.seed(seed)
    int_list = [list(map(int, x)) for x in T1]
    flattened_list = list(itertools.chain(*int_list))
    total_cols = sum(flattened_list)

    data = np.random.randint(0, 100, size=(row_num, total_cols))
    df = pd.DataFrame(data, columns=[f'Col_{i+1}' for i in range(total_cols)])

    return df

class TestTaskFunc(unittest.TestCase):

    def test_correct_shape(self):
        T1 = (('13', '17', '18', '21', '32'), ('07', '11', '13', '14', '28'), ('01', '05', '06', '08', '15', '16'))
        df = task_func(T1, row_num=5, seed=2022)
        expected_cols = 225  # sum of integers in T1
        self.assertEqual(df.shape, (5, expected_cols))

    def test_with_different_row_num(self):
        T1 = (('1', '3'),)
        df = task_func(T1, row_num=2, seed=32)
        self.assertEqual(df.shape[0], 2)

    def test_empty_T1(self):
        T1 = (('0',),)
        df = task_func(T1, row_num=5)
        self.assertEqual(df.shape, (5, 0))

    def test_single_column_output(self):
        T1 = (('1',),)
        df = task_func(T1, row_num=1)
        self.assertEqual(df.shape, (1, 1))

    def test_negative_values_in_T1(self):
        T1 = (('1', '-1'),)
        df = task_func(T1, row_num=5)
        # In this case, total_cols would be 0, resulting in an empty DataFrame
        self.assertEqual(df.shape, (5, 0))

if __name__ == '__main__':
    unittest.main()