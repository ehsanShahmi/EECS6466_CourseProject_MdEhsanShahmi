import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import unittest

# Here is your prompt:
def task_func(df1, df2, features=["feature1", "feature2", "feature3"], target="target"):
    """
    Perform linear regression analysis with specified characteristics and targets.
    The function should merge two dataframes based on the 'id' column, perform
    linear regression using columns specified in features to predict the target,
    and plot the residuals.

    Parameters:
    - df1 (DataFrame): The first dataframe containing columns 'id' and the features specified.
    - df2 (DataFrame): The second dataframe containing columns 'id' and target.
    - features (list of str, optional): List of feature column names. Default is ['feature1', 'feature2', 'feature3'].
    - target (str, optional): Name of the target column. Default is 'target'.

    Returns:
    dict: A dictionary containing:
        - 'coefficients': Regression coefficients (list).
        - 'intercept': Regression intercept (float).
        - 'residuals_plot': A matplotlib Axes object representing the residuals plot, with the title 'Residuals Plot', x-axis label 'Predicted Values', and y-axis label 'Residuals'.

    Requirements:
    - pandas
    - sklearn.linear_model.LinearRegression
    - matplotlib.pyplot

    Example:
    >>> df1 = pd.DataFrame({'id': [1, 2, 3], 'feature1': [1.2, 3.4, 5.6], 'feature2': [2.3, 4.5, 6.7], 'feature3': [3.4, 5.6, 7.8]})
    >>> df2 = pd.DataFrame({'id': [1, 2, 3], 'target': [4.5, 6.7, 8.9]})
    >>> result = task_func(df1, df2)
    >>> result['coefficients']
    [0.3333333333333334, 0.33333333333333354, 0.3333333333333335]
    >>> type(result['residuals_plot'])
    <class 'matplotlib.axes._axes.Axes'>
    """

    df = pd.merge(df1, df2, on="id")
    X = df[features]
    y = df[target]
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    residuals = y - y_pred
    fig, ax = plt.subplots()
    ax.scatter(y_pred, residuals)  # scatter plot of residuals
    ax.axhline(y=0, color="r", linestyle="-")  # horizontal line at y=0
    ax.set_xlabel("Predicted Values")
    ax.set_ylabel("Residuals")
    ax.set_title("Residuals Plot")
    return {
        "coefficients": list(model.coef_),
        "intercept": model.intercept_,
        "residuals_plot": ax,
    }

# Test suite
class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.df1 = pd.DataFrame({
            'id': [1, 2, 3],
            'feature1': [1.2, 3.4, 5.6],
            'feature2': [2.3, 4.5, 6.7],
            'feature3': [3.4, 5.6, 7.8]
        })
        self.df2 = pd.DataFrame({
            'id': [1, 2, 3],
            'target': [4.5, 6.7, 8.9]
        })

    def test_coefficients_length(self):
        result = task_func(self.df1, self.df2)
        self.assertEqual(len(result['coefficients']), 3)

    def test_intercept_type(self):
        result = task_func(self.df1, self.df2)
        self.assertIsInstance(result['intercept'], float)

    def test_residuals_plot_type(self):
        result = task_func(self.df1, self.df2)
        self.assertIsInstance(result['residuals_plot'], plt.Axes)

    def test_features_default(self):
        result = task_func(self.df1, self.df2)
        self.assertEqual(result['coefficients'], [0.3333333333333334, 0.33333333333333354, 0.3333333333333335])

    def test_function_merges_dataframes(self):
        result = task_func(self.df1, self.df2)
        merged_df = pd.merge(self.df1, self.df2, on="id")
        self.assertEqual(len(merged_df), 3)

if __name__ == '__main__':
    unittest.main()