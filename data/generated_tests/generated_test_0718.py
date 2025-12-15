import unittest
import numpy as np

class TestTaskFunc(unittest.TestCase):

    def test_equal_word_counts(self):
        text1 = 'Hello world'
        text2 = 'Greetings planet'
        result = task_func(text1, text2)
        self.assertFalse(np.isnan(result[0]), "T-statistic should not be NaN")
        self.assertFalse(np.isnan(result[1]), "P-value should not be NaN")

    def test_unequal_word_counts(self):
        text1 = 'Hello world'
        text2 = 'Greetings'
        result = task_func(text1, text2)
        self.assertTrue(np.isnan(result[0]), "T-statistic should be NaN for unequal word counts")
        self.assertTrue(np.isnan(result[1]), "P-value should be NaN for unequal word counts")

    def test_identical_strings(self):
        text1 = 'Same same same'
        text2 = 'Same same same'
        result = task_func(text1, text2)
        self.assertEqual(result[0], 0.0, "T-statistic should be 0 for identical strings")
        self.assertEqual(result[1], 1.0, "P-value should be 1 for identical strings")

    def test_empty_strings(self):
        text1 = ''
        text2 = ''
        result = task_func(text1, text2)
        self.assertTrue(np.isnan(result[0]), "T-statistic should be NaN for empty strings")
        self.assertTrue(np.isnan(result[1]), "P-value should be NaN for empty strings")

    def test_different_word_lengths(self):
        text1 = 'One two three'
        text2 = 'Four five'
        result = task_func(text1, text2)
        self.assertTrue(np.isnan(result[0]), "T-statistic should be NaN for different lengths of word counts")
        self.assertTrue(np.isnan(result[1]), "P-value should be NaN for different lengths of word counts")

if __name__ == '__main__':
    unittest.main()