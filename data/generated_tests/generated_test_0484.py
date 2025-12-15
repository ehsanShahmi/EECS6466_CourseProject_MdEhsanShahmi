import math
import numpy as np
from datetime import datetime
import pandas as pd
import unittest

def task_func(
    start_time,
    end_time,
    step,
    columns=["Timestamp", "Sensor1", "Sensor2", "Sensor3", "SensorStatus"],
    sensor_statuses=["OK", "MAINTENANCE_REQUIRED", "ERROR"],
    random_seed=42,
):
    np.random.seed(random_seed)
    
    if start_time > end_time:
        raise ValueError("start_time cannot be after end_time")
    if step < 0:
        raise ValueError("step must be positive")

    timestamps = list(range(start_time, end_time, step))

    data = []
    for ts in timestamps:
        dt = datetime.utcfromtimestamp(ts / 1000).strftime("%Y-%m-%d %H:%M:%S.%f")
        sensor1 = math.sin(ts / 1000) + np.random.normal(0, 0.1)
        sensor2 = math.cos(ts / 1000) + np.random.normal(0, 0.1)
        sensor3 = math.tan(ts / 1000) + np.random.normal(0, 0.1)
        status = np.random.choice(sensor_statuses)
        row = [dt, sensor1, sensor2, sensor3, status]
        data.append(row)

    return pd.DataFrame(data, columns=columns)

class TestTaskFunc(unittest.TestCase):

    def test_output_type(self):
        df = task_func(0, 5000, 1000)
        self.assertIsInstance(df, pd.DataFrame)

    def test_column_names(self):
        df = task_func(0, 5000, 1000)
        expected_columns = ["Timestamp", "Sensor1", "Sensor2", "Sensor3", "SensorStatus"]
        self.assertListEqual(list(df.columns), expected_columns)

    def test_output_shape(self):
        df = task_func(0, 5000, 1000)
        expected_shape = (5, 5)  # Expected 5 rows and 5 columns
        self.assertEqual(df.shape, expected_shape)

    def test_timestamp_order(self):
        df = task_func(0, 5000, 1000)
        timestamps = pd.to_datetime(df['Timestamp'])
        self.assertTrue((timestamps.is_monotonic_increasing))

    def test_exceptions(self):
        with self.assertRaises(ValueError):
            task_func(5000, 2000, 1000)  # start_time > end_time
        with self.assertRaises(ValueError):
            task_func(0, 5000, -1000)  # step < 0

if __name__ == "__main__":
    unittest.main()