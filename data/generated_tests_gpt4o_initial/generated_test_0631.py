import os
import unittest
import pandas as pd

OUTPUT_DIR = './output'

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Create a temporary output directory before each test."""
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

    def tearDown(self):
        """Remove the output directory after each test."""
        if os.path.exists(OUTPUT_DIR):
            for filename in os.listdir(OUTPUT_DIR):
                file_path = os.path.join(OUTPUT_DIR, filename)
                os.remove(file_path)
            os.rmdir(OUTPUT_DIR)

    def test_save_dataframe_creates_file(self):
        """Test that the function saves the DataFrame to a CSV file."""
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        filename = 'data.csv'
        filepath = task_func(df, filename, output_dir=OUTPUT_DIR)
        
        self.assertTrue(os.path.isfile(filepath), "File was not created.")

    def test_save_dataframe_correct_format(self):
        """Test that the generated CSV file has the correct format."""
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        filename = 'data.csv'
        filepath = task_func(df, filename, output_dir=OUTPUT_DIR)
        
        with open(filepath, 'r') as f:
            content = f.readlines()
        
        self.assertEqual(content[0].strip(), 'A,B', "Header is incorrect.")
        self.assertEqual(content[1].strip(), '1,4', "First row is incorrect.")
        self.assertEqual(content[2].strip(), '2,5', "Second row is incorrect.")
        self.assertEqual(content[3].strip(), '3,6', "Third row is incorrect.")

    def test_invalid_output_directory_creates_directory(self):
        """Test that the function creates the output directory if it doesn't exist."""
        temp_dir = './test_output'
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        filename = 'data.csv'
        task_func(df, filename, output_dir=temp_dir)

        self.assertTrue(os.path.exists(temp_dir), "Output directory was not created.")
        self.assertTrue(os.path.isfile(os.path.join(temp_dir, filename)), "CSV file was not created in new directory.")

    def test_multiple_saves_to_same_file(self):
        """Test that multiple saves overwrite the same file."""
        df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
        df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
        filename = 'data.csv'
        
        task_func(df1, filename, output_dir=OUTPUT_DIR)
        filepath = task_func(df2, filename, output_dir=OUTPUT_DIR)

        with open(filepath, 'r') as f:
            content = f.readlines()
        
        self.assertEqual(content[1].strip(), '5,7', "CSV was not overwritten correctly.")

if __name__ == '__main__':
    unittest.main()