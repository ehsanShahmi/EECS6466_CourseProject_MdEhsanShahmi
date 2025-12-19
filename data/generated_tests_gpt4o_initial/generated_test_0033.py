import numpy as np
import unittest
from functools import reduce

def task_func(list_of_pairs):
    """ 
    Calculate the product of the second values in each tuple in a list of tuples and return the product as a single-element numeric array.
    
    Parameters:
    list_of_pairs (list): A list of tuples, where the first element is the category 
                          and the second element is the numeric value.
    
    Returns:
    numpy.ndarray: A 1D numpy array containing a single element that is the product of the second values in the list of tuples.
    
    Requirements:
    - numpy
    - functools.reduce
    
    Example:
    >>> list_of_pairs = [('Fruits', 5), ('Vegetables', 9), ('Dairy', -1), ('Bakery', -2), ('Meat', 4)]
    >>> product_array = task_func(list_of_pairs)
    >>> print(product_array)
    [360]
    """
    second_values = [pair[1] for pair in list_of_pairs]
    product = reduce(np.multiply, second_values)
    product_array = np.array([product])

    return product_array

class TestTaskFunc(unittest.TestCase):
    
    def test_product_positive_numbers(self):
        list_of_pairs = [('Fruits', 2), ('Vegetables', 3), ('Grains', 4)]
        expected = np.array([24])
        result = task_func(list_of_pairs)
        np.testing.assert_array_equal(result, expected)
    
    def test_product_with_zero(self):
        list_of_pairs = [('Fruits', 0), ('Vegetables', 5), ('Dairy', 3)]
        expected = np.array([0])
        result = task_func(list_of_pairs)
        np.testing.assert_array_equal(result, expected)

    def test_product_with_negative_numbers(self):
        list_of_pairs = [('Fruits', -1), ('Vegetables', 3), ('Grains', -4)]
        expected = np.array([12])
        result = task_func(list_of_pairs)
        np.testing.assert_array_equal(result, expected)

    def test_product_all_negative_numbers(self):
        list_of_pairs = [('Fruits', -1), ('Vegetables', -2), ('Dairy', -3)]
        expected = np.array([-6])
        result = task_func(list_of_pairs)
        np.testing.assert_array_equal(result, expected)

    def test_product_empty_list(self):
        list_of_pairs = []
        expected = np.array([1])
        result = task_func(list_of_pairs)
        np.testing.assert_array_equal(result, expected)

if __name__ == '__main__':
    unittest.main()