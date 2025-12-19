import textwrap
import re
import unittest

def task_func(input_string, width):
    """
    Divide a multi-line string into separate strings and wrap each line to a certain width.
    
    Parameters:
    - input_string (str): The multi-line string that needs to be wrapped.
    - width (int): The width to wrap each line to.
    
    Returns:
    - str: The wrapped string where each line is wrapped to the specified width.
    
    Requirements:
    - textwrap
    - re
    
    Example:
    >>> task_func('Another line\\nWith wrapping', 8)
    'Another\\nline\\nWith\\nwrapping'
    """

    lines = input_string.split('\\n')
    wrapped_lines = [textwrap.fill(line, width, break_long_words=False) for line in lines]
    wrapped_string = '\\n'.join(wrapped_lines)
    wrapped_string = re.sub(r'\bis\b', 'was', wrapped_string)
    
    return wrapped_string

class TestTaskFunc(unittest.TestCase):

    def test_wrap_simple_case(self):
        input_str = 'Another line\\nWith wrapping'
        width = 8
        expected_output = 'Another\\nline\\nWith\\nwrapping'
        self.assertEqual(task_func(input_str, width), expected_output)

    def test_wrap_long_words(self):
        input_str = 'This is a singlelongword\\nAnd anotherlongword'
        width = 10
        expected_output = 'This is a\\nsinglelongword\\nAnd\\nanotherlongword'
        self.assertEqual(task_func(input_str, width), expected_output)

    def test_wrap_with_word_replacement(self):
        input_str = 'This is a test'
        width = 5
        expected_output = 'This\\nwas\\na\\ntest'
        self.assertEqual(task_func(input_str, width), expected_output)
    
    def test_wrap_multiline_with_special_chars(self):
        input_str = 'Line 1!\\nLine 2@\\nLine 3#'
        width = 6
        expected_output = 'Line 1!\\nLine\\n2@\\nLine\\n3#'
        self.assertEqual(task_func(input_str, width), expected_output)
        
    def test_wrap_empty_string(self):
        input_str = ''
        width = 5
        expected_output = ''
        self.assertEqual(task_func(input_str, width), expected_output)

if __name__ == '__main__':
    unittest.main()