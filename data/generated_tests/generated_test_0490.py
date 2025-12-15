import unittest
import os
import json
import xmltodict

# Here is your prompt:
def task_func(s, file_path):
    """
    Converts an XML string into a dictionary representation and saves it as a JSON file.
    This is useful for easily accessing and persisting data stored in XML format.

    Parameters:
    s (str): The XML string to be converted.
    file_path (str): The path where the JSON file will be saved.

    Returns:
    dict: A dictionary representation of the XML string.

    Requirements:
    - xmltodict
    - json

    Examples:
    >>> result = task_func('<person><name>John</name><age>30</age></person>', "temp.json")
    >>> result['person']['name'] + ', ' + result['person']['age']
    'John, 30'
    >>> result = task_func('<school><class><student>Emma</student></class></school>', "temp.json")
    >>> result['school']['class']['student']
    'Emma'
    """

    my_dict = xmltodict.parse(s)
    # Save the dictionary to a JSON file
    with open(file_path, 'w') as json_file:
        json.dump(my_dict, json_file, indent=4)

    return my_dict

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        self.test_file = "test_output.json"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_conversion_person(self):
        xml_input = '<person><name>John</name><age>30</age></person>'
        expected_output = {'person': {'name': 'John', 'age': '30'}}
        result = task_func(xml_input, self.test_file)
        self.assertEqual(result, expected_output)

    def test_conversion_school(self):
        xml_input = '<school><class><student>Emma</student></class></school>'
        expected_output = {'school': {'class': {'student': 'Emma'}}}
        result = task_func(xml_input, self.test_file)
        self.assertEqual(result, expected_output)

    def test_json_file_creation(self):
        xml_input = '<data><item>Test</item></data>'
        task_func(xml_input, self.test_file)
        self.assertTrue(os.path.exists(self.test_file))

    def test_json_file_contents(self):
        xml_input = '<data><item>Test</item></data>'
        task_func(xml_input, self.test_file)
        with open(self.test_file, 'r') as json_file:
            data = json.load(json_file)
            self.assertEqual(data, {'data': {'item': 'Test'}})

    def test_invalid_xml(self):
        invalid_xml_input = '<data><item>Test</data>'
        with self.assertRaises(xmltodict.expat.ExpatError):
            task_func(invalid_xml_input, self.test_file)

if __name__ == '__main__':
    unittest.main()