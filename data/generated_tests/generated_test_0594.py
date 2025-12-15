import csv
import os
import shutil
import unittest
from datetime import datetime
from random import randint

# Constants
WEATHER_CONDITIONS = ['Sunny', 'Cloudy', 'Rainy', 'Snowy', 'Stormy']
OUTPUT_DIR = './output'


# Here is your prompt:
def task_func(hours, output_dir=OUTPUT_DIR):
    """
    Generate weather data for the specified number of hours, save it in a CSV file with columns 'Time' and 'Condition'
     and back up the file to a backup directory.
    
    Parameters:
    - hours (int): The number of hours for which weather data is to be generated.
    - output_dir (str, optional): The output file path

    Returns:
    - str: The path of the generated CSV file.
    
    Requirements:
    - datetime
    - os
    - random
    - csv
    - shutil
    
    Example:
    >>> 'weather_data.csv' in task_func(24)
    True
    >>> 'weather_data.csv' in task_func(10)
    True
    """
    FILE_PATH = os.path.join(output_dir, 'weather_data.csv')
    BACKUP_PATH = os.path.join(output_dir, 'backup/')
    data = [['Time', 'Condition']]
    for i in range(hours):
        row = [datetime.now().strftime('%H:%M:%S.%f'), WEATHER_CONDITIONS[randint(0, len(WEATHER_CONDITIONS)-1)]]
        data.append(row)

    with open(FILE_PATH, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    
    if not os.path.exists(BACKUP_PATH):
        os.makedirs(BACKUP_PATH)
    shutil.copy(FILE_PATH, BACKUP_PATH)

    return FILE_PATH

# Test Suite
class TestWeatherDataGeneration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(OUTPUT_DIR):
            shutil.rmtree(OUTPUT_DIR)

    def test_generate_weather_data_for_24_hours(self):
        file_path = task_func(24)
        self.assertTrue(os.path.exists(file_path))
        self.assertIn('weather_data.csv', file_path)

    def test_generate_weather_data_for_10_hours(self):
        file_path = task_func(10)
        self.assertTrue(os.path.exists(file_path))
        self.assertIn('weather_data.csv', file_path)

    def test_file_contains_correct_columns(self):
        file_path = task_func(5)
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            headers = next(reader)
            self.assertEqual(headers, ['Time', 'Condition'])

    def test_backup_directory_creation(self):
        task_func(1)
        backup_path = os.path.join(OUTPUT_DIR, 'backup/')
        self.assertTrue(os.path.exists(backup_path))

    def test_backup_file_creation(self):
        file_path = task_func(1)
        backup_path = os.path.join(OUTPUT_DIR, 'backup/', 'weather_data.csv')
        self.assertTrue(os.path.exists(backup_path))

if __name__ == '__main__':
    unittest.main()