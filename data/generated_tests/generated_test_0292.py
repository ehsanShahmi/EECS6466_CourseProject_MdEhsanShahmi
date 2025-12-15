import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import unittest

# Here is your prompt:
"""
def task_func(df):
    """
    Scale the 'Age' and 'Income' columns between 0 and 1 for each group by 'id' in the provided pandas DataFrame. 
    Additionally, create a histogram of the 'Income' column after scaling and return both the scaled DataFrame 
    and the histogram data.

    Parameters:
    df (DataFrame): The pandas DataFrame with columns ['id', 'age', 'income'].

    Returns:
    tuple: A tuple containing the scaled DataFrame and the histogram data for the 'income' column.

    Requirements:
    - pandas
    - sklearn.preprocessing.MinMaxScaler
    - numpy

    Example:
    >>> df = pd.DataFrame({'id': [1, 1, 2, 2, 3, 3], 'age': [25, 26, 35, 36, 28, 29],'income': [50000, 60000, 70000, 80000, 90000, 100000]})
    >>> df_scaled, income_hist = task_func(df)
    >>> print(df_scaled.iloc[0]['age'])
    0.0
    >>> print(df_scaled.iloc[0]['income'])
    0.0
    """
    
    scaler = MinMaxScaler(feature_range=(0, 1))
    #Scaling the 'age' and 'income' columns
    df_grouped = df.groupby('id').apply(
        lambda x: pd.DataFrame(
            scaler.fit_transform(x[['age', 'income']]), 
            columns=['age', 'income'], 
            index=x.index
        )
    )

    # Creating a histogram of the 'income' column
    hist, bins = np.histogram(df_grouped['income'], bins=10)

    return df_grouped, (hist, bins)
"""

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'id': [1, 1, 2, 2, 3, 3],
            'age': [25, 26, 35, 36, 28, 29],
            'income': [50000, 60000, 70000, 80000, 90000, 100000]
        })

    def test_scaling_range(self):
        df_scaled, _ = task_func(self.df)
        # Check if scaled values are between 0 and 1
        self.assertTrue((df_scaled['age'] >= 0).all() and (df_scaled['age'] <= 1).all())
        self.assertTrue((df_scaled['income'] >= 0).all() and (df_scaled['income'] <= 1).all())

    def test_histogram_length(self):
        _, income_hist = task_func(self.df)
        hist, _ = income_hist
        # Check if histogram has 10 bins
        self.assertEqual(len(hist), 10)

    def test_group_scaling(self):
        df_scaled, _ = task_func(self.df)
        # Check if scaling is based on groups
        group_1 = df_scaled.loc[df_scaled.index.get_level_values('id') == 1]
        group_2 = df_scaled.loc[df_scaled.index.get_level_values('id') == 2]
        # Ensure age and income are scaled properly within each group
        self.assertTrue(group_1['age'].iloc[0] < group_1['age'].iloc[1])  # age should increase
        self.assertTrue(group_2['income'].iloc[0] < group_2['income'].iloc[1])  # income should increase

    def test_output_type(self):
        df_scaled, income_hist = task_func(self.df)
        self.assertIsInstance(df_scaled, pd.DataFrame)
        self.assertIsInstance(income_hist, tuple)
        self.assertEqual(len(income_hist), 2)

    def test_exclusion_of_unnecessary_columns(self):
        df_scaled, _ = task_func(self.df)
        # Ensure only 'age' and 'income' are in the result
        self.assertIn('age', df_scaled.columns)
        self.assertIn('income', df_scaled.columns)
        self.assertNotIn('id', df_scaled.columns)

if __name__ == '__main__':
    unittest.main()