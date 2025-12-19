from random import shuffle, randint
import pandas as pd
import unittest

def task_func(l, n_groups = 5):
    """
    Generate a Series from a list "l". The function shuffles the list, 
    then creates a longer series by cycling through the shuffled list. 
    For each element in the series, it randomly selects n_groups characters
    from the start of the string and moves them to the end. 
    
    Parameters:
    - l (list): A list of strings.
    - n_groups (int): number of groups. Default value is 5.

    Returns:
    - pd.Series: A Series where each element is modified by moving "n" 
                 characters from the start to the end.

    Requirements:
    - pandas
    - random.shuffle
    - random.randint
    """
    if not l:
        return pd.Series()

    shuffle(l)
    random_shifts = [(randint(1, max(1, len(x) - 1)), randint(1, max(1, len(x) - 1))) for x in l]

    modified_elements = []
    for _ in range(n_groups):
        for element, (start, end) in zip(l, random_shifts):
            new_element = element[start:] + element[:end] if len(element) > 1 else element
            modified_elements.append(new_element)

    return pd.Series(modified_elements)

class TestTaskFunc(unittest.TestCase):

    def test_empty_list(self):
        result = task_func([])
        self.assertTrue(isinstance(result, pd.Series))
        self.assertEqual(len(result), 0)

    def test_single_element_list(self):
        result = task_func(['A'])
        self.assertTrue(isinstance(result, pd.Series))
        self.assertEqual(len(result), 5)  # n_groups = 5, so should repeat 5 times
        self.assertTrue(all(x == 'A' for x in result))  # all elements should be 'A'

    def test_multiple_elements(self):
        result = task_func(['AB', 'CD', 'EF'])
        self.assertTrue(isinstance(result, pd.Series))
        self.assertEqual(len(result), 15)  # 3 elements, each repeated n_groups times
        self.assertTrue(all(x in ['AB', 'CD', 'EF'] for x in result))  # all elements should be from the original list

    def test_strings_of_different_lengths(self):
        result = task_func(['AB', 'C', 'DEFG'])
        self.assertTrue(isinstance(result, pd.Series))
        self.assertEqual(len(result), 15)  # still will return 15 items
        self.assertTrue(all(x in ['AB', 'C', 'DEFG'] for x in result))

    def test_check_structure_type(self):
        result = task_func(['XYZ', '12345'])
        self.assertTrue(isinstance(result, pd.Series))
        self.assertEqual(result.dtype, object)  # Series should contain strings, which are object dtype

if __name__ == '__main__':
    unittest.main()