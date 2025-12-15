import string
import matplotlib.pyplot as plt
import unittest

def task_func(s):
    """
    Calculate the frequency of each letter in a string and return a bar chart of frequencies.
    Results are case-insensitive. If non-string input is provided, function will throw an error.

    Parameters:
    s (str): The string to calculate letter frequencies.

    Returns:
    tuple: A tuple containing:
        - dict: A dictionary with the frequency of each letter.
        - Axes: The bar subplot of 'Letter Frequencies' with 'Letters' on the x-axis and 'Frequency'
                on the y-axis.
    """
    if not isinstance(s, str):
        raise TypeError("Expected string input")

    LETTERS = string.ascii_lowercase

    s = s.lower()

    letter_counts = {letter: s.count(letter) for letter in LETTERS}

    fig, ax = plt.subplots()
    ax.bar(letter_counts.keys(), letter_counts.values())
    ax.set_xlabel("Letters")
    ax.set_ylabel("Frequency")
    ax.set_title("Letter Frequencies")

    return letter_counts, ax


class TestTaskFunction(unittest.TestCase):
    
    def test_basic_functionality(self):
        s = 'This is a test string.'
        freqs, ax = task_func(s)
        expected_freqs = {'a': 1, 'b': 0, 'c': 0, 'd': 0, 'e': 1, 'f': 0, 'g': 1, 'h': 1, 'i': 3, 
                          'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 1, 'o': 0, 'p': 0, 'q': 0, 
                          'r': 1, 's': 4, 't': 4, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 
                          'z': 0}
        self.assertEqual(freqs, expected_freqs)
        self.assertIsInstance(ax, plt.Axes)
    
    def test_empty_string(self):
        s = ''
        freqs, ax = task_func(s)
        expected_freqs = {letter: 0 for letter in string.ascii_lowercase}
        self.assertEqual(freqs, expected_freqs)
        self.assertIsInstance(ax, plt.Axes)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            task_func(12345)
        with self.assertRaises(TypeError):
            task_func(None)
        with self.assertRaises(TypeError):
            task_func(['This', 'is', 'a', 'list'])

    def test_case_insensitivity(self):
        s = 'AaBbCc'
        freqs, ax = task_func(s)
        expected_freqs = {letter: 1 if letter in 'abc' else 0 for letter in string.ascii_lowercase}
        self.assertEqual(freqs, expected_freqs)
        self.assertIsInstance(ax, plt.Axes)

    def test_special_characters(self):
        s = 'This!! is@ a test# string...'
        freqs, ax = task_func(s)
        expected_freqs = {'a': 1, 'b': 0, 'c': 0, 'd': 0, 'e': 1, 'f': 0, 'g': 1, 'h': 1, 'i': 3,
                          'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 1, 'o': 0, 'p': 0, 'q': 0, 
                          'r': 1, 's': 4, 't': 4, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 
                          'z': 0}
        self.assertEqual(freqs, expected_freqs)
        self.assertIsInstance(ax, plt.Axes)

if __name__ == '__main__':
    unittest.main()