import pandas as pd
import random
import unittest

def task_func(product_list, categories, min_value=10, max_value=100):
    report_data = []

    for product in product_list:
        category = categories[random.randint(0, len(categories) - 1)]
        quantity_sold = random.randint(min_value, max_value)
        revenue = quantity_sold * random.randint(min_value, max_value)
        report_data.append([product, category, quantity_sold, revenue])

    report_df = pd.DataFrame(report_data, columns=['Product', 'Category', 'Quantity Sold', 'Revenue'])
    return report_df

class TestTaskFunc(unittest.TestCase):

    def test_report_shape(self):
        product_list = ['Product 1', 'Product 2']
        categories = ['Electronics', 'Fashion', 'Home', 'Beauty', 'Sports']
        report = task_func(product_list, categories)
        self.assertEqual(report.shape, (len(product_list), 4), "Report shape should match the number of products and 4 columns.")

    def test_categories_in_report(self):
        product_list = ['Product 1']
        categories = ['Electronics', 'Fashion', 'Home', 'Beauty', 'Sports']
        report = task_func(product_list, categories)
        self.assertIn(report.iloc[0]['Category'], categories, "Category should be one of the predefined categories.")

    def test_quantity_sold_range(self):
        product_list = ['Product 1']
        categories = ['Electronics', 'Fashion', 'Home', 'Beauty', 'Sports']
        min_value = 10
        max_value = 50
        report = task_func(product_list, categories, min_value, max_value)
        quantity_sold = report.iloc[0]['Quantity Sold']
        self.assertGreaterEqual(quantity_sold, min_value, "Quantity Sold should not be less than min_value.")
        self.assertLessEqual(quantity_sold, max_value, "Quantity Sold should not be more than max_value.")

    def test_revenue_calculation(self):
        product_list = ['Product 1']
        categories = ['Electronics', 'Fashion', 'Home', 'Beauty', 'Sports']
        min_value = 10
        max_value = 20
        report = task_func(product_list, categories, min_value, max_value)
        quantity_sold = report.iloc[0]['Quantity Sold']
        revenue = report.iloc[0]['Revenue']
        self.assertEqual(revenue, quantity_sold * random.randint(min_value, max_value), "Revenue should be calculated as Quantity Sold times a random value.")

    def test_multiple_products_report(self):
        product_list = ['Product 1', 'Product 2', 'Product 3']
        categories = ['Electronics', 'Fashion', 'Home', 'Beauty', 'Sports']
        report = task_func(product_list, categories)
        self.assertEqual(len(report), len(product_list), "Report should contain an entry for each product.")

if __name__ == '__main__':
    unittest.main()