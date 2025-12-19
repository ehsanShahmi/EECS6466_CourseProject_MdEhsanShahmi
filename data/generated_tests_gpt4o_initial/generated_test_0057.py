import unittest
import pandas as pd
import tempfile
import os
from your_module import task_func  # Replace with the actual module name where task_func is defined

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Create a temporary CSV file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.csv')
        self.csv_data = """A,B,C,D
1,2,3,4
4,5,6,7
7,8,9,10
"""
        self.temp_file.write(self.csv_data.encode('utf-8'))
        self.temp_file.close()

    def tearDown(self):
        # Remove the temporary file
        if os.path.exists(self.temp_file.name):
            os.remove(self.temp_file.name)

    def test_corr_dataframe_shape(self):
        corr, ax = task_func(self.temp_file.name, 'Correlation Heatmap')
        self.assertEqual(corr.shape, (4, 4), "Correlation matrix shape should be (4, 4)")

    def test_corr_dataframe_values(self):
        corr, ax = task_func(self.temp_file.name, 'Correlation Heatmap')
        expected_values = pd.DataFrame(
            [[1.0, 1.0, 1.0, 1.0],
             [1.0, 1.0, 1.0, 1.0],
             [1.0, 1.0, 1.0, 1.0],
             [1.0, 1.0, 1.0, 1.0]],
            columns=['A', 'B', 'C', 'D'],
            index=['A', 'B', 'C', 'D']
        )
        pd.testing.assert_frame_equal(corr, expected_values.round(2), "Correlation values do not match expected.")

    def test_heatmap_title(self):
        corr, ax = task_func(self.temp_file.name, 'Test Title')
        self.assertEqual(ax.get_title(), 'Test Title', "Heatmap title should match the provided title.")

    def test_non_existent_file(self):
        with self.assertRaises(FileNotFoundError):
            task_func('non_existent_file.csv', 'Correlation Heatmap')

    def test_empty_csv(self):
        empty_file = tempfile.NamedTemporaryFile(delete=False, suffix='.csv')
        empty_file.write(b"")  # Write an empty CSV file
        empty_file.close()
        
        with self.assertRaises(pd.errors.EmptyDataError):
            task_func(empty_file.name, 'Empty CSV Test')
        
        os.remove(empty_file.name)

if __name__ == '__main__':
    unittest.main()