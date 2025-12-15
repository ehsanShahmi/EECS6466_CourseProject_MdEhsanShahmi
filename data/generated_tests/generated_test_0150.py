import pandas as pd
import numpy as np
import unittest
import matplotlib.pyplot as plt

def task_func(product_dict, product_keys):
    columns = ['Product', 'Quantity', 'Price', 'Profit']
    data = []

    for key in product_keys:
        quantity, price = product_dict[key]
        profit = quantity * price
        data.append([key, quantity, price, profit])

    df = pd.DataFrame(data, columns=columns)

    if not df.empty:
        avg_price = np.mean(df['Price'])
        avg_profit = np.mean(df['Profit'])

        df['Average Price'] = avg_price
        df['Average Profit'] = avg_profit

        ax = df.plot(x='Product', y='Profit', kind='bar', legend=False, title="Profit for each product")
        ax.set_ylabel("Profit")
    else:
        ax = None

    return df, ax

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.product_dict = {
            'Apple': [100, 2.5],
            'Orange': [80, 3.5],
            'Banana': [120, 1.5],
        }
        self.product_keys_full = ['Apple', 'Banana']
        self.product_keys_empty = []
        self.product_keys_invalid = ['Grape']
    
    def test_profit_report_non_empty(self):
        report, ax = task_func(self.product_dict, self.product_keys_full)
        self.assertEqual(len(report), 2)
        self.assertEqual(report['Product'].iloc[0], 'Apple')
        self.assertEqual(report['Quantity'].iloc[0], 100)
        self.assertAlmostEqual(report['Profit'].iloc[0], 250.0)
        
    def test_average_columns(self):
        report, ax = task_func(self.product_dict, self.product_keys_full)
        self.assertTrue('Average Price' in report.columns)
        self.assertTrue('Average Profit' in report.columns)
        self.assertAlmostEqual(report['Average Price'].iloc[0], 2.0)
        self.assertAlmostEqual(report['Average Profit'].iloc[0], 215.0)

    def test_no_products(self):
        report, ax = task_func(self.product_dict, self.product_keys_empty)
        self.assertTrue(report.empty)
        self.assertIsNone(ax)

    def test_invalid_product_key(self):
        with self.assertRaises(KeyError):
            task_func(self.product_dict, self.product_keys_invalid)

    def test_profit_chart_creation(self):
        report, ax = task_func(self.product_dict, self.product_keys_full)
        self.assertIsNotNone(ax)
        self.assertEqual(ax.get_title(), "Profit for each product")
        self.assertEqual(ax.get_ylabel(), "Profit")
        
if __name__ == '__main__':
    unittest.main()