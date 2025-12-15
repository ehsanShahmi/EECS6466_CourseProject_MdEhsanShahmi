import json
import tempfile
import unittest
from glob import glob
from pathlib import Path

def task_func(directory, string):
    """
    Search for a specific string within the JSON data of files in a given directory and its subdirectories.

    This function recursively scans the specified directory for JSON files, then checks each file to see if 
    the given string is present within the JSON data structure.

    Parameters:
    directory (str): The directory path where the search should be performed.
    string (str): The string to search for within the JSON data of the files.

    Returns:
    list: A list of file paths (str) containing the string within their JSON data.

    Requirements:
    - json
    - pathlib
    - glob

    Note:
    - The string search is case-sensitive and looks for a match within the structure of the JSON data, not 
    just as a substring in the file content.
    - If the directory does not contain any JSON files or if no JSON files contain the string, an empty list 
    is returned.
    """
    json_files = glob(f"{directory}/**/*.json", recursive=True)
    found_files = []

    for file in json_files:
        try:
            with open(file, 'r') as f:
                data = json.load(f)
                if string in data:
                    found_files.append(str(file))
        except (IOError, json.JSONDecodeError):
            continue

    return found_files

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        """Create a temporary directory and JSON files for testing."""
        self.test_dir = tempfile.mkdtemp()
        with open(f"{self.test_dir}/test1.json", "w") as f:
            json.dump({"name": "Alice", "age": 30, "category": "user"}, f)
        with open(f"{self.test_dir}/test2.json", "w") as f:
            json.dump({"title": "Book", "author": "Author Name"}, f)
        with open(f"{self.test_dir}/nested/test3.json", "w") as f:
            json.dump({"name": "Bob", "preferences": {"likes": "Pizza"}}, f)

    def tearDown(self):
        """Clean up the temporary directory after tests."""
        for path in Path(self.test_dir).rglob("*"):
            path.unlink()
        Path(self.test_dir).rmdir()

    def test_string_found_in_multiple_files(self):
        """Test case where the searched string is found in multiple files."""
        result = task_func(self.test_dir, "name")
        self.assertIn(f"{self.test_dir}/test1.json", result)
        self.assertIn(f"{self.test_dir}/nested/test3.json", result)

    def test_string_found_in_one_file(self):
        """Test case where the searched string is found in one file only."""
        result = task_func(self.test_dir, "author")
        self.assertEqual(result, [f"{self.test_dir}/test2.json"])

    def test_string_not_found(self):
        """Test case where the searched string is not found in any files."""
        result = task_func(self.test_dir, "nonexistent")
        self.assertEqual(result, [])

    def test_case_sensitivity(self):
        """Test case to verify that the search is case-sensitive."""
        result = task_func(self.test_dir, "NAME")
        self.assertEqual(result, [])

    def test_empty_directory(self):
        """Test case for an empty directory."""
        empty_dir = tempfile.mkdtemp()
        result = task_func(empty_dir, "anything")
        self.assertEqual(result, [])
        Path(empty_dir).rmdir()

if __name__ == '__main__':
    unittest.main()