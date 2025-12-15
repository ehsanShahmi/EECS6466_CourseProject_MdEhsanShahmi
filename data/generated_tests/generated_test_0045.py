import pandas as pd
import numpy as np
import unittest
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df: pd.DataFrame):
    """
    Perform PCA on a DataFrame (excluding non-numeric columns) and draw a scatter plot of the first two main components. The principal columns should be name 'Component 1' and 'Component 2'.
    Missing values are replaced by column's average.

    Parameters:
    df (DataFrame): The pandas DataFrame.

    Returns:
    DataFrame: A pandas DataFrame with the first two principal components. The columns should be 'principal component 1' and 'principal component 2'.
    Axes: A matplotlib Axes object representing the scatter plot. The xlabel should be 'principal component' and the ylabel 'principal component 2'.

    Requirements:
    - pandas
    - numpy
    - sklearn.decomposition.PCA
    - seaborn
    - matplotlib

    Example:
    >>> df = pd.DataFrame([[1,2,3],[4,5,6],[7.0,np.nan,9.0]], columns=["c1","c2","c3"])
    >>> principalDf, ax = task_func(df)
    >>> print(principalDf)
       Component 1  Component 2
    0     4.450915    -0.662840
    1    -0.286236     1.472436
    2    -4.164679    -0.809596
    """
    # Implementation of the task_func as provided.
    df_numeric = df.select_dtypes(include=[np.number])
    df_numeric = df_numeric.fillna(df_numeric.mean(axis=0))
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(df_numeric)
    principalDf = pd.DataFrame(
        data=principalComponents,
        columns=["Component 1", "Component 2"],
    )
    ax = sns.scatterplot(data=principalDf, x="Component 1", y="Component 2")
    plt.show()
    return principalDf, ax

class TestTaskFunc(unittest.TestCase):

    def test_pca_output_shape(self):
        df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7.0, np.nan, 9.0]], columns=["c1", "c2", "c3"])
        principalDf, _ = task_func(df)
        self.assertEqual(principalDf.shape, (3, 2), "Output DataFrame should have shape (3, 2)")

    def test_pca_column_names(self):
        df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7.0, np.nan, 9.0]], columns=["c1", "c2", "c3"])
        principalDf, _ = task_func(df)
        self.assertListEqual(list(principalDf.columns), ["Component 1", "Component 2"], 
                             "Output DataFrame should have columns named 'Component 1' and 'Component 2'")

    def test_nan_replacement(self):
        df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7.0, np.nan, 9.0]], columns=["c1", "c2", "c3"])
        principalDf, _ = task_func(df)
        self.assertTrue(principalDf["Component 1"].isnull().sum() == 0, 
                        "Component 1 should not contain NaN values")
        self.assertTrue(principalDf["Component 2"].isnull().sum() == 0, 
                        "Component 2 should not contain NaN values")
    
    def test_plot_output(self):
        df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7.0, np.nan, 9.0]], columns=["c1", "c2", "c3"])
        _, ax = task_func(df)
        self.assertIsNotNone(ax, "The plot axis should not be None")

    def test_pca_for_identical_rows(self):
        df = pd.DataFrame([[1, 1, 1], [1, 1, 1], [1, 1, 1]], columns=["c1", "c2", "c3"])
        principalDf, _ = task_func(df)
        expected_values = 0
        self.assertTrue(np.all(principalDf == expected_values), "PCA of identical rows should have all components as zero")

if __name__ == '__main__':
    unittest.main()