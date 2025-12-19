import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import random
from matplotlib.axes import Axes
import unittest

class ValueObject:
    value = 0

    def __init__(self, mu=0, std=1, seed=77):
        random.seed(seed)
        self.value = random.gauss(mu, std)

def task_func(obj_list) -> Axes:
    '''
    Draw the histogram and the custom normal distribution curve from the mean and standard deviation
    derived from the values of a list of ValueObjects and return the plotted Axes. For an empty list,
    the mean and the standard deviation is 0.
    
    Parameters:
    obj_list (list): The list of objects.
    attr (str): The attribute to plot.

    Returns:
    Axes: The plotted Axes.

    Requirements:
    - numpy
    - scipy.stats
    - matplotlib
    - random

    Example:
    >>> obj_list = [ValueObject(mu=23, std=77), ValueObject(mu=23, std=77, seed=222), ValueObject(mu=23, std=77, seed=333)]
    >>> ax = task_func(obj_list)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    '''

    if len(obj_list) == 0:
        values = [0]
    else:
        values = [obj.value for obj in obj_list]

    # Create a new figure and axis
    fig, ax = plt.subplots()

    # Plot histogram
    ax.hist(values, bins=30, density=True, alpha=0.6, color='g')
    mean = np.mean(values)
    std = np.std(values)

    # Plot the PDF.
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mean, std)
    ax.plot(x, p, 'k', linewidth=2)

    title = "Fit results: mu = %.2f,  std = %.2f" % (mean, std)
    ax.set_title(title)

    plt.close(fig)  # Close the figure to avoid display during function execution
    return ax

class TestTaskFunc(unittest.TestCase):

    def test_empty_list(self):
        """Test when given an empty list, the mean and std should be 0."""
        obj_list = []
        ax = task_func(obj_list)
        self.assertEqual(ax.get_title(), "Fit results: mu = 0.00,  std = 0.00")
    
    def test_single_value_object(self):
        """Test with a single ValueObject."""
        obj_list = [ValueObject(mu=10, std=5)]
        ax = task_func(obj_list)
        self.assertGreater(len(ax.patches), 0)  # histogram should have bars
    
    def test_multiple_value_objects(self):
        """Test functionality with multiple ValueObjects."""
        obj_list = [
            ValueObject(mu=10, std=5, seed=1),
            ValueObject(mu=10, std=5, seed=2),
            ValueObject(mu=10, std=5, seed=3)
        ]
        ax = task_func(obj_list)
        self.assertGreater(len(ax.patches), 0)  # histogram should have bars
    
    def test_mean_std_calculation(self):
        """Test if the mean and std are calculated correctly."""
        obj_list = [
            ValueObject(mu=10, std=5, seed=1),
            ValueObject(mu=20, std=5, seed=2)
        ]
        ax = task_func(obj_list)
        mean = np.mean([obj.value for obj in obj_list])
        std = np.std([obj.value for obj in obj_list])
        self.assertIn(f"mu = {mean:.2f}", ax.get_title())
        self.assertIn(f"std = {std:.2f}", ax.get_title())
    
    def test_histogram_bins(self):
        """Test if the histogram is using the correct number of bins."""
        obj_list = [ValueObject(mu=10, std=5) for _ in range(100)]
        ax = task_func(obj_list)
        self.assertEqual(len(ax.patches), 30)  # Sanity check for default number of bins

if __name__ == "__main__":
    unittest.main()