import unittest
import os
from your_module import task_func  # Replace 'your_module' with the actual module name where task_func is defined.

class TestTaskFunc(unittest.TestCase):
    
    def test_valid_path_with_forward_slash(self):
        result = task_func('Docs/src/Scripts/temp', '/')
        self.assertEqual(result, ['Docs', 'src', 'Scripts', 'temp'])
        
    def test_valid_path_with_backslashes(self):
        result = task_func(r'Docs\\src\\Scripts\\temp', '\\')
        self.assertEqual(result, ['Docs', 'src', 'Scripts', 'temp'])
        
    def test_empty_path(self):
        result = task_func('', '/')
        self.assertEqual(result, [])
        
    def test_invalid_characters_in_path(self):
        result = task_func('Docs/src/<Scripts>/temp', '/')
        self.assertEqual(result, [])
        
    def test_path_with_leading_and_trailing_delimiters(self):
        result = task_func('/Docs/src/Scripts/temp/', '/')
        self.assertEqual(result, ['Docs', 'src', 'Scripts', 'temp'])

if __name__ == '__main__':
    unittest.main()