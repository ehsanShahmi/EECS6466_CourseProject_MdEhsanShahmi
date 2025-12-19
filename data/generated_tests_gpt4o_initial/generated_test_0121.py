import unittest
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Here is your prompt:
import pandas as pd
import numpy as np

def task_func(my_list, seed=42):
    """
    Adds an item "12" to a list 'my_list', simulates sales data for different categories with an optional seed for reproducibility, and returns the data along with a bar plot.
    
    The sales data is a DataFrame with random sales figures for predefined categories.
    The categories are 'Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports'.
    
    Parameters:
    my_list (list): The input list.
    seed (int, optional): Seed for the random number generator (default is None, which means no seed).
    
    Returns:
    tuple: A tuple containing a pandas DataFrame of simulated sales data and the corresponding matplotlib Axes object.
    
    Raises:
    TypeError: If 'my_list' is not a list.

    Requirements:
    - pandas
    - numpy

    Example:
    >>> my_list = [1, 2, 3]
    >>> data, ax = task_func(my_list, seed=123)
    >>> print(data)
             Category  Sales
    0     Electronics   1395
    1         Fashion   1266
    2  Home & Kitchen    198
    3      Automotive    351
    4          Sports   2472
    >>> ax.get_title()  # Returns 'Category-wise Sales Data'
    'Category-wise Sales Data'
    """

    if not isinstance(my_list, list):
        raise TypeError("Input must be a list.")

    if seed is not None:
        np.random.seed(seed)

    my_list.append(12)
    categories = ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']
    sales_data = []
    for category in categories:
        sales = my_list[np.random.randint(0, len(my_list))] * np.random.randint(100, 1000)
        sales_data.append([category, sales])

    sales_df = pd.DataFrame(sales_data, columns=['Category', 'Sales'])

    ax = sales_df.plot(kind='bar', x='Category', y='Sales', legend=False)
    ax.set_title('Category-wise Sales Data')
    ax.set_ylabel('Sales')

    return sales_df, ax

class TestTaskFunc(unittest.TestCase):

    def test_valid_input(self):
        my_list = [1, 2, 3]
        data, ax = task_func(my_list)
        self.assertEqual(len(data), 5)
        self.assertIn('Category', data.columns)
        self.assertIn('Sales', data.columns)

    def test_list_appended(self):
        my_list = [1, 2, 3]
        task_func(my_list)
        self.assertIn(12, my_list)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            task_func("not a list")

    def test_sales_data_range(self):
        my_list = [5, 10, 15]
        data, _ = task_func(my_list)
        for sales in data['Sales']:
            self.assertGreaterEqual(sales, 0)

    def test_plot_title(self):
        my_list = [1, 2, 3]
        _, ax = task_func(my_list)
        self.assertEqual(ax.get_title(), 'Category-wise Sales Data')

if __name__ == '__main__':
    unittest.main()