import string
import random
import pandas as pd
import numpy as np
import unittest

# Constants
NUM_SAMPLES = 1000  # Number of samples

def task_func():
    """
    Generates a DataFrame with two columns: a string field and a float field.
    The string field contains randomly generated strings of 10 ASCII letters.
    The float field contains randomly generated numbers between 0 and 10000,
    formatted with two decimal places and a comma as the thousands separator.

    Parameters:
    - None

    Returns:
        DataFrame: A pandas DataFrame with NUM_SAMPLES rows. Each row contains a
        random string in the 'String Field' column and a formatted float in the
        'Float Field' column.
    """
    data = {
        "String Field": [
            "".join(random.choices(string.ascii_letters, k=10))
            for _ in range(NUM_SAMPLES)
        ],
        "Float Field": [f"{x:,.2f}" for x in np.random.uniform(0, 10000, NUM_SAMPLES)],
    }

    df = pd.DataFrame(data)

    return df

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        self.dataset = task_func()

    def test_dataframe_shape(self):
        """Test that the DataFrame has the correct number of rows and columns."""
        self.assertEqual(self.dataset.shape, (NUM_SAMPLES, 2))

    def test_string_field_content(self):
        """Test that the 'String Field' only contains strings of length 10."""
        for value in self.dataset["String Field"]:
            self.assertIsInstance(value, str)
            self.assertEqual(len(value), 10)

    def test_float_field_formatting(self):
        """Test that the 'Float Field' values are formatted correctly."""
        for value in self.dataset["Float Field"]:
            self.assertIsInstance(value, str)
            self.assertRegex(value, r'^\d{1,3}(,\d{3})*(\.\d{2})?$')

    def test_column_names(self):
        """Test that the DataFrame has the correct column names."""
        expected_columns = ["String Field", "Float Field"]
        self.assertListEqual(list(self.dataset.columns), expected_columns)

    def test_float_field_range(self):
        """Test that the 'Float Field' values are in the correct range."""
        for value in self.dataset["Float Field"]:
            float_value = float(value.replace(',', ''))
            self.assertGreaterEqual(float_value, 0)
            self.assertLessEqual(float_value, 10000)

if __name__ == '__main__':
    unittest.main()