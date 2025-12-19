import base64
import re
from html import unescape
import textwrap
import unittest

def task_func(raw_string, line_length):
    """
    Decode a raw string from base64, decouple HTML entities, replace multiple spaces with a single space, strip leading and subsequent spaces, and wrap text to a certain line length.

    Parameters:
    - raw_string (str): The base64 encoded string.
    - line_length (int): The maximum length of a line.

    Returns:
    - wrapped_text (str): The cleaned and formatted string.

    Requirements:
    - base64
    - re
    - html
    - textwrap

    Example:
    >>> task_func('SGVsbG8sICBXb3JsZCEgICAg', 5)
    'Hello\\n, Wor\\nld!'
    """

    # Decode the string from base64
    decoded_string = base64.b64decode(raw_string).decode('utf-8')

    # Unescape HTML entities
    unescaped_string = unescape(decoded_string)

    # Replace multiple spaces with a single space and strip leading and trailing spaces
    cleaned_string = re.sub(' +', ' ', unescaped_string).strip()

    # Wrap the text
    wrapped_text = textwrap.fill(cleaned_string, line_length)

    return wrapped_text

class TestTaskFunc(unittest.TestCase):
    
    def test_basic_decoding_and_wrapping(self):
        result = task_func('SGVsbG8sICBXb3JsZCEgICAg', 5)
        expected = 'Hello\n, Wor\nld!'
        self.assertEqual(result, expected)

    def test_html_entity_decoding(self):
        result = task_func('SGllbmFuZCBJbGx1bWluYXRvciBpbmRvbmUncyB0aGUgY29taW5nIHZhbHVlLCBub29jaG1vcml0c2Vk', 10)
        expected = "I guess\nI'll\nbe coming\nvalue,\nnoochmori"
        self.assertEqual(result, expected)

    def test_multiple_spaces_handling(self):
        result = task_func('SGVsbG8gIAAgICAgVGhpcyBpcyBhIHRlc3Q= ', 15)
        expected = 'Hello  This is a\ntest'
        self.assertEqual(result, expected)

    def test_stripping_spaces(self):
        result = task_func('   SG VsbG8sIFRvbyAgICB0aGVyZSwgYXJlIHlvdSB3aWxsIGZpbmQgbWUu   ', 20)
        expected = 'Hello, Toro\nthere, are you\nwill find me.'
        self.assertEqual(result, expected)

    def test_empty_string(self):
        result = task_func('', 10)
        expected = ''
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()