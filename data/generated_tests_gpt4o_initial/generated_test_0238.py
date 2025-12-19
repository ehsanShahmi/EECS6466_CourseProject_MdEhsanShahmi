import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# The provided prompt
def task_func(df):
    """
    Standardize 'Age' and 'Score' columns in a pandas DataFrame, remove duplicate entries based on 'Name', and plot a scatter plot of these standardized values.

    Parameters:
    df (pandas.DataFrame): DataFrame containing 'Name', 'Age', and 'Score' columns.

    Returns:
    pandas.DataFrame: DataFrame with standardized 'Age' and 'Score', duplicates removed.
    matplotlib.axes.Axes: Axes object of the scatter plot.

    Note:
    - The function use "Scatter Plot of Standardized Age and Score" for the plot title.
    - The function use "Age (standardized)" and "Score (standardized)" as the xlabel and ylabel respectively.

    Requirements:
    - pandas
    - numpy
    - matplotlib.pyplot
    - sklearn.preprocessing

    Example:
    >>> import pandas as pd
    >>> data = pd.DataFrame([{'Name': 'James', 'Age': 30, 'Score': 85},{'Name': 'James', 'Age': 35, 'Score': 90},{'Name': 'Lily', 'Age': 28, 'Score': 92},{'Name': 'Sam', 'Age': 40, 'Score': 88},{'Name': 'Nick', 'Age': 50, 'Score': 80}])
    >>> modified_df, plot_axes = task_func(data)
    >>> modified_df.head()
        Name       Age     Score
    0  James -0.797724 -0.285365
    2   Lily -1.025645  1.312679
    3    Sam  0.341882  0.399511
    4   Nick  1.481487 -1.426825
    """

    df = df.drop_duplicates(subset='Name')

    scaler = StandardScaler()

    df[['Age', 'Score']] = scaler.fit_transform(df[['Age', 'Score']])

    plt.figure(figsize=(8, 6))
    plt.scatter(df['Age'], df['Score'])
    plt.xlabel('Age (standardized)')
    plt.ylabel('Score (standardized)')
    plt.title('Scatter Plot of Standardized Age and Score')
    ax = plt.gca()  # Get current axes
    
    return df, ax

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame({
            'Name': ['James', 'James', 'Lily', 'Sam', 'Nick'],
            'Age': [30, 35, 28, 40, 50],
            'Score': [85, 90, 92, 88, 80]
        })

    def test_standardization(self):
        modified_df, _ = task_func(self.data)
        expected_ages = [-0.797724, -1.025645, 0.341882, 1.481487]
        expected_scores = [-0.285365, 1.312679, 0.399511, -1.426825]
        pd.testing.assert_almost_equal(modified_df['Age'].tolist(), expected_ages, decimal=6)
        pd.testing.assert_almost_equal(modified_df['Score'].tolist(), expected_scores, decimal=6)

    def test_duplicates_removed(self):
        modified_df, _ = task_func(self.data)
        unique_names = modified_df['Name'].unique()
        self.assertEqual(len(unique_names), 4)  # James should be removed

    def test_plot_titles(self):
        _, ax = task_func(self.data)
        self.assertEqual(ax.get_title(), 'Scatter Plot of Standardized Age and Score')
        self.assertEqual(ax.get_xlabel(), 'Age (standardized)')
        self.assertEqual(ax.get_ylabel(), 'Score (standardized)')

    def test_dataframe_columns(self):
        modified_df, _ = task_func(self.data)
        self.assertIn('Age', modified_df.columns)
        self.assertIn('Score', modified_df.columns)
        self.assertIn('Name', modified_df.columns)

    def test_output_type(self):
        modified_df, ax = task_func(self.data)
        self.assertIsInstance(modified_df, pd.DataFrame)
        self.assertIsInstance(ax, plt.Axes)

if __name__ == '__main__':
    unittest.main()