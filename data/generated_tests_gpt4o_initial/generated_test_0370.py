import os
import unittest
import json
import tempfile
import shutil

# Here is your prompt:
import os
import re
import json
import glob

def task_func(directory_path: str) -> list:
    """
    Protect all double quotes in all JSON files in the specified directory by prepending them with a double backslash.
    
    Functionality:
    - Reads each JSON file in the given directory.
    - Escapes the double quotes by prepending them with a double backslash.
    - Writes back the modified content to the respective JSON file.
    
    Parameters:
    - directory_path (str): Path to the directory containing JSON files.
    
    Returns:
    - list: A list of the processed JSON files.
    
    Requirements:
    - re
    - json
    - glob
    - os

    Raises:
    - FileNotFoundError: If the specified directory does not exist.
    
    Example:
    >>> import tempfile
    >>> import json
    >>> directory = tempfile.mkdtemp()
    >>> with open(directory + "/file1.json", "w") as file:
    ...     json.dump({"name": "John", "age": 30, "city": "New York"}, file)
    >>> with open(directory + "/file2.json", "w") as file:
    ...     json.dump('{"book": "Harry Potter", "author": "J.K. Rowling", "quote": "\\"Magic\\" is everywhere!"}', file)
    >>> files = task_func(directory)
    >>> len(files)
    2
    """
    
    # Check if directory exists
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Directory {directory_path} not found.")
    
    json_files = glob.glob(directory_path + '/*.json')
    processed_files = []
    
    for json_file in json_files:
        with open(json_file, 'r') as file:
            data = json.load(file)
        
        escaped_data = json.dumps(data, ensure_ascii=False)
        escaped_data = re.sub(r'(?<!\\)"', r'\\\"', escaped_data)
        
        with open(json_file, 'w') as file:
            file.write(escaped_data)
        
        processed_files.append(json_file)
    
    return processed_files

class TestTaskFunction(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_process_single_json_file(self):
        with open(os.path.join(self.test_dir, "file1.json"), "w") as file:
            json.dump({"name": "John", "age": 30, "quote": 'He said, "Hello!"'}, file)
        
        processed_files = task_func(self.test_dir)
        
        self.assertEqual(len(processed_files), 1)
        with open(os.path.join(self.test_dir, "file1.json"), "r") as file:
            content = file.read()
            self.assertIn(r'\"', content)
            self.assertNotIn('"', content)

    def test_process_multiple_json_files(self):
        with open(os.path.join(self.test_dir, "file1.json"), "w") as file:
            json.dump({"name": "Alice", "greeting": 'Hi "there"'}, file)
        
        with open(os.path.join(self.test_dir, "file2.json"), "w") as file:
            json.dump({"item": "Book", "description": 'This is a "great" book.'}, file)
        
        processed_files = task_func(self.test_dir)
        
        self.assertEqual(len(processed_files), 2)
        for filename in processed_files:
            with open(filename, "r") as file:
                content = file.read()
                self.assertIn(r'\"', content)
                self.assertNotIn('"', content)

    def test_empty_directory(self):
        processed_files = task_func(self.test_dir)
        self.assertEqual(processed_files, [])

    def test_directory_not_found(self):
        with self.assertRaises(FileNotFoundError):
            task_func("non_existent_directory")

    def test_json_file_with_no_quotes(self):
        with open(os.path.join(self.test_dir, "file1.json"), "w") as file:
            json.dump({"name": "John", "age": 30}, file)
        
        processed_files = task_func(self.test_dir)
        
        self.assertEqual(len(processed_files), 1)
        with open(os.path.join(self.test_dir, "file1.json"), "r") as file:
            content = file.read()
            self.assertNotIn(r'\"', content)
            self.assertNotIn('"', content)

if __name__ == '__main__':
    unittest.main()