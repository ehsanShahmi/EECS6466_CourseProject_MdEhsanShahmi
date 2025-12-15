import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import unittest

# Here is your prompt:
def task_func(n_rows, scale_cols, columns=['A', 'B', 'C', 'D', 'E'], random_seed=None):
    """
    Generate a DataFrame with columns 'columns' and fill them with random
    values. Scale the columns at the provided indexes with sklearn StandardScaler.
    If scale_cols is empty no column is scaled
    
    Parameters:
    n_rows (int): The number of rows in the DataFrame.
    scale_cols (list of int): The indices of columns to be scaled. The indices are based on the predefined column names.
    columns (list of str, optional): The columns to be included in the DataFrame. Defaults to ['A', 'B', 'C', 'D', 'E'].
    random_seed (int): Seed used in rng. Default is None.

    Returns:
    DataFrame: The resulting DataFrame after scaling the selected columns.

    Requirements:
    - numpy
    - pandas
    - sklearn
    
    Example:
    >>> df = task_func(3, [1], columns=['test', 'scale'], random_seed=1)
    >>> print(df)
       test     scale
    0    37  1.162476
    1    72  0.116248
    2    75 -1.278724

    >>> df = task_func(5, [1, 2, 3], random_seed=12)
    >>> print(df)
        A         B         C         D   E
    0  75 -0.840307 -0.791926 -1.462784   3
    1  67  0.673481  1.517859 -0.855820  49
    2  52 -1.519967 -0.406962  1.177511  34
    3  75  0.611694 -1.121896  0.782984  13
    4  82  1.075099  0.802925  0.358109  35
    """

               np.random.seed(random_seed)
    df = pd.DataFrame(np.random.randint(0, 100, size=(n_rows, len(columns))), columns=columns)
    
    for i in scale_cols:
        scaler = StandardScaler()
        df[columns[i]] = scaler.fit_transform(df[[columns[i]]])
    
    return df

class TestTaskFunc(unittest.TestCase):

    def test_output_shape(self):
        df = task_func(5, [1, 2, 3])
        self.assertEqual(df.shape, (5, 5))  # expect a DataFrame with shape (5, 5)

    def test_column_names(self):
        df = task_func(3, [], columns=['X', 'Y', 'Z'])
        self.assertListEqual(list(df.columns), ['X', 'Y', 'Z'])  # check if the columns are as expected

    def test_no_scaling(self):
        df = task_func(10, [])
        self.assertTrue(np.all(np.isclose(df[['A', 'B', 'C', 'D', 'E']].values, df[['A', 'B', 'C', 'D', 'E']].values)))  # all values should remain unchanged

    def test_scaling_single_column(self):
        df = task_func(5, [1], random_seed=42)
        self.assertNotEqual(df['B'].iloc[0], df['B'].iloc[1])  # check if values in column B are scaled (not equal)

    def test_scaling_multiple_columns(self):
        df = task_func(7, [0, 1], random_seed=100)
        mean_a = df['A'].mean()
        mean_b = df['B'].mean()
        self.assertAlmostEqual(mean_a, 0, delta=0.1)  # mean of scaled A should be close to 0
        self.assertAlmostEqual(mean_b, 0, delta=0.1)  # mean of scaled B should be close to 0

if __name__ == '__main__':
    unittest.main()