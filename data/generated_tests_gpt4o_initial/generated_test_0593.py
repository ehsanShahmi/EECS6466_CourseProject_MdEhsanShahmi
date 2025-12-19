import unittest
import os
import pandas as pd
from datetime import datetime
from task_module import task_func  # Assuming the function is saved in task_module.py

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.output_dir = './output'
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def tearDown(self):
        # Remove the output directory and its contents after each test
        for filename in os.listdir(self.output_dir):
            file_path = os.path.join(self.output_dir, filename)
            if os.path.isfile(file_path):
                os.unlink(file_path)
        os.rmdir(self.output_dir)

    def test_output_file_creation(self):
        """Test that the function creates a CSV file."""
        file_path, ax = task_func(1, self.output_dir)
        self.assertTrue(os.path.isfile(file_path))
        self.assertIn('traffic_data.csv', file_path)

    def test_csv_content(self):
        """Test that the CSV file contains the correct headers."""
        file_path, ax = task_func(1, self.output_dir)
        df = pd.read_csv(file_path)
        self.assertListEqual(list(df.columns), ['Time', 'Car', 'Bus', 'Truck', 'Bike'])

    def test_data_generation(self):
        """Test that data is generated within correct limits."""
        file_path, ax = task_func(5, self.output_dir)
        df = pd.read_csv(file_path)
        self.assertEqual(df.shape[0], 5)  # Ensure we have 5 rows of data
        for vehicle in ['Car', 'Bus', 'Truck', 'Bike']:
            self.assertTrue(df[vehicle].between(0, 50).all())  # Ensure vehicle counts are between 0 and 50

    def test_plot_return_type(self):
        """Test that the function returns a matplotlib axes object."""
        file_path, ax = task_func(1, self.output_dir)
        self.assertIsInstance(ax, plt.Axes)

if __name__ == '__main__':
    unittest.main()