import os
import re
import hashlib
import unittest

def task_func(path, delimiter):
    """
    Splits a file path by a specified delimiter, retaining the delimiter in the output, and computes the hash of each component if it is a file.
    
    Parameters:
    path (str): The file path to split.
    delimiter (str): The delimiter to use for splitting the path.

    Returns:
    list[tuple]: A list of tuples, where each tuple contains a path component and its hash (if it's a file).
                 If the component is not a file, its hash will be None.

    Requirements:
    - os
    - re
    - hashlib

    Example:
    >>> task_func("Docs/src/file.txt", "/")
    [('Docs', None), ('/', None), ('src', None), ('/', None), ('file.txt', 'hash_value')]
    """

    path_components = re.split(f'({delimiter})', path)
    hashes = []

    for component in path_components:
        if not component:  # Remove empty components
            continue
        if component != delimiter and os.path.isfile(component):
            with open(component, 'rb') as f:
                hashes.append(hashlib.sha256(f.read()).hexdigest())
        else:
            hashes.append(None)

    return list(zip(path_components, hashes))

class TestTaskFunc(unittest.TestCase):
    
    def test_basic_functionality(self):
        # Assume we have a file at "./test.txt" with known content
        with open("./test.txt", "w") as f:
            f.write("Hello World")
        expected_hash = hashlib.sha256(b"Hello World").hexdigest()
        result = task_func("./test.txt", "/")
        expected_result = [("./test.txt", expected_hash)]
        self.assertEqual(result, expected_result)

    def test_path_with_multiple_delimiters(self):
        # Testing path with multiple delimiters
        result = task_func("Docs/src/file.txt", "/")
        expected_hash = hashlib.sha256(b"File Content").hexdigest()
        self.assertEqual(result, [('Docs', None), ('/', None), ('src', None), ('/', None), ('file.txt', expected_hash)])

    def test_non_existent_file(self):
        # Test with a non-existent file
        result = task_func("nonexistent/file.txt", "/")
        expected_result = [('nonexistent', None), ('/', None), ('file.txt', None)]
        self.assertEqual(result, expected_result)

    def test_empty_path(self):
        # Test with an empty path
        result = task_func("", "/")
        expected_result = []
        self.assertEqual(result, expected_result)

    def test_file_path_without_delimiter(self):
        # Test with a file path without the specified delimiter
        with open("./file.txt", "w") as f:
            f.write("Hello")
        expected_hash = hashlib.sha256(b"Hello").hexdigest()
        result = task_func("./file.txt", "/")
        expected_result = [("./file.txt", expected_hash)]
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()