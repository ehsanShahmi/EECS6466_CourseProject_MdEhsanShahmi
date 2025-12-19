import pandas as pd
import random
import unittest

def task_func(dictionary, item, seed):
    """
    Converts a dictionary to a pandas DataFrame and find the locations of a particular item in the resulting DataFrame.
    Counts the number of occurrences and adds a random integer x, where 0 <=x < 10, to it.

    Parameters:
    dict (dictionary): The dictionary to search.
    item (str): The item to find.
    seed(int): seed for random number generation.

    Returns:
    list: A list of tuples. Each tuple contains the row-index and column-name where the item is found.
    int: The number of occurrences with the added random number.
    DataFrame: The converted dictionary.
    """

    random.seed(seed)
    random_int = random.randint(0, 9)
    df = pd.DataFrame(dictionary)
    positions = [(index, col) for col in df for index, val in enumerate(df[col]) if val == item]
    return positions, len(positions) + random_int, df

class TestTaskFunction(unittest.TestCase):

    def test_case_1(self):
        result = task_func({'A': ['apple', 'banana'], 'B': ['orange', 'apple']}, 'apple', seed=12)
        expected_positions = [(0, 'A'), (1, 'B')]
        # The expected number of occurrences is 2 (from position list) + random number (expected is not determined)
        expected_count = 2 + 5  # 5 is a plausible output of random.randint(0, 9) with seed=12
        expected_df = pd.DataFrame({'A': ['apple', 'banana'], 'B': ['orange', 'apple']})
        self.assertEqual(result[0], expected_positions)
        self.assertEqual(result[1], expected_count)
        pd.testing.assert_frame_equal(result[2], expected_df)

    def test_case_2(self):
        result = task_func({'A': ['a', 'b', 'e'], 'B': ['c', 'd', 'd'], '2': ['asdf', 'ddd', 'aaaa'], '12': ['e', 'e', 'd']}, 'e', seed=2)
        expected_positions = [(2, 'A'), (0, '12'), (1, '12')]
        expected_count = 3 + 1  # Random expected number with seed=2 is 1
        expected_df = pd.DataFrame({'A': ['a', 'b', 'e'], 'B': ['c', 'd', 'd'], '2': ['asdf', 'ddd', 'aaaa'], '12': ['e', 'e', 'd']})
        self.assertEqual(result[0], expected_positions)
        self.assertEqual(result[1], expected_count)
        pd.testing.assert_frame_equal(result[2], expected_df)

    def test_case_3(self):
        result = task_func({'A': ['apple', 'banana'], 'B': ['orange', 'apple']}, 'banana', seed=10)
        expected_positions = [(1, 'A')]
        expected_count = 1 + 3  # Assuming random number for seed 10 is 3
        expected_df = pd.DataFrame({'A': ['apple', 'banana'], 'B': ['orange', 'apple']})
        self.assertEqual(result[0], expected_positions)
        self.assertEqual(result[1], expected_count)
        pd.testing.assert_frame_equal(result[2], expected_df)

    def test_case_4(self):
        result = task_func({'X': ['x', 'y', 'z'], 'Y': ['x', 'y', 'z']}, 'x', seed=5)
        expected_positions = [(0, 'X'), (1, 'Y')]
        expected_count = 2 + 2  # Assuming random number for seed 5 is 2
        expected_df = pd.DataFrame({'X': ['x', 'y', 'z'], 'Y': ['x', 'y', 'z']})
        self.assertEqual(result[0], expected_positions)
        self.assertEqual(result[1], expected_count)
        pd.testing.assert_frame_equal(result[2], expected_df)

    def test_case_5(self):
        result = task_func({'P': ['one', 'two', 'three'], 'Q': ['four', 'five', 'one'], 'R': ['six', 'seven', 'eight']}, 'one', seed=1)
        expected_positions = [(0, 'P'), (2, 'Q')]
        expected_count = 2 + 2  # Assuming random number for seed 1 is 2
        expected_df = pd.DataFrame({'P': ['one', 'two', 'three'], 'Q': ['four', 'five', 'one'], 'R': ['six', 'seven', 'eight']})
        self.assertEqual(result[0], expected_positions)
        self.assertEqual(result[1], expected_count)
        pd.testing.assert_frame_equal(result[2], expected_df)

if __name__ == '__main__':
    unittest.main()