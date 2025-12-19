import unittest
import os
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
from contextlib import redirect_stdout

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.valid_script_path = 'valid_script.sh'
        self.invalid_script_path = 'invalid_script.sh'
        self.non_existent_script_path = 'non_existent_script.sh'
        self.valid_csv_path = 'valid_data.csv'
        self.invalid_csv_path = 'invalid_data.csv'
        
        # Creating a valid script and CSV for testing
        with open(self.valid_script_path, 'w') as f:
            f.write("#!/bin/bash\necho 'col1,col2\n1,2\n3,4' > valid_data.csv")
        os.chmod(self.valid_script_path, 0o755)

        # Creating an invalid CSV with more than two columns
        with open(self.invalid_csv_path, 'w') as f:
            f.write("col1,col2,col3\n1,2,3\n4,5,6")

    def tearDown(self):
        # Remove created files
        try:
            os.remove(self.valid_script_path)
            os.remove(self.valid_csv_path)
            os.remove(self.invalid_csv_path)
        except (FileNotFoundError, PermissionError):
            pass

    def test_valid_script_execution(self):
        """Test with a valid script that produces a valid CSV."""
        df, ax = task_func(self.valid_script_path, self.valid_csv_path)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape[1], 2)
        plt.close()  # Close plot to prevent display

    def test_invalid_script_execution(self):
        """Test with an invalid script."""
        with self.assertRaises(ValueError) as context:
            task_func(self.invalid_script_path, self.valid_csv_path)
        self.assertEqual(str(context.exception), "Error occurred while executing the script or script not found")

    def test_non_existent_script(self):
        """Test with a non-existent script."""
        with self.assertRaises(ValueError) as context:
            task_func(self.non_existent_script_path, self.valid_csv_path)
        self.assertEqual(str(context.exception), "Error occurred while executing the script or script not found")

    def test_invalid_csv_columns(self):
        """Test with a CSV that does not have exactly 2 columns."""
        with self.assertRaises(ValueError) as context:
            task_func(self.valid_script_path, self.invalid_csv_path)
        self.assertEqual(str(context.exception), "CSV file must contain exactly 2 columns")

    def test_csv_not_created(self):
        """Test CSV not created."""
        os.remove(self.valid_csv_path)  # Remove CSV to simulate it not being created
        with self.assertRaises(ValueError) as context:
            task_func(self.valid_script_path, self.valid_csv_path)
        self.assertEqual(str(context.exception), "Error occurred while executing the script or script not found")

if __name__ == '__main__':
    unittest.main()