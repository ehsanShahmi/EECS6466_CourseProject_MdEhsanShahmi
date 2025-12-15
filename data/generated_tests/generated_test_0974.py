import unittest
import os
import tempfile
import shutil
from pathlib import Path

# Here is your prompt:
def task_func(source_path, destination_path):
    """
    Lists files in the specified source directory without descending into subdirectories and copies them to a
    destination directory.

    Parameters:
    - source_path (str):      The source directory path to analyze. Must be an existing, accessible directory.
    - destination_path (str): The destination directory path where files will be copied.
                              If it does not exist, this function will create it.

    Returns:
    Tuple[str, List[str]]: A tuple containing the name of the source directory and a list of filenames (not
                           full paths) that were copied.

    Raises:
    - ValueError: If source_path does not exist or is not a directory.

    Requirements:
    - shutil
    - pathlib

    Example:
    >>> x = task_func('/Docs/src/Scripts')
    >>> type(x)
    <class 'tuple'>
    >>> x
    ('Scripts', ['file_1_in_scripts_dir.txt', 'file_2_in_scripts_dir.txt'])
    """

    source_path = pathlib.Path(source_path).resolve()
    destination_path = pathlib.Path(destination_path).resolve()

    if not (source_path.exists() and source_path.is_dir()):
        raise ValueError("source_path must be an existing directory.")

    destination_path.mkdir(parents=True, exist_ok=True)

    results = []
    for entry in source_path.iterdir():
        if entry.is_file():
            results.append(str(entry.name))
            shutil.copy(str(entry), str(destination_path))
    return (source_path.name, results)


class TestTaskFunc(unittest.TestCase):
    def setUp(self):
        """Set up a temporary directory structure for testing."""
        self.test_dir = tempfile.TemporaryDirectory()
        self.src_dir = Path(self.test_dir.name) / "source"
        self.dest_dir = Path(self.test_dir.name) / "destination"
        self.src_dir.mkdir(parents=True, exist_ok=True)

        # Create some test files in the source directory
        for i in range(5):
            with open(self.src_dir / f"file_{i}.txt", 'w') as f:
                f.write(f"This is file {i}.")

    def tearDown(self):
        """Cleanup the temporary directory after tests."""
        self.test_dir.cleanup()

    def test_correct_file_copying(self):
        """Test that files are copied from source to destination."""
        result = task_func(str(self.src_dir), str(self.dest_dir))
        expected_files = [f"file_{i}.txt" for i in range(5)]
        
        # Verify the result
        self.assertEqual(result[0], self.src_dir.name)
        self.assertListEqual(result[1], expected_files)
        
        # Verify files are physically copied
        for file in expected_files:
            self.assertTrue((self.dest_dir / file).exists())

    def test_empty_source_directory(self):
        """Test handling of an empty source directory."""
        empty_src_dir = Path(self.test_dir.name) / "empty_source"
        empty_src_dir.mkdir(parents=True, exist_ok=True)
        
        result = task_func(str(empty_src_dir), str(self.dest_dir))
        
        self.assertEqual(result[0], empty_src_dir.name)
        self.assertListEqual(result[1], [])
        self.assertEqual(len(list(self.dest_dir.iterdir())), 0)

    def test_non_existent_source(self):
        """Test handling of a non-existent source directory."""
        with self.assertRaises(ValueError) as context:
            task_func(str(Path(self.test_dir.name) / "non_existent"), str(self.dest_dir))
        self.assertEqual(str(context.exception), "source_path must be an existing directory.")

    def test_invalid_source_path(self):
        """Test handling of an invalid source path (not a directory)."""
        invalid_file = self.src_dir / "invalid_file.txt"
        
        with open(invalid_file, 'w') as f:
            f.write("This is an invalid file.")

        with self.assertRaises(ValueError) as context:
            task_func(str(invalid_file), str(self.dest_dir))
        self.assertEqual(str(context.exception), "source_path must be an existing directory.")

if __name__ == '__main__':
    unittest.main()