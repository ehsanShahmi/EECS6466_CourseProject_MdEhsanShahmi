import unittest
import pandas as pd
import os
import tempfile
from matplotlib import axes
from your_module import task_func  # Replace 'your_module' with the actual module name where task_func is defined

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.valid_csv = tempfile.NamedTemporaryFile(delete=False, mode='w', newline='')
        self.empty_csv = tempfile.NamedTemporaryFile(delete=False, mode='w', newline='')
        self.stop_words_csv = tempfile.NamedTemporaryFile(delete=False, mode='w', newline='')

        # Create a valid CSV with some text data
        self.valid_csv.write("Hello\nWorld\nThis is a test\nText data processing\n")
        self.valid_csv.close()

        # Create an empty CSV
        self.empty_csv.close()

        # Create a CSV with only stop words
        self.stop_words_csv.write("the\nan\nat\na\n")
        self.stop_words_csv.close()

    def tearDown(self):
        os.remove(self.valid_csv.name)
        os.remove(self.empty_csv.name)
        os.remove(self.stop_words_csv.name)

    def test_valid_input_no_save(self):
        ax = task_func(self.valid_csv.name)
        self.assertIsInstance(ax, axes.Axes)

    def test_valid_input_with_save(self):
        result = task_func(self.valid_csv.name, 'test_plot.png')
        self.assertIsNone(result)
        self.assertTrue(os.path.exists('test_plot.png'))
        os.remove('test_plot.png')

    def test_empty_input(self):
        result = task_func(self.empty_csv.name)
        self.assertIsNone(result)

    def test_only_stop_words(self):
        result = task_func(self.stop_words_csv.name)
        self.assertIsNone(result)

    def test_invalid_csv_format(self):
        with self.assertRaises(ValueError):
            task_func("non_existent_file.csv")

if __name__ == '__main__':
    unittest.main()