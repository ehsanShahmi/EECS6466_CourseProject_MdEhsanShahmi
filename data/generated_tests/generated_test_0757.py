import numpy as np
import unittest
import datetime

def task_func(arr):
    """
    Reverse the order of words separated by. "" in all strings of a numpy array.

    Parameters:
    - arr (numpy array): The numpy array.

    Returns:
    - numpy.ndarray: The numpy array with the strings reversed.

    Requirements:
    - numpy
    - datetime

    Example:
    >>> arr = np.array(['apple.orange', 'red.green.yellow'])
    >>> reversed_arr = task_func(arr)
    >>> print(reversed_arr)
    ['orange.apple' 'yellow.green.red']
    """

    vectorized_reverse = np.vectorize(lambda s: '.'.join(s.split('.')[::-1]))
    
    now = datetime.datetime.now()
    
    return vectorized_reverse(arr)

class TestTaskFunc(unittest.TestCase):

    def test_basic_functionality(self):
        arr = np.array(['apple.orange', 'red.green.yellow'])
        expected = np.array(['orange.apple', 'yellow.green.red'])
        np.testing.assert_array_equal(task_func(arr), expected)

    def test_empty_strings(self):
        arr = np.array(['', 'example.test'])
        expected = np.array(['', 'test.example'])
        np.testing.assert_array_equal(task_func(arr), expected)

    def test_single_word_strings(self):
        arr = np.array(['apple', 'banana'])
        expected = np.array(['apple', 'banana'])  # No change expected for single words
        np.testing.assert_array_equal(task_func(arr), expected)

    def test_varied_length_strings(self):
        arr = np.array(['a.b.c', '1.2.3.4'])
        expected = np.array(['c.b.a', '4.3.2.1'])
        np.testing.assert_array_equal(task_func(arr), expected)

    def test_numeric_strings(self):
        arr = np.array(['123.456', '789.000'])
        expected = np.array(['456.123', '000.789'])
        np.testing.assert_array_equal(task_func(arr), expected)

if __name__ == '__main__':
    unittest.main()