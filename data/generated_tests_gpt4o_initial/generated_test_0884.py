import pandas as pd
from scipy.stats import chi2_contingency
import unittest

def task_func(df, columns=['A', 'B', 'C'], larger=50, equal=900):
    """
    Filters a pandas DataFrame based on the values of specific rows, and performs
    a chi-square independence test on the first two columns.

    The function filters rows based on the following criteria:
        Keep only rows where:
            The value of the second column: df['second'] > larger
            and
            The value of the third column: df['third'] == equal
    
    After filtering a contingency table of the first two columns is computed,
    which is then used in the chi2 independence test. The p_value of the test
    is returned.        

    Parameters:
    df (pd.DataFrame): A DataFrame containing at least the columns specified in the 'columns' parameter.
    columns (list): A list of column names to consider for the operation, defaulting to ['A', 'B', 'C'].
                    The first column should contain categorical data, the second numerical data (used for filtering with values > 'larger'),
                    and the third numerical data (used for filtering with a fixed value of 'equal').
    larger (float, optional): Used for filtering rows against the second column where values > 'larger'.
                              Defaults to 50.
    equal (float, optional): Used for filtering rows against the third column where values == equal.
                             Defaults to 900.

    Returns:
    float: The p-value from the chi-square independence test, indicating the statistical significance.
           
    Raises:
    ValueError: If there's insufficient data for the test (no rows meeting the criteria).
    ValueError: If the number of specified columns is not 3.
    ValueError: If the specified columns are not contained in df.
    """

    if len(columns) != 3:
        raise ValueError("Exactly three columns should be specified.")
    
    for column in columns:
        if column not in df.columns:
            raise ValueError('The specified columns should exist in the DataFrame.')
    
    col_categorical, col_numerical, col_filter = columns

    # Filtering the data based on the specified conditions
    selected = df[(df[col_numerical] > larger) & (df[col_filter] == equal)][[col_categorical, col_numerical]]

    # Creating a contingency table for the chi-square test
    contingency_table = pd.crosstab(selected[col_categorical], selected[col_numerical])
    
    # Check if the contingency table is empty (no data meeting the criteria)
    if contingency_table.size == 0:
        raise ValueError("Insufficient data - no matching data for the applied conditions.")
    
    # Performing the chi-square test
    _, p_value, _, _ = chi2_contingency(contingency_table)
    
    return p_value

class TestTaskFunc(unittest.TestCase):

    def test_valid_input(self):
        df = pd.DataFrame({
            'A': ['Yes', 'No', 'Yes', 'No'],
            'B': [55, 70, 40, 85],
            'C': [900, 900, 800, 900]
        })
        result = task_func(df)
        self.assertAlmostEqual(result, 0.22313016014842973, places=8)

    def test_custom_columns(self):
        df = pd.DataFrame({
            'test': ['A', 'B', 'B', 'A', 'C', 'D'],
            'hi': [55, 70, 75, 85, 900, 100],
            'column3': [900, 900, 900, 900, 900, 900]
        })
        result = task_func(df, columns=['test', 'hi', 'column3'], larger=50, equal=900)
        self.assertAlmostEqual(result, 1.0, places=8)

    def test_insufficient_data(self):
        df = pd.DataFrame({
            'A': ['Yes', 'No'],
            'B': [10, 20],
            'C': [100, 100]
        })
        with self.assertRaises(ValueError) as context:
            task_func(df)
        self.assertEqual(str(context.exception), "Insufficient data - no matching data for the applied conditions.")

    def test_invalid_column_count(self):
        df = pd.DataFrame({
            'A': ['Yes', 'No'],
            'B': [55, 70],
            'C': [900, 900]
        })
        with self.assertRaises(ValueError) as context:
            task_func(df, columns=['A', 'B'])  # Only 2 columns provided
        self.assertEqual(str(context.exception), "Exactly three columns should be specified.")

    def test_column_not_in_dataframe(self):
        df = pd.DataFrame({
            'A': ['Yes', 'No', 'Yes'],
            'B': [70, 80, 60],
            'C': [900, 800, 900]
        })
        with self.assertRaises(ValueError) as context:
            task_func(df, columns=['A', 'D', 'C'])  # 'D' does not exist in df
        self.assertEqual(str(context.exception), "The specified columns should exist in the DataFrame.")

if __name__ == '__main__':
    unittest.main()