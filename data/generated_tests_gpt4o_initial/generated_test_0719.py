import unittest
import os

# Here is your prompt:
import re
import os
import glob

def task_func(directory, word):
    """
    Count the number of files in a directory that contain a specific word.
    
    Parameters:
    - directory (str): The directory path.
    - word (str): The word to search for.
    
    Returns:
    - count (int): The number of files that contain the given word.
    
    Requirements:
    - re
    - os
    - glob
    
    Example:
    >>> task_func('./documents', 'word')
    2
    >>> task_func('./documents', 'apple')
    3
    """

    count = 0
    # Pattern to match word boundaries and ignore case, handling punctuation
    pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
    for filename in glob.glob(os.path.join(directory, '*.*')):
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
            if pattern.search(text):
                count += 1
    return count

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Create a temporary directory and files for testing."""
        self.test_dir = 'test_documents'
        os.makedirs(self.test_dir, exist_ok=True)
        with open(os.path.join(self.test_dir, 'file1.txt'), 'w') as f:
            f.write("This is a test file with the word apple.")
        with open(os.path.join(self.test_dir, 'file2.txt'), 'w') as f:
            f.write("This is another test file with the word banana.")
        with open(os.path.join(self.test_dir, 'file3.txt'), 'w') as f:
            f.write("This file mentions apple and other words.")
        with open(os.path.join(self.test_dir, 'file4.txt'), 'w') as f:
            f.write("This file does not contain the target word.")
    
    def tearDown(self):
        """Remove the temporary directory and files after testing."""
        for filename in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, filename))
        os.rmdir(self.test_dir)

    def test_count_files_with_apple(self):
        """Test case for counting files containing the word 'apple'."""
        result = task_func(self.test_dir, 'apple')
        self.assertEqual(result, 2)

    def test_count_files_with_banana(self):
        """Test case for counting files containing the word 'banana'."""
        result = task_func(self.test_dir, 'banana')
        self.assertEqual(result, 1)

    def test_count_files_with_no_matches(self):
        """Test case for counting files with no matching words."""
        result = task_func(self.test_dir, 'orange')
        self.assertEqual(result, 0)

    def test_count_files_with_case_insensitivity(self):
        """Test case to check case insensitivity of word matching."""
        result = task_func(self.test_dir, 'Apple')
        self.assertEqual(result, 2)

    def test_count_files_with_nonexistent_directory(self):
        """Test case for handling a nonexistent directory."""
        result = task_func('./nonexistent_dir', 'apple')
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()