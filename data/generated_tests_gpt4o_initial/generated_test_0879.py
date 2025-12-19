import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import unittest

def task_func(data, col1, col2):
    """
    Perform a chi-square test of independence of variables in a contingency table.

    This function takes a DataFrame containing categorical data and two column names, then constructs a contingency table
    from the two categorical columns and performs a chi-square test of independence.
    It returns the p-value of the test, which indicates the probability of observing the
    data if the null hypothesis (independence of the variables) is true.

    Parameters:
    data (pd.DataFrame): A DataFrame containing the categorical variables.
    col1 (str): The name of the first categorical column in 'data'.
    col2 (str): The name of the second categorical column in 'data'.

    Returns:
    float: The p-value of the chi-square test of independence.

    Raises:
    ValueError: If 'data' is empty, if 'col1' or 'col2' are not in 'data', if one or both of the columns do not have multiple categories,
                or if some categories have less than 5 observations (violating the chi-square test assumptions).
    TypeError: If one or both of the columns contain non-categorical data.
    """

    # Check if DataFrame is empty
    if data.empty:
        raise ValueError("The input DataFrame is empty.")

    # Check if specified columns exist
    if col1 not in data or col2 not in data:
        raise ValueError(f"One or both of the columns '{col1}' and '{col2}' do not exist in the DataFrame.")

    # Check for non-categorical data (numerical values)
    if np.issubdtype(data[col1].dtype, np.number) or np.issubdtype(data[col2].dtype, np.number):
        raise TypeError("One or both of the columns contain non-categorical data. The chi-square test requires categorical data.")

    # Check for single category (no variability)
    if len(data[col1].unique()) < 2 or len(data[col2].unique()) < 2:
        raise ValueError("One or both of the columns do not have multiple categories. The chi-square test requires variability in data.")

    # Check for small counts in numerous categories
    contingency_table = pd.crosstab(data[col1], data[col2])
    if (contingency_table < 5).any().any():
        raise ValueError("Some categories have less than 5 observations. This violates the assumptions of the chi-square test.")

    # Perform the chi-square test
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    return p


class TestChiSquareTest(unittest.TestCase):

    def test_empty_dataframe(self):
        """ Test with an empty DataFrame. """
        with self.assertRaises(ValueError):
            data = pd.DataFrame()
            task_func(data, 'A', 'B')

    def test_columns_not_in_dataframe(self):
        """ Test with columns not present in the DataFrame. """
        data = pd.DataFrame({'A': ['a', 'b', 'a', 'b'], 'B': ['x', 'y', 'x', 'y']})
        with self.assertRaises(ValueError):
            task_func(data, 'A', 'C')

    def test_single_category_in_columns(self):
        """ Test with one column having a single category. """
        data = pd.DataFrame({'A': ['a'] * 10, 'B': ['x', 'y'] * 5})
        with self.assertRaises(ValueError):
            task_func(data, 'A', 'B')

    def test_non_categorical_data(self):
        """ Test with non-categorical data in one column. """
        data = pd.DataFrame({'A': ['a', 'b', 'a', 'b'], 'B': [1, 2, 1, 2]})
        with self.assertRaises(TypeError):
            task_func(data, 'A', 'B')

    def test_small_counts_in_categories(self):
        """ Test with small counts in categories. """
        data = pd.DataFrame({'A': ['a', 'a', 'b', 'b'], 'B': ['x', 'y', 'x', 'y']})
        with self.assertRaises(ValueError):
            task_func(data, 'A', 'B')


if __name__ == '__main__':
    unittest.main()