import pandas as pd
import seaborn as sns
import unittest
import matplotlib.pyplot as plt

# Constants
COLUMNS = ['col1', 'col2', 'col3']

def task_func(data):
    """
    You are given a list of elements. Each element of the list is a list of 3 values. Use this list of elements to build a dataframe with 3 columns 'col1', 'col2' and 'col3' and create a distribution of chart of the different values of "col3" grouped by "col1" and "col2" using seaborn.

    The function's logic is as follows:
    1. Build a pandas DataFrame by using list of elements. Make sure to name the columns as 'col1', 'col2' and 'col3', the constant COLUMNS is provided for this purpose.
    2. Create a new dataframe by grouping the values in the column 'col3' by ['col1', 'col2'].
    3. Reset the index of the newly created dataframe. This dataframe is the first element of the output tuple.
    4. Create a distribution plot of the 'col3' column of the previous dataframe using seaborn. This plot is the second and last element of the output tuple.
        - The xlabel (label for the x-axis) is set to the 'col3'.

    Parameters:
    data (list): The DataFrame to be visualized.

    Returns:
    tuple:
        pandas.DataFrame: The DataFrame of the analyzed data.
        plt.Axes: The seaborn plot object.

    Requirements:
    - pandas
    - seaborn
    """
    df = pd.DataFrame(data, columns=COLUMNS)
    analyzed_df = df.groupby(COLUMNS[:-1])[COLUMNS[-1]].nunique().reset_index()
    ax = sns.histplot(analyzed_df[COLUMNS[-1]], kde=True)

    return analyzed_df, ax

class TestTaskFunc(unittest.TestCase):
    
    def test_empty_data(self):
        data = []
        analyzed_df, plot = task_func(data)
        self.assertEqual(analyzed_df.shape[0], 0)
    
    def test_single_row_data(self):
        data = [[1, 1, 1]]
        analyzed_df, plot = task_func(data)
        self.assertEqual(analyzed_df.shape[0], 1)
        self.assertEqual(analyzed_df.iloc[0]['col3'], 1)
    
    def test_multiple_rows_same_group(self):
        data = [[1, 1, 1], [1, 1, 2]]
        analyzed_df, plot = task_func(data)
        self.assertEqual(analyzed_df.shape[0], 1)
        self.assertEqual(analyzed_df.iloc[0]['col3'], 2)
    
    def test_multiple_groups(self):
        data = [[1, 1, 1], [1, 2, 2], [2, 1, 3], [2, 2, 4]]
        analyzed_df, plot = task_func(data)
        self.assertEqual(analyzed_df.shape[0], 4)
    
    def test_identical_rows(self):
        data = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
        analyzed_df, plot = task_func(data)
        self.assertEqual(analyzed_df.shape[0], 1)
        self.assertEqual(analyzed_df.iloc[0]['col3'], 1)

if __name__ == '__main__':
    unittest.main()