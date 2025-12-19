import csv
import os
import unittest
from datetime import datetime
from random import randint

# Constants
SENSORS = ['Temperature', 'Humidity', 'Pressure']
OUTPUT_DIR = './output'

def task_func(hours, output_dir=OUTPUT_DIR):
    """
    Create sensor data for the specified number of hours and save it in a CSV file
    with coloumns 'Time', 'Temperature', 'Humidity' and 'Pressure'.

    Parameters:
    - hours (int): The number of hours for which sensor data is to be generated.
    - output_dir (str, optional): The output file path

    Returns:
    - hours (int): Number of hours to generate data for.
    """

    FILE_PATH = os.path.join(output_dir, 'sensor_data.csv')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    data = [['Time'] + SENSORS]
    for i in range(hours):
        row = [datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')] + [randint(0, 100) for _ in SENSORS]
        data.append(row)

    with open(FILE_PATH, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

    return FILE_PATH

class TestSensorDataGeneration(unittest.TestCase):

    def setUp(self):
        """Set up test case environment."""
        self.test_output_dir = './test_output'
        if not os.path.exists(self.test_output_dir):
            os.makedirs(self.test_output_dir)

    def tearDown(self):
        """Clean up after tests."""
        try:
            os.remove(os.path.join(self.test_output_dir, 'sensor_data.csv'))
        except OSError:
            pass
        try:
            os.rmdir(self.test_output_dir)
        except OSError:
            pass

    def test_generate_data_for_one_hour(self):
        """Test generating data for 1 hour."""
        file_path = task_func(1, self.test_output_dir)
        self.assertTrue(os.path.exists(file_path))
        self.assertIsInstance(file_path, str)
        self.assertIn('sensor_data.csv', file_path)
    
    def test_generate_data_for_zero_hours(self):
        """Test generating data for 0 hours, expecting the file path."""
        file_path = task_func(0, self.test_output_dir)
        self.assertTrue(os.path.exists(file_path))
        self.assertIsInstance(file_path, str)
        self.assertIn('sensor_data.csv', file_path)
    
    def test_file_contents(self):
        """Ensure the contents of the generated CSV file are correct."""
        task_func(1, self.test_output_dir)
        with open(os.path.join(self.test_output_dir, 'sensor_data.csv'), 'r') as f:
            reader = csv.reader(f)
            rows = list(reader)
            self.assertEqual(rows[0], ['Time', 'Temperature', 'Humidity', 'Pressure'])
            self.assertEqual(len(rows), 2)  # One header row + one data row

    def test_data_within_range(self):
        """Test that generated sensor data is within the expected range."""
        task_func(1, self.test_output_dir)
        with open(os.path.join(self.test_output_dir, 'sensor_data.csv'), 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                # Check that sensor data is within the range 0-100
                for value in row[1:]:
                    self.assertTrue(0 <= int(value) <= 100)

if __name__ == '__main__':
    unittest.main()