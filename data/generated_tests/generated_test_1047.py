from datetime import datetime
import random
import matplotlib.pyplot as plt
import unittest

def task_func(date_str):
    """
    Generates a list of random integers, where the count of integers equals the day of the month in the
    provided date, then generates a line plot of these integers and returns the Axes object of the plot.

    Parameters:
    - date_str (str): The date string in "yyyy-mm-dd" format.

    Returns:
    - matplotlib.axes.Axes: The Axes object containing the plot.

    Requirements:
    - datetime.datetime
    - random
    - matplotlib.pyplot

    Example:
    >>> ax = task_func('2023-06-15')
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """

    date = datetime.strptime(date_str, "%Y-%m-%d")
    num_of_values = date.day
    random_values = [random.randint(1, 100) for _ in range(num_of_values)]
    _, ax = plt.subplots()
    ax.plot(random_values)
    return ax

class TestTaskFunc(unittest.TestCase):

    def test_valid_date_january(self):
        """Test with a valid date in January"""
        ax = task_func('2023-01-15')
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines[0].get_xydata()), 15)

    def test_valid_date_february_leap_year(self):
        """Test with a valid leap year date in February"""
        ax = task_func('2024-02-29')
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines[0].get_xydata()), 29)

    def test_valid_date_february_non_leap_year(self):
        """Test with a valid non-leap year date in February"""
        ax = task_func('2023-02-28')
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines[0].get_xydata()), 28)

    def test_valid_date_december(self):
        """Test with a valid date in December"""
        ax = task_func('2023-12-25')
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines[0].get_xydata()), 25)

    def test_invalid_date_format(self):
        """Test with an invalid date format"""
        with self.assertRaises(ValueError):
            task_func('15-01-2023')

if __name__ == '__main__':
    unittest.main()