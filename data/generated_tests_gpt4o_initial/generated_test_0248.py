import unittest
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

# Here is your prompt:
import numpy as np
import matplotlib.pyplot as plt
import itertools


def task_func(data_list):
    """
    Unzips the provided list of tuples and plots the numerical values for each position.

    Parameters:
    - data_list (list of tuples): A list containing tuples. Each tuple should contain a character and two numerical values.

    Returns:
    - Axes: The plot with the unzipped numerical values.

    Requirements:
    - numpy
    - matplotlib.pyplot
    - itertools

    Raises:
    - ValueError: If the data_list is empty.

    Example:
    >>> plot = task_func([('a', 1, 2), ('b', 2, 3), ('c', 3, 4), ('d', 4, 5), ('e', 5, 6)])
    >>> type(plot)
    <class 'matplotlib.axes._axes.Axes'>
    """

    unzipped_data = list(itertools.zip_longest(*data_list, fillvalue=np.nan))
    if len(unzipped_data) == 0:
        raise ValueError('Empty data_list')

    fig, ax = plt.subplots()
    for i, column in enumerate(unzipped_data[1:], start=1):
        ax.plot(column, label='Position {}'.format(i))
    ax.legend()
    return ax


class TestTaskFunc(unittest.TestCase):

    def test_valid_input(self):
        data_list = [('a', 1, 2), ('b', 2, 3), ('c', 3, 4)]
        plot = task_func(data_list)
        self.assertIsInstance(plot, Axes)

    def test_empty_data_list(self):
        with self.assertRaises(ValueError) as context:
            task_func([])
        self.assertEqual(str(context.exception), 'Empty data_list')

    def test_inconsistent_length_tuples(self):
        data_list = [('a', 1, 2), ('b', 2), ('c', 3, 4)]
        plot = task_func(data_list)
        self.assertIsInstance(plot, Axes)

    def test_nan_fill_value(self):
        data_list = [('a', 1, 2), ('b', 2, 3), ('c', 3)]
        plot = task_func(data_list)
        unzipped_data = list(itertools.zip_longest(*data_list, fillvalue=np.nan))
        self.assertTrue(np.isnan(unzipped_data[1][2]))  # Check if the NaN is present
    
    def test_multiple_columns(self):
        data_list = [('a', 1, 2), ('b', 2, 3), ('c', 3, 4), ('d', 4, 5)]
        plot = task_func(data_list)
        lines = plot.lines
        self.assertEqual(len(lines), 2)  # There should be 2 lines for 2 numerical columns


if __name__ == '__main__':
    unittest.main()