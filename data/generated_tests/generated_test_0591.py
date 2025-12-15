import unittest
import os
import pandas as pd
from datetime import datetime
from random import randint

TEMP_CATEGORIES = ['Cold', 'Normal', 'Hot']
FILE_PATH = 'custom_data.csv'

def task_func(hours, file_path=FILE_PATH):
    data = {'Time': [], 'Temperature': [], 'Category': []}
    for i in range(hours):
        temp = randint(-10, 40)  # random temperature between -10 and 40
        data['Time'].append(datetime.now().strftime('%H:%M:%S.%f'))
        data['Temperature'].append(temp)
        if temp < 0:
            data['Category'].append(TEMP_CATEGORIES[0])
        elif temp > 25:
            data['Category'].append(TEMP_CATEGORIES[2])
        else:
            data['Category'].append(TEMP_CATEGORIES[1])

    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    ax = df.plot(x='Time', y='Temperature', kind='line', title="Temperature Data Over Time")
    plt.show()
    
    return file_path, ax

class TestTemperatureDataGeneration(unittest.TestCase):

    def test_file_generation(self):
        """Test if the CSV file is generated correctly."""
        hours = 5
        file_path, _ = task_func(hours)
        self.assertTrue(os.path.isfile(file_path))

    def test_correct_number_of_records(self):
        """Test if the correct number of temperature records are generated."""
        hours = 10
        file_path, _ = task_func(hours)
        df = pd.read_csv(file_path)
        self.assertEqual(len(df), hours)

    def test_temperature_range(self):
        """Test if the generated temperatures are within the expected range."""
        hours = 10
        file_path, _ = task_func(hours)
        df = pd.read_csv(file_path)
        self.assertTrue(df['Temperature'].between(-10, 40).all())

    def test_categories_assignment(self):
        """Test if categories are correctly assigned to the temperature data."""
        hours = 10
        file_path, _ = task_func(hours)
        df = pd.read_csv(file_path)
        
        for temp, category in zip(df['Temperature'], df['Category']):
            if temp < 0:
                self.assertEqual(category, TEMP_CATEGORIES[0])
            elif temp > 25:
                self.assertEqual(category, TEMP_CATEGORIES[2])
            else:
                self.assertEqual(category, TEMP_CATEGORIES[1])

    def test_file_cleanup(self):
        """Test if the generated file can be deleted after the tests."""
        hours = 5
        file_path, _ = task_func(hours)
        os.remove(file_path)
        self.assertFalse(os.path.isfile(file_path))

if __name__ == '__main__':
    unittest.main()