import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import unittest

# Provided prompt
def task_func(df):
    '''
    Processes a DataFrame containing dates and lists of numbers. It converts the lists into separate columns,
    performs Principal Component Analysis (PCA), and returns the explained variance ratio of the principal components
    along with a bar chart visualizing this ratio. Returns 0,0 if the input DataFrame is empty.

    Parameters:
    df (DataFrame): A pandas DataFrame with columns 'Date' and 'Value'. 'Date' is a date column, and 'Value' contains 
                    lists of numbers.

    Returns:
    tuple: (explained_variance_ratio, ax)
           explained_variance_ratio (ndarray): The explained variance ratio of the principal components.
           ax (Axes): The matplotlib Axes object for the variance ratio bar chart.

    Note:
    - The function use "Explained Variance Ratio of Principal Components" for the plot title.
    - The function use "Principal Component" and "Explained Variance Ratio" as the xlabel and ylabel respectively.
    
    Requirements:
    - pandas
    - sklearn.decomposition
    - matplotlib.pyplot

    Example:
    >>> df = pd.DataFrame([['2021-01-01', [8, 10, 12]], ['2021-01-02', [7, 9, 11]]], columns=['Date', 'Value'])
    >>> explained_variance_ratio, ax = task_func(df)
    >>> print(len(explained_variance_ratio))
    2
    '''

    # Data preparation

    if df.empty:
        return 0,0

    df['Date'] = pd.to_datetime(df['Date'])
    df = pd.concat([df['Date'], df['Value'].apply(pd.Series)], axis=1)
    
    # Performing PCA
    pca = PCA()
    pca.fit(df.iloc[:,1:])
    
    # Extracting explained variance ratio
    explained_variance_ratio = pca.explained_variance_ratio_
    
    # Creating bar chart
    fig, ax = plt.subplots()
    ax.bar(range(len(explained_variance_ratio)), explained_variance_ratio)
    ax.set_title('Explained Variance Ratio of Principal Components')
    ax.set_xlabel('Principal Component')
    ax.set_ylabel('Explained Variance Ratio')
    
    return explained_variance_ratio, ax

# Test suite
class TestTaskFunc(unittest.TestCase):

    def test_empty_dataframe(self):
        df = pd.DataFrame(columns=['Date', 'Value'])
        result = task_func(df)
        self.assertEqual(result, (0, 0))

    def test_single_row_input(self):
        df = pd.DataFrame([['2021-01-01', [1, 2, 3]]], columns=['Date', 'Value'])
        explained_variance_ratio, _ = task_func(df)
        self.assertEqual(len(explained_variance_ratio), 1)

    def test_multiple_rows_input(self):
        df = pd.DataFrame([
            ['2021-01-01', [1, 2, 3]],
            ['2021-01-02', [4, 5, 6]],
            ['2021-01-03', [7, 8, 9]]
        ], columns=['Date', 'Value'])
        explained_variance_ratio, _ = task_func(df)
        self.assertEqual(len(explained_variance_ratio), 3)

    def test_non_numeric_values(self):
        df = pd.DataFrame([
            ['2021-01-01', [1, 2, 'a']],
            ['2021-01-02', [4, 5, 6]],
        ], columns=['Date', 'Value'])
        with self.assertRaises(ValueError):
            task_func(df)

    def test_large_numbers(self):
        df = pd.DataFrame([
            ['2021-01-01', [10**6, 10**7, 10**8]],
            ['2021-01-02', [10**5, 10**6, 10**7]],
            ['2021-01-03', [10**4, 10**5, 10**6]]
        ], columns=['Date', 'Value'])
        explained_variance_ratio, _ = task_func(df)
        self.assertEqual(len(explained_variance_ratio), 3)


if __name__ == '__main__':
    unittest.main()