import numpy as np
import random
import unittest

def task_func(my_list):
    """
    Appends a randomly selected integer between 0 and 100 to the given list 'my_list' and 
    returns a numpy array of random floating-point numbers. The size of the returned array 
    is equal to the sum of the numbers in the modified list.

    Parameters:
        my_list (list): A list of integers to which a random number will be added.

    Returns:
        numpy.ndarray: An array of random floating-point numbers. The length of the array 
                       is equal to the sum of the integers in 'my_list' after a random 
                       number has been appended.

    Requirements:
    - numpy
    - random
                       
    Examples:
        >>> result = task_func([2, 3, 5])
        >>> 10 <= len(result) <= 110  # Expecting the length to be within the range after adding a random number between 0 and 100
        True
        >>> isinstance(result, np.ndarray)
        True
    """

    random_number = random.randint(0, 100)
    my_list.append(random_number)

    size = sum(my_list)
    random_array = np.random.rand(size)

    return random_array

class TestTaskFunc(unittest.TestCase):

    def test_output_type(self):
        """Test that the output is of type numpy.ndarray."""
        result = task_func([1, 2, 3])
        self.assertIsInstance(result, np.ndarray)

    def test_output_length(self):
        """Test the output length is correct after appending."""
        original_list = [1, 2, 3]
        result = task_func(original_list)
        appended_value = original_list[-1]  # The last value appended
        expected_length = sum(original_list) + appended_value
        self.assertEqual(len(result), expected_length)

    def test_random_number_range(self):
        """Test that the random number is in the correct range (0 to 100)."""
        my_list = [0, 0, 0]
        modified_list = my_list.copy()
        task_func(modified_list)  # Modify the list
        random_number = modified_list[-1]  # Get the randomly appended number
        self.assertGreaterEqual(random_number, 0)
        self.assertLessEqual(random_number, 100)

    def test_sum_of_modified_list(self):
        """Test that the sum of the modified list is correct."""
        my_list = [2, 3]
        task_func(my_list)  # Modify the list
        self.assertGreaterEqual(sum(my_list), 2)  # At least one random number should be added

    def test_multiple_appends(self):
        """Test that the function behaves correctly over multiple calls."""
        my_list = [1, 1, 1]
        first_result = task_func(my_list)
        length_after_first_call = len(first_result)

        second_result = task_func(my_list)
        length_after_second_call = len(second_result)

        self.assertGreater(length_after_second_call, length_after_first_call)

if __name__ == '__main__':
    unittest.main()