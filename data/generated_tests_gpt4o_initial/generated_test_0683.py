import unittest
import math
import yaml
import os

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Create a temporary YAML file for testing
        self.test_file = 'test_data.yaml'
        with open(self.test_file, 'w') as file:
            yaml.dump({'ele': 0, 'other_key': 1}, file)

    def tearDown(self):
        # Remove the temporary YAML file after tests
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_cosine_of_zero(self):
        result = task_func(self.test_file, 'ele')
        self.assertEqual(result['ele'], math.cos(0))

    def test_cosine_of_positive_value(self):
        with open(self.test_file, 'w') as file:
            yaml.dump({'ele': 0.5, 'other_key': 1}, file)
        
        result = task_func(self.test_file, 'ele')
        self.assertEqual(result['ele'], math.cos(0.5))

    def test_cosine_of_negative_value(self):
        with open(self.test_file, 'w') as file:
            yaml.dump({'ele': -1, 'other_key': 1}, file)
        
        result = task_func(self.test_file, 'ele')
        self.assertEqual(result['ele'], math.cos(-1))

    def test_key_not_in_data(self):
        with open(self.test_file, 'w') as file:
            yaml.dump({'other_key': 1}, file)
        
        result = task_func(self.test_file, 'ele')
        # Since 'ele' does not exist, it should be unchanged
        self.assertEqual(result['other_key'], 1)
        self.assertNotIn('ele', result)

    def test_empty_yaml(self):
        with open(self.test_file, 'w') as file:
            yaml.dump({}, file)
        
        result = task_func(self.test_file, 'ele')
        # The result should still be an empty dict
        self.assertEqual(result, {})


if __name__ == '__main__':
    unittest.main()