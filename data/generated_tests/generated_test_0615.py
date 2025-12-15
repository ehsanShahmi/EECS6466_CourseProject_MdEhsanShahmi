import unittest
import pandas as pd
from random import seed

# Here is your prompt:
from random import randint, seed
import pandas as pd


# Method
def task_func(goals, penalties, rng_seed=None):
    """
    Generate a Pandas DataFrame with colomns 'Team' and 'Match Result' of the results of football matches for multiple
    teams, incorporating random goals and penalties. Penalties are converted into fines using a predefined cost.

    Parameters:
    - goals (int): The maximum number of goals a team can score in a match. Must be non-negative.
    - penalties (int): The maximum number of penalties a team can receive in a match. Must be non-negative.
    - rng_seed (int, optional): Seed for the random number generator to ensure reproducible results. Defaults to None.

    Returns:
    - pd.DataFrame: A pandas DataFrame with columns ['Team', 'Match Result'], detailing each team's goals and accumulated fines.

    Requirements:
    - pandas
    - random

    Example:
    >>> seed(42)  # Setting seed for reproducibility in this example
    >>> results = task_func(5, 3, 42)
    >>> print(results)
         Team      Match Result
    0  Team A     (5 goals, $0)
    1  Team B  (0 goals, $2000)
    2  Team C  (1 goals, $1000)
    3  Team D     (1 goals, $0)
    4  Team E     (5 goals, $0)
    """

               # Constants
    TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    PENALTY_COST = 1000  # in dollars

    if rng_seed is not None:
        seed(rng_seed)  # Set seed for reproducibility

    match_results = []
    for team in TEAMS:
        team_goals = randint(0, abs(goals))
        team_penalties = randint(0, abs(penalties))
        penalty_cost = PENALTY_COST * team_penalties
        result_string = f"({team_goals} goals, ${penalty_cost})"
        match_results.append([team, result_string])

    results_df = pd.DataFrame(match_results, columns=['Team', 'Match Result'])

    return results_df


class TestTaskFunction(unittest.TestCase):
    
    def test_zero_goals_and_penalties(self):
        result = task_func(0, 0, rng_seed=42)
        expected_result = pd.DataFrame({
            'Team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
            'Match Result': ['(0 goals, $0)', '(0 goals, $0)', '(0 goals, $0)', '(0 goals, $0)', '(0 goals, $0)']
        })
        pd.testing.assert_frame_equal(result, expected_result)
    
    def test_non_zero_goals_and_zero_penalties(self):
        result = task_func(5, 0, rng_seed=42)
        expected_teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
        expected_result = pd.DataFrame({
            'Team': expected_teams,
            'Match Result': ['(5 goals, $0)', '(0 goals, $0)', '(1 goals, $0)', '(1 goals, $0)', '(5 goals, $0)']
        })
        pd.testing.assert_frame_equal(result.sort_values('Team').reset_index(drop=True), expected_result.sort_values('Team').reset_index(drop=True)
    
    def test_zero_goals_and_non_zero_penalties(self):
        result = task_func(0, 3, rng_seed=42)
        expected_result = pd.DataFrame({
            'Team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
            'Match Result': ['(0 goals, $0)', '(0 goals, $2000)', '(0 goals, $1000)', '(0 goals, $0)', '(0 goals, $0)']
        })
        pd.testing.assert_frame_equal(result, expected_result)      
    
    def test_negative_goals_or_penalties(self):
        with self.assertRaises(ValueError):
            task_func(-1, 3)
        with self.assertRaises(ValueError):
            task_func(5, -1)
    
    def test_default_rng_seed_reproducibility(self):
        result1 = task_func(5, 3)
        result2 = task_func(5, 3)
        pd.testing.assert_frame_equal(result1, result2)

if __name__ == '__main__':
    unittest.main()