import unittest
import os
import csv

# Here is your prompt:
import csv
import random

# Constants
DATA = ['Temperature', 'Humidity', 'Pressure']
RANGE = {
    'Temperature': (-50, 50),
    'Humidity': (0, 100),
    'Pressure': (980, 1040)
}

def task_func(file_name="data.csv"):
    """
    Generate a CSV file with weather data for each hour of the current day.

    Parameters:
    file_name (str): The path to the CSV file to be created.
    
    Returns:
    str: The path to the created file.

    Note:
    - The row names for the csv are 'Temperature', 'Humidity', and 'Pressure' 
    - Temperature ranged rom -50 to 50
    - Humidity ranged rom 0 to 100
    - Pressure ranged rom 980 to 1040

    Requirements:
    - os
    - datetime
    - csv
    - random

    Example:
    >>> task_func("data.csv")
    'path/to/data.csv'
    """

    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Time'] + DATA)
        
        for hour in range(24):
            row = [f'{hour}:00']
            for data_type in DATA:
                min_val, max_val = RANGE[data_type]
                row.append(random.uniform(min_val, max_val))
            writer.writerow(row)

    return file_name

class TestWeatherDataCSVGeneration(unittest.TestCase):
    
    def test_file_creation(self):
        """
        Test that the CSV file is created.
        """
        file_name = "test_data.csv"
        result = task_func(file_name)
        self.assertEqual(result, file_name)
        self.assertTrue(os.path.isfile(file_name))
        os.remove(file_name)  # Clean up

    def test_file_contents(self):
        """
        Test that the CSV file contains the correct header and data format.
        """
        file_name = "test_data.csv"
        task_func(file_name)

        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            self.assertEqual(headers, ['Time'] + DATA)

            for row in reader:
                self.assertEqual(len(row), 4)  # Time + 3 weather data
                self.assertTrue(row[0].endswith(':00'))  # Check hour format
            file.close()

        os.remove(file_name)  # Clean up

    def test_temperature_range(self):
        """
        Test that the temperature values are within the specified range.
        """
        file_name = "test_data.csv"
        task_func(file_name)

        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header

            for row in reader:
                temperature = float(row[1])  # Temperature is the second column
                self.assertGreaterEqual(temperature, -50)
                self.assertLessEqual(temperature, 50)
        
        os.remove(file_name)  # Clean up

    def test_humidity_range(self):
        """
        Test that the humidity values are within the specified range.
        """
        file_name = "test_data.csv"
        task_func(file_name)

        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header

            for row in reader:
                humidity = float(row[2])  # Humidity is the third column
                self.assertGreaterEqual(humidity, 0)
                self.assertLessEqual(humidity, 100)
        
        os.remove(file_name)  # Clean up

    def test_pressure_range(self):
        """
        Test that the pressure values are within the specified range.
        """
        file_name = "test_data.csv"
        task_func(file_name)

        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header

            for row in reader:
                pressure = float(row[3])  # Pressure is the fourth column
                self.assertGreaterEqual(pressure, 980)
                self.assertLessEqual(pressure, 1040)
        
        os.remove(file_name)  # Clean up

if __name__ == '__main__':
    unittest.main()