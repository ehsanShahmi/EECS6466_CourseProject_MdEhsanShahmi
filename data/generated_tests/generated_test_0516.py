import pandas as pd
import numpy as np
import statsmodels.api as sm
import unittest

def task_func(
    array: list, random_seed: int = 0
) -> (pd.DataFrame, sm.regression.linear_model.RegressionResultsWrapper):
    """
    Generate a Pandas DataFrame from a 2D list and perform a multiple linear regression.

    The function first validates the input list, creates a DataFrame, separates independent and dependent variables,
    adds a constant to the model, and fits a linear regression using statsmodels.

    Parameters:
    - array (list of list of int): A 2D list where each sub-list represents a row of data.
                                   Each sub-list should have exactly 5 elements, where the first 4 elements are
                                   treated as independent variables ('A', 'B', 'C', 'D') and the last element is
                                   the dependent (Response) variable.

    - random_seed (int): A seed for reproducibility in numpy for statsmodels. Defaults to 0.

    Returns:
    - df (pd.DataFrame): DataFrame with columns 'A', 'B', 'C', 'D', 'Response'.
    - results (statsmodels.RegressionResults): Results of the linear regression.

    Requirements:
    - pandas
    - numpy
    - statsmodels.api.sm

    Example:
    >>> df, results = task_func([[1,2,3,4,5], [6,7,8,9,10]])
    >>> print(df)
       A  B  C  D  Response
    0  1  2  3  4         5
    1  6  7  8  9        10
    """

    COLUMNS = ["A", "B", "C", "D", "Response"]

    np.random.seed(random_seed)

    if not all(len(row) == len(COLUMNS) for row in array):
        raise ValueError(
            "Each sub-list in the input 2D list must have exactly 5 elements."
        )

    df = pd.DataFrame(array, columns=COLUMNS)
    X = df[COLUMNS[:-1]]
    y = df["Response"]
    X = sm.add_constant(X)

    model = sm.OLS(y, X)
    results = model.fit()

    return df, results

class TestTaskFunc(unittest.TestCase):

    def test_valid_input(self):
        array = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
        df, results = task_func(array)
        self.assertEqual(df.shape, (2, 5))
        self.assertAlmostEqual(results.params['const'], 0.0, delta=0.1)

    def test_incorrect_length_input(self):
        array = [[1, 2, 3, 4]]
        with self.assertRaises(ValueError):
            task_func(array)

    def test_empty_input(self):
        array = []
        with self.assertRaises(ValueError):
            task_func(array)

    def test_non_numeric_input(self):
        array = [[1, 2, 3, "4", 5]]
        with self.assertRaises(ValueError):
            task_func(array)

    def test_with_random_seed(self):
        array = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
        df_1, results_1 = task_func(array, random_seed=5)
        df_2, results_2 = task_func(array, random_seed=5)
        self.assertTrue(np.array_equal(df_1, df_2))
        self.assertAlmostEqual(results_1.rsquared, results_2.rsquared)

if __name__ == '__main__':
    unittest.main()