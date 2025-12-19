import json
import math
import unittest
from decimal import Decimal

def task_func(decimal_value, precision=2):
    """
    Calculate the square root of the given decimal value to a certain precision and then encode the result as a JSON string.
    
    Parameters:
    decimal_value (Decimal): The decimal value to find the square root of.
    precision (int, Optional): The number of decimal places to round the square root to. Defaults to 2.
    
    Returns:
    str: The square root of the decimal value encoded as a JSON string.
    
    Requirements:
    - json
    - math
    
    Example:
    >>> from decimal import Decimal
    >>> decimal_value = Decimal('3.9')
    >>> json_str = task_func(decimal_value, decimal_value)
    >>> print(json_str)
    "1.97"
    """
    square_root = round(math.sqrt(decimal_value), precision)
    json_str = json.dumps(str(square_root))
    return json_str

class TestTaskFunc(unittest.TestCase):
    
    def test_positive_decimal(self):
        decimal_value = Decimal('9.0')
        expected_json = json.dumps("3.0")
        self.assertEqual(task_func(decimal_value), expected_json)
    
    def test_another_positive_decimal(self):
        decimal_value = Decimal('2.25')
        expected_json = json.dumps("1.5")
        self.assertEqual(task_func(decimal_value), expected_json)

    def test_precision(self):
        decimal_value = Decimal('2')
        expected_json = json.dumps("1.41")
        self.assertEqual(task_func(decimal_value, 2), expected_json)
    
    def test_zero(self):
        decimal_value = Decimal('0.0')
        expected_json = json.dumps("0.0")
        self.assertEqual(task_func(decimal_value), expected_json)

    def test_negative_decimal(self):
        decimal_value = Decimal('-4.0')
        with self.assertRaises(ValueError):
            task_func(decimal_value)

if __name__ == '__main__':
    unittest.main()