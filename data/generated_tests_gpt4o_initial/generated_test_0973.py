import os
import shutil
import unittest

# Here is your prompt:
def task_func(path, delimiter="/"):
    """
    Splits a given file path by a specific delimiter and computes disk usage for each directory component.

    Parameters:
    - path (str): The file path to split.
    - delimiter (str, optional): The delimiter to use for splitting the path. Default is '/'.

    Returns:
    list: A list of tuples where each tuple contains a path component and its disk usage as a dictionary.
          The disk usage dictionary contains keys 'total', 'used', and 'free'.

    Raises:
    - ValueError: If the 'path' is empty, not a string, or contain invalid components.
    - FileNotFoundError: If the 'path' does not exist in the filesystem.

    Requirements:
    - os
    - shutil

    Examples:
    >>> task_func('Docs/src', '/')
    [('Docs', {'total': 100, 'used': 50, 'free': 50}), ('src', {'total': 200, 'used': 100, 'free': 100})]

    >>> task_func('a/b', '/')
    [('a', {'total': 300, 'used': 150, 'free': 150}), ('b', {'total': 400, 'used': 200, 'free': 200})]
    """

    if not path or not isinstance(path, str):
        raise ValueError("Path must be a non-empty string")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Path '{path}' does not exist")

    path_components = path.strip(delimiter).split(delimiter)
    if not all(path_components):
        raise ValueError("Path contains invalid components")

    results = []
    for index, component in enumerate(path_components):
        sub_path = delimiter.join(path_components[: index + 1])
        if not sub_path.startswith(delimiter):
            sub_path = delimiter + sub_path
        usage = shutil.disk_usage(sub_path)
        results.append(
            (component, {"total": usage.total, "used": usage.used, "free": usage.free})
        )

    return results


class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Create temporary directories for testing
        os.makedirs('test_dir/Docs/src', exist_ok=True)
        os.makedirs('test_dir/a/b', exist_ok=True)

    def tearDown(self):
        # Remove the temporary directories after tests
        shutil.rmtree('test_dir')

    def test_basic_functionality(self):
        expected = [('Docs', {'total': 100, 'used': 50, 'free': 50}), ('src', {'total': 200, 'used': 100, 'free': 100})]
        # Mocking the return value of shutil.disk_usage
        shutil.disk_usage = lambda x: type('obj', (object,), {'total': 100, 'used': 50, 'free': 50}) if x == 'test_dir/Docs' else type('obj', (object,), {'total': 200, 'used': 100, 'free': 100})
        result = task_func('test_dir/Docs/src', '/')
        self.assertEqual(result, expected)

    def test_empty_path(self):
        with self.assertRaises(ValueError):
            task_func("")

    def test_invalid_type_path(self):
        with self.assertRaises(ValueError):
            task_func(123)

    def test_non_existent_path(self):
        with self.assertRaises(FileNotFoundError):
            task_func('non_existent/path')

    def test_path_with_invalid_components(self):
        os.makedirs('test_dir/invalid//path', exist_ok=True)
        with self.assertRaises(ValueError):
            task_func('invalid//path', '/')

if __name__ == '__main__':
    unittest.main()