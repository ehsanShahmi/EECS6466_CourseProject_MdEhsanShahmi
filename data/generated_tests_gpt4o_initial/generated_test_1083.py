import unittest
import pandas as pd
from task_module import task_func  # Assume the function is in a module named 'task_module'
from matplotlib.axes import Axes

class TestTaskFunc(unittest.TestCase):

    def test_valid_data(self):
        data = {'Salary_String': ['1,000', '2,000', '3,000'], 'Experience': [1, 2, 3]}
        ax = task_func(data)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(ax.get_title(), "Normalized Salary vs Experience")

    def test_missing_keys(self):
        data = {'Salary_String': ['1,000', '2,000']}
        with self.assertRaises(ValueError) as context:
            task_func(data)
        self.assertEqual(str(context.exception), 
                         "Input data must contain 'Salary_String' and 'Experience' keys.")

    def test_empty_dataframe(self):
        data = {'Salary_String': [], 'Experience': []}
        ax = task_func(data)
        self.assertIsInstance(ax, Axes)
        self.assertEqual(ax.get_title(), "Normalized Salary vs Experience")

    def test_invalid_salary_format(self):
        data = {'Salary_String': ['1,000a', '2,000', '3,000'], 'Experience': [1, 2, 3]}
        with self.assertRaises(ValueError) as context:
            task_func(data)
        self.assertEqual(str(context.exception), "Error converting Salary_String to float.")

    def test_normalization_range(self):
        data = {'Salary_String': ['1,000', '2,000', '3,000'], 'Experience': [1, 2, 3]}
        ax = task_func(data)
        normalized_salaries = ax.collections[0].get_offsets()[:, 1]  # Get the Y values from the scatter plot
        self.assertTrue((normalized_salaries >= 0).all() and (normalized_salaries <= 1).all())

if __name__ == '__main__':
    unittest.main()