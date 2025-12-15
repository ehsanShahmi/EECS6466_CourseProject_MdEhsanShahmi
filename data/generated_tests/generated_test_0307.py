import unittest
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO

# Here is your prompt:
import seaborn as sns
import matplotlib.pyplot as plt
import random


def task_func(list_of_lists, seed=0):
    """
    Create a histogram from the data in a list of lists. If any sublist is empty, 
    it will be filled with 5 random integers ranging from 0 to 100 (both inclusive)
    The histogram will then be constructed using the combined data from all sublists.
    
    Parameters:
    list_of_lists (list): A list containing multiple sublists with integers.
    seed (int, Optional): Seed value for random number generation. Default is 0.
    
    Returns:
    matplotlib.axes._axes.Axes: The histogram plot object.
    
    Requirements:
    - random
    - seaborn
    - matplotlib.pyplot
    
    Example:
    >>> plot = task_func([[1, 2, 3], [], [4, 5, 6]])
    >>> type(plot)
    <class 'matplotlib.axes._axes.Axes'>
    """

               random.seed(seed)
    data = []
    # Initialize a fresh plot
    plt.figure()
    for list_ in list_of_lists:
        if list_:
            data += list_
        else:
            data += [random.randint(0, 100) for _ in range(5)]

    plot = sns.histplot(data)
    return plot


class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        plt.close('all')  # Close any prior plots

    def test_non_empty_sublists(self):
        """Test with all non-empty sublists."""
        input_data = [[1, 2, 3], [4, 5, 6]]
        plot = task_func(input_data)
        self.assertIsInstance(plot, plt.Axes)

    def test_empty_sublists(self):
        """Test with empty sublists that should be replaced by random numbers."""
        input_data = [[], [], []]
        plot = task_func(input_data)
        self.assertIsInstance(plot, plt.Axes)

    def test_mixed_sublists(self):
        """Test with a mix of empty and non-empty sublists."""
        input_data = [[1, 2, 3], [], [4, 5]]
        plot = task_func(input_data)
        self.assertIsInstance(plot, plt.Axes)

    def test_seed_functionality(self):
        """Test that using the same seed gives the same histogram for empty sublists."""
        input_data_1 = [[], []]
        input_data_2 = [[], []]
        plot_1 = task_func(input_data_1, seed=0)
        plot_2 = task_func(input_data_2, seed=0)
        
        # Verify the data is consistent (not the same objects, but comparable)
        data_1 = plot_1.patches
        data_2 = plot_2.patches
        self.assertEqual(len(data_1), len(data_2))

    def test_random_numbers_range(self):
        """Test that random numbers generated are between 0 and 100."""
        input_data = [[], []]
        plot = task_func(input_data)
        values = [patch.get_x() + patch.get_width() / 2 for patch in plot.patches]  # Extract histogram values
        for value in values:
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 100)


if __name__ == '__main__':
    unittest.main()