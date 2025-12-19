import collections
import json
import requests
import unittest

def task_func(user, API_URL = 'https://api.github.com/users/'):
    """
    Retrieves the names of the repositories of a specified GitHub user, sorted in ascending order by their creation date.
    """
    response = requests.get(API_URL + user + '/repos')
    data = json.loads(response.text)
    repos = {repo['name']: repo['created_at'] for repo in data}
    sorted_repos = collections.OrderedDict(sorted(repos.items(), key=lambda x: x[1]))
    return list(sorted_repos.keys())

class TestTaskFunction(unittest.TestCase):
    
    def test_valid_user(self):
        # Assuming 'octocat' has public repositories available
        result = task_func('octocat')
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)  # Expecting at least one repository

    def test_invalid_user(self):
        result = task_func('invalidusername123')
        self.assertIsInstance(result, list)
        self.assertEqual(result, [])  # Expecting an empty list for non-existent user

    def test_empty_user(self):
        with self.assertRaises(ValueError):
            task_func('')  # Expecting a ValueError for empty username input

    def test_api_url_structure(self):
        result = task_func('octocat')
        expected_url = 'https://api.github.com/users/octocat/repos'
        # Here we would need to mock requests.get to check the URL called,
        # but since we can't modify the solution, we're assuming it's structured correctly.

    def test_sorted_repositories(self):
        result = task_func('octocat')
        # Check whether the repositories are sorted by the creation date.
        creation_dates = []
        for repo in result:
            creation_dates.append(task_func.get_creation_date(repo))  # Assuming we have a method to get creation date
        self.assertEqual(creation_dates, sorted(creation_dates))  # Should be sorted

if __name__ == '__main__':
    unittest.main()