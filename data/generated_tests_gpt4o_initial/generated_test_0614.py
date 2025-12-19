import pandas as pd
import seaborn as sns
import unittest

# Here is your prompt:
def task_func(goals, penalties):
    """
    Visualize the distribution of goals and penalties for a number of teams and return the data as a
    DataFrame with columns 'Team', 'Goals' and 'Penalties'.

    Parameters:
    - goals (dict): A dictionary where keys are team names and values are numbers of goals scored.
    - penalties (dict): A dictionary where keys are team names and values are numbers of penalties incurred.

    Returns:
    tuple: A tuple containing:
        - DataFrame: A pandas DataFrame with the goals and penalties for the teams.
        - Axes: A seaborn pairplot visualization of goals and penalties distribution for the teams.

    Requirements:
    - pandas
    - seaborn

    Example:
    >>> goals = {'Team A': 3, 'Team B': 2, 'Team C': 1, 'Team D': 0, 'Team E': 2}
    >>> penalties = {'Team A': 1, 'Team B': 0, 'Team C': 2, 'Team D': 3, 'Team E': 1}
    >>> df, plot = task_func(goals, penalties)
    >>> print(df)
         Team  Goals  Penalties
    0  Team A      3          1
    1  Team B      2          0
    2  Team C      1          2
    3  Team D      0          3
    4  Team E      2          1
    """

class TestTaskFunc(unittest.TestCase):
    
    def test_correct_dataframe_structure(self):
        goals = {'Team A': 3, 'Team B': 2}
        penalties = {'Team A': 1, 'Team B': 0}
        df, plot = task_func(goals, penalties)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape[1], 3)
        self.assertListEqual(list(df.columns), ['Team', 'Goals', 'Penalties'])

    def test_dataframe_content(self):
        goals = {'Team A': 3, 'Team B': 2, 'Team C': 1}
        penalties = {'Team A': 1, 'Team B': 0, 'Team C': 2}
        df, plot = task_func(goals, penalties)
        expected_data = {
            'Team': ['Team A', 'Team B', 'Team C'],
            'Goals': [3, 2, 1],
            'Penalties': [1, 0, 2]
        }
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(df.reset_index(drop=True), expected_df)

    def test_missing_teams(self):
        goals = {'Team A': 3}
        penalties = {'Team B': 1}
        df, plot = task_func(goals, penalties)
        self.assertIn('Team A', df['Team'].values)
        self.assertIn('Team B', df['Team'].values)
        self.assertNotIn('Team C', df['Team'].values)
        self.assertNotIn('Team D', df['Team'].values)

    def test_empty_input(self):
        goals = {}
        penalties = {}
        df, plot = task_func(goals, penalties)
        self.assertTrue(df.empty)

    def test_pairplot_created(self):
        goals = {'Team A': 3, 'Team B': 2}
        penalties = {'Team A': 1, 'Team B': 0}
        df, plot = task_func(goals, penalties)
        self.assertIsNotNone(plot)

if __name__ == '__main__':
    unittest.main()