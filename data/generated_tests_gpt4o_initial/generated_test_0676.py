import pandas as pd
import numpy as np
import unittest

# Here is the provided prompt with the task function
def task_func(df):
    """
    Generate a DataFrame that contains savegames for a number of games between different teams.
    Each row of the input DataFrame represents a match, and contains two teams and their respective scores.
    The function adds a 'winner' column to the DataFrame, which is the team with the highest score in each match.
    If the scores are equal, the winner is should be randomly decided.
    
    Parameters:
    - df (pandas.DataFrame): The input DataFrame with columns 'team1', 'team2', 'score1', 'score2'.

    Returns:
    - df (pandas.DataFrame): The DataFrame with the added 'winner' column.
    """
    def determine_winner(row):
        if row['score1'] > row['score2']:
            return row['team1']
        elif row['score1'] < row['score2']:
            return row['team2']
        else:
            return random.choice([row['team1'], row['team2']])
    
    winner_series = pd.Series([determine_winner(row) for index, row in df.iterrows()], index=df.index)
    df['winner'] = winner_series
    return df

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        # Prepare test DataFrames
        self.df_test_1 = pd.DataFrame({
            'team1': ['Team A', 'Team B', 'Team C'],
            'team2': ['Team D', 'Team E', 'Team F'],
            'score1': [3, 5, 2],
            'score2': [2, 5, 4]
        })
        
        self.df_test_2 = pd.DataFrame({
            'team1': ['Team X', 'Team Y'],
            'team2': ['Team Z', 'Team W'],
            'score1': [1, 1],
            'score2': [1, 1]
        })
        
        self.df_test_3 = pd.DataFrame({
            'team1': ['Team A', 'Team B'],
            'team2': ['Team B', 'Team A'],
            'score1': [0, 0],
            'score2': [0, 0]
        })

    def test_winner_column_exists(self):
        result_df = task_func(self.df_test_1)
        self.assertIn('winner', result_df.columns)

    def test_winner_dtype(self):
        result_df = task_func(self.df_test_1)
        self.assertEqual(result_df['winner'].dtype, object)

    def test_winner_correctness(self):
        result_df = task_func(self.df_test_1)
        expected_winners = ['Team A', 'Team E', 'Team F']
        self.assertTrue(all(result_df['winner'] == expected_winners))

    def test_random_winner_on_tie(self):
        result_df = task_func(self.df_test_2)
        self.assertTrue(all(result_df['winner'].isin(['Team X', 'Team Y', 'Team Z', 'Team W'])))

    def test_tie_between_same_teams(self):
        result_df = task_func(self.df_test_3)
        self.assertTrue(result_df['winner'].isin(['Team A', 'Team B']).all())

if __name__ == '__main__':
    unittest.main()