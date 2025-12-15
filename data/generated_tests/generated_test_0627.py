import unittest
import pandas as pd
from random import randint
from statistics import mean

# The provided code prompt (function, imports, etc.)
from random import randint
from statistics import mean
import pandas as pd


def task_func(products_list):
    """
    This function takes in a list of product names and generates random sales data for each product over a period of
    12 months. It then calculates the average sales for each product and returns the results as a pandas DataFrame with
    columns: 'Product', 'Month 1', 'Month 2', ..., 'Month 12', 'Average Sales'.
    
    Parameters:
    products_list (list): A list of product names.
    
    Returns:
    DataFrame: A pandas DataFrame with columns: 'Product', 'Month 1', 'Month 2', ..., 'Month 12', 'Average Sales'.
    
    Requirements:
    - pandas
    - random
    - statistics
    
    Example:
    >>> products = ['Apples', 'Bananas', 'Grapes', 'Oranges', 'Pineapples']
    >>> sales_data = task_func(products)
    >>> type(sales_data)
    <class 'pandas.core.frame.DataFrame'>
    """

    sales_data = []

    for product in products_list:
        sales = [randint(100, 500) for _ in range(12)]
        avg_sales = mean(sales)
        sales.append(avg_sales)
        sales_data.append([product] + sales)

    sales_df = pd.DataFrame(sales_data, columns=['Product'] + [f'Month {i+1}' for i in range(12)] + ['Average Sales'])

    return sales_df


class TestTaskFunc(unittest.TestCase):
    def test_empty_product_list(self):
        result = task_func([])
        self.assertTrue(result.empty)
    
    def test_single_product(self):
        result = task_func(['Apples'])
        self.assertEqual(len(result), 1)
        self.assertIn('Apples', result['Product'].values)
        self.assertEqual(len(result.columns), 14)  # 12 months + product name + average sales

    def test_multiple_products(self):
        products = ['Apples', 'Bananas', 'Grapes']
        result = task_func(products)
        
        self.assertEqual(len(result), 3)
        for product in products:
            self.assertIn(product, result['Product'].values)

    def test_average_sales_calculation(self):
        result = task_func(['Oranges'])
        # Check that the average sales is the mean of the first 12 month sales data
        sales = result.iloc[0, 1:13].values
        average_sales = result.iloc[0, 13]
        
        self.assertAlmostEqual(average_sales, mean(sales))

    def test_dataframe_structure(self):
        products = ['Apples', 'Bananas']
        result = task_func(products)
        
        self.assertIsInstance(result, pd.DataFrame)
        self.assertListEqual(list(result.columns), ['Product'] + [f'Month {i+1}' for i in range(12)] + ['Average Sales'])


if __name__ == '__main__':
    unittest.main()