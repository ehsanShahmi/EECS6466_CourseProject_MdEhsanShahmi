import unittest
import pandas as pd
import numpy as np
from random import seed

# Provided code (from prompt)
import pandas as pd
import numpy as np
import random
from random import randint, seed

CATEGORIES = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Toys & Games']

def task_func(mystrings, n_products, seed=0):
    catalogue_data = []
    random.seed(seed)
    np.random.seed(seed)
    for _ in range(n_products):
        product_name = mystrings[randint(0, len(mystrings) - 1)].replace(' ', '_')
        category = CATEGORIES[randint(0, len(CATEGORIES) - 1)]
        price = round(np.random.normal(50, 10), 2)
        catalogue_data.append([product_name, category, price])

    catalogue_df = pd.DataFrame(catalogue_data, columns=['Product Name', 'Category', 'Price'])

    return catalogue_df

# Test Suite
class TestTaskFunc(unittest.TestCase):

    def test_output_shape(self):
        result = task_func(['Product1', 'Product2'], 5, seed=42)
        self.assertEqual(result.shape[0], 5)
        self.assertEqual(result.shape[1], 3)

    def test_product_name_format(self):
        result = task_func(['Product A', 'Product B'], 3, seed=0)
        product_names = result['Product Name'].tolist()
        for name in product_names:
            self.assertTrue('_' in name)

    def test_category_assignment(self):
        result = task_func(['Product1', 'Product2'], 10, seed=1)
        categories = result['Category'].unique()
        self.assertTrue(set(categories).issubset(set(CATEGORIES)))

    def test_price_distribution(self):
        result = task_func(['Product1', 'Product2'], 100, seed=2)
        self.assertTrue(all(result['Price'] >= 0))  # Prices should be non-negative
        self.assertTrue(all(result['Price'] <= 100))  # Assuming the price will be within a reasonable range

    def test_randomness_with_seed(self):
        result1 = task_func(['Product1', 'Product2'], 5, seed=3)
        result2 = task_func(['Product1', 'Product2'], 5, seed=3)
        pd.testing.assert_frame_equal(result1, result2)  # Outputs should be the same with the same seed

if __name__ == '__main__':
    unittest.main()