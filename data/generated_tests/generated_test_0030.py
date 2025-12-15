import json
import os
import re
import unittest

def task_func(
    file_path,
    attribute,
    INPUT_JSON={
        "type": "object",
        "properties": {
            "name": {"type": str},  
            "age": {"type": int},   
            "email": {"type": str}  
        },
        "required": ["name", "age", "email"]
    },
    EMAIL_REGEX=r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"):
    """
    Validate the structure and contents of a JSON file against predefined schema rules and retrieve a specified attribute from the JSON object. Ensures that all required fields exist, match their defined types, and checks the validity of the email format using a regular expression.
    
    Parameters:
    file_path (str): The path to the JSON file.
    attribute (str): The attribute to retrieve from the JSON object.
    INPUT_JSON (dict): The input json to validate. The default value is:
    '{
        "type": "object",
        "properties": {
            "name": {"type": str},  
            "age": {"type": int},   
            "email": {"type": str}  
        },
        "required": ["name", "age", "email"]
    }'.
    EMAIL_REGEX (str): The regex used to check the email validity. Default to 'r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")'

    Returns:
    Any: The value of the specified attribute, consistent with the type defined in the JSON schema.

    Requirements:
    - json
    - os
    - re

    Errors:
    - Raises ValueError if the file does not exist, required attributes are missing, types do not match, or the email format is invalid.

    Example:
    >>> task_func('/path/to/file.json', 'email')
    'john.doe@example.com'
    """

    if not os.path.isfile(file_path):
        raise ValueError(f'{file_path} does not exist.')

    with open(file_path, 'r') as f:
        data = json.load(f)

    for key in INPUT_JSON['required']:
        if key not in data:
            raise ValueError(f'{key} is missing from the JSON object.')
        if not isinstance(data[key], INPUT_JSON['properties'][key]['type']):
            raise ValueError(f'{key} is not of type {INPUT_JSON["properties"][key]["type"]}.')

    if 'email' in data and not re.fullmatch(EMAIL_REGEX, data['email']):
        raise ValueError('Email is not valid.')

    return data[attribute]

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        # Create example JSON files for testing
        self.valid_json_path = 'valid.json'
        self.invalid_json_path = 'invalid.json'
        self.missing_field_path = 'missing_field.json'
        self.invalid_type_path = 'invalid_type.json'
        self.invalid_email_path = 'invalid_email.json'

        valid_data = {
            "name": "John Doe",
            "age": 30,
            "email": "john.doe@example.com"
        }

        invalid_data = {
            "name": "John Doe",
            "age": "thirty",  # Invalid type
            "email": "john.doe@example.com"
        }

        missing_field_data = {
            "name": "John Doe",
            # Age is missing
            "email": "john.doe@example.com"
        }

        invalid_email_data = {
            "name": "John Doe",
            "age": 30,
            "email": "john.doe@example"  # Invalid email format
        }

        # Write JSON files
        with open(self.valid_json_path, 'w') as f:
            json.dump(valid_data, f)
        with open(self.invalid_json_path, 'w') as f:
            json.dump(invalid_data, f)
        with open(self.missing_field_path, 'w') as f:
            json.dump(missing_field_data, f)
        with open(self.invalid_email_path, 'w') as f:
            json.dump(invalid_email_data, f)

    def tearDown(self):
        # Clean up the files created during tests
        for file_path in [self.valid_json_path, self.invalid_json_path, self.missing_field_path, self.invalid_email_path]:
            try:
                os.remove(file_path)
            except Exception:
                pass

    def test_valid_data(self):
        result = task_func(self.valid_json_path, 'email')
        self.assertEqual(result, "john.doe@example.com")

    def test_invalid_type(self):
        with self.assertRaises(ValueError) as context:
            task_func(self.invalid_json_path, 'email')
        self.assertTrue('age is not of type <class \'int\'>.' in str(context.exception))

    def test_missing_field(self):
        with self.assertRaises(ValueError) as context:
            task_func(self.missing_field_path, 'email')
        self.assertTrue('age is missing from the JSON object.' in str(context.exception))

    def test_invalid_email_format(self):
        with self.assertRaises(ValueError) as context:
            task_func(self.invalid_email_path, 'email')
        self.assertTrue('Email is not valid.' in str(context.exception))

    def test_file_not_exist(self):
        with self.assertRaises(ValueError) as context:
            task_func('non_existent_file.json', 'email')
        self.assertEqual(str(context.exception), 'non_existent_file.json does not exist.')

if __name__ == '__main__':
    unittest.main()