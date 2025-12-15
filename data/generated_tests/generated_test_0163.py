import unittest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Here is your prompt:
import numpy as np
import pandas as pd


def task_func(rows=5, cols=5):
    """
    Generates a DataFrame with random numerical data and visualizes this data in a stacked bar chart for
    specified categories.

    Parameters:
    rows (int, optional): Number of rows for the DataFrame. Defaults to 5.
    cols (int, optional): Number of columns for the DataFrame, corresponding to the number of categories.
    Defaults to 5, with a maximum of 5 categories ("A", "B", "C", "D", "E").

    Returns:
    matplotlib.axes._axes.Axes: The Axes object displaying the stacked bar chart.

    Requirements:
    - numpy
    - pandas

    Raises:
    ValueError: If the number of columns exceeds the number of available categories.

    Example:
    >>> import matplotlib
    >>> ax = task_func(3, 3)  # Generates a 3x3 DataFrame and plots it
    >>> isinstance(ax, matplotlib.axes.Axes)
    True
    """
    np.random.seed(0)
    categories = ['A', 'B', 'C', 'D', 'E']
    if cols > len(categories):
        raise ValueError(f"Maximum number of columns allowed is {len(categories)}")

    data = pd.DataFrame(np.random.rand(rows, cols) * 100, columns=categories[:cols])

    ax = data.plot(kind='bar', stacked=True, figsize=(10, 6))
    ax.set_ylabel('Value')
    ax.set_title('Stacked Bar Chart')

    return ax

class TestTaskFunc(unittest.TestCase):

    def test_default_values(self):
        ax = task_func()
        self.assertEqual(ax.patches[0].get_height() + ax.patches[1].get_height(), ax.patches[0].get_height())

    def test_custom_row_count(self):
        ax = task_func(rows=10, cols=5)
        self.assertEqual(ax.collections[0].get_array().size, 10 * 5)

    def test_custom_column_count(self):
        ax = task_func(rows=5, cols=3)
        self.assertEqual(len(ax.get_xticklabels()), 3)

    def test_too_many_columns(self):
        with self.assertRaises(ValueError):
            task_func(rows=5, cols=6)

    def test_return_type(self):
        ax = task_func(rows=5, cols=2)
        self.assertIsInstance(ax, plt.Axes)

if __name__ == '__main__':
    unittest.main()