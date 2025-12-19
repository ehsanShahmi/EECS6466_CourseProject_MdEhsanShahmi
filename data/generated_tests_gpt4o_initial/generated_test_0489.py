import pandas as pd
import unittest
from datetime import datetime, timedelta
import random

def task_func(epoch_milliseconds, seed=0):
    """
    Generate user activity logs from a given epoch time to the current time.

    This function iterates from the starting epoch time to the current system
    time, incrementally increasing the time by a random number of seconds (an
    integer in [1, 10]) between each log entry. Each log entry records a user
    performing an activity at a specific time.

    Parameters:
    - epoch_milliseconds (int): Starting epoch time in milliseconds. Must be in
                                the past compared to current system time.
    - seed (int): random seed for reproducibility. Defaults to 0.

    Returns:
    - pd.DataFrame: A DataFrame containing logs of user activities, with columns:
        - 'User':   User names, randomly chosen from a predefined list of users,
                    ['user1', 'user2', 'user3', 'user4', 'user5'].
        - 'Activity': Activities performed by the users, randomly chosen from a
                      predefined list of activities, ['login', 'logout', 'browse',
                      'search', 'purchase'].
        - 'Time': The timestamp of when the activity occurred, incrementally
                  increasing from the starting epoch time to the current time.

    Raises:
    - ValueError: If the start time is after the current system time.
    
    Requirements:
    - pandas
    - datetime.datetime.fromtimestamp
    - datetime.timedelta
    - random

    Example:
    >>> log = task_func(1615168051807)
    >>> type(log)
    <class 'pandas.core.frame.DataFrame'>
    >>> log.iloc[0]
    User                             user4
    Activity                        search
    Time        2021-03-08 12:47:31.807000
    Name: 0, dtype: object
    """

    random.seed(seed)

    USERS = ["user1", "user2", "user3", "user4", "user5"]
    ACTIVITIES = ["login", "logout", "browse", "search", "purchase"]

    start_time = datetime.fromtimestamp(epoch_milliseconds / 1000.0)
    end_time = datetime.now()
    if start_time >= end_time:
        raise ValueError("Start time must be before current system time")

    logs = []
    current_time = start_time
    while current_time <= end_time:
        user = random.choice(USERS)
        activity = random.choice(ACTIVITIES)
        logs.append([user, activity, current_time])
        current_time += timedelta(seconds=random.randint(1, 10))
    log_df = pd.DataFrame(logs, columns=["User", "Activity", "Time"])
    return log_df

class TestTaskFunc(unittest.TestCase):

    def test_output_type(self):
        """Test if the output is a DataFrame."""
        log = task_func(1615168051807)
        self.assertIsInstance(log, pd.DataFrame)
        
    def test_dataframe_columns(self):
        """Test if the DataFrame has the correct columns."""
        log = task_func(1615168051807)
        self.assertEqual(list(log.columns), ["User", "Activity", "Time"])
        
    def test_user_activity_range(self):
        """Test if users and activities are from the specified lists."""
        log = task_func(1615168051807, seed=1)
        valid_users = {"user1", "user2", "user3", "user4", "user5"}
        valid_activities = {"login", "logout", "browse", "search", "purchase"}

        for user in log['User']:
            self.assertIn(user, valid_users)
        for activity in log['Activity']:
            self.assertIn(activity, valid_activities)

    def test_time_increasing(self):
        """Test if the 'Time' column is in increasing order."""
        log = task_func(1615168051807, seed=1)
        self.assertTrue((log['Time'].diff().dropna() > timedelta(0)).all())

    def test_start_time_error(self):
        """Test if ValueError is raised for future start time."""
        future_time = int((datetime.now() + timedelta(days=1)).timestamp() * 1000)
        with self.assertRaises(ValueError):
            task_func(future_time)

if __name__ == '__main__':
    unittest.main()