import unittest
import os
import tempfile
import shutil

# Here is your prompt:
import re
import os
import shutil


def task_func(directory):
    """
    Find the files with filenames that contain "like" or "what" in a directory, create a new subdirectory called "Interesting Files" 
    and move those files to the new subdirectory.

    Parameters:
    directory (str): The directory path.

    Returns:
    List of files moved

    Requirements:
    - re
    - os
    - shutil

    Example:
    >>> import tempfile
    >>> temp_dir = tempfile.mkdtemp()
    >>> files = ['file_with_like.txt', 'another_file_with_what.doc', 'file_without_keywords.jpg', 'hidden_what_in_name.whatever']
    >>> for file in files:
    ...     with open(os.path.join(temp_dir, file), 'w') as f:
    ...         _ = f.write("Dummy content for testing.")
    >>> task_func(temp_dir)
    ['another_file_with_what.doc', 'hidden_what_in_name.whatever', 'file_with_like.txt']
    """

    pattern = re.compile(r'(like|what)', re.IGNORECASE)
    interesting_files = [file for file in os.listdir(directory) if pattern.search(file)]

    if not os.path.exists(os.path.join(directory, 'Interesting Files')):
        os.mkdir(os.path.join(directory, 'Interesting Files'))

    for file in interesting_files:
        shutil.move(os.path.join(directory, file), os.path.join(directory, 'Interesting Files'))

    return interesting_files

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Create a temporary directory and files for testing."""
        self.test_dir = tempfile.mkdtemp()
        self.files = [
            'file_with_like.txt',
            'another_file_with_what.doc',
            'file_without_keywords.jpg',
            'hidden_what_in_name.whatever'
        ]
        for file in self.files:
            with open(os.path.join(self.test_dir, file), 'w') as f:
                f.write("Dummy content for testing.")

    def tearDown(self):
        """Remove the temporary directory after tests."""
        shutil.rmtree(self.test_dir)

    def test_task_func_moves_correct_files(self):
        """Test that the function moves the correct files."""
        moved_files = task_func(self.test_dir)
        self.assertIn('file_with_like.txt', moved_files)
        self.assertIn('another_file_with_what.doc', moved_files)
        self.assertIn('hidden_what_in_name.whatever', moved_files)
        self.assertNotIn('file_without_keywords.jpg', moved_files)

    def test_interesting_files_directory_created(self):
        """Test that the 'Interesting Files' directory is created."""
        task_func(self.test_dir)
        interesting_fp = os.path.join(self.test_dir, 'Interesting Files')
        self.assertTrue(os.path.isdir(interesting_fp))

    def test_no_files_are_moved_if_none_match(self):
        """Test behavior when no files match the criteria."""
        os.remove(os.path.join(self.test_dir, 'file_with_like.txt'))
        os.remove(os.path.join(self.test_dir, 'another_file_with_what.doc'))
        os.remove(os.path.join(self.test_dir, 'hidden_what_in_name.whatever'))
        moved_files = task_func(self.test_dir)
        self.assertEqual(moved_files, [])

    def test_multiple_calls(self):
        """Test that multiple calls do not create duplicate directories or move files wrongly."""
        task_func(self.test_dir)
        moved_files_first = task_func(self.test_dir)
        self.assertEqual(moved_files_first, [])

if __name__ == '__main__':
    unittest.main()