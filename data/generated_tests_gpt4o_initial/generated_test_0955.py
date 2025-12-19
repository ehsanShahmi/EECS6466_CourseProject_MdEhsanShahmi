import unittest
import numpy as np
import matplotlib.pyplot as plt
from task_module import task_func  # Assuming the function is in a file named task_module.py

class TestTaskFunc(unittest.TestCase):

    def test_valid_input_with_spaces(self):
        mystrings = ['Lorem ipsum', 'consectetur adipiscing']
        text = 'Lorem ipsum dolor sit amet lorem Ipsum'
        ax = task_func(mystrings, text)
        self.assertIsInstance(ax, plt.Axes)
    
    def test_input_with_no_replacements(self):
        mystrings = ['Hello World']
        text = 'Goodbye Universe'
        ax = task_func(mystrings, text)
        self.assertIsInstance(ax, plt.Axes)
    
    def test_case_insensitivity(self):
        mystrings = ['hello', 'world']
        text = 'Hello world hello WORLD'
        ax = task_func(mystrings, text)
        self.assertIsInstance(ax, plt.Axes)

    def test_empty_text(self):
        mystrings = ['Lorem ipsum']
        text = ''
        with self.assertRaises(ValueError):
            task_func(mystrings, text)

    def test_multiple_spaces_in_input(self):
        mystrings = ['a b c', 'd e f']
        text = 'a b c a b c d e f'
        ax = task_func(mystrings, text)
        self.assertIsInstance(ax, plt.Axes)

if __name__ == '__main__':
    unittest.main()