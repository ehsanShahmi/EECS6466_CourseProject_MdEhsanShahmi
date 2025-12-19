import json
import re
from collections import Counter
import unittest

# Constants
REPLACE_NONE = "None"

def task_func(json_str):
    """
    Process a JSON string by:
    1. Removing None values.
    2. Counting the frequency of each unique value.
    3. Replacing all email addresses with the placeholder "None".
    
    Parameters:
    json_str (str): The JSON string to be processed.
    
    Returns:
    dict: A dictionary containing:
        - "data": Processed JSON data.
        - "value_counts": A Counter object with the frequency of each unique value.
    """
    data = json.loads(json_str)
    
    # Remove None values and replace emails
    processed_data = {}
    for key, value in data.items():
        if value is None:
            continue
        if isinstance(value, str) and re.match(r"[^@]+@[^@]+\.[^@]+", value):
            value = REPLACE_NONE
        processed_data[key] = value

    # Count frequency of each unique value
    value_counts = Counter(processed_data.values())

    return {"data": processed_data, "value_counts": value_counts}

class TestTaskFunc(unittest.TestCase):
    
    def test_remove_none_values(self):
        json_str = '{"name": "John", "age": null, "email": "john@example.com"}'
        expected_result = {'data': {'name': 'John', 'email': 'None'}, 'value_counts': Counter({'John': 1, 'None': 1})}
        self.assertEqual(task_func(json_str), expected_result)

    def test_replace_email_address(self):
        json_str = '{"user": "Alice", "contact": "alice@example.com", "status": null}'
        expected_result = {'data': {'user': 'Alice', 'contact': 'None'}, 'value_counts': Counter({'Alice': 1, 'None': 1})}
        self.assertEqual(task_func(json_str), expected_result)

    def test_multiple_emails_and_none(self):
        json_str = '{"owner": null, "emails": ["user1@example.com", "user2@example.com"], "name": "Bob"}'
        expected_result = {'data': {'name': 'Bob', 'emails': ['None', 'None']}, 'value_counts': Counter({'Bob': 1, 'None': 2})}
        self.assertEqual(task_func(json_str), expected_result)

    def test_no_valid_data(self):
        json_str = '{"a": null, "b": null, "c": null}'
        expected_result = {'data': {}, 'value_counts': Counter()}
        self.assertEqual(task_func(json_str), expected_result)

    def test_with_numbers_and_none(self):
        json_str = '{"integer": 42, "float": null, "string": "Hello"}'
        expected_result = {'data': {'integer': 42, 'string': 'Hello'}, 'value_counts': Counter({42: 1, 'Hello': 1})}
        self.assertEqual(task_func(json_str), expected_result)

if __name__ == '__main__':
    unittest.main()