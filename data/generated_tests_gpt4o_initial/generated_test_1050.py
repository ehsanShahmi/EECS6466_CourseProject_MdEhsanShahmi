import os
import hashlib
import unittest

# Provided Prompt
DIRECTORY = "./hashed_files"

def task_func(input_string):
    """
    Hash each non-empty line of a multi-line string using SHA256 and save the hashes to files.
    The filename is the first 10 characters of the hash, with a '.txt' extension.

    Parameters:
    - input_string (str): A multi-line string to be processed.

    Returns:
    - list[str]: A list of file paths where the hashes of non-empty lines are saved.

    Requirements:
    - os
    - hashlib

    Notes:
    - If the DIRECTORY does not exist, it is created.
    - Empty lines in the input string are ignored.

    Example:
    >>> file_paths = task_func('line a\nfollows by line b\n\n...bye\n')
    >>> print(file_paths)
    ['./hashed_files/489fe1fa6c.txt', './hashed_files/67009597fe.txt', './hashed_files/eab4758603.txt']
    """

    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)

    file_paths = []
    lines = input_string.split("\n")
    for line in lines:
        if line:  # Check if line is not empty
            line_hash = hashlib.sha256(line.encode()).hexdigest()
            filename = line_hash[:10] + ".txt"
            filepath = os.path.join(DIRECTORY, filename)
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(line_hash)
            file_paths.append(filepath)

    return file_paths


class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        if os.path.exists(DIRECTORY):
            for f in os.listdir(DIRECTORY):
                os.remove(os.path.join(DIRECTORY, f))
        else:
            os.makedirs(DIRECTORY)
    
    def tearDown(self):
        for f in os.listdir(DIRECTORY):
            os.remove(os.path.join(DIRECTORY, f))
    
    def test_basic_functionality(self):
        input_str = "line a\nfollows by line b\n\n...bye\n"
        expected_filenames = [
            "489fe1fa6c.txt",
            "67009597fe.txt",
            "eab4758603.txt"
        ]
        result = task_func(input_str)
        self.assertEqual(sorted(os.listdir(DIRECTORY)), sorted(expected_filenames))
    
    def test_empty_string(self):
        input_str = ""
        result = task_func(input_str)
        self.assertEqual(result, [])
        self.assertEqual(os.listdir(DIRECTORY), [])
    
    def test_single_line(self):
        input_str = "single line"
        expected_filename = "c9c8fddf40.txt"  # SHA256 of "single line"
        result = task_func(input_str)
        self.assertEqual(sorted(os.listdir(DIRECTORY)), [expected_filename])
    
    def test_multiple_empty_lines(self):
        input_str = "\n\n\n"
        result = task_func(input_str)
        self.assertEqual(result, [])
        self.assertEqual(os.listdir(DIRECTORY), [])
    
    def test_special_characters(self):
        input_str = "line with special char @!#\nnew line\n"
        expected_filenames = [
            "93330ab72a.txt",  # SHA256 of "line with special char @!#"
            "ec4988c21d.txt"   # SHA256 of "new line"
        ]
        result = task_func(input_str)
        self.assertEqual(sorted(os.listdir(DIRECTORY)), sorted(expected_filenames))


if __name__ == "__main__":
    unittest.main()