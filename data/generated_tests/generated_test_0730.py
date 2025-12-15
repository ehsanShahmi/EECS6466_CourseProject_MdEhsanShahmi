import unittest
import pickle
import os
from datetime import datetime
import pytz

# Constants
FILE_NAME = 'save.pkl'

# The provided code does not need to be modified or included.
# Below is the test suite for the task_func as per the requirements.


class TestTaskFunc(unittest.TestCase):

    def test_current_time(self):
        """Test saving and loading the current UTC time."""
        dt = datetime.now(pytz.UTC)
        loaded_dt = task_func(dt)
        self.assertEqual(dt, loaded_dt)

    def test_specific_time(self):
        """Test saving and loading a specific UTC time."""
        dt = datetime(2023, 10, 1, 12, 0, 0, tzinfo=pytz.UTC)
        loaded_dt = task_func(dt)
        self.assertEqual(dt, loaded_dt)

    def test_time_difference(self):
        """Test that the task_func accurately saves and loads 
        a slightly modified time without affecting the original."""
        dt = datetime.now(pytz.UTC)
        loaded_dt = task_func(dt)
        self.assertEqual(dt.tzinfo, loaded_dt.tzinfo)  # Ensure timezone info is preserved
        self.assertFalse(dt.timestamp() - loaded_dt.timestamp() > 1)  # Check timestamp difference

    def test_empty_datetime(self):
        """Test saving None as the datetime object."""
        with self.assertRaises(TypeError):
            task_func(None)

    def test_invalid_type(self):
        """Test saving a non-datetime object."""
        with self.assertRaises(pickle.PicklingError):
            task_func("not a datetime")


if __name__ == '__main__':
    unittest.main()