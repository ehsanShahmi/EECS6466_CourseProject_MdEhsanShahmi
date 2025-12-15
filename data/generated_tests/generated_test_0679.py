import pandas as pd
from collections import Counter
import unittest

# Here is your prompt:
# import pandas as pd
# from collections import Counter

# def task_func(df):
#     """
#     Calculate the frequency of combinations of elements in a DataFrame.
#     The function adds a 'combination' column to the DataFrame, which is the combination of items in each row.
#     It then calculates the frequency of each combination.
#     
#     Parameters:
#     - df (pandas.DataFrame): The input DataFrame with columns 'item1', 'item2', 'item3', 'item4', 'item5'.
#     
#     Returns:
#     - dict: A dictionary containing the frequency of all combination.
# 
#     Requirements:
#     - pandas
#     - collections
# 
#     Example:
#     >>> df = pd.DataFrame({'item1': ['a', 'b', 'a'], 'item2': ['b', 'c', 'b'], 'item3': ['c', 'd', 'c'], 'item4': ['d', 'e', 'd'], 'item5': ['e', 'f', 'e']})
#     >>> task_func(df)
#     {('a', 'b', 'c', 'd', 'e'): 2, ('b', 'c', 'd', 'e', 'f'): 1}
#     """

def task_func(df):
    df['combination'] = pd.Series(df.apply(lambda row: tuple(sorted(row)), axis=1))
    combination_freq = Counter(df['combination'])
    return dict(combination_freq)

class TestTaskFunc(unittest.TestCase):

    def test_basic_functionality(self):
        df = pd.DataFrame({
            'item1': ['a', 'b', 'a'],
            'item2': ['b', 'c', 'b'],
            'item3': ['c', 'd', 'c'],
            'item4': ['d', 'e', 'd'],
            'item5': ['e', 'f', 'e']
        })
        expected_output = {('a', 'b', 'c', 'd', 'e'): 2, ('b', 'c', 'd', 'e', 'f'): 1}
        self.assertEqual(task_func(df), expected_output)

    def test_empty_dataframe(self):
        df = pd.DataFrame(columns=['item1', 'item2', 'item3', 'item4', 'item5'])
        expected_output = {}
        self.assertEqual(task_func(df), expected_output)

    def test_single_row(self):
        df = pd.DataFrame({
            'item1': ['x'],
            'item2': ['y'],
            'item3': ['z'],
            'item4': ['w'],
            'item5': ['v']
        })
        expected_output = {('v', 'w', 'x', 'y', 'z'): 1}
        self.assertEqual(task_func(df), expected_output)

    def test_duplicates_in_row(self):
        df = pd.DataFrame({
            'item1': ['a', 'a'],
            'item2': ['b', 'b'],
            'item3': ['c', 'c'],
            'item4': ['d', 'd'],
            'item5': ['e', 'e']
        })
        expected_output = {('a', 'b', 'c', 'd', 'e'): 2}
        self.assertEqual(task_func(df), expected_output)

    def test_all_unique_combinations(self):
        df = pd.DataFrame({
            'item1': ['a', 'b', 'c'],
            'item2': ['d', 'e', 'f'],
            'item3': ['g', 'h', 'i'],
            'item4': ['j', 'k', 'l'],
            'item5': ['m', 'n', 'o']
        })
        expected_output = {
            ('a', 'd', 'g', 'j', 'm'): 1,
            ('b', 'e', 'h', 'k', 'n'): 1,
            ('c', 'f', 'i', 'l', 'o'): 1
        }
        self.assertEqual(task_func(df), expected_output)

if __name__ == '__main__':
    unittest.main()