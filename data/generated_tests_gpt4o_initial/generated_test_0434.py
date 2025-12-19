import pandas as pd
import unittest

# Here is your prompt:
import pandas as pd
import re
import random


def task_func(s: str, seed: int = 0) -> pd.DataFrame:
    """
    Generate a Pandas DataFrame of products with their ID, quantity, code, price, product, and description
    based on a specified string of product data.

    The input string is expected to be divided into segments by newlines. Each segment is expected to
    be further split into parts by whitespace: ID, quantity, code, price, and a product description.
    The function will remove trailing whitespaces in each field and assign a product name per unique code.
    Product name is randomly sampled from: ['Apple', 'Banana', 'Orange', 'Pear', 'Grape'].
    The same product name will be assigned to each code for each input s, however different codes can be
    mapped to the same name.

    Parameters:
    - s    (str): Product data string split by newline, then whitespace.
                  Expected format per segment: '<ID> <Quantity> <Code> <Price> <Description>'
                  If incomplete, this function raises ValueError.
    - seed (int): Random seed for reproducibility. Defaults to 0.

    Returns:
    - data_df (pd.DataFrame): DataFrame with columns: ['ID', 'Quantity', 'Code', 'Price', 'Product', 'Description'].
                              Quantity and Price are expected to be integers.

    Requirements:
    - pandas
    - re
    - random

    Examples:
    >>> s = '1 10 A10B 100 This is a description with spaces'
    >>> df = task_func(s)
    >>> df
      ID  Quantity  Code  Price Product                        Description
    0  1        10  A10B    100    Pear  This is a description with spaces

    >>> s = '1 10 A10B 100 This is a description with spaces\\n2 20 B20C 200 Another description example'
    >>> df = task_func(s)
    >>> df
      ID  Quantity  Code  Price Product                        Description
    0  1        10  A10B    100    Pear  This is a description with spaces
    1  2        20  B20C    200    Pear        Another description example
    """

           
    if not s:
        raise ValueError("Incomplete data provided.")

    random.seed(seed)

    products = ["Apple", "Banana", "Orange", "Pear", "Grape"]
    code_to_product = dict()

    data_list = []
    segments = [segment.strip() for segment in s.split("\n")]
    for segment in segments:
        if segment:
            elements = re.split(r"\s+", segment.strip(), 4)
            if len(elements) < 5:
                raise ValueError("Incomplete data provided.")
            id, quantity, code, price, description = elements
            product = code_to_product.get(code, random.choice(products))
            data_list.append([id, quantity, code, price, product, description])
    df = pd.DataFrame(
        data_list, columns=["ID", "Quantity", "Code", "Price", "Product", "Description"]
    )
    df["Quantity"] = df["Quantity"].astype(int)
    df["Price"] = df["Price"].astype(int)
    return df


class TestTaskFunc(unittest.TestCase):

    def test_single_product(self):
        s = '1 10 A10B 100 This is a description with spaces'
        df = task_func(s, seed=0)
        self.assertEqual(len(df), 1)
        self.assertEqual(df.at[0, 'ID'], '1')
        self.assertEqual(df.at[0, 'Quantity'], 10)
        self.assertEqual(df.at[0, 'Code'], 'A10B')
        self.assertEqual(df.at[0, 'Price'], 100)

    def test_multiple_products(self):
        s = '1 10 A10B 100 This is a description with spaces\n2 20 B20C 200 Another description example'
        df = task_func(s, seed=0)
        self.assertEqual(len(df), 2)
        self.assertIn(df.at[0, 'Code'], ['A10B', 'B20C'])
        self.assertIn(df.at[1, 'Code'], ['A10B', 'B20C'])

    def test_incomplete_data(self):
        s = '1 10 A10B 100 This is a description with spaces\n2 20 B20C'
        with self.assertRaises(ValueError):
            task_func(s)

    def test_empty_input(self):
        s = ''
        with self.assertRaises(ValueError):
            task_func(s)

    def test_product_association(self):
        s = '1 10 A10B 100 Description\n2 20 A10B 200 Another description'
        df = task_func(s, seed=0)
        self.assertTrue(df['Product'].nunique() == 1)  # Same product for the same code

if __name__ == '__main__':
    unittest.main()