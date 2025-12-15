import pandas as pd
import unittest
from random import choices, seed

def task_func(products, ratings, weights, random_seed=42):
    """
    Generates a DataFrame containing ratings for a given list of products. Ratings are generated randomly based on the provided weights. 
    The DataFrame is sorted by ratings in descending order.

    Parameters:
    products (list): List of product names.
    ratings (list): List of possible ratings.
    weights (list): List of weights corresponding to each rating for weighted random selection.
    random_seed (int, optional): Seed for random number generation for reproducibility. Defaults to 42.

    Returns:
    pandas.DataFrame: A DataFrame with two columns: 'Product' and 'Rating', sorted by 'Rating' in descending order.
    """
    seed(random_seed)  # Setting the seed for reproducibility
    product_ratings = []

    for product in products:
        rating = choices(ratings, weights, k=1)[0]
        product_ratings.append([product, rating])

    df = pd.DataFrame(product_ratings, columns=["Product", "Rating"])
    df.sort_values("Rating", ascending=False, inplace=True)

    return df

class TestTaskFunction(unittest.TestCase):

    def test_output_type(self):
        products = ["Product A", "Product B"]
        ratings = [1, 2, 3, 4, 5]
        weights = [0.2, 0.3, 0.2, 0.2, 0.1]
        result = task_func(products, ratings, weights)
        self.assertIsInstance(result, pd.DataFrame)

    def test_correct_columns(self):
        products = ["Product A", "Product B"]
        ratings = [1, 2, 3, 4, 5]
        weights = [0.2, 0.3, 0.2, 0.2, 0.1]
        result = task_func(products, ratings, weights)
        self.assertTrue('Product' in result.columns)
        self.assertTrue('Rating' in result.columns)

    def test_sorted_output(self):
        products = ["Product A", "Product B", "Product C"]
        ratings = [1, 2, 3, 4, 5]
        weights = [0.2, 0.3, 0.2, 0.2, 0.1]
        result = task_func(products, ratings, weights)
        self.assertTrue(all(result['Rating'].iloc[i] >= result['Rating'].iloc[i + 1] for i in range(len(result) - 1)))

    def test_reproducibility(self):
        products = ["Product A", "Product B"]
        ratings = [1, 2, 3, 4, 5]
        weights = [0.2, 0.3, 0.2, 0.2, 0.1]
        result1 = task_func(products, ratings, weights, random_seed=42)
        result2 = task_func(products, ratings, weights, random_seed=42)
        pd.testing.assert_frame_equal(result1, result2)

    def test_matching_length(self):
        products = ["Product A", "Product B", "Product C"]
        ratings = [1, 2, 3, 4, 5]
        weights = [0.2, 0.3, 0.2, 0.2, 0.1]
        result = task_func(products, ratings, weights)
        self.assertEqual(len(result), len(products))

if __name__ == '__main__':
    unittest.main()