import pandas as pd
import matplotlib.pyplot as plt
import unittest
from random import randint

# Here is your prompt:
import pandas as pd
import matplotlib.pyplot as plt
from random import randint


def task_func(num_types=5, integer_range=(0, 100)):
    """
    Generate a DataFrame containing random integer values across a specified number of categories,
    and visualize these data as a horizontal stacked bar chart.

    Parameters:
    num_types (int, optional): The number of distinct categories for which data will be generated. Defaults to 5.
    integer_range (tuple, optional): The inclusive range from which random integers are drawn. Defaults to (0, 100).

    Returns:
    tuple: A tuple containing a matplotlib Figure and Axes objects for the generated plot.

    Requirements:
    - pandas
    - matplotlib
    - random

    Note:
    The plot displays categories on the y-axis and their corresponding values on the x-axis, with
    data segmented by category.

    Example:
    >>> fig, ax = task_func(3, (0, 50))
    >>> isinstance(fig, plt.Figure)
    True
    """

    LABELS = [f'Type{i + 1}' for i in range(num_types)]
    data = pd.DataFrame({label: [randint(*integer_range) for _ in range(num_types)] for label in LABELS})

    fig, ax = plt.subplots()
    data.plot(kind='barh', stacked=True, ax=ax)

    return fig, ax

class TestTaskFunc(unittest.TestCase):
    
    def test_default_parameters(self):
        """ Test the function with default parameters. """
        fig, ax = task_func()
        self.assertIsInstance(fig, plt.Figure)
        self.assertIsInstance(ax, plt.Axes)

    def test_custom_num_types(self):
        """ Test the function with a custom number of types. """
        num_types = 3
        fig, ax = task_func(num_types=num_types)
        self.assertIsInstance(fig, plt.Figure)
        self.assertIsInstance(ax, plt.Axes)
        
        # Ensure that the data has the correct number of columns.
        data = ax.get_children()[0].get_array()
        self.assertEqual(data.shape[0], num_types)

    def test_integer_range(self):
        """ Test the function with a custom integer range. """
        integer_range = (10, 50)
        fig, ax = task_func(integer_range=integer_range)
        data = ax.get_children()[0].get_array()

        # Check that all values are within the specified integer range.
        for i in range(data.shape[1]):
            for value in data[:, i]:
                self.assertGreaterEqual(value, integer_range[0])
                self.assertLessEqual(value, integer_range[1])

    def test_large_num_types(self):
        """ Test the function with a large number of types. """
        num_types = 10
        fig, ax = task_func(num_types=num_types)
        data = ax.get_children()[0].get_array()
        
        # Ensure that the data has the correct number of columns.
        self.assertEqual(data.shape[0], num_types)

    def test_no_data_generated(self):
        """ Test with num_types set to zero, expecting no data to be plotted. """
        fig, ax = task_func(num_types=0)
        data = ax.get_children()
        
        # Expect no data to be plotted, hence no children in ax.
        self.assertEqual(len(data), 0)

if __name__ == "__main__":
    unittest.main()