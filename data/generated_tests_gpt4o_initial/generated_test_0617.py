from random import randint, seed
import matplotlib.pyplot as plt
import pandas as pd
import re
import unittest

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars

def task_func(goals, penalties, rng_seed=None, teams=TEAMS):
    """
    Generate and analyze a Pandas DataFrame of football match results for multiple teams,
    incorporating random goals and penalties, then visualize the analyzed data with columns 'Team', 'Goals',
    and 'Penalty Cost'. Penalties are converted into fines based on a predetermined penalty cost.

    Parameters:
    - goals (int): The maximum number of goals a team can score in a match.
    - penalties (int): The maximum number of penalties a team can receive in a match.
    - rng_seed (int, optional): Seed for the random number generator to ensure reproducibility. Defaults to None.
    - teams (list of str, optional): List of team names to assign players

    Returns:
    - DataFrame: A pandas DataFrame containing teams, their goals, and penalty costs, along with the original match results.

    Requirements:
    - pandas
    - matplotlib.pyplot
    - random
    - re
    """

    if rng_seed is not None:
        seed(rng_seed)

    match_results = []

    for team in teams:
        team_goals = randint(0, goals)
        team_penalties = randint(0, penalties)
        penalty_cost = PENALTY_COST * team_penalties
        result_string = f"({team_goals} goals, ${penalty_cost})"
        match_results.append([team, result_string])

    results_df = pd.DataFrame(match_results, columns=['Team', 'Match Result'])

    if not results_df.empty:
        results_df['Goals'] = results_df['Match Result'].apply(lambda x: int(re.search(r'\((\d+) goals', x).group(1)))
        results_df['Penalty Cost'] = results_df['Match Result'].apply(lambda x: int(re.search(r'\$(\d+)', x).group(1)))

        ax = results_df.set_index('Team')[['Goals', 'Penalty Cost']].plot(kind='bar', stacked=True)
        plt.ylabel('Counts')
        plt.title('Football Match Results Analysis')
        plt.tight_layout()
        plt.show()

    return results_df

class TestTaskFunc(unittest.TestCase):

    def test_return_type(self):
        result_df = task_func(5, 3)
        self.assertIsInstance(result_df, pd.DataFrame)

    def test_team_count(self):
        result_df = task_func(5, 3)
        self.assertEqual(len(result_df), len(TEAMS))

    def test_goals_range(self):
        result_df = task_func(5, 3, rng_seed=42)
        goals_series = result_df['Goals']
        self.assertTrue(all(0 <= goal <= 5 for goal in goals_series), "Goals should be in the range [0, 5].")

    def test_penalty_cost_calculation(self):
        result_df = task_func(5, 3, rng_seed=42)
        penalty_costs = result_df['Penalty Cost']
        penalties_received = result_df['Match Result'].apply(lambda x: int(re.search(r'\((\d+) goals', x).group(1)))
        for index, penalties in enumerate(penalties_received):
            expected_cost = penalties * PENALTY_COST
            self.assertEqual(penalty_costs[index], expected_cost)

    def test_visualization_no_error(self):
        try:
            task_func(5, 3, rng_seed=42)
        except Exception as e:
            self.fail(f"Visualization raised an error: {e}")

if __name__ == '__main__':
    unittest.main()