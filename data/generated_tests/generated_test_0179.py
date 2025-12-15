import re
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd
import unittest

def task_func(df):
    """
    Analyzes a given DataFrame containing article titles and content to identify articles with titles that include
    the words "how" or "what". It calculates the TF-IDF scores for the words in the content of these articles and
    visualizes these scores in a bar plot.

    Parameters:
    df (DataFrame): A DataFrame containing at least two columns: 'Title' and 'Content'.

    Returns:
    Axes: A matplotlib Axes object displaying a bar plot of the TF-IDF scores.

    Note:
    - If the DataFrame does not contain 'Title' and 'Content' columns, the function returns an empty plot.
    - If no articles have titles containing "how" or "what," the function also returns an empty plot.
    - Set the name of the y-axis to 'TF-IDF Score'.
    - Set xticks to display the feature names vertically.

    Requirements:
    - re
    - matplotlib
    - sklearn
    - numpy

    Example:
    >>> import pandas as pd
    >>> data = {'Title': ['How to make pancakes', 'News update'], 'Content': ['Pancakes are easy to make.', 'Today’s news is about politics.']}
    >>> df = pd.DataFrame(data)
    >>> ax = task_func(df)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """

    pattern = re.compile(r'(how|what)', re.IGNORECASE)

    # Check if the DataFrame has the required columns
    if not set(['Title', 'Content']).issubset(df.columns):
        fig, ax = plt.subplots()
        return ax

    interesting_articles = df[df['Title'].apply(lambda x: bool(pattern.search(x)))]

    fig, ax = plt.subplots()

    # If there are no interesting articles, return an empty plot
    if interesting_articles.empty:
        return ax

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(interesting_articles['Content'])
    tfidf_scores = np.array(X.sum(axis=0))[0]

    ax.bar(vectorizer.get_feature_names_out(), tfidf_scores)
    ax.set_ylabel('TF-IDF Score')
    plt.xticks(rotation='vertical')

    return ax

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        self.valid_data = pd.DataFrame({
            'Title': ['How to cook', 'What is Python', 'The joy of cooking'],
            'Content': ['Cooking can be fun.', 'Python is a programming language.', 'Cooking is an art.']
        })
        self.empty_data = pd.DataFrame(columns=['Title', 'Content'])
        self.invalid_data = pd.DataFrame({
            'Header1': ['How to cook', 'What is Python'],
            'Header2': ['Cooking can be fun.', 'Python is a programming language.']
        })

    def test_empty_df(self):
        ax = task_func(self.empty_data)
        self.assertEqual(len(ax.containers), 0)

    def test_invalid_columns(self):
        ax = task_func(self.invalid_data)
        self.assertEqual(len(ax.containers), 0)

    def test_no_matching_titles(self):
        no_matches = pd.DataFrame({
            'Title': ['Learning to bake', 'The science of baking'],
            'Content': ['Baking is an interesting task.', 'Science helps us understand baking better.']
        })
        ax = task_func(no_matches)
        self.assertEqual(len(ax.containers), 0)

    def test_matching_titles(self):
        ax = task_func(self.valid_data)
        self.assertGreater(len(ax.containers), 0)
        
    def test_tfidf_scores_plot(self):
        ax = task_func(self.valid_data)
        feature_names = ax.get_xticks()
        self.assertTrue(len(feature_names) > 0)
        self.assertEqual(ax.get_ylabel(), 'TF-IDF Score')

if __name__ == '__main__':
    unittest.main()