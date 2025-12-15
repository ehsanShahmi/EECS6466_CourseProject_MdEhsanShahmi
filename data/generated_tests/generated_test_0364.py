import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import unittest
import numpy as np

# Here is your prompt with the provided task function.
# Constants
FEATURES = ['feature '+str(i) for i in range(1, 11)]
TARGET = 'target'

def task_func(df):
    """
    Train a linear regression model on a given DataFrame.
    
    Parameters:
    df (DataFrame): The DataFrame with features and target.
    
    Returns:
    LinearRegression: The trained linear regression model.
    
    Requirements:
    - pandas
    - sklearn.model_selection.train_test_split
    - sklearn.linear_model.LinearRegression
    
    Raises:
    - The function will raise a ValueError is input df is not a DataFrame.

    Example:
    >>> import numpy as np
    >>> np.random.seed(0)
    >>> df = pd.DataFrame({'feature ' + str(i): np.random.rand(100) for i in range(1, 11)})
    >>> df['target'] = df.apply(lambda row: sum(row), axis=1)
    >>> model = task_func(df)
    >>> print(len(model.coef_))
    10
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input df is not a DataFrame")
    
    X = df[FEATURES]
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    return model

class TestTaskFunction(unittest.TestCase):
    
    def setUp(self):
        np.random.seed(0)
        self.df_valid = pd.DataFrame({
            'feature ' + str(i): np.random.rand(100) for i in range(1, 11)
        })
        self.df_valid['target'] = self.df_valid.sum(axis=1)

    def test_valid_dataframe(self):
        model = task_func(self.df_valid)
        self.assertIsInstance(model, LinearRegression)
        self.assertEqual(len(model.coef_), 10)

    def test_invalid_dataframe_type(self):
        with self.assertRaises(ValueError):
            task_func("Not a DataFrame")

    def test_empty_dataframe(self):
        df_empty = pd.DataFrame(columns=FEATURES + [TARGET])
        with self.assertRaises(ValueError):
            task_func(df_empty)

    def test_dataframe_with_nan(self):
        df_nan = self.df_valid.copy()
        df_nan.iloc[0, 0] = np.nan
        with self.assertRaises(ValueError):
            task_func(df_nan)

    def test_dataframe_feature_target_length_mismatch(self):
        df_mismatch = pd.DataFrame({
            'feature ' + str(i): np.random.rand(50) for i in range(1, 11)
        })
        df_mismatch['target'] = np.random.rand(50)
        with self.assertRaises(ValueError):
            task_func(df_mismatch)

if __name__ == '__main__':
    unittest.main()