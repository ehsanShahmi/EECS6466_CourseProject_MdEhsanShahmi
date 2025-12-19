from nltk.tokenize import RegexpTokenizer
from string import punctuation
import os
import unittest

def task_func(text, output_filename):
    """
    Extracts words from the input text that begin with the '$' character and saves them to a specified file,
    excluding any words that are solely composed of punctuation characters.

    This function is useful for processing texts where '$' is used to denote special terms or entities and saves
    these terms to a file for further analysis or usage.

    Parameters:
    input_text (str): The text from which to extract '$' prefixed words.
    output_filename (str): The filename for the output file where the extracted words will be saved.

    Returns:
    str: The absolute path to the output file containing the '$' prefixed words.

    Requirements:
    - nltk.tokenize.RegexpTokenizer
    - string.punctuation
    - os

    Example:
    >>> example_text = "$example $valid $!invalid $$ alsoInvalid"
    >>> task_func(example_text, 'extracted_dollar_words.txt')
    '/absolute/path/to/extracted_dollar_words.txt'
    """

    punctuation_set = set(punctuation)
    tokenizer = RegexpTokenizer(r'\$\w+')
    dollar_prefixed_words = tokenizer.tokenize(text)
    valid_dollar_words = [word for word in dollar_prefixed_words if
                          not all(char in punctuation_set for char in word[1:])]

    with open(output_filename, 'w') as file:
        for word in valid_dollar_words:
            file.write(word + '\n')

    return os.path.abspath(output_filename)

class TestTaskFunc(unittest.TestCase):

    def test_basic_extraction(self):
        text = "$example $valid $!invalid $$ alsoInvalid"
        expected_words = ["$example", "$valid"]
        output_file = 'test_output_1.txt'
        result = task_func(text, output_file)
        
        with open(output_file, 'r') as f:
            extracted_words = f.read().strip().split('\n')
        
        self.assertEqual(extracted_words, expected_words)
        self.assertTrue(os.path.exists(result))
        os.remove(output_file)

    def test_no_dollar_words(self):
        text = "No special words here."
        expected_words = []
        output_file = 'test_output_2.txt'
        result = task_func(text, output_file)
        
        with open(output_file, 'r') as f:
            extracted_words = f.read().strip().split('\n')
        
        self.assertEqual(extracted_words, expected_words)
        self.assertTrue(os.path.exists(result))
        os.remove(output_file)

    def test_only_punctuation_words(self):
        text = "$! $@ $$"
        expected_words = []
        output_file = 'test_output_3.txt'
        result = task_func(text, output_file)
        
        with open(output_file, 'r') as f:
            extracted_words = f.read().strip().split('\n')
        
        self.assertEqual(extracted_words, expected_words)
        self.assertTrue(os.path.exists(result))
        os.remove(output_file)

    def test_mixed_content(self):
        text = "This text has $valid $word and $!invalid, but also $anotherValid."
        expected_words = ["$valid", "$word", "$anotherValid"]
        output_file = 'test_output_4.txt'
        result = task_func(text, output_file)
        
        with open(output_file, 'r') as f:
            extracted_words = f.read().strip().split('\n')
        
        self.assertEqual(extracted_words, expected_words)
        self.assertTrue(os.path.exists(result))
        os.remove(output_file)

    def test_empty_input(self):
        text = ""
        expected_words = []
        output_file = 'test_output_5.txt'
        result = task_func(text, output_file)
        
        with open(output_file, 'r') as f:
            extracted_words = f.read().strip().split('\n')
        
        self.assertEqual(extracted_words, expected_words)
        self.assertTrue(os.path.exists(result))
        os.remove(output_file)

if __name__ == "__main__":
    unittest.main()