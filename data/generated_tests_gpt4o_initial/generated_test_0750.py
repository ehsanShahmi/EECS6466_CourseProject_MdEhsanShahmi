import unittest
import pandas as pd
import statsmodels.api as sm

# Here is your prompt:
def task_func(df: pd.DataFrame, height: int, weight: int, columns: list) -> sm.regression.linear_model.RegressionResultsWrapper:
    """
    Performs an OLS linear regression on a subset of the provided DataFrame. The subset is created by filtering rows 
    where the value in the second column of 'columns' is greater than 'height' and the value in the third column is 
    less than 'weight'. The first column in 'columns' is used as the dependent variable / target (y), and the rest as independent 
    variables (X) in the regression.

    If df is empty, or if no rows match the conditions None is returned.


    Parameters:
    - df (pd.DataFrame): The DataFrame to analyze.
    - height (int): The threshold to filter rows based on the second column in 'columns'.
    - weight (int): The threshold to filter rows based on the third column in 'columns'.
    - columns (list of str): A list of column names to use, where the first is the dependent variable.

    Returns:
    - sm.regression.linear_model.RegressionResultsWrapper: The result of the OLS regression, or None if no rows meet the criteria or DataFrame is empty.

    Requirements:
    - pandas
    - statsmodels

    Example:
    >>> df = pd.DataFrame({'Age': [30, 40], 'Height': [60, 70], 'Weight': [100, 150]})
    >>> model = task_func(df, 50, 120, ['Age', 'Height', 'Weight'])

    >>> df = pd.DataFrame(np.random.randint(10,98,size=(100, 3)), columns=['Age', 'Height', 'Weight'])
    >>> model = task_func(df, 45, 72, columns=['Age', 'Height', 'Weight'])

    """
    # Check for empty DataFrame
    if df.empty:
        return None

    # Filter the DataFrame based on provided column names
    selected_df = df[(df[columns[1]] > height) & (df[columns[2]] < weight)]

    # If no rows match the condition, return None
    if selected_df.empty:
        return None
    
    X = selected_df[columns[1:]]
    y = selected_df[columns[0]]
    X = sm.add_constant(X)
    model = sm.OLS(y, X)
    results = model.fit()
    return results

class TestTaskFunc(unittest.TestCase):
    
    def test_empty_dataframe(self):
        df = pd.DataFrame()
        result = task_func(df, 50, 120, ['Age', 'Height', 'Weight'])
        self.assertIsNone(result, "Expected None for empty DataFrame")
        
    def test_no_matching_rows(self):
        df = pd.DataFrame({'Age': [30, 40], 'Height': [60, 70], 'Weight': [100, 150]})
        result = task_func(df, 80, 200, ['Age', 'Height', 'Weight'])
        self.assertIsNone(result, "Expected None when no rows match conditions")

    def test_one_matching_row(self):
        df = pd.DataFrame({'Age': [30, 40, 50], 'Height': [60, 80, 70], 'Weight': [100, 150, 110]})
        result = task_func(df, 65, 120, ['Age', 'Height', 'Weight'])
        self.assertIsInstance(result, sm.regression.linear_model.RegressionResultsWrapper, 
                              "Expected RegressionResultsWrapper for one matching row")

    def test_multiple_matching_rows(self):
        df = pd.DataFrame({'Age': [30, 40, 50, 60], 'Height': [70, 75, 80, 85], 'Weight': [100, 150, 90, 110]})
        result = task_func(df, 65, 120, ['Age', 'Height', 'Weight'])
        self.assertIsInstance(result, sm.regression.linear_model.RegressionResultsWrapper, 
                              "Expected RegressionResultsWrapper for multiple matching rows")

    def test_various_inputs(self):
        df = pd.DataFrame({'Age': [25, 35, 45, 55], 'Height': [55, 65, 75, 85], 'Weight': [60, 70, 80, 90]})
        result = task_func(df, 60, 85, ['Age', 'Height', 'Weight'])
        self.assertIsInstance(result, sm.regression.linear_model.RegressionResultsWrapper, 
                              "Expected RegressionResultsWrapper for varied inputs that match conditions")


if __name__ == "__main__":
    unittest.main()