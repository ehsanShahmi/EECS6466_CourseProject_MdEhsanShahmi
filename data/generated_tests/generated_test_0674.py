import os
import pandas as pd
import unittest

# Here is your prompt:
import pandas as pd
import os

def task_func(filename):
    """
    Read a CSV file of pandas, reverse the order of the lines and write the inverted lines back into the file. Then move the cursor back to the beginning of the file. 
    The header should not be inverted and the file may be empty.

    Parameters:
    - filename (str): The name of the CSV file.

    Returns:
    - filename (str): The name of the CSV file.

    Requirements:
    - os
    - pandas

    Example:
    >>> task_func('file.csv')
    'file.csv'
    """

    if not os.path.exists(filename):
        return filename

    # Check if empty
    with open(filename, 'r') as file:
        if not file.read(1):
            return filename

    df = pd.read_csv(filename)
    df = df.iloc[::-1]
    df.to_csv(filename, index=False)

    with open(filename, 'r+') as file:
        file.seek(0)

    return filename


class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Create a temporary CSV file for testing."""
        self.test_file = 'test.csv'
        self.empty_file = 'empty.csv'
        self.nonexistent_file = 'nonexistent.csv'

        # Prepare a CSV file for testing with sample data
        with open(self.test_file, 'w') as f:
            f.write('Header1,Header2\n')
            f.write('Value1,Value2\n')
            f.write('Value3,Value4\n')

        # Prepare an empty CSV file for testing
        with open(self.empty_file, 'w') as f:
            pass

    def tearDown(self):
        """Remove the created files after testing."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.empty_file):
            os.remove(self.empty_file)

    def test_nonexistent_file(self):
        """Test if the function returns the filename for a nonexistent file."""
        result = task_func(self.nonexistent_file)
        self.assertEqual(result, self.nonexistent_file)

    def test_empty_file(self):
        """Test if the function returns the filename for an empty file."""
        result = task_func(self.empty_file)
        self.assertEqual(result, self.empty_file)

    def test_file_reversed_content(self):
        """Test if the content of the file is correctly reversed."""
        task_func(self.test_file)

        # Read the modified file
        with open(self.test_file, 'r') as f:
            content = f.readlines()

        # Check if the content is reversed but header remains the same
        expected_content = ['Header1,Header2\n', 'Value3,Value4\n', 'Value1,Value2\n']
        self.assertEqual(content, expected_content)

    def test_file_cursor_position(self):
        """Test if the file cursor is at the beginning after function execution."""
        task_func(self.test_file)
        with open(self.test_file, 'r+') as f:
            f.seek(0)
            first_line = f.readline()
            self.assertEqual(first_line, 'Header1,Header2\n')

    def test_file_not_changed(self):
        """Test if calling the function on an already reversed file returns the same content."""
        task_func(self.test_file)  # First inversion
        task_func(self.test_file)  # Second inversion

        with open(self.test_file, 'r') as f:
            content = f.readlines()

        # After reversing twice, we should get the original content back
        expected_content = ['Header1,Header2\n', 'Value1,Value2\n', 'Value3,Value4\n']
        self.assertEqual(content, expected_content)

if __name__ == '__main__':
    unittest.main()