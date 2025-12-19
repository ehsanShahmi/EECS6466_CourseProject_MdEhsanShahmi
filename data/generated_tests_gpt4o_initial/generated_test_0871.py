import numpy as np
import itertools
import unittest
import os

def task_func(data_list, file_name):
    """
    This function takes a list of tuples. The first value of each tuple is a string,
    the other values are numeric. E.g. ('test', 2, 12.4, -2)
    It calculates the mean over all tuples of the numerical values for each tuple position excluding the first position, 
    and writes the results into a specified text file.
    The content in the text file is formated as follows:
    'Position 'x': 'mean', where x is the current tuple position and 'mean' denotes the 
    computed mean value. Each Position is written in a new line.
    It returns a list of the calculated mean values.

    Missing values and non numeric values at positions other than the first are filled / replaced with np.nan. 
    If an empty list is handed to the function an empty list is returned and an empty file is created.

    The function utilizes the 'numpy' library for numerical operations and the 'itertools' library 
    to handle the iteration through the data structure.

    Parameters:
    - data_list (list of tuples): A list containing tuples of the form (string, numeric, numeric, ...)
    - file_name (str): The name of the text file to store the mean values.

    Returns:
    - list: A list of mean values calculated from the numerical data in the tuples.

    Requirements:
    - numpy
    - itertools

    Example:
    >>> data = [('a', 1, 2), ('b', 2, 3), ('c', 3, 4), ('d', 4, 5), ('e', 5, 6)]
    >>> task_func(data, 'mean_values.txt')
    [3.0, 4.0]
    >>> with open('mean_values.txt') as file:
    ...    txt_content = file.readlines()
    >>> print(txt_content)
    ['Position 1: 3.0\\n', 'Position 2: 4.0\\n']
    >>> data_list=[('hi', 'test', -12, 4), ('hallo', 1.2, 'test'), ('hola', -3, 34, 12.1)]
    >>> task_func(data_list, 'test.txt')
    [-0.9, 11.0, 8.05]
    >>> with open('test.txt') as file:
    ...     txt_content = file.readlines()
    >>> print(txt_content)
    ['Position 1: -0.9\\n', 'Position 2: 11.0\\n', 'Position 3: 8.05\\n']
    """
    
    # Unzipping the data to separate the elements of the tuples
    unzipped_data = list(itertools.zip_longest(*data_list, fillvalue=np.nan))
    mean_values = []
    # Calculating the mean values excluding the first position (non-numerical)
    for column in unzipped_data[1:]:
        numeric_values = [val for val in column if isinstance(val, (int, float))]
        if numeric_values:
            mean_values.append(np.nanmean(numeric_values))
        else:
            mean_values.append(np.nan)

    # Writing the mean values to the specified file
    with open(file_name, 'w') as f:
        for i, mean_value in enumerate(mean_values, start=1):
            f.write('Position {}: {}\n'.format(i, mean_value))
    
    # Returning the list of mean values for testing purposes
    return mean_values


class TestTaskFunc(unittest.TestCase):

    def test_mean_values_basic(self):
        data = [('a', 1, 2), ('b', 2, 3), ('c', 3, 4), ('d', 4, 5), ('e', 5, 6)]
        result = task_func(data, 'mean_values.txt')
        self.assertEqual(result, [3.0, 4.0])
        with open('mean_values.txt') as file:
            txt_content = file.readlines()
        self.assertEqual(txt_content, ['Position 1: 3.0\n', 'Position 2: 4.0\n'])

    def test_mean_values_with_nan(self):
        data_list = [('hi', 'test', -12, 4), ('hallo', 1.2, 'test'), ('hola', -3, 34, 12.1)]
        result = task_func(data_list, 'test.txt')
        self.assertEqual(result, [-0.9, 11.0, 8.05])
        with open('test.txt') as file:
            txt_content = file.readlines()
        self.assertEqual(txt_content, ['Position 1: -0.9\n', 'Position 2: 11.0\n', 'Position 3: 8.05\n'])

    def test_empty_list(self):
        result = task_func([], 'empty.txt')
        self.assertEqual(result, [])
        with open('empty.txt') as file:
            content = file.read()
        self.assertEqual(content, '')

    def test_no_numeric_values(self):
        data_list = [('a', 'b', 'c'), ('d', 'e', 'f')]
        result = task_func(data_list, 'no_numeric.txt')
        self.assertEqual(result, [np.nan, np.nan])
        with open('no_numeric.txt') as file:
            txt_content = file.readlines()
        self.assertEqual(txt_content, ['Position 1: nan\n', 'Position 2: nan\n'])

    def test_inconsistent_tuple_length(self):
        data_list = [('a', 1), ('b', 2, 3), ('c', 3)]
        result = task_func(data_list, 'inconsistent.txt')
        self.assertEqual(result, [2.0, 3.0])
        with open('inconsistent.txt') as file:
            txt_content = file.readlines()
        self.assertEqual(txt_content, ['Position 1: 2.0\n', 'Position 2: 3.0\n'])

if __name__ == '__main__':
    unittest.main()