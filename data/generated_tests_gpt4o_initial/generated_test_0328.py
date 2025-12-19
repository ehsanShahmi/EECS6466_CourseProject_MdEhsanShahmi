import collections
import random
import unittest
from queue import PriorityQueue

# Here is your prompt:
def task_func(number_teams=5):
    """
    Create a random sports ranking and sort it by points in descending order.
    
    Note:
    - Each team is assigned a name in the format "Team i" and a corresponding random number of points, where i ranges from 1 to the specified number of teams. 
    - The ranking is then sorted in descending order of points and returned as an OrderedDict.

    Parameters:
    number_teams (int, optional): The number of teams in the ranking. Default is 5.

    Returns:
    OrderedDict: Sorted dictionary where keys are team names and values are points.

    Requirements:
    - collections
    - random
    - queue.PriorityQueue


    Example:
    >>> random.seed(0)
    >>> ranking = task_func()
    >>> print(ranking)
    OrderedDict([('Team 4', 50), ('Team 5', 40), ('Team 1', 30), ('Team 2', 20), ('Team 3', 10)])
    """

    # Constants
    
    TEAMS = []
    POINTS = []

    for i in range(1, number_teams+1):
        TEAMS.append("Team "+str(i))
        POINTS.append(10*i)
    
    shuffled_points = POINTS.copy()
    random.shuffle(shuffled_points)
    ranking = dict(zip(TEAMS, shuffled_points))

    sorted_ranking = PriorityQueue()
    for team, points in ranking.items():
        sorted_ranking.put((-points, team))

    sorted_ranking_dict = collections.OrderedDict()
    while not sorted_ranking.empty():
        points, team = sorted_ranking.get()
        sorted_ranking_dict[team] = -points

    return sorted_ranking_dict


class TestTaskFunc(unittest.TestCase):

    def test_default_team_count(self):
        """Test if the function returns a ranking of 5 teams by default."""
        ranking = task_func()
        self.assertEqual(len(ranking), 5)
        self.assertTrue(all(f"Team {i}" in ranking for i in range(1, 6)))

    def test_custom_team_count(self):
        """Test if the function correctly creates a ranking for a custom number of teams."""
        number_teams = 10
        ranking = task_func(number_teams)
        self.assertEqual(len(ranking), number_teams)
        self.assertTrue(all(f"Team {i}" in ranking for i in range(1, number_teams + 1)))

    def test_ranking_order(self):
        """Test if the ranking is sorted in descending order."""
        ranking = task_func()
        points = list(ranking.values())
        self.assertEqual(points, sorted(points, reverse=True))

    def test_randomness_in_ranking(self):
        """Test if consecutive calls produce different rankings."""
        random.seed(0)  # Same seed for reproducibility
        ranking1 = task_func()
        random.seed(1)  # Different seed
        ranking2 = task_func()
        self.assertNotEqual(ranking1, ranking2)

    def test_non_negative_points(self):
        """Test if all points in the ranking are non-negative."""
        ranking = task_func()
        for points in ranking.values():
            self.assertGreaterEqual(points, 0)


if __name__ == '__main__':
    unittest.main()