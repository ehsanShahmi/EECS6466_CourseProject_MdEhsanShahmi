from random import randint, seed
import matplotlib.pyplot as plt
import pandas as pd
import unittest

# Constants (they can be overridden with default parameters)
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars


def task_func(goals, penalties, teams=TEAMS, penalty_cost=PENALTY_COST, rng_seed=None):
    """
    Generate a Dataframe to show the football match results of teams 'Team' with random goals 'Goals' and
    penalties 'Penalty Cost', and create a bar plot of the results. Penalties are converted into fines according to the
    penalty costs.

    Parameters:
    - goals (int): The maximum number of goals a team can score in a match.
    - penalties (int): The maximum number of penalties a team can receive in a match.
    - teams (list of str, optional): A list of team names. Default is ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'].
    - penalty_cost (int, optional): Cost of a penalty in dollars. Default is 1000.
    - rng_seed (int, optional): Random seed for reproducibility. Default is None.

    Returns:
    - DataFrame: A pandas DataFrame containing columns for teams, their goals, and penalty costs.
    - Axes: A matplotlib Axes object representing the bar plot of the results.

    Requirements:
    - pandas
    - matplotlib.pyplot
    - random

    Example:
    >>> seed(42)  # Setting seed for reproducibility
    >>> df, ax = task_func(5, 3, rng_seed=42)
    >>> isinstance(df, pd.DataFrame) and 'Team' in df.columns and 'Goals' in df.columns and 'Penalty Cost' in df.columns
    True
    >>> all(df['Goals'] <= 5) and all(df['Penalty Cost'] <= 3000)  # Goals and penalties are within expected range
    True
    """
    
    if rng_seed is not None:
        seed(rng_seed)

    # Ensure goals and penalties are treated as positive
    goals = abs(goals)
    penalties = abs(penalties)

    match_results = []
    for team in teams:
        team_goals = randint(0, goals)
        team_penalties = randint(0, penalties)
        team_penalty_cost = penalty_cost * team_penalties
        match_results.append([team, team_goals, team_penalty_cost])

    results_df = pd.DataFrame(match_results, columns=['Team', 'Goals', 'Penalty Cost'])
    ax = results_df.plot(kind='bar', x='Team', y=['Goals', 'Penalty Cost'], stacked=True)
    plt.ylabel('Results')

    return results_df, ax


class TestTaskFunc(unittest.TestCase):
    
    def test_dataframe_structure(self):
        df, ax = task_func(5, 3, rng_seed=42)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIn('Team', df.columns)
        self.assertIn('Goals', df.columns)
        self.assertIn('Penalty Cost', df.columns)

    def test_goals_range(self):
        df, ax = task_func(5, 3, rng_seed=42)
        self.assertTrue(all(df['Goals'] <= 5), "Goals exceed maximum allowed")

    def test_penalty_cost_range(self):
        df, ax = task_func(5, 3, rng_seed=42)
        self.assertTrue(all(df['Penalty Cost'] <= 3000), "Penalty costs exceed expected maximum")

    def test_empty_teams(self):
        df, ax = task_func(5, 3, teams=[], rng_seed=42)
        self.assertEqual(len(df), 0, "DataFrame should be empty when no teams are provided")

    def test_negative_input_values(self):
        df, ax = task_func(-5, -3, rng_seed=42)
        self.assertTrue(all(df['Goals'] >= 0), "Goals should not be negative")
        self.assertTrue(all(df['Penalty Cost'] >= 0), "Penalty costs should not be negative")


if __name__ == '__main__':
    unittest.main()