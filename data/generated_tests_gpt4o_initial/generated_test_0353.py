import pandas as pd
import random
import unittest

def task_func(product_list, categories, min_value=10, max_value=100):
    report_data = []
    for product in product_list:
        category = categories[random.randint(0, len(categories)-1)]
        quantity_sold = random.randint(min_value, max_value)
        revenue = random.randint(min_value, max_value)
        total_revenue = quantity_sold * revenue
        report_data.append([product, category, quantity_sold, revenue, total_revenue])
    report_df = pd.DataFrame(report_data, columns=['Product', 'Category', 'Quantity Sold', 'Revenue', 'Total Revenue'])
    return report_df

class TestTaskFunction(unittest.TestCase):

    def setUp(self):
        self.products = ['Product A', 'Product B', 'Product C']
        self.categories = ['Electronics', 'Fashion', 'Home', 'Beauty', 'Sports']
    
    def test_product_count(self):
        report = task_func(self.products, self.categories, 10, 50)
        self.assertEqual(len(report), len(self.products))

    def test_column_names(self):
        report = task_func(self.products, self.categories, 10, 50)
        expected_columns = ['Product', 'Category', 'Quantity Sold', 'Revenue', 'Total Revenue']
        self.assertTrue(all(column in report.columns for column in expected_columns))

    def test_quantity_sold_range(self):
        report = task_func(self.products, self.categories, 10, 50)
        self.assertTrue((report['Quantity Sold'] >= 10).all())
        self.assertTrue((report['Quantity Sold'] <= 50).all())

    def test_revenue_range(self):
        report = task_func(self.products, self.categories, 10, 50)
        self.assertTrue((report['Revenue'] >= 10).all())
        self.assertTrue((report['Revenue'] <= 50).all())

    def test_total_revenue_calculation(self):
        report = task_func(self.products, self.categories, 10, 10)
        for index, row in report.iterrows():
            self.assertEqual(row['Total Revenue'], row['Quantity Sold'] * row['Revenue'])

if __name__ == '__main__':
    unittest.main()