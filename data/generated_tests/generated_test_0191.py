import random
from scipy import stats
import unittest

# The provided prompt's function code is not to be modified, but will be used for testing purposes

# Test suite for the task_func function
class TestTaskFunc(unittest.TestCase):

    def test_sales_return_type(self):
        """Test if the function returns a dictionary."""
        animals = ['Dog', 'Cat', 'Bird']
        sales = task_func(animals, 5)
        self.assertIsInstance(sales, dict, "Expected output to be a dictionary.")

    def test_sales_include_all_animals(self):
        """Test if the sales dictionary contains all animal types."""
        animals = ['Dog', 'Cat', 'Bird']
        sales = task_func(animals, 5)
        for animal in animals:
            self.assertIn(animal, sales.keys(), f"{animal} should be in sales dictionary.")

    def test_sales_non_negative(self):
        """Test if the total number of sales is non-negative."""
        animals = ['Dog', 'Cat', 'Bird']
        sales = task_func(animals, 5)
        total_sales = sum(sales.values())
        self.assertGreaterEqual(total_sales, 0, "Total sales should be non-negative.")

    def test_sales_distribution(self):
        """Test that the function can handle varying mean values."""
        animals = ['Dog', 'Cat', 'Bird']
        for mean in [0, 10, 100]:
            sales = task_func(animals, mean)
            total_sales = sum(sales.values())
            self.assertGreaterEqual(total_sales, 0, "Total sales should be non-negative for mean: {}".format(mean))

    def test_empty_animal_list(self):
        """Test the function with an empty animal list."""
        animals = []
        sales = task_func(animals, 5)
        self.assertEqual(sales, {}, "Sales should be an empty dictionary when no animals are provided.")

# If this script is executed, run the test suite
if __name__ == '__main__':
    unittest.main()