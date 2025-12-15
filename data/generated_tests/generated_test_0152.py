import pandas as pd
import numpy as np
from random import randint
import unittest

# Constants
STUDENTS = ['Joe', 'Amy', 'Mark', 'Sara', 'John', 'Emily', 'Zoe', 'Matt']
COURSES = ['Math', 'Physics', 'Chemistry', 'Biology', 'English', 'History', 'Geography', 'Computer Science']

def task_func():
    """
    Generates a DataFrame containing random grades for a predefined list of students across a set of courses.
    Each student will have one grade per course and an average grade calculated across all courses.
    
    Returns:
    DataFrame: A pandas DataFrame with columns for each student's name, their grades for each course,
               and their average grade across all courses.
    
    Requirements:
    - pandas
    - numpy
    - random
    
    Note:
    The grades are randomly generated for each course using a uniform distribution between 0 and 100.
    """
    students_data = []

    for student in STUDENTS:
        grades = [randint(0, 100) for _ in COURSES]
        average_grade = np.mean(grades)
        students_data.append([student] + grades + [average_grade])

    columns = ['Name'] + COURSES + ['Average Grade']
    grades_df = pd.DataFrame(students_data, columns=columns)

    return grades_df

class TestTaskFunc(unittest.TestCase):

    def test_return_type(self):
        result = task_func()
        self.assertIsInstance(result, pd.DataFrame)

    def test_correct_columns(self):
        result = task_func()
        expected_columns = ['Name'] + COURSES + ['Average Grade']
        self.assertListEqual(list(result.columns), expected_columns)

    def test_number_of_students(self):
        result = task_func()
        self.assertEqual(len(result), len(STUDENTS))

    def test_grades_range(self):
        result = task_func()
        for grade in result.iloc[:, 1:-1].values.flatten():
            self.assertGreaterEqual(grade, 0)
            self.assertLessEqual(grade, 100)

    def test_average_grade_computation(self):
        result = task_func()
        for index, row in result.iterrows():
            grades = row[1:-1].values
            average_grade = np.mean(grades)
            self.assertAlmostEqual(row['Average Grade'], average_grade, places=2)

if __name__ == '__main__':
    unittest.main()