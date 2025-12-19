import unittest
import os
import tempfile
from your_module import task_func  # Replace 'your_module' with the actual name of your module

class TestUniqueNonStopWords(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the temporary directory
        for file_name in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, file_name))
        os.rmdir(self.test_dir)

    def test_empty_directory(self):
        # Test when the directory is empty
        result = task_func(self.test_dir)
        self.assertEqual(result, 0)

    def test_single_file_with_no_non_stopwords(self):
        # Test with a file containing only stopwords
        with open(os.path.join(self.test_dir, 'stopwords.txt'), 'w') as f:
            f.write("the is an and")
        result = task_func(self.test_dir)
        self.assertEqual(result, 0)

    def test_single_file_with_non_stopwords(self):
        # Test with a file containing non-stopwords
        with open(os.path.join(self.test_dir, 'non_stopwords.txt'), 'w') as f:
            f.write("Python programming language is great")
        result = task_func(self.test_dir)
        self.assertEqual(result, 6)  # 'Python', 'programming', 'language', 'great', unique count

    def test_multiple_files_with_mix(self):
        # Test with multiple files having a mix of stopwords and non-stopwords
        with open(os.path.join(self.test_dir, 'file1.txt'), 'w') as f:
            f.write("This is a test file")
        with open(os.path.join(self.test_dir, 'file2.txt'), 'w') as f:
            f.write("Another example file is here")
        result = task_func(self.test_dir)
        self.assertEqual(result, 7)  # Unique non-stopwords: 'This', 'test', 'file', 'Another', 'example', 'is', 'here'

    def test_identical_words_in_multiple_files(self):
        # Test with identical non-stopwords in different files
        with open(os.path.join(self.test_dir, 'file1.txt'), 'w') as f:
            f.write("Unique unique words")
        with open(os.path.join(self.test_dir, 'file2.txt'), 'w') as f:
            f.write("Unique words are important")
        result = task_func(self.test_dir)
        self.assertEqual(result, 5)  # Unique non-stopwords: 'Unique', 'unique', 'words', 'are', 'important'

if __name__ == '__main__':
    unittest.main()