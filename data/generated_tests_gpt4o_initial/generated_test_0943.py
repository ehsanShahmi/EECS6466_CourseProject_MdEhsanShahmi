import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
import unittest

def task_func(start_date='2016-01-01', periods=24, freq='M', model='additive'):
    """
    Generate a sales time-series and decompose it into trend, seasonal, and residual components.
    
    Parameters:
    - start_date (str): The start date of the time-series in the format 'YYYY-MM-DD'. Default is '2016-01-01'.
    - periods (int): The number of periods to generate for the time-series. Default is 24.
    - freq (str): The frequency of the time-series data. Default is 'M' (Monthly End).
    - model (str): The type of seasonal decomposition ('additive' or 'multiplicative'). Default is 'additive'.

    Returns:
    - A dictionary containing 'trend', 'seasonal', and 'residual' components as Pandas Series.
    
    Requirements:
    - numpy
    - pandas
    - statsmodels
    
    Examples:
    >>> result = task_func('2016-01-01', 24, 'M')
    >>> all(key in result for key in ['trend', 'seasonal', 'residual'])
    True

    >>> result = task_func('2020-01-01', 24, 'M', 'multiplicative')
    >>> len(result['seasonal'])
    24
    """

    date_range = pd.date_range(start=start_date, periods=periods, freq=freq)
    sales_data = np.random.randint(low=100, high=500, size=periods)
    sales_series = pd.Series(sales_data, index=date_range)
    try:
        decomposition = seasonal_decompose(sales_series, model=model, period=12 if freq == 'M' else 4)
    except ValueError as e:
        return {'error': str(e)}
    
    return {
        'trend': decomposition.trend,
        'seasonal': decomposition.seasonal,
        'residual': decomposition.resid
    }

class TestTaskFunc(unittest.TestCase):

    def test_default_parameters(self):
        result = task_func()
        self.assertTrue(all(key in result for key in ['trend', 'seasonal', 'residual']))

    def test_custom_start_date(self):
        result = task_func(start_date='2020-01-01')
        self.assertEqual(len(result['seasonal']), 24)

    def test_multiplicative_model(self):
        result = task_func(model='multiplicative')
        self.assertTrue(all(key in result for key in ['trend', 'seasonal', 'residual']))

    def test_periods_length(self):
        result = task_func(periods=36)
        self.assertEqual(len(result['seasonal']), 36)

    def test_invalid_model(self):
        result = task_func(model='invalid_model')
        self.assertIn('error', result)

if __name__ == '__main__':
    unittest.main()