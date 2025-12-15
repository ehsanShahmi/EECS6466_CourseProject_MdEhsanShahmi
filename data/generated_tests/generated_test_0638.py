import numpy as np
import pandas as pd
import unittest

# Here is your prompt:
def task_func(num_teams=5, num_games=100):
    """
    Create a Pandas DataFrame that displays the random scores of different teams in multiple games.
    The function generates random scores for each game played by each team and populates them in
    a DataFrame with index=teams, columns=games.

    Parameters:
    - num_teams (int, optional): The number of teams participating. Default is 5.
    - num_games (int, optional): The number of games played. Default is 100.

    Returns:
    DataFrame: The generated DataFrame containing random scores for each team in each game.

    Requirements:
    - pandas
    - numpy

    Example:
    >>> df = task_func(num_teams=3, num_games=10)
    >>> type(df)
    <class 'pandas.core.frame.DataFrame'>
    """

    scores = np.random.randint(0, 101, size=(num_teams, num_games))
    teams = ['Team' + str(i) for i in range(1, num_teams + 1)]
    games = ['Game' + str(i) for i in range(1, num_games + 1)]
    df = pd.DataFrame(scores, index=teams, columns=games)
    return df


class TestTaskFunc(unittest.TestCase):

    def test_default_params(self):
        """Test the function with default parameters."""
        df = task_func()
        self.assertEqual(df.shape, (5, 100))  # Should be 5 teams and 100 games
        self.assertEqual(df.index.tolist(), ['Team1', 'Team2', 'Team3', 'Team4', 'Team5'])

    def test_custom_params(self):
        """Test the function with custom parameters."""
        df = task_func(num_teams=3, num_games=10)
        self.assertEqual(df.shape, (3, 10))  # Should be 3 teams and 10 games
        self.assertEqual(df.index.tolist(), ['Team1', 'Team2', 'Team3'])
        self.assertEqual(df.columns.tolist(), ['Game1', 'Game2', 'Game3', 'Game4', 'Game5', 'Game6', 'Game7', 'Game8', 'Game9', 'Game10'])

    def test_score_range(self):
        """Test if the scores are within the correct range (0 to 100)."""
        df = task_func(num_teams=4, num_games=5)
        self.assertTrue((df.values >= 0).all() and (df.values <= 100).all())

    def test_empty_dataframe(self):
        """Test the function with zero teams."""
        df = task_func(num_teams=0, num_games=10)
        self.assertTrue(df.empty)  # DataFrame should be empty

    def test_no_games(self):
        """Test the function with zero games."""
        df = task_func(num_teams=5, num_games=0)
        self.assertTrue(df.empty)  # DataFrame should be empty


if __name__ == '__main__':
    unittest.main()