import unittest
import numpy as np
import matplotlib.pyplot as plt

# Constants
ALPHABET = list(string.ascii_lowercase)

# Provided prompt does not require any modifications

class TestTaskFunc(unittest.TestCase):
    def test_empty_word(self):
        """Test with empty string"""
        with self.assertRaises(ValueError):
            task_func('')

    def test_valid_word(self):
        """Test with a valid lowercase word"""
        ax = task_func('abc')
        self.assertEqual(ax.get_title(), 'Alphabetical Position of Letters in Word')

    def test_invalid_characters(self):
        """Test with invalid characters"""
        with self.assertRaises(ValueError):
            task_func('abc1')  # Contains numeric

    def test_special_characters(self):
        """Test with special characters"""
        with self.assertRaises(ValueError):
            task_func('he@llo')  # Contains special character

    def test_single_character(self):
        """Test with a single character word"""
        ax = task_func('z')
        self.assertEqual(ax.get_title(), 'Alphabetical Position of Letters in Word')

# If this is run as a script, execute the test suite
if __name__ == '__main__':
    unittest.main()