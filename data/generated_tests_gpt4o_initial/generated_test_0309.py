import unittest
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Here is your prompt:
def task_func(list_of_lists, seed=42):
    """
    Scale the values in a list of lists to a (0,1) range using MinMaxScaler.
    If any inner list is empty, the function fills it with five random integers between 0 and 100, and then scales the values.
    
    Parameters:
    list_of_lists (list of list of int): A list containing inner lists of integers.
    seed (int, Optional): Seed for random number generation. Default is 42.
    
    Returns:
    list of list of float: A list of lists containing scaled values between the range [0, 1].
    """

    np.random.seed(seed)
    random.seed(seed)
    scaled_data = []
    scaler = MinMaxScaler(feature_range=(0, 1))
    for list_ in list_of_lists:
        if not list_:
            list_ = [random.randint(0, 100) for _ in range(5)]
        # Reshape the data to fit the scaler
        reshaped_data = np.array(list_).reshape(-1, 1)
        scaled_list = scaler.fit_transform(reshaped_data)
        # Flatten the list and append to the result
        scaled_data.append(scaled_list.flatten().tolist())
    
    return scaled_data


class TestTaskFunc(unittest.TestCase):
    
    def test_standard_input(self):
        input_data = [[1, 2, 3], [4, 5, 6]]
        expected_output = [[0.0, 0.5, 1.0], [0.0, 0.5, 1.0]]
        self.assertAlmostEqual(task_func(input_data), expected_output)

    def test_empty_inner_list(self):
        input_data = [[1, 2, 3], []]
        output = task_func(input_data)
        self.assertEqual(len(output[1]), 5)  # Should fill with 5 random integers
        
    def test_multiple_empty_lists(self):
        input_data = [[], [], []]
        output = task_func(input_data)
        for inner_list in output:
            self.assertEqual(len(inner_list), 5)  # Each should be filled with 5 random integers
            
    def test_varied_lengths(self):
        input_data = [[1], [2, 3], []]
        output = task_func(input_data)
        self.assertEqual(len(output[0]), 1)    # First inner list should remain with 1 value
        self.assertEqual(len(output[1]), 2)    # Second inner list should remain with 2 values
        self.assertEqual(len(output[2]), 5)    # Third inner list should now have 5 values

    def test_all_empty_lists(self):
        input_data = [[], [], [], []]
        output = task_func(input_data)
        for inner_list in output:
            self.assertEqual(len(inner_list), 5)  # Every inner list should have been filled

if __name__ == '__main__':
    unittest.main()