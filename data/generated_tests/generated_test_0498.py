import unittest
import os
import json
import xmltodict

# Here is your prompt:
def task_func(s, save_json, json_file_path):
    """ 
    Converts an XML string into a dictionary representation and optionally saves it as a JSON file.

    This function is useful for easily accessing data stored in XML format and saving it for future use.

    Parameters:
    s (str): The XML string to be converted.
    save_json (bool): Whether to save the parsed XML as a JSON file.
    json_file_path (str): The file path to save the JSON file. Required if save_json is True.

    Returns:
    dict: A dictionary representation of the XML string.

    Raises:
    ValueError: If the input XML string is empty or contains only whitespace.

    Requirements:
    - xmltodict
    - json

    Examples:
    Convert a simple XML string to a dictionary.
    >>> result = task_func('<person><name>John</name><age>30</age></person>')
    >>> result['person']['name'] + ', ' + result['person']['age']
    'John, 30'

    Convert an XML string with nested elements.
    >>> result = task_func('<school><class><student>Emma</student></class></school>')
    >>> result['school']['class']['student']
    'Emma'

    Save the parsed XML as a JSON file.
    >>> task_func('<data><item>1</item><item>2</item></data>', save_json=True, json_file_path='data.json')
    # A JSON file 'data.json' will be created with the parsed XML data.
    """

    if not s.strip():  # Check for empty or whitespace-only string
        raise ValueError("The input XML string is empty or contains only whitespace.")
    
    my_dict = xmltodict.parse(s)

    if save_json and json_file_path:
        with open(json_file_path, 'w') as json_file:
            json.dump(my_dict, json_file, indent=4)

    return my_dict

class TestTaskFunc(unittest.TestCase):

    def test_valid_simple_xml(self):
        result = task_func('<person><name>John</name><age>30</age></person>', save_json=False, json_file_path=None)
        self.assertEqual(result['person']['name'], 'John')
        self.assertEqual(result['person']['age'], '30')

    def test_valid_nested_xml(self):
        result = task_func('<school><class><student>Emma</student></class></school>', save_json=False, json_file_path=None)
        self.assertEqual(result['school']['class']['student'], 'Emma')

    def test_empty_xml(self):
        with self.assertRaises(ValueError):
            task_func('  ', save_json=False, json_file_path=None)

    def test_save_json_file(self):
        json_file_path = 'test_data.json'
        task_func('<data><item>1</item><item>2</item></data>', save_json=True, json_file_path=json_file_path)
        
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
            self.assertEqual(data['data']['item'], ['1', '2'])

        os.remove(json_file_path)  # Clean up

    def test_no_save_json_path(self):
        with self.assertRaises(TypeError):
            task_func('<data><item>1</item></data>', save_json=True, json_file_path=None)

if __name__ == '__main__':
    unittest.main()