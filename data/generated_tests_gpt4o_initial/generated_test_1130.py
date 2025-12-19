import os
import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

# Here is your prompt:
import os
import hashlib
import json
from pathlib import Path

def task_func(directory: str) -> str:
    """
    Create SHA256 hashes for all files in the specified directory, including files in subdirectories, 
    and save these hashes in a JSON file named 'hashes.json' in the given directory.

    Parameters:
    - directory (str): The path to the directory containing files to be hashed.
    
    Returns:
    str: The absolute path of the JSON file ('hashes.json') containing the hashes.
    
    Requirements:
    - os
    - hashlib
    - json
    - pathlib.Path

    Example:
    >>> json_file = task_func("/path/to/directory")
    >>> print(f"Hashes saved at: {json_file}")
    """

               hash_dict = {}
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = Path(root) / file
            with open(file_path, 'rb') as f:
                bytes = f.read()  # read entire file as bytes
                readable_hash = hashlib.sha256(bytes).hexdigest()
                hash_dict[str(file_path)] = readable_hash
                
    # Save to JSON file
    json_file = Path(directory) / 'hashes.json'
    with open(json_file, 'w') as f:
        json.dump(hash_dict, f)
    return str(json_file)

class TestTaskFunc(unittest.TestCase):

    def test_empty_directory(self):
        with TemporaryDirectory() as tmpdirname:
            result = task_func(tmpdirname)
            self.assertTrue(os.path.isfile(result))
            with open(result, 'r') as f:
                data = json.load(f)
                self.assertEqual(data, {})

    def test_single_file_hash(self):
        with TemporaryDirectory() as tmpdirname:
            file_path = Path(tmpdirname) / "testfile.txt"
            with open(file_path, 'w') as f:
                f.write("Hello, World!")
            result = task_func(tmpdirname)
            self.assertTrue(os.path.isfile(result))
            with open(result, 'r') as f:
                data = json.load(f)
                expected_hash = hashlib.sha256(b"Hello, World!").hexdigest()
                self.assertEqual(data[str(file_path)], expected_hash)

    def test_multiple_files_hash(self):
        with TemporaryDirectory() as tmpdirname:
            file1_path = Path(tmpdirname) / "file1.txt"
            file2_path = Path(tmpdirname) / "file2.txt"
            with open(file1_path, 'w') as f:
                f.write("File 1 content.")
            with open(file2_path, 'w') as f:
                f.write("File 2 content.")
            result = task_func(tmpdirname)
            self.assertTrue(os.path.isfile(result))
            with open(result, 'r') as f:
                data = json.load(f)
                expected_hash1 = hashlib.sha256(b"File 1 content.").hexdigest()
                expected_hash2 = hashlib.sha256(b"File 2 content.").hexdigest()
                self.assertEqual(data[str(file1_path)], expected_hash1)
                self.assertEqual(data[str(file2_path)], expected_hash2)

    def test_nested_directories(self):
        with TemporaryDirectory() as tmpdirname:
            nested_dir = Path(tmpdirname) / "nested"
            nested_dir.mkdir()
            file_path = nested_dir / "testfile.txt"
            with open(file_path, 'w') as f:
                f.write("Nested file content.")
            result = task_func(tmpdirname)
            self.assertTrue(os.path.isfile(result))
            with open(result, 'r') as f:
                data = json.load(f)
                expected_hash = hashlib.sha256(b"Nested file content.").hexdigest()
                self.assertEqual(data[str(file_path)], expected_hash)

    def test_non_existent_directory(self):
        with self.assertRaises(FileNotFoundError):
            task_func("/non/existent/directory")

if __name__ == "__main__":
    unittest.main()