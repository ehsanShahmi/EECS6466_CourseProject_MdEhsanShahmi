import unittest
import os
import csv

# Here is your prompt:
import csv
import collections
import operator

def task_func(csv_file_path):
    """
    Find the best-selling product from a given CSV file with sales data.

    This function parses a CSV file assumed to have a header followed by rows containing
    two columns: 'product' and 'quantity'. It computes the total sales per product and
    determines the product with the highest cumulative sales. The CSV file must include
    at least these two columns, where 'product' is the name of the product as a string
    and 'quantity' is the number of units sold as an integer.

    Args:
        csv_file_path (str): The file path to the CSV file containing sales data.

    Returns:
        str: The name of the top-selling product based on the total quantity sold.

    Requirements:
    - csv
    - collections
    - operator

    Example:
    >>> task_func("path/to/sales.csv")
    'Product ABC'
    """

    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        sales_data = collections.defaultdict(int)
        for row in reader:
            product, quantity = row[0], int(row[1])
            sales_data[product] += quantity

    top_selling_product = max(sales_data.items(), key=operator.itemgetter(1))[0]

    return top_selling_product

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        """Set up temporary CSV files for testing."""
        self.test_file_1 = 'test_sales_1.csv'
        self.test_file_2 = 'test_sales_2.csv'
        self.test_file_3 = 'test_sales_3.csv'
        
        # Setup CSV test data
        with open(self.test_file_1, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['product', 'quantity'])
            writer.writerow(['Product A', 10])
            writer.writerow(['Product B', 5])
            writer.writerow(['Product A', 15])
            
        with open(self.test_file_2, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['product', 'quantity'])
            writer.writerow(['Product C', 20])
            writer.writerow(['Product D', 30])
            writer.writerow(['Product C', 10])
            
        with open(self.test_file_3, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['product', 'quantity'])
            writer.writerow(['Product E', 5])
            writer.writerow(['Product F', 2])

    def tearDown(self):
        """Remove temporary CSV files after testing."""
        for file in [self.test_file_1, self.test_file_2, self.test_file_3]:
            if os.path.exists(file):
                os.remove(file)

    def test_best_selling_product_case_1(self):
        """Test case 1: Determine the best-selling product correctly."""
        result = task_func(self.test_file_1)
        self.assertEqual(result, 'Product A')

    def test_best_selling_product_case_2(self):
        """Test case 2: Determine the best-selling product with different products."""
        result = task_func(self.test_file_2)
        self.assertEqual(result, 'Product D')

    def test_best_selling_product_case_3(self):
        """Test case 3: No clear best-selling, different quantities."""
        result = task_func(self.test_file_3)
        self.assertEqual(result, 'Product E')

    def test_best_selling_product_empty_file(self):
        """Test case 4: Handle an empty file, should raise an error."""
        empty_file = 'empty_sales.csv'
        with open(empty_file, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['product', 'quantity'])
        
        with self.assertRaises(ValueError):
            task_func(empty_file)
        
        os.remove(empty_file)

    def test_best_selling_product_no_sales(self):
        """Test case 5: Handle a file with no sales rows, should raise an error."""
        no_sales_file = 'no_sales.csv'
        with open(no_sales_file, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['product', 'quantity'])
        
        with self.assertRaises(IndexError):
            task_func(no_sales_file)
        
        os.remove(no_sales_file)

if __name__ == '__main__':
    unittest.main()