import pandas as pd
import random
import unittest

def task_func(product_list, categories):
    """
    Create a sales report for a list of products in different categories.
    The report includes the quantity sold and revenue generated for each product.
    
    Parameters:
    product_list (list): The list of products.
    categories (list): A list of categories for the products.
    
    Returns:
    DataFrame: A pandas DataFrame with sales data for the products.
    
    Note:
    - The column names uses are 'Product', 'Category', 'Quantity Sold', and 'Revenue'.
    - The quantity sold is random number from 1 to 100
    - The revenue is the number of quantity sold times with the random number from 10 to 100

    Requirements:
    - pandas
    - random
    
    Example:
    >>> random.seed(0)
    >>> report = task_func(['Product 1'], ['Electronics', 'Fashion', 'Home', 'Beauty', 'Sports'])
    >>> report.iloc[0]['Category'] in ['Electronics', 'Fashion', 'Home', 'Beauty', 'Sports']
    True
    """

           
    report_data = []

    for product in product_list:
        category = categories[random.randint(0, len(categories)-1)]
        quantity_sold = random.randint(1, 100)
        revenue = quantity_sold * random.randint(10, 100)
        report_data.append([product, category, quantity_sold, revenue])

    report_df = pd.DataFrame(report_data, columns=['Product', 'Category', 'Quantity Sold', 'Revenue'])
    return report_df

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.categories = ['Electronics', 'Fashion', 'Home', 'Beauty', 'Sports']
        self.product_list = ['Product A', 'Product B', 'Product C']

    def test_non_empty_report(self):
        report = task_func(self.product_list, self.categories)
        self.assertFalse(report.empty, "The report should not be empty.")

    def test_correct_column_names(self):
        report = task_func(self.product_list, self.categories)
        expected_columns = ['Product', 'Category', 'Quantity Sold', 'Revenue']
        self.assertListEqual(list(report.columns), expected_columns, "The report should have correct column names.")

    def test_quantity_sold_range(self):
        report = task_func(self.product_list, self.categories)
        self.assertTrue((report['Quantity Sold'] >= 1).all() and (report['Quantity Sold'] <= 100).all(),
                        "Quantity Sold should be in the range of 1 to 100.")

    def test_revenue_calculation(self):
        report = task_func(self.product_list, self.categories)
        for index, row in report.iterrows():
            quantity_sold = row['Quantity Sold']
            # Revenue is calculated using a random number, ensuring it's valid with this check
            self.assertGreaterEqual(row['Revenue'], quantity_sold * 10, "Revenue should be at least quantity sold times 10.")
            self.assertLessEqual(row['Revenue'], quantity_sold * 100, "Revenue should be at most quantity sold times 100.")

    def test_random_category_assignment(self):
        report = task_func(self.product_list, self.categories)
        unique_categories = report['Category'].unique()
        for category in unique_categories:
            self.assertIn(category, self.categories, "Each product's category should be from the given categories.")

if __name__ == '__main__':
    unittest.main()