import pandas as pd
import unittest
from random import seed

class TestTaskFunction(unittest.TestCase):

    def test_default_output_structure(self):
        df = task_func()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape[1], 2)
        self.assertIn('Letter', df.columns)
        self.assertIn('Category', df.columns)

    def test_letter_count_in_dataframe(self):
        df = task_func()
        unique_letters = df['Letter'].unique()
        self.assertEqual(len(unique_letters), 9)  # Default letters count A-I

    def test_category_count_in_dataframe(self):
        df = task_func()
        unique_categories = df['Category'].unique()
        self.assertEqual(len(unique_categories), 3)  # Default categories count

    def test_custom_input_letters(self):
        letters = ['X', 'Y']
        categories = ['Alpha', 'Beta']
        df = task_func(letters=letters, categories=categories)
        self.assertEqual(len(df['Letter'].unique()), len(letters))
        self.assertEqual(len(df['Category'].unique()), len(categories))

    def test_random_shuffling_effect(self):
        seed(0)  # Set seed for reproducibility
        df1 = task_func()
        seed(0)  # Reset seed
        df2 = task_func()

        # The dataframes should be the same since we are using the same seed
        pd.testing.assert_frame_equal(df1, df2)


if __name__ == '__main__':
    unittest.main()