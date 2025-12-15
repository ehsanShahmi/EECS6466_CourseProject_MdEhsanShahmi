import unittest
import os
import pickle
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

# Here is your prompt:
import pickle
import os
import matplotlib.pyplot as plt

def task_func(numbers, file_path="save.pkl"):
    """
    Save a Matplotlib image generated from the provided "numbers" list in a pickle file.
    The function then reads the image back from the file for validation and deletes the pickle file afterward.

    Parameters:
    - numbers  (list): List of int/float values used to generate the matplotlib figure.
    - file_path (str): Path to temporary pickle file. Defaults to 'save.pkl'.

    Returns:
    - loaded_fig (matplotlib.figure.Figure): The loaded matplotlib figure from file_path.

    Requirements:
    - pickle
    - os
    - matplotlib.pyplot

    Raises:
    - TypeError: If the input is not a list of numbers.
    
    Example:
    >>> numbers = [random.random() for _ in range(100)]
    >>> loaded_fig = task_func(numbers)
    >>> type(loaded_fig)
    <class 'matplotlib.figure.Figure'>
    """

    if not isinstance(numbers, list) or not all(
        isinstance(item, (int, float)) for item in numbers
    ):
        raise TypeError("Expect list of numbers.")

    fig = plt.figure()
    plt.plot(numbers)

    with open(file_path, "wb") as file:
        pickle.dump(fig, file)

    with open(file_path, "rb") as file:
        loaded_fig = pickle.load(file)

    os.remove(file_path)

    return loaded_fig

class TestTaskFunc(unittest.TestCase):

    def test_valid_integer_list(self):
        # Test with a valid list of integers
        numbers = [1, 2, 3, 4, 5]
        loaded_fig = task_func(numbers)
        self.assertIsInstance(loaded_fig, Figure)

    def test_valid_float_list(self):
        # Test with a valid list of floats
        numbers = [1.1, 2.2, 3.3, 4.4, 5.5]
        loaded_fig = task_func(numbers)
        self.assertIsInstance(loaded_fig, Figure)

    def test_mixed_numeric_list(self):
        # Test with a valid mixed numeric list (int and float)
        numbers = [1, 2.5, 3, 4.75]
        loaded_fig = task_func(numbers)
        self.assertIsInstance(loaded_fig, Figure)

    def test_empty_list(self):
        # Test with an empty list
        numbers = []
        loaded_fig = task_func(numbers)
        self.assertIsInstance(loaded_fig, Figure)

    def test_invalid_type(self):
        # Test with invalid type (not a list)
        with self.assertRaises(TypeError):
            task_func("not a list")
        
        # Test with a list containing invalid types
        with self.assertRaises(TypeError):
            task_func([1, 2, 'invalid', 4.0])

if __name__ == "__main__":
    unittest.main()