import pandas as pd
import unittest
from your_module import task_func  # Replace 'your_module' with the actual module name if needed

class TestTaskFunc(unittest.TestCase):

    def test_output_data_types(self):
        """Test to check if the output is a DataFrame."""
        df = task_func(5)
        self.assertIsInstance(df, pd.DataFrame)

    def test_output_dimensions(self):
        """Test to check if the output DataFrame has correct dimensions."""
        n = 10
        df = task_func(n)
        self.assertEqual(df.shape[0], n)
        self.assertEqual(df.shape[1], 3)  # expect 3 columns: Country, Product, Sales

    def test_country_product_values(self):
        """Test to check if countries and products are sampled correctly."""
        n = 20
        countries = ['USA', 'UK', 'China']
        products = ['Product A', 'Product B']
        
        df = task_func(n, countries=countries, products=products)

        unique_countries = df['Country'].unique()
        unique_products = df['Product'].unique()

        self.assertTrue(set(unique_countries).issubset(set(countries)))
        self.assertTrue(set(unique_products).issubset(set(products)))

    def test_sales_range(self):
        """Test to check if sales values are in the expected range of 1 to 100."""
        n = 30
        df = task_func(n)
        self.assertTrue((df['Sales'] >= 1).all() and (df['Sales'] <= 100).all())

    def test_random_seed_output(self):
        """Test to check if the output is consistent with a given random seed."""
        random_seed = 42
        df1 = task_func(5, random_seed=random_seed)
        df2 = task_func(5, random_seed=random_seed)

        pd.testing.assert_frame_equal(df1, df2)

if __name__ == '__main__':
    unittest.main()