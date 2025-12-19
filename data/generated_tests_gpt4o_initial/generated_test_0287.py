import os
import json
import unittest
from collections import Counter

# Here is your prompt:
def task_func(filename, directory):
    """
    Count the number of words in .txt files within a specified directory, 
    export the counts to a JSON file, and then return the total number of words.

    Parameters:
    filename (str): The name of the output JSON file.
    directory (str): The directory where .txt files are located.

    Returns:
    int: total number of words in .txt files

    Requirements:
    - collections.Counter
    - os
    - json

    Example:
    >>> with open("./testdir/single_file.txt","r") as f: print f.read()
    hello world hello
    >>> count = task_func('single_file.txt', './testdir/')
    >>> print(count)
    3
    """
    total_words = 0
    word_counts = Counter()

    for file_name in os.listdir(directory):
        if not file_name.endswith('.txt'):
            continue
        with open(os.path.join(directory, file_name), 'r') as file:
            words = file.read().split()
            word_counts.update(words)

    with open(filename, 'w') as file:
        json.dump(dict(word_counts), file)
    
    for word in word_counts:
        total_words += word_counts[word]
    return total_words


class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        os.makedirs('./testdir', exist_ok=True)
        with open('./testdir/file_one.txt', 'w') as f:
            f.write('hello world hello')
        with open('./testdir/file_two.txt', 'w') as f:
            f.write('goodbye world')
        with open('./testdir/file_three.doc', 'w') as f:
            f.write('this is a document')

    def tearDown(self):
        for filename in os.listdir('./testdir'):
            os.remove(os.path.join('./testdir', filename))
        os.rmdir('./testdir')

    def test_word_count_in_multiple_files(self):
        result = task_func('output.json', './testdir/')
        self.assertEqual(result, 5)  # 3 from file_one and 2 from file_two

    def test_exported_json_structure(self):
        task_func('output.json', './testdir/')
        with open('output.json', 'r') as f:
            word_counts = json.load(f)
        self.assertIn('hello', word_counts)
        self.assertIn('world', word_counts)
        self.assertIn('goodbye', word_counts)
        self.assertEqual(word_counts['hello'], 2)
        self.assertEqual(word_counts['world'], 2)
        self.assertEqual(word_counts['goodbye'], 1)

    def test_ignore_non_txt_files(self):
        result = task_func('output.json', './testdir/')
        with open('output.json', 'r') as f:
            word_counts = json.load(f)
        self.assertNotIn('this', word_counts)  # Word count from .doc file should be ignored
        self.assertNotIn('is', word_counts)

    def test_empty_directory(self):
        os.rmdir('./testdir')
        os.makedirs('./testdir', exist_ok=True)
        result = task_func('output_empty.json', './testdir/')
        self.assertEqual(result, 0)  # No files means a total word count of 0

    def test_no_txt_files_in_directory(self):
        os.rmdir('./testdir')
        os.makedirs('./testdir', exist_ok=True)
        with open('./testdir/file_one.doc', 'w') as f:
            f.write('this is not a text file')
        result = task_func('output_no_txt.json', './testdir/')
        self.assertEqual(result, 0)  # Should be 0 since there are no txt files


if __name__ == '__main__':
    unittest.main()