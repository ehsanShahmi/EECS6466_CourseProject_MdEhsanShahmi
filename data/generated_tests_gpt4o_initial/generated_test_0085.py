import numpy as np
import pandas as pd
import unittest
from datetime import datetime, timedelta

# Here is your prompt:
def task_func(start_date, end_date, random_seed=42):
    """
    Generate and plot weather data for a specified date range.
    
    This function creates a DataFrame containing simulated daily weather data 
    within the specified date range. It generates random values for temperature, 
    humidity, and wind speed for each day. The function also plots these parameters 
    over the date range and returns both the DataFrame and the plot object.
    
    Parameters:
    - start_date (datetime): The start date for the data generation.
    - end_date (datetime): The end date for the data generation.
    - random_seed (int, optional): Seed for the random number generator to ensure reproducibility. Defaults to 42.
    
    The generated weather data ranges are as follows:
    - Temperature: Between -10°C and 40°C.
    - Humidity: Between 20% and 100%.
    - Wind Speed: Between 0 and 20 meters per second.
    
    Returns:
    - DataFrame: A pandas DataFrame with columns ['Date', 'Temperature', 'Humidity', 'Wind Speed'], containing the generated weather data for each day within the specified range.
    - Axes: A matplotlib Axes object of the plot showing the generated weather data.
    
    Raises:
    - ValueError: If 'end_date' is before 'start_date', indicating an invalid date range.
    """

    if end_date < start_date:
        raise ValueError("End date must be after start date")

    np.random.seed(random_seed)

    COLUMNS = ["Date", "Temperature", "Humidity", "Wind Speed"]
    data = []
    date = start_date

    while date <= end_date:
        temp = np.random.uniform(-10, 40)
        humidity = np.random.uniform(20, 100)
        wind_speed = np.random.uniform(0, 20)
        data.append([date, temp, humidity, wind_speed])
        date += timedelta(days=1)

    df = pd.DataFrame(data, columns=COLUMNS)
    ax = df.plot(x='Date', y=['Temperature', 'Humidity', 'Wind Speed'], title="Generated Weather Data")

    return df, ax

class TestTaskFunc(unittest.TestCase):
    
    def test_valid_date_range(self):
        start_date = datetime(2021, 1, 1)
        end_date = datetime(2021, 1, 10)
        df, ax = task_func(start_date, end_date)
        self.assertEqual(len(df), 10)
        
    def test_invalid_date_range(self):
        start_date = datetime(2021, 1, 10)
        end_date = datetime(2021, 1, 1)
        with self.assertRaises(ValueError):
            task_func(start_date, end_date)

    def test_dataframe_columns(self):
        start_date = datetime(2021, 1, 1)
        end_date = datetime(2021, 1, 5)
        df, ax = task_func(start_date, end_date)
        self.assertTrue(all(column in df.columns for column in ["Date", "Temperature", "Humidity", "Wind Speed"]))

    def test_temperature_range(self):
        start_date = datetime(2021, 1, 1)
        end_date = datetime(2021, 1, 5)
        df, ax = task_func(start_date, end_date)
        self.assertTrue((df['Temperature'] >= -10).all() and (df['Temperature'] <= 40).all())

    def test_humidity_range(self):
        start_date = datetime(2021, 1, 1)
        end_date = datetime(2021, 1, 5)
        df, ax = task_func(start_date, end_date)
        self.assertTrue((df['Humidity'] >= 20).all() and (df['Humidity'] <= 100).all())

if __name__ == '__main__':
    unittest.main()