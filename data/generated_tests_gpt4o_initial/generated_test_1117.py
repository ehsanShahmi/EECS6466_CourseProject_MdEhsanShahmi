import collections
import random
import json
import unittest

# Constants
PREFICES = ['EMP$$', 'MAN$$', 'DEV$$', 'HR$$']
LEVELS = ['Junior', 'Mid', 'Senior']

def task_func(department_data):
    """
    Generate a JSON object from employee data based on given department codes and their employee counts.

    Note:
    - The keys are department codes (from the list: ['EMP$$', 'MAN$$', 'DEV$$', 'HR$$']) and the values are lists of 
    employee levels ('Junior', 'Mid', 'Senior') in that department.

    Parameters:
    department_data (dict): A dictionary with department codes as keys and number of employees as values.

    Returns:
    str: A JSON object representing employee levels for each department.

    Requirements:
    - collections
    - random
    - json

    Example:
    >>> random.seed(0)
    >>> department_info = {'EMP$$': 10, 'MAN$$': 5, 'DEV$$': 8, 'HR$$': 7}
    >>> level_data_json = task_func(department_info)
    >>> print(level_data_json)
    {"EMP$$": ["Mid", "Mid", "Junior", "Mid", "Senior", "Mid", "Mid", "Mid", "Mid", "Mid"], "MAN$$": ["Senior", "Junior", "Senior", "Junior", "Mid"], "DEV$$": ["Junior", "Junior", "Senior", "Mid", "Senior", "Senior", "Senior", "Junior"], "HR$$": ["Mid", "Junior", "Senior", "Junior", "Senior", "Mid", "Mid"]}
    """

    level_data = collections.defaultdict(list)
    
    for prefix, num_employees in department_data.items():
        if prefix not in PREFICES:
            continue

        for _ in range(num_employees):
            level = random.choice(LEVELS)
            level_data[prefix].append(level)

    return json.dumps(level_data)

# Test Suite
class TestTaskFunc(unittest.TestCase):
    
    def test_empty_department_data(self):
        """Test with an empty department data dict"""
        department_info = {}
        result = task_func(department_info)
        expected = json.dumps({})
        self.assertEqual(result, expected)

    def test_single_department(self):
        """Test with one department having employees"""
        department_info = {'EMP$$': 3}
        result = task_func(department_info)
        data = json.loads(result)
        self.assertIn('EMP$$', data)
        self.assertEqual(len(data['EMP$$']), 3)

    def test_multiple_departments(self):
        """Test with multiple departments"""
        department_info = {'EMP$$': 2, 'HR$$': 4}
        result = task_func(department_info)
        data = json.loads(result)
        self.assertIn('EMP$$', data)
        self.assertEqual(len(data['EMP$$']), 2)
        self.assertIn('HR$$', data)
        self.assertEqual(len(data['HR$$']), 4)

    def test_invalid_department_code(self):
        """Test with an invalid department code"""
        department_info = {'INVALID': 5}
        result = task_func(department_info)
        expected = json.dumps({})
        self.assertEqual(result, expected)

    def test_randomness_and_level_values(self):
        """Test the randomness and value consistency in valid departments"""
        random.seed(0)  # to ensure reproducibility in this test
        department_info = {'EMP$$': 5, 'MAN$$': 3}
        result = task_func(department_info)
        data = json.loads(result)
        self.assertIn('EMP$$', data)
        self.assertTrue(all(level in LEVELS for level in data['EMP$$']))
        self.assertIn('MAN$$', data)
        self.assertTrue(all(level in LEVELS for level in data['MAN$$']))

if __name__ == '__main__':
    unittest.main()