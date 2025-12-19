import unittest
import numpy as np

# Here is your prompt:
import numpy as np
import itertools

def task_func(data_list):
    """
    Unzips a list of tuples and calculates the mean of the numeric values for 
    each position.

    The function accepts a list of tuples, where each tuple consists of 
    alphanumeric values. It unzips the tuples, and calculates the mean of 
    numeric values at each position using numpy, where non numeric values are
    ignores. If all values at a position are non numeric, the mean at this
    position is set to be np.nan.
    If the provided tuples have different number of entries, missing values are 
    treated as zeros.

    Parameters:
    - data_list (list of tuples): The data to process, structured as a list of tuples. Each tuple can contain alphanumeric values.

    Returns:
    - list: A list of mean values for each numeric position across the tuples. Non-numeric positions are ignored.
            An empty list is returned if the input list (data_list) is empty.

    Requirements:
    - numpy
    - itertools

    Example:
    >>> task_func([('a', 1, 2), ('b', 2, 3), ('c', 3, 4), ('d', 4, 5), ('e', 5, 6)])
    [nan, 3.0, 4.0]
    >>> task_func([(1, 'a', 2), ('a', 3, 5), ('c', 1, -2)])
    [1.0, 2.0, 1.6666666666666667]
    """

    # Unzip the data while handling uneven tuple lengths by filling missing values with NaN
    unzipped_data = list(itertools.zip_longest(*data_list, fillvalue=np.nan))

    # Calculate the mean of numeric values, ignoring non-numeric ones
    mean_values = [np.nanmean([val for val in column if isinstance(val, (int, float))]) for column in unzipped_data]

    return mean_values


class TestTaskFunc(unittest.TestCase):
    
    def test_multiple_tuples_same_length(self):
        input_data = [('a', 1, 2), ('b', 2, 3), ('c', 3, 4), ('d', 4, 5), ('e', 5, 6)]
        expected_output = [np.nan, 3.0, 4.0]
        np.testing.assert_almost_equal(task_func(input_data), expected_output)

    def test_mixed_data_types(self):
        input_data = [(1, 'a', 2), ('a', 3, 5), ('c', 1, -2)]
        expected_output = [1.0, 2.0, 1.6666666666666667]
        np.testing.assert_almost_equal(task_func(input_data), expected_output)
    
    def test_empty_input(self):
        input_data = []
        expected_output = []
        self.assertEqual(task_func(input_data), expected_output)

    def test_tuples_with_no_numeric_values(self):
        input_data = [('a', 'b', 'c'), ('d', 'e', 'f')]
        expected_output = [np.nan, np.nan, np.nan]
        np.testing.assert_almost_equal(task_func(input_data), expected_output)

    def test_varying_tuple_lengths(self):
        input_data = [(1, 2), (3, 'a', 4), ('b', 5)]
        expected_output = [2.0, 5.0, np.nan]
        np.testing.assert_almost_equal(task_func(input_data), expected_output)


if __name__ == '__main__':
    unittest.main()