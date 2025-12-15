import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        self.students = ["Alice", "Bob", "Charlie", "David", "Eve"]
        self.seed = 42

    def test_function_return_type(self):
        """Test if the function returns a tuple containing a DataFrame and a matplotlib Axes."""
        scores, plot = task_func(self.students, self.seed)
        self.assertIsInstance(scores, pd.DataFrame, "The first return value should be a pandas DataFrame.")
        self.assertIsNotNone(plot, "The second return value should be a matplotlib Axes object.")

    def test_dataframe_shape(self):
        """Test if the DataFrame has the correct shape."""
        scores, plot = task_func(self.students, self.seed)
        self.assertEqual(scores.shape, (len(self.students), 2), "The shape of the DataFrame should be (number of students, 2).")

    def test_sorted_scores(self):
        """Test if the scores in the DataFrame are sorted in ascending order."""
        scores, plot = task_func(self.students, self.seed)
        sorted_scores = scores['Score'].sort_values().reset_index(drop=True)
        self.assertTrue((scores['Score'].reset_index(drop=True) == sorted_scores).all(), 
                        "Scores in the DataFrame are not sorted in ascending order.")

    def test_student_names_in_dataframe(self):
        """Test if all student names are present in the DataFrame."""
        scores, plot = task_func(self.students, self.seed)
        self.assertListEqual(sorted(scores['Student'].tolist()), sorted(self.students), 
                             "The DataFrame should contain all the student names.")

    def test_score_range(self):
        """Test if all scores are within the expected range."""
        scores, plot = task_func(self.students, self.seed)
        self.assertTrue((scores['Score'] >= 0).all() and (scores['Score'] < 100).all(), 
                        "All scores should be between 0 and 99.")

if __name__ == '__main__':
    unittest.main()