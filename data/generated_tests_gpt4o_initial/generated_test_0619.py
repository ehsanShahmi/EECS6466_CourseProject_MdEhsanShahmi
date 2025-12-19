from random import randint, seed
import pandas as pd
from sklearn.linear_model import LinearRegression
import unittest


# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars


def task_func(goals, penalties, rng_seed=None):
    """
    Simulates football match results with random goals and penalties for multiple teams,
    and trains a linear regression model to predict penalty costs from goals.

    Parameters:
    - goals (int): Maximum number of goals a team can score in a match.
    - penalties (int): Maximum number of penalties a team can receive in a match.
    - rng_seed (int, optional): Seed for the random number generator to ensure reproducibility. Defaults to None.

    Returns:
    - tuple:
        - pd.DataFrame: Contains 'Team', 'Goals', and 'Penalty Cost' columns.
        - LinearRegression: Trained model to predict 'Penalty Cost' based on 'Goals'.

    Requirements:
    - pandas
    - sklearn.linear_model
    - random

    Example:
    >>> df, model = task_func(5, 3, rng_seed=42)
    >>> predictions = model.predict([[2], [3]])
    >>> print(predictions)
    [706.89655172 439.65517241]
    """
    if rng_seed is not None:
        seed(rng_seed)

    # Generate match results
    match_results = []
    for team in TEAMS:
        team_goals = randint(0, goals)
        team_penalties = randint(0, penalties)
        penalty_cost = PENALTY_COST * team_penalties
        match_results.append([team, team_goals, penalty_cost])

    # Create DataFrame
    results_df = pd.DataFrame(match_results, columns=['Team', 'Goals', 'Penalty Cost'])

    # Train Linear Regression Model
    X = results_df[['Goals']]
    y = results_df['Penalty Cost']
    model = LinearRegression().fit(X, y)

    return results_df, model


class TestTaskFunc(unittest.TestCase):
    
    def test_output_dataframe_shape(self):
        df, model = task_func(5, 3)
        self.assertEqual(df.shape, (5, 3), "DataFrame should have 5 rows and 3 columns")
        
    def test_penalty_cost_calculation(self):
        df, model = task_func(3, 2, rng_seed=0)
        self.assertTrue((df['Penalty Cost'] == df['Goals'] * PENALTY_COST).all(),
                        "Penalty costs should be calculated correctly")

    def test_model_fits_correctly(self):
        df, model = task_func(4, 2, rng_seed=1)
        self.assertIsInstance(model, LinearRegression, "The trained model should be a LinearRegression instance")
        self.assertEqual(len(model.coef_), 1, "The model should have one coefficient for 'Goals'")

    def test_reproducibility_with_rng_seed(self):
        df1, model1 = task_func(4, 3, rng_seed=42)
        df2, model2 = task_func(4, 3, rng_seed=42)
        pd.testing.assert_frame_equal(df1, df2, "The DataFrame outputs should be the same with the same seed")

    def test_total_goals_within_bounds(self):
        df, model = task_func(5, 3)
        self.assertTrue(df['Goals'].between(0, 5).all(), "Goals should be within the defined bounds")

        
if __name__ == '__main__':
    unittest.main()