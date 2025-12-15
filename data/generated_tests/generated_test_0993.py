import unittest
import matplotlib.pyplot as plt
from task_module import task_func  # Assuming your function will be in task_module.py

class TestTaskFunc(unittest.TestCase):

    def test_basic_functionality(self):
        text = 'Hello world! This is a test.'
        ax = task_func(text)
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(len(ax.patches) > 0)  # Check if there are any histogram bars drawn

    def test_empty_string(self):
        text = ''
        ax = task_func(text)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.patches), 0)  # No histogram bars should be drawn

    def test_single_word(self):
        text = 'Hello'
        ax = task_func(text)
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(len(ax.patches) > 0)  # One histogram bar for one word

    def test_multiple_words_with_variety(self):
        text = 'A quick brown fox jumps over the lazy dog.'
        ax = task_func(text)
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(len(ax.patches) > 1)  # Check if multiple histogram bars are drawn

    def test_special_characters(self):
        text = 'C++ is great!!!'
        ax = task_func(text)
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(len(ax.patches) > 0)  # Histogram should have at least one bar


if __name__ == '__main__':
    unittest.main()