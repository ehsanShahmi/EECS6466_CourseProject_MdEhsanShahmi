import json
from datetime import datetime
from decimal import Decimal
import unittest

class TestTaskFunc(unittest.TestCase):

    def test_serialize_datetime(self):
        """ Test serialization of a datetime object """
        my_obj = {'time': datetime(2023, 4, 1, 12, 0)}
        expected_result = '{"time": "2023-04-01T12:00:00"}'
        self.assertEqual(task_func(my_obj), expected_result)

    def test_serialize_decimal(self):
        """ Test serialization of a Decimal object """
        my_obj = {'amount': Decimal('10.99')}
        expected_result = '{"amount": "10.99"}'
        self.assertEqual(task_func(my_obj), expected_result)

    def test_serialize_datetime_and_decimal(self):
        """ Test serialization of both datetime and Decimal objects """
        my_obj = {'time': datetime(2023, 4, 1, 12, 0), 'amount': Decimal('10.99')}
        expected_result = '{"time": "2023-04-01T12:00:00", "amount": "10.99"}'
        self.assertEqual(task_func(my_obj), expected_result)

    def test_serialize_simple_dictionary(self):
        """ Test serialization of a simple dictionary without complex types """
        my_obj = {'name': 'Alice', 'age': 30}
        expected_result = '{"name": "Alice", "age": 30}'
        self.assertEqual(task_func(my_obj), expected_result)

    def test_serialize_nested_structure(self):
        """ Test serialization of a nested structure including datetime and Decimal """
        my_obj = {
            'event': 'Meeting',
            'details': {
                'time': datetime(2023, 4, 1, 12, 0),
                'cost': Decimal('200.00')
            }
        }
        expected_result = '{"event": "Meeting", "details": {"time": "2023-04-01T12:00:00", "cost": "200.00"}}'
        self.assertEqual(task_func(my_obj), expected_result)

# This code can be executed as a test suite
if __name__ == '__main__':
    unittest.main()