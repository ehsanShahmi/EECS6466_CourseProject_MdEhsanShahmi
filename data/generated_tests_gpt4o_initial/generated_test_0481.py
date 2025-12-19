import pandas as pd
import random
import re
import unittest

def task_func(data_list, seed=42):
    """
    Randomizes the order of comma-separated substrings within each string in a list,
    normalizing spaces to ensure a single space follows each comma using regex, then
    returns a DataFrame comparing original and randomized strings.

    Parameters:
    data_list (list of str): List of strings with substrings to be randomized.
    seed (int, optional): Seed for random number generator for reproducibility. Defaults to None.

    Returns:
    pandas.DataFrame: A DataFrame with columns 'Original String' and 'Randomized String'.

    Requirements:
    - pandas
    - random
    - re

    Example:
    >>> df = task_func(['lamp, bag, mirror', 'table, chair, bag'], seed=42)
    >>> df['Original String'][0]
    'lamp, bag, mirror'
    >>> df['Randomized String'][0]
    'mirror, lamp, bag'
    """

    random.seed(seed)

    df = pd.DataFrame(data_list, columns=["Original String"])

    randomized_strings = []
    for s in data_list:
        substrings = re.split("\s*,\s*", s)
        random_positions = random.sample(range(len(substrings)), len(substrings))
        randomized_s = ", ".join([substrings[i] for i in random_positions])
        randomized_strings.append(randomized_s)

    df["Randomized String"] = randomized_strings

    return df

class TestTaskFunc(unittest.TestCase):

    def test_basic_functionality(self):
        df = task_func(['lamp, bag, mirror', 'table, chair, bag'], seed=42)
        self.assertEqual(df['Original String'][0], 'lamp, bag, mirror')
        self.assertEqual(df['Original String'][1], 'table, chair, bag')
        self.assertIn(df['Randomized String'][0], ['mirror, lamp, bag', 'bag, mirror, lamp', 'lamp, bag, mirror'])
        self.assertIn(df['Randomized String'][1], ['table, chair, bag', 'chair, bag, table', 'bag, table, chair'])

    def test_empty_string(self):
        df = task_func([''])
        self.assertEqual(df['Original String'][0], '')
        self.assertEqual(df['Randomized String'][0], '')

    def test_single_element_string(self):
        df = task_func(['lamp'])
        self.assertEqual(df['Original String'][0], 'lamp')
        self.assertEqual(df['Randomized String'][0], 'lamp')

    def test_repeated_elements(self):
        df = task_func(['lamp, lamp, bag, bag'])
        self.assertEqual(df['Original String'][0], 'lamp, lamp, bag, bag')
        self.assertIn(df['Randomized String'][0], ['lamp, lamp, bag, bag', 'bag, lam, bag, lamp', 'bag, lamp, lamp, bag'])

    def test_same_input_diff_order(self):
        df1 = task_func(['apple, banana, cherry'], seed=100)
        df2 = task_func(['apple, banana, cherry'], seed=200)
        self.assertNotEqual(df1['Randomized String'][0], df2['Randomized String'][0])

if __name__ == '__main__':
    unittest.main()