import json
from datetime import datetime
import numpy as np
from decimal import Decimal
import unittest

class TestTaskFunc(unittest.TestCase):

    def test_serializes_datetime(self):
        input_data = {'time': datetime(2023, 4, 1, 12, 0, tzinfo=None)}
        expected_result = '{"time": "2023-04-01T12:00:00"}'
        result = task_func(input_data)
        self.assertEqual(result, expected_result)

    def test_serializes_numpy_array(self):
        input_data = {'array': np.array([1, 2, 3])}
        expected_result = '{"array": [1, 2, 3]}'
        result = task_func(input_data)
        self.assertEqual(result, expected_result)

    def test_serializes_decimal(self):
        input_data = {'amount': Decimal('10.99')}
        expected_result = '{"amount": "10.99"}'
        result = task_func(input_data)
        self.assertEqual(result, expected_result)

    def test_serializes_combined_types(self):
        input_data = {
            'time': datetime(2023, 4, 1, 12, 0, tzinfo=None),
            'array': np.array([1, 2, 3]),
            'amount': Decimal('10.99')
        }
        expected_result = '{"time": "2023-04-01T12:00:00", "array": [1, 2, 3], "amount": "10.99"}'
        result = task_func(input_data)
        self.assertEqual(result, expected_result)

    def test_raises_type_error_on_unsupported_type(self):
        input_data = {'unsupported': set([1, 2, 3])}  # set is not supported
        with self.assertRaises(TypeError):
            task_func(input_data)

if __name__ == '__main__':
    unittest.main()