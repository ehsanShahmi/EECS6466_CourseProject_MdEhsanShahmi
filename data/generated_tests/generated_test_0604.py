import subprocess
import logging
import os
import unittest

def task_func(filepath):
    """
    Attempts to compile a existing C++ file specified by 'filepath'. The output of the compilation process
    is logged, indicating whether the compilation was successful or not. This function is useful
    for automating the compilation of C++ code and tracking compilation results.
    The log should indicate whether the compilation was successful or if an error occurred.

    Parameters:
    filepath (str): The path of the C++ file to be compiled.

    Returns:
    None: This function does not return anything but logs the outcome of the compilation process.

    Raises:
    - subprocess.CalledProcessError: If the compilation process fails.
    - FileNotFoundError: If the compiler is not found or the specified file does not exist.

    Requirements:
    - subprocess
    - logging

    Examples:
    >>> import os
    >>> with open('example.cpp', 'w') as f: \
            _ = f.write("int main(){return 0;}")
    >>> task_func('example.cpp')
    >>> os.path.exists('example')
    True
    """

    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Try to compile the C++ file
    try:
        subprocess.check_call(['g++', filepath, '-o', filepath.split('.')[0]])
        logging.info('Successfully compiled %s', filepath)
    except subprocess.CalledProcessError as e:
        logging.error('Failed to compile %s: %s', filepath, e)

    except FileNotFoundError as e:
        logging.error('Compiler not found or file does not exist: %s', e)

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.valid_cpp_file = 'test_valid.cpp'
        self.invalid_cpp_file = 'test_invalid.cpp'
        self.nonexistent_file = 'nonexistent.cpp'
        self.valid_cpp_code = "int main() { return 0; }"

        # Create a valid C++ file
        with open(self.valid_cpp_file, 'w') as f:
            f.write(self.valid_cpp_code)

        # Create an invalid C++ file
        with open(self.invalid_cpp_file, 'w') as f:
            f.write("int main{ return 0; }")  # Syntax error: missing parentheses

    def tearDown(self):
        # Remove the created files if they exist
        for file in [self.valid_cpp_file, self.invalid_cpp_file, 'test_valid']:
            if os.path.exists(file):
                os.remove(file)

    def test_successful_compilation(self):
        """Test compilation of a valid C++ file."""
        task_func(self.valid_cpp_file)
        self.assertTrue(os.path.exists('test_valid'))

    def test_failed_compilation(self):
        """Test compilation of an invalid C++ file."""
        with self.assertLogs('root', level='ERROR') as log:
            task_func(self.invalid_cpp_file)
            self.assertIn('Failed to compile', log.output[0])

    def test_nonexistent_file(self):
        """Test handling of a nonexistent file."""
        with self.assertLogs('root', level='ERROR') as log:
            task_func(self.nonexistent_file)
            self.assertIn('Compiler not found or file does not exist:', log.output[0])

    def test_compilation_output_file_creation(self):
        """Test that the output file is created after successful compilation."""
        task_func(self.valid_cpp_file)
        self.assertTrue(os.path.exists('test_valid'))

    def test_multiple_compilations(self):
        """Test multiple compilations to ensure no unexpected issues."""
        task_func(self.valid_cpp_file)
        self.assertTrue(os.path.exists('test_valid'))
        task_func(self.invalid_cpp_file)
        with self.assertLogs('root', level='ERROR') as log:
            task_func(self.invalid_cpp_file)
            self.assertIn('Failed to compile', log.output[0])

if __name__ == '__main__':
    unittest.main()