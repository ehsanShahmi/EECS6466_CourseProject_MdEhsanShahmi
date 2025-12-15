from itertools import combinations
import pandas as pd
import unittest

def task_func(number_list, element):
    """
    Find all unique combinations of 3 numbers from a list that add up to a certain element.
    
    If the number_list is empty, or there is no combination that adds up to the element,
    an empty dataframe is returned.
    

    Parameters:
    number_list (list): The list of numbers.
    element (int): The number to which the combination of 3 numbers should add up.

    Returns:
    Pandas DataFrame: A pandas Dataframe with the column 'Combinations',
         where each row contains a tuple containing a unique combination of 3 numbers that add up to the element.
    """
    combinations_list = list(combinations(number_list, 3))
    valid_combinations = [comb for comb in combinations_list if sum(comb) == element]
    
    # Return only unique combinations
    return pd.DataFrame({'Combinations': list(set(valid_combinations))})

class TestTaskFunc(unittest.TestCase):

    def test_positive_numbers(self):
        result = task_func([1, 2, 3, 4, 5], 6)
        expected = pd.DataFrame({'Combinations': [(1, 2, 3)]})
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True)

    def test_negative_and_positive_numbers(self):
        result = task_func([-1, 1, 0, -2, 2, 3], 0)
        expected = pd.DataFrame({'Combinations': [(-1, -2, 3), (-1, 1, 0), (0, -2, 2)]})
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True)

    def test_no_combinations(self):
        result = task_func([1, 2, 3], 10)
        expected = pd.DataFrame({'Combinations': []})
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))

    def test_empty_list(self):
        result = task_func([], 0)
        expected = pd.DataFrame({'Combinations': []})
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))

    def test_duplicate_combinations(self):
        result = task_func([1, 1, 1, 1, 1], 3)
        expected = pd.DataFrame({'Combinations': [(1, 1, 1)]})
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))

if __name__ == '__main__':
    unittest.main()