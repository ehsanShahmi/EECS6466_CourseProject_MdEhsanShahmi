import os
import sys
import importlib
from pkgutil import iter_modules
import unittest

def task_func(package_name):
    """
    Adds all modules of a specified package to the system path. This function is useful for dynamically
    importing modules from a package that might not be on the standard path.

    Parameters:
    package_name (str): The name of the package whose modules are to be added to the system path.

    Returns:
    list: A list of module names that were added to the system path.

    Raises:
    ImportError: If the package is not installed or cannot be found. The exception message should contain
                 the instruction to install the package (i.e., f"pip install {package_name}").

    Requirements:
    - os
    - sys
    - importlib
    - pkgutil.iter_modules

    Examples:
    Assuming 'pandas' is a valid package with modules 'module1' and 'module2',

    >>> len(task_func('pandas')) >= 2
    True

    Verify that 'numpy' (a common package) modules are added to the path,
    >>> 'random' in task_func('numpy')
    True
    """
    added_modules = []
    try:
        package = importlib.import_module(package_name)
    except ImportError:
        raise ImportError(f"The package '{package_name}' is not installed! Please install the package first using 'pip install {package_name}'")

    for _, module_name, _ in iter_modules(package.__path__):
        module_path = os.path.join(package.__path__[0], module_name)
        if module_path not in sys.path:
            sys.path.append(module_path)
            added_modules.append(module_name)

    return added_modules

class TestTaskFunc(unittest.TestCase):

    def test_valid_package(self):
        """Test with a valid package (e.g., numpy)"""
        result = task_func('numpy')
        self.assertIn('random', result)
        self.assertIn('linalg', result)

    def test_valid_package_multiple_modules(self):
        """Test that a valid package with multiple modules returns those modules"""
        result = task_func('numpy')
        self.assertGreaterEqual(len(result), 2)

    def test_invalid_package(self):
        """Test with an invalid package name"""
        with self.assertRaises(ImportError) as context:
            task_func('nonexistent_package')
        self.assertEqual(str(context.exception), "The package 'nonexistent_package' is not installed! Please install the package first using 'pip install nonexistent_package'")

    def test_package_already_in_sys_path(self):
        """Test if modules from a package that is already in sys.path are not added again"""
        original_sys_path_length = len(sys.path)
        task_func('numpy')
        self.assertEqual(original_sys_path_length, len(sys.path))

    def test_empty_package_name(self):
        """Test with an empty package name"""
        with self.assertRaises(ImportError) as context:
            task_func('')
        self.assertTrue("No module named ''" in str(context.exception))

if __name__ == '__main__':
    unittest.main()