import os
import unittest
from nltk import word_tokenize

# Here is your prompt:
import os
from nltk import word_tokenize

def task_func(file_path='File.txt'):
    """
    Tokenizes a text file using the NLTK library. This function reads each line from the file, 
    breaks it into words or punctuation, and stores the tokens in a list.
    
    Parameters:
    - file_path (str): The path to the text file. Defaults to 'File.txt'.
    
    Returns:
    - list: A list of tokens.
    
    Requirements:
    - os
    - nltk.word_tokenize
    
    Examples:
    >>> task_func('sample.txt')
    ['Hello', ',', 'world', '!']
    >>> task_func('data.txt')
    ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog', '.']
    """

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    tokens = []

    with open(file_path, 'r') as file:
        for line in file:
            tokens.extend(word_tokenize(line))

    return tokens


class TestTaskFunc(unittest.TestCase):
    
    def test_tokenization_of_sample_file(self):
        # Create a sample file for testing
        with open('sample.txt', 'w') as f:
            f.write('Hello, world!')
        
        expected_output = ['Hello', ',', 'world', '!']
        self.assertEqual(task_func('sample.txt'), expected_output)

    def test_tokenization_of_data_file(self):
        # Create a data file for testing
        with open('data.txt', 'w') as f:
            f.write('The quick brown fox jumps over the lazy dog.')
        
        expected_output = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog', '.']
        self.assertEqual(task_func('data.txt'), expected_output)

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            task_func('non_existent_file.txt')

    def test_empty_file(self):
        # Create an empty file for testing
        with open('empty.txt', 'w') as f:
            pass
        
        expected_output = []
        self.assertEqual(task_func('empty.txt'), expected_output)

    def test_tokenization_with_special_characters(self):
        # Create a file with special characters
        with open('special_chars.txt', 'w') as f:
            f.write('Hello!!! This is a test... @Python?')
        
        expected_output = ['Hello', '!', '!', '!', 'This', 'is', 'a', 'test', '.', '.', '.', '@', 'Python', '?']
        self.assertEqual(task_func('special_chars.txt'), expected_output)

if __name__ == '__main__':
    unittest.main()