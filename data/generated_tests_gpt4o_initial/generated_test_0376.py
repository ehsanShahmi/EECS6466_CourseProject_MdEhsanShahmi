import unittest
import nltk

# Ensure that the necessary NLTK resources are available
nltk.download('stopwords')

# Start of the test suite for the provided task
class TestTaskFunc(unittest.TestCase):
    
    def test_basic_functionality(self):
        text = 'This is a sample text. This text is for testing.'
        expected_output = {'sample': 1, 'text': 2, 'testing': 1}
        self.assertEqual(task_func(text), expected_output)

    def test_case_insensitivity(self):
        text = 'The Quick brown Fox jumps over the lazy dog. the quick BROWN fox.'
        expected_output = {'quick': 2, 'brown': 2, 'fox': 2, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
        self.assertEqual(task_func(text), expected_output)

    def test_removal_of_stopwords(self):
        text = 'A journey of a thousand miles begins with a single step.'
        expected_output = {'journey': 1, 'thousand': 1, 'miles': 1, 'begins': 1, 'single': 1, 'step': 1}
        self.assertEqual(task_func(text), expected_output)

    def test_punctuation_handling(self):
        text = 'Hello!!! Can you, hear me? Yes, I can. Yes!!!'
        expected_output = {'hello': 1, 'can': 2, 'you': 1, 'hear': 1, 'me': 1, 'yes': 2}
        self.assertEqual(task_func(text), expected_output)

    def test_empty_string(self):
        text = ''
        expected_output = {}
        self.assertEqual(task_func(text), expected_output)

# This will allow the test suite to be run directly if executed as a script
if __name__ == '__main__':
    unittest.main()