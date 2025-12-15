import unittest
import pandas as pd
from datetime import datetime, timedelta
from your_module_name import task_func  # Replace 'your_module_name' with the actual module name where task_func is defined

# Constants
ROOMS = ["Room1", "Room2", "Room3", "Room4", "Room5"]

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # This method will run before each test case
        self.future_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        self.past_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        self.booking_info = {"Room1": "Booked", "Room2": "Available"}
        self.empty_booking_info = {}

    def test_valid_booking_data(self):
        """Test with valid future date and booking data"""
        report_df, ax = task_func(self.future_date, self.booking_info)
        self.assertEqual(report_df.shape[0], 5)
        self.assertIn("Room1", report_df["Room"].values)
        self.assertIn("Room2", report_df["Room"].values)
        self.assertEqual(report_df.loc[report_df["Room"] == "Room1", "Booking Status"].values[0], "Booked")
        self.assertEqual(report_df.loc[report_df["Room"] == "Room2", "Booking Status"].values[0], "Available")
        self.assertEqual(report_df.loc[report_df["Room"] == "Room3", "Booking Status"].values[0], "Not Listed")

    def test_invalid_date_format(self):
        """Test with invalid date format"""
        with self.assertRaises(ValueError):
            task_func("invalid_date_format", self.booking_info)

    def test_past_date(self):
        """Test with a past date"""
        with self.assertRaises(ValueError):
            task_func(self.past_date, self.booking_info)

    def test_empty_booking_data(self):
        """Test with empty booking data"""
        report_df, ax = task_func(self.future_date, self.empty_booking_info)
        self.assertEqual(report_df.shape[0], 5)
        self.assertEqual(report_df["Booking Status"].values.tolist(), ["Not Listed"] * 5)

    def test_incomplete_booking_data(self):
        """Test with incomplete booking data"""
        incomplete_booking_info = {"Room1": "Booked"}
        report_df, ax = task_func(self.future_date, incomplete_booking_info)
        self.assertEqual(report_df.shape[0], 5)
        self.assertEqual(report_df.loc[report_df["Room"] == "Room1", "Booking Status"].values[0], "Booked")
        self.assertEqual(report_df.loc[report_df["Room"] == "Room2", "Booking Status"].values[0], "Not Listed")

if __name__ == '__main__':
    unittest.main()