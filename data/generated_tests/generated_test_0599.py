import pandas as pd
import unittest
import matplotlib.pyplot as plt

class TestTaskFunc(unittest.TestCase):
    
    def test_no_words_starting_with_letter(self):
        """Test case where no words start with the specified letter."""
        df = {'Word': ['banana', 'cherry', 'fig']}
        letter = 'a'
        ax = task_func(df, letter)
        
        self.assertIsNone(ax)  # Expecting None when no words match

    def test_single_word_matching(self):
        """Test case where only one word starts with the specified letter."""
        df = {'Word': ['apple', 'banana', 'cherry']}
        letter = 'a'
        ax = task_func(df, letter)
        
        self.assertIsNotNone(ax)  # Expecting a valid Axes object
        self.assertEqual(ax.get_title(), "Histogram of Word Lengths starting with 'a'")  # Check title

    def test_multiple_words_matching(self):
        """Test case where multiple words start with the specified letter."""
        df = {'Word': ['apple', 'avocado', 'banana', 'apricot']}
        letter = 'a'
        ax = task_func(df, letter)
        
        self.assertIsNotNone(ax)  # Expecting a valid Axes object
        self.assertEqual(len(ax.patches), 3)  # Expecting 3 bins for lengths 5, 7 (apple, avocado) and 6(apricot)

    def test_word_lengths_histogram(self):
        """Test case to validate the histogram for correct word length distribution."""
        df = {'Word': ['apple', 'avocado', 'banana', 'grape', 'fig']}
        letter = 'a'
        ax = task_func(df, letter)
        
        self.assertIsNotNone(ax)  # Expecting a valid Axes object
        lengths = [len(word) for word in df['Word'] if word.startswith(letter)]
        self.assertIn(len(ax.patches), lengths)  # Validate that the histogram covers the expected lengths

    def test_case_insensitivity(self):
        """Test case to verify that the function is case-sensitive to the starting letter."""
        df = {'Word': ['Apple', 'avocado', 'Banana']}
        letter = 'a'
        ax = task_func(df, letter)
        
        self.assertIsNone(ax)  # Expecting None as 'a' should not match 'Apple'
    
if __name__ == "__main__":
    unittest.main()