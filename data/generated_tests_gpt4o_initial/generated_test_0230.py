import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Here is your prompt
COLUMNS = ['Name', 'Age', 'Country', 'Score']

def task_func(df):
    """
    Generates a histogram of scores and a boxplot of scores by country from a pandas DataFrame. 
    It considers only unique names for both plots.

    Parameters:
    df (DataFrame): A pandas DataFrame containing the columns 'Name', 'Age', 'Country', and 'Score'.

    Returns:
    matplotlib.figure.Figure: A matplotlib figure containing the histogram and boxplot.

    Requirements:
    - matplotlib.pyplot
    - seaborn
    - pandas

    Note:
    - The function would return "Invalid input" string if the input is invalid (e.g., does not contain the required 'Name' key).
    - The histogram of scores has a title "Histogram of Scores".
    - The boxplot of scores has a title "Boxplot of Scores by Country".

    Example:
    >>> data = pd.DataFrame([{'Name': 'James', 'Age': 30, 'Country': 'USA', 'Score': 85}, {'Name': 'Nick', 'Age': 50, 'Country': 'Australia', 'Score': 80}])
    >>> fig = task_func(data)
    >>> axes = fig.get_axes()
    >>> print(axes[0].get_title())
    Histogram of Scores

    >>> print(task_func("not a dataframe"))
    Invalid input
    """

               
    if not isinstance(df, pd.DataFrame):
        return "Invalid input"
    
    try:
        df = df.drop_duplicates(subset='Name')

        fig = plt.figure(figsize=(10, 5))

        plt.subplot(1, 2, 1)
        sns.histplot(df['Score'], bins=10)
        plt.title('Histogram of Scores')

        plt.subplot(1, 2, 2)
        sns.boxplot(x='Country', y='Score', data=df)
        plt.title('Boxplot of Scores by Country')

        plt.tight_layout()

        return fig
    except Exception as e:
        return "Invalid input"


class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        self.valid_data = pd.DataFrame([
            {'Name': 'James', 'Age': 30, 'Country': 'USA', 'Score': 85},
            {'Name': 'Nick', 'Age': 50, 'Country': 'Australia', 'Score': 80},
            {'Name': 'Anna', 'Age': 22, 'Country': 'USA', 'Score': 90}
        ])
        self.invalid_data_type = "not a dataframe"
        self.empty_data = pd.DataFrame(columns=COLUMNS)
        self.data_with_duplicates = pd.DataFrame([
            {'Name': 'James', 'Age': 30, 'Country': 'USA', 'Score': 85},
            {'Name': 'James', 'Age': 30, 'Country': 'USA', 'Score': 95}
        ])
        
    def test_valid_input_generates_figures(self):
        fig = task_func(self.valid_data)
        self.assertIsInstance(fig, plt.Figure)
        axes = fig.get_axes()
        self.assertEqual(axes[0].get_title(), 'Histogram of Scores')
        self.assertEqual(axes[1].get_title(), 'Boxplot of Scores by Country')
        
    def test_invalid_input_returns_invalid_string(self):
        result = task_func(self.invalid_data_type)
        self.assertEqual(result, "Invalid input")
        
    def test_empty_dataframe_returns_invalid_string(self):
        result = task_func(self.empty_data)
        self.assertEqual(result, "Invalid input")
        
    def test_data_with_duplicates_handled_correctly(self):
        fig = task_func(self.data_with_duplicates)
        axes = fig.get_axes()
        self.assertEqual(axes[0].get_title(), 'Histogram of Scores')
        
    def test_function_output_for_unique_names(self):
        fig = task_func(self.valid_data)
        axes = fig.get_axes()
        score_data = [p.get_array() for p in axes[1].artists]
        unique_scores = {score[0] for score in score_data}
        self.assertEqual(len(unique_scores), len(self.valid_data['Score'].unique()))
        
if __name__ == '__main__':
    unittest.main()