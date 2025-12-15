import unittest
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter

# Here is your prompt:
def task_func(data):
    """
    Plot a scatter graph of tuples and highlight the tuple with the maximum value at index 1.
    
    Parameters:
    data (list of tuple): A list of tuples where each tuple contains two integers.
    
    Returns:
    matplotlib.axes.Axes: The Axes object of the plot for further manipulation and testing, with the title 'Max Tuple Highlighted', x-axis labeled 'x', y-axis labeled 'y', and a legend.
    
    Requirements:
    - numpy
    - operator
    - matplotlib.pyplot
    
    Example:
    >>> ax = task_func([(10, 20), (30, 40), (25, 50)])
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """
    max_tuple = max(data, key=itemgetter(1))
    tuples = np.array(data)
    x = tuples[:,0]
    y = tuples[:,1]
    fig, ax = plt.subplots()
    ax.scatter(x, y, label='Data')
    ax.scatter(*max_tuple, color='red', label='Max Tuple')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Max Tuple Highlighted')
    ax.legend()
    return ax

class TestTaskFunc(unittest.TestCase):

    def test_standard_case(self):
        data = [(10, 20), (30, 40), (25, 50)]
        ax = task_func(data)
        # Check the title of the plot
        self.assertEqual(ax.get_title(), 'Max Tuple Highlighted')
        # Check the labels
        self.assertEqual(ax.get_xlabel(), 'x')
        self.assertEqual(ax.get_ylabel(), 'y')
        # Check if the max tuple is highlighted (40 in this case)
        self.assertEqual(ax.collections[1].get_offsets()[0][0], 30)
        self.assertEqual(ax.collections[1].get_offsets()[0][1], 40)

    def test_empty_input(self):
        data = []
        with self.assertRaises(ValueError):
            task_func(data)
        
    def test_single_tuple(self):
        data = [(15, 25)]
        ax = task_func(data)
        # Check if the single tuple is highlighted
        self.assertEqual(ax.collections[1].get_offsets()[0][0], 15)
        self.assertEqual(ax.collections[1].get_offsets()[0][1], 25)

    def test_negative_values(self):
        data = [(10, -20), (-30, -40), (-25, -50)]
        ax = task_func(data)
        # Check if the max tuple is identified correctly (10, -20)
        self.assertEqual(ax.collections[1].get_offsets()[0][0], 10)
        self.assertEqual(ax.collections[1].get_offsets()[0][1], -20)

    def test_identical_values(self):
        data = [(10, 20), (30, 20), (25, 20)]
        ax = task_func(data)
        # Check which one is chosen as max (first encountered - (10,20))
        self.assertEqual(ax.collections[1].get_offsets()[0][0], 10)
        self.assertEqual(ax.collections[1].get_offsets()[0][1], 20)

if __name__ == '__main__':
    unittest.main()