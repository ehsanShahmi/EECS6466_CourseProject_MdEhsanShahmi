import unittest
import pandas as pd
from random import choice
import numpy as np

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTIES_COSTS = [100, 200, 300, 400, 500]

# The function to be tested is not included as per instructions

class TestTaskFunc(unittest.TestCase):

    def test_no_goals_no_penalties(self):
        goals = {'Team A': 0, 'Team B': 0}
        penalties = {'Team A': 0, 'Team B': 0}
        expected_df = pd.DataFrame({
            'Team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
            'Goals': [0, 0, 0, 0, 0],
            'Penalties': [0, 0, 0, 0, 0],
            'Penalties Cost': [0, 0, 0, 0, 0],
            'Performance Score': [0, 0, 0, 0, 0]
        })
        result_df = task_func(goals, penalties)
        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_with_goals_no_penalties(self):
        goals = {'Team A': 5, 'Team B': 3}
        penalties = {'Team A': 0, 'Team B': 0}
        result_df = task_func(goals, penalties)
        
        # Check the performance scores
        self.assertEqual(result_df.loc[result_df['Team'] == 'Team A', 'Performance Score'].values[0], 5)
        self.assertEqual(result_df.loc[result_df['Team'] == 'Team B', 'Performance Score'].values[0], 3)

    def test_with_penalties_no_goals(self):
        goals = {'Team A': 0, 'Team B': 0}
        penalties = {'Team A': 4, 'Team B': 2}
        result_df = task_func(goals, penalties)

        # Check the performance scores to verify they are 0 (since goals - penalties = negative)
        self.assertEqual(result_df.loc[result_df['Team'] == 'Team A', 'Performance Score'].values[0], 0)
        self.assertEqual(result_df.loc[result_df['Team'] == 'Team B', 'Performance Score'].values[0], 0)

    def test_performance_score_calculation(self):
        goals = {'Team A': 10, 'Team B': 5}
        penalties = {'Team A': 3, 'Team B': 1}
        result_df = task_func(goals, penalties)

        # Performance Score should be calculated as goals - penalties
        self.assertEqual(result_df.loc[result_df['Team'] == 'Team A', 'Performance Score'].values[0], 7)
        self.assertEqual(result_df.loc[result_df['Team'] == 'Team B', 'Performance Score'].values[0], 4)

    def test_penalties_cost_calculation(self):
        goals = {'Team A': 2}
        penalties = {'Team A': 2}
        result_df = task_func(goals, penalties)

        # The Penalties Cost should be calculated as penalties * random penalty cost
        penalties_cost = result_df.loc[result_df['Team'] == 'Team A', 'Penalties Cost'].values[0]
        expected_costs = [200, 400, 600, 800, 1000]
        self.assertIn(penalties_cost, expected_costs)


if __name__ == '__main__':
    unittest.main()