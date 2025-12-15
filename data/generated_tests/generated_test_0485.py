import unittest
from datetime import datetime
from task_module import task_func  # assuming the function is saved in task_module.py


class TestTaskFunction(unittest.TestCase):

    def test_valid_date_range(self):
        """ Test with a valid date range. """
        ax = task_func('2021-01-01', '2021-01-10')
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.get_lines()), 5)  # 5 time zones

    def test_start_date_equals_end_date(self):
        """ Test with start date equal to end date. """
        ax = task_func('2021-01-01', '2021-01-01')
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.get_lines()), 5)  # Should still create lines, just no visible difference.

    def test_inverted_dates(self):
        """ Test with inverted dates (start is after end). """
        with self.assertRaises(ValueError):
            task_func('2021-01-10', '2021-01-01')

    def test_invalid_date_format(self):
        """ Test with invalid date format. """
        with self.assertRaises(ValueError):
            task_func('01-01-2021', '2021-01-10')

    def test_non_existent_date(self):
        """ Test with a non-existent date. """
        with self.assertRaises(ValueError):
            task_func('2021-02-30', '2021-03-01')


if __name__ == '__main__':
    unittest.main()