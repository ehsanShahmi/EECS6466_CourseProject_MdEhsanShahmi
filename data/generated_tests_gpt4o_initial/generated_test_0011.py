import unittest
import numpy as np
import itertools
import random

def task_func(T1, max_value=100):
    """
    Converts elements in 'T1', a tuple of tuples containing string representations 
    of integers, to integers and creates a list of random integers. The size of the 
    list equals the sum of these integers. Returns the 25th, 50th, and 75th percentiles 
    of this list.

    Parameters:
    T1 (tuple of tuple of str): A tuple of tuples, each containing string representations of integers.
    max_value (int): The upper bound for random number generation, exclusive. Default is 100.
    
    Returns:
    tuple: A tuple (p25, p50, p75) representing the 25th, 50th, and 75th percentiles of the list.

    Requirements:
    - numpy
    - itertools
    - random
    
    Example:
    >>> import random
    >>> random.seed(42)
    >>> T1 = (('13', '17', '18', '21', '32'), ('07', '11', '13', '14', '28'), ('01', '05', '06', '08', '15', '16'))
    >>> percentiles = task_func(T1)
    >>> print(percentiles)
    (24.0, 48.0, 77.0)
    """

    int_list = [list(map(int, x)) for x in T1]
    flattened_list = list(itertools.chain(*int_list))
    total_nums = sum(flattened_list)

    random_nums = [random.randint(0, max_value) for _ in range(total_nums)]

    p25 = np.percentile(random_nums, 25)
    p50 = np.percentile(random_nums, 50)
    p75 = np.percentile(random_nums, 75)

    return p25, p50, p75

class TestTaskFunction(unittest.TestCase):

    def test_basic_case(self):
        random.seed(42)
        T1 = (('13', '17', '18', '21', '32'), ('07', '11', '13', '14', '28'), ('01', '05', '06', '08', '15', '16'))
        result = task_func(T1)
        self.assertEqual(result, (24.0, 48.0, 77.0))

    def test_empty_tuple(self):
        T1 = ((),)
        result = task_func(T1)
        # Expecting percentiles of an empty list
        with self.assertRaises(ValueError):
            np.percentile([], 25)

    def test_single_value_tuple(self):
        T1 = (('5',),)
        result = task_func(T1)
        self.assertTrue(isinstance(result, tuple))
        self.assertEqual(len(result), 3)

    def test_different_max_value(self):
        T1 = (('10', '20'), ('30', '40'))
        result = task_func(T1, max_value=50)
        self.assertTrue(isinstance(result, tuple))
        self.assertEqual(len(result), 3)

    def test_large_input(self):
        T1 = (('100',)*10, ('50',)*20)
        result = task_func(T1)
        self.assertTrue(isinstance(result, tuple))
        self.assertEqual(len(result), 3)

if __name__ == '__main__':
    unittest.main()