import json
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import unittest

def task_func(json_data: str, data_key: str):
    # The implementation of the function should not be modified
    
    data = json.loads(json_data)
    try:
        for key in data_key.split("."):
            data = data[key]
        values = pd.Series(data, dtype=pd.Float64Dtype)
    except KeyError:
        raise KeyError(f"Key path '{data_key}' not found in the provided JSON data.")

    if values.empty:
        return values, None, None

    scaler = MinMaxScaler()
    normalized_values = pd.Series(
        scaler.fit_transform(values.values.reshape(-1, 1)).flatten(),
        dtype=pd.Float64Dtype,
    )

    fig, ax = plt.subplots()
    ax.plot(values, label="Original Data")
    ax.plot(normalized_values, label="Normalized Data")
    ax.set_title("Comparison of Original and Normalized Data")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.legend()

    return values, normalized_values, ax

class TestTaskFunction(unittest.TestCase):

    def test_valid_json_data(self):
        json_str = '{"data": {"values": [5, 10, 15, 20, 25]}}'
        original_data, normalized_data, ax = task_func(json_str, 'data.values')
        self.assertIsInstance(original_data, pd.Series)
        self.assertIsInstance(normalized_data, pd.Series)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(original_data), 5)
        self.assertEqual(len(normalized_data), 5)

    def test_empty_data(self):
        json_str = '{"data": {"values": []}}'
        original_data, normalized_data, ax = task_func(json_str, 'data.values')
        self.assertIsInstance(original_data, pd.Series)
        self.assertTrue(original_data.empty)
        self.assertIsNone(normalized_data)
        self.assertIsNone(ax)

    def test_invalid_key_path(self):
        json_str = '{"data": {"values": [5, 10, 15, 20, 25]}}'
        with self.assertRaises(KeyError):
            task_func(json_str, 'data.non_existent_key')

    def test_non_numeric_data(self):
        json_str = '{"data": {"values": ["a", "b", "c"]}}'
        with self.assertRaises(ValueError):
            task_func(json_str, 'data.values')

    def test_small_numeric_data(self):
        json_str = '{"data": {"values": [0, 1]}}'
        original_data, normalized_data, ax = task_func(json_str, 'data.values')
        self.assertIsInstance(original_data, pd.Series)
        self.assertIsInstance(normalized_data, pd.Series)
        self.assertEqual(normalized_data.iloc[0], 0.0)
        self.assertEqual(normalized_data.iloc[1], 1.0)

if __name__ == '__main__':
    unittest.main()