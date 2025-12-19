import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import unittest

def task_func(l):
    '''
    Draw a histogram of the given array with a Gaussian fit.

    Parameters:
    l (numpy array): The input array.

    Returns:
    ax (matplotlib.axes._axes.Axes): Axes object with the plot.

    Note:
    - This function use "Fit results: mu = {mean},  std = {standard deviation}" as the title of the plot, 
    where the values are rounded to two decimal points.


    Requirements:
    - numpy
    - scipy.stats
    - matplotlib.pyplot

    Example:
    >>> l = np.array([5, 5, 5, 5, 5])
    >>> ax = task_func(l)
    >>> print(ax.get_title())
    Fit results: mu = 5.00,  std = 0.00
    >>> plt.close()
    '''

    fig, ax = plt.subplots()
    ax.hist(l, bins='auto', density=True, alpha=0.6, color='g')

    mu, std = stats.norm.fit(l)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mu, std)
    ax.plot(x, p, 'k', linewidth=2)
    title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
    ax.set_title(title)
    return ax

class TestTaskFunc(unittest.TestCase):

    def test_histogram_title_with_integers(self):
        l = np.array([1, 2, 3, 4, 5])
        ax = task_func(l)
        self.assertEqual(ax.get_title(), "Fit results: mu = 3.00,  std = 1.58")
        plt.close()

    def test_histogram_title_with_zeros(self):
        l = np.array([0, 0, 0, 0, 0])
        ax = task_func(l)
        self.assertEqual(ax.get_title(), "Fit results: mu = 0.00,  std = 0.00")
        plt.close()

    def test_histogram_title_with_negatives(self):
        l = np.array([-3, -2, -1, 0, 1, 2, 3])
        ax = task_func(l)
        self.assertAlmostEqual(float(ax.get_title().split('=')[1].split(',')[0].strip()), 0.00, places=2)
        self.assertAlmostEqual(float(ax.get_title().split('=')[2].strip()), 1.87, places=2)
        plt.close()

    def test_histogram_with_large_values(self):
        l = np.array([100, 200, 300, 400, 500])
        ax = task_func(l)
        self.assertEqual(ax.get_title(), "Fit results: mu = 300.00,  std = 141.42")
        plt.close()

    def test_histogram_with_float_values(self):
        l = np.array([1.5, 2.5, 3.5, 4.5, 5.5])
        ax = task_func(l)
        self.assertAlmostEqual(float(ax.get_title().split('=')[1].split(',')[0].strip()), 3.00, places=2)
        self.assertAlmostEqual(float(ax.get_title().split('=')[2].strip()), 1.58, places=2)
        plt.close()

if __name__ == '__main__':
    unittest.main()