import pandas as pd
import unittest
from statsmodels.tsa.seasonal import seasonal_decompose
from your_module import task_func  # Replace 'your_module' with the appropriate module name where task_func is defined.

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.valid_data = pd.DataFrame({
            "group": ["A"] * 14,
            "date": pd.to_datetime(["2022-01-01", "2022-01-02", "2022-01-03", "2022-01-04", 
                                    "2022-01-05", "2022-01-06", "2022-01-07", "2022-01-08",
                                    "2022-01-09", "2022-01-10", "2022-01-11", "2022-01-12", 
                                    "2022-01-13", "2022-01-14"]),
            "value": [10, 12, 13, 15, 17, 16, 14, 13, 12, 15, 17, 18, 20, 19],
        })
        
    def test_valid_input(self):
        result, ax = task_func(self.valid_data, freq='D', decomposition_model='multiplicative')
        self.assertIsInstance(result, seasonal_decompose)
        self.assertIsNotNone(ax)

    def test_invalid_dataframe(self):
        with self.assertRaises(ValueError):
            task_func("not_a_dataframe", freq='D', decomposition_model='multiplicative')
    
    def test_missing_columns(self):
        invalid_data = pd.DataFrame({
            "group": ["A"] * 14,
            "date": pd.to_datetime(["2022-01-01"] * 14)
        })  # 'value' column is missing
        with self.assertRaises(ValueError):
            task_func(invalid_data, freq='D', decomposition_model='multiplicative')

    def test_invalid_freq(self):
        with self.assertRaises(ValueError):
            task_func(self.valid_data, freq=123, decomposition_model='multiplicative')

    def test_invalid_decomposition_model(self):
        with self.assertRaises(ValueError):
            task_func(self.valid_data, freq='D', decomposition_model='invalid_model')

if __name__ == '__main__':
    unittest.main()