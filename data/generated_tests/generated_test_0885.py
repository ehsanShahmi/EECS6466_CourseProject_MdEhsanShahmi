import pandas as pd
import numpy as np
import unittest
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Here is your prompt:
def task_func(df, col_a='A', col_b='B', col_c='C', seed=None):
    """
    This function filters rows from the input DataFrame 'df' based on conditions in columns 'B' and 'C', 
    then uses linear regression to predict values in column 'B' using data from column 'A'. 
    Specifically, it selects rows where column 'B' values are greater than 50 and column 'C' values equal 900.
    
    A train test split of the remaining data is performed, where the test_size = 0.2
    and col_a is used as X value and col_b is used as Y values / target.

    This data is used to train a LinearRegression model. 

    The test split is used to generate predictions for col_b. These predictions
    are returned as well as the trained model.

    If df is empty or empty after the filtering, None is returned.
    If df does contain non numeric data None is returned.
    If the specified columns are not contained in df, None is returned.

    Parameters:
    df (DataFrame): The input pandas DataFrame with numeric data.
    col_a (str): The name of the first column to use for prediction (default is 'A').
    col_b (str): The name of the second column, the values of which are to be predicted (default is 'B').
    col_c (str): The name of the third column to use for row selection (default is 'C').
    seed (int, optional): random seed for the train test split. Default is None.

    Returns:
    ndarray: The predicted values for the filtered rows in column 'B', or None if input is invalid.
    LinearRegression: The trained linear regression model is returned, if 
    
    Requirements:
    - pandas
    - sklearn.model_selection
    - sklearn.linear_model

    Example:
    >>> np.random.seed(32)
    >>> df = pd.DataFrame({'A': np.random.randint(0, 100, 1000),
    ...                    'B': np.random.randint(0, 100, 1000),
    ...                    'C': np.random.choice([900, 800, 700, 600], 1000)})
    >>> predictions, model = task_func(df, seed=1)
    >>> print(predictions)
    [77.21974339 76.26960987 76.34878767 77.16695819 76.53353585 76.86344332
     76.86344332 77.19335079 76.81065812 76.77106923 76.79746183 77.0481915
     76.23002098 76.63910624 77.114173   76.04527279 77.0217989  76.0188802
     77.18015449 76.91622851 76.62590994 76.90303222 76.75787293 77.29892118
     77.18015449 76.07166539 76.04527279 76.88983592]
    >>> print(model)
    LinearRegression()

    >>> df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
    ...                    'B': [10, 80, 80, 80, 80],
    ...                    'C': [900, 900, 900, 900, 900]})
    >>> predictions, model = task_func(df, seed=12)
    >>> print(predictions) 
    [80.]
    >>> print(model)
    LinearRegression()
    """

    # Validating the input dataframe
    if df.empty or not all(col in df for col in [col_a, col_b, col_c]):
        return None  # Invalid input scenario
    
    try:
        # Ensuring the columns contain numeric data
        df[[col_a, col_b, col_c]] = df[[col_a, col_b, col_c]].apply(pd.to_numeric, errors='raise')
    except ValueError:
        return None  # Non-numeric data encountered

    # Filtering the data based on the conditions
    selected = df[(df[col_b] > 50) & (df[col_c] == 900)][[col_a, col_b]]

    if selected.empty:
        return None
    
    # Preparing the data for linear regression
    X_train, X_test, y_train, _ = train_test_split(selected[col_a].values.reshape(-1, 1),
                                                   selected[col_b].values,
                                                   test_size=0.2,
                                                   random_state=seed)

    # Applying linear regression
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    return predictions, model

# Test Suite
class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Create a sample DataFrame for testing
        np.random.seed(42)
        self.df = pd.DataFrame({
            'A': np.random.randint(0, 100, 100),
            'B': np.random.randint(0, 100, 100),
            'C': np.random.choice([900, 800], 100)
        })

    def test_valid_prediction(self):
        self.df.loc[self.df.index[:20], 'B'] = np.random.randint(51, 100, 20)  # Ensure some B values are > 50
        self.df.loc[self.df.index[:20], 'C'] = 900  # Ensure C values are 900
        predictions, model = task_func(self.df)
        self.assertIsNotNone(predictions)
        self.assertIsInstance(model, LinearRegression)

    def test_empty_dataframe(self):
        df_empty = pd.DataFrame(columns=['A', 'B', 'C'])
        result = task_func(df_empty)
        self.assertIsNone(result)

    def test_non_numeric_data(self):
        self.df.loc[0, 'A'] = 'non_numeric'  # Introduce non-numeric value
        result = task_func(self.df)
        self.assertIsNone(result)

    def test_incomplete_columns(self):
        df_incomplete = pd.DataFrame({
            'A': np.random.randint(0, 100, 100),
            'B': np.random.randint(0, 100, 100)
            # Missing column 'C'
        })
        result = task_func(df_incomplete)
        self.assertIsNone(result)

    def test_no_rows_meeting_criteria(self):
        self.df['B'] = [40]*100  # Set all B values to < 50
        self.df['C'] = [900]*100  # Set all C values to 900
        result = task_func(self.df)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()