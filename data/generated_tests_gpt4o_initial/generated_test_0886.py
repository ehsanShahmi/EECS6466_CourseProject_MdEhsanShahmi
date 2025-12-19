import pandas as pd
import unittest
from collections import Counter

# Here is your prompt:
# 
# import pandas as pd
# from collections import Counter
# 
# def task_func(data):
#     """
#     Analyze a dictionary of student data to return a dataframe sorted by name and age in ascending order, 
#     the average score per student as a pandas Series, and the most common age as an integer.
#     
#     Parameters:
#     data (dict): A dictionary containing student data with three keys:
#         - 'Name': List of student names.
#         - 'Age': List of student ages.
#         - 'Score': List of student scores.
# 
#     Returns:
#     pd.DataFrame, pd.Series, int or None: 
#         - A dataframe sorted by 'Name' and 'Age' in ascending order.
#         - A series representing average scores indexed by student names.
#         - An integer representing the most common age or None if no data is available.
# 
#     Raises:
#     ValueError: If the dictionary does not have the required keys.
# 
#     Requirements:
#     - pandas
#     - collections
# 
#     Example:
#     >>> data = {
#     ...     'Name': ['Tom', 'Nick', 'John', 'Tom', 'John', 'John', 'Nick', 'Tom', 'John', 'Tom'],
#     ...     'Age': [20, 21, 19, 20, 19, 19, 21, 20, 19, 20],
#     ...     'Score': [85, 79, 92, 88, 90, 92, 81, 86, 90, 85]
#     ... }
#     >>> df, avg_scores, common_age = task_func(data)
#     >>> print(df)
#        Name  Age  Score
#     2  John   19     92
#     4  John   19     90
#     5  John   19     92
#     8  John   19     90
#     1  Nick   21     79
#     6  Nick   21     81
#     0   Tom   20     85
#     3   Tom   20     88
#     7   Tom   20     86
#     9   Tom   20     85
#     """

class TestStudentDataAnalysis(unittest.TestCase):

    def test_correct_output(self):
        data = {
            'Name': ['Tom', 'Nick', 'John', 'Tom', 'John', 'John', 'Nick', 'Tom', 'John', 'Tom'],
            'Age': [20, 21, 19, 20, 19, 19, 21, 20, 19, 20],
            'Score': [85, 79, 92, 88, 90, 92, 81, 86, 90, 85]
        }
        df, avg_scores, common_age = task_func(data)
        
        expected_df = pd.DataFrame({
            'Name': ['John', 'John', 'John', 'John', 'Nick', 'Nick', 'Tom', 'Tom', 'Tom', 'Tom'],
            'Age': [19, 19, 19, 19, 21, 21, 20, 20, 20, 20],
            'Score': [92, 90, 92, 90, 79, 81, 85, 88, 86, 85]
        }).sort_values(['Name', 'Age'])
        expected_avg_scores = pd.Series({'John': 90.75, 'Nick': 80.0, 'Tom': 86.0})
        expected_common_age = 19
        
        pd.testing.assert_frame_equal(df.reset_index(drop=True), expected_df.reset_index(drop=True))
        pd.testing.assert_series_equal(avg_scores, expected_avg_scores)
        self.assertEqual(common_age, expected_common_age)

    def test_empty_data(self):
        data = {
            'Name': [],
            'Age': [],
            'Score': []
        }
        df, avg_scores, common_age = task_func(data)
        
        expected_df = pd.DataFrame(columns=['Name', 'Age', 'Score'])
        expected_avg_scores = pd.Series(dtype=float)
        expected_common_age = None
        
        pd.testing.assert_frame_equal(df, expected_df)
        pd.testing.assert_series_equal(avg_scores, expected_avg_scores)
        self.assertIsNone(common_age)

    def test_missing_keys(self):
        data = {
            'Name': ['Tom', 'Nick'],
            'Score': [85, 79]
        }
        with self.assertRaises(ValueError):
            task_func(data)

    def test_single_entry(self):
        data = {
            'Name': ['Tom'],
            'Age': [20],
            'Score': [85]
        }
        df, avg_scores, common_age = task_func(data)
        
        expected_df = pd.DataFrame({
            'Name': ['Tom'],
            'Age': [20],
            'Score': [85]
        })
        expected_avg_scores = pd.Series({'Tom': 85.0})
        expected_common_age = 20
        
        pd.testing.assert_frame_equal(df.reset_index(drop=True), expected_df.reset_index(drop=True))
        pd.testing.assert_series_equal(avg_scores, expected_avg_scores)
        self.assertEqual(common_age, expected_common_age)

    def test_all_students_same_age(self):
        data = {
            'Name': ['Tom', 'Nick', 'John'],
            'Age': [20, 20, 20],
            'Score': [85, 79, 92]
        }
        df, avg_scores, common_age = task_func(data)
        
        expected_df = pd.DataFrame({
            'Name': ['John', 'Nick', 'Tom'],
            'Age': [20, 20, 20],
            'Score': [92, 79, 85]
        }).sort_values(['Name'])
        
        expected_avg_scores = pd.Series({'John': 92.0, 'Nick': 79.0, 'Tom': 85.0})
        expected_common_age = 20
        
        pd.testing.assert_frame_equal(df.reset_index(drop=True), expected_df.reset_index(drop=True))
        pd.testing.assert_series_equal(avg_scores, expected_avg_scores)
        self.assertEqual(common_age, expected_common_age)

if __name__ == '__main__':
    unittest.main()