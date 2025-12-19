import pandas as pd
import random
import statistics
import unittest

def task_func(students, subjects, seed=None):
    """
    Create a grade report for a list of students across various subjects. Each student's grades are randomly generated, 
    and the report includes the average grade for each student. The randomness is seeded for reproducibility if a seed is provided.

    Parameters:
    students (list of str): The students for whom the report is being generated.
    subjects (list of str): The subjects included in the report.
    seed (int, optional): A seed for the random number generator to ensure reproducibility. If None, the randomness is seeded by the system.

    Returns:
    DataFrame: A pandas DataFrame containing each student's grades across the subjects and their average grade. 
               Columns are ['Student', 'Subject1', 'Subject2', ..., 'Average Grade'].
    """
    if seed is not None:
        random.seed(seed)

    report_data = []

    for student in students:
        grades = [random.randint(0, 100) for _ in subjects]
        avg_grade = statistics.mean(grades)
        report_data.append((student,) + tuple(grades) + (avg_grade,))

    report_df = pd.DataFrame(report_data, columns=['Student'] + subjects + ['Average Grade'])

    return report_df

class TestTaskFunc(unittest.TestCase):

    def test_empty_students(self):
        """Test the function with an empty list of students."""
        report = task_func([], ['Math', 'English'], seed=1)
        self.assertTrue(report.empty)

    def test_single_student(self):
        """Test the function with a single student."""
        report = task_func(['Alice'], ['Math', 'English'], seed=1)
        self.assertEqual(len(report), 1)
        self.assertEqual(report.iloc[0]['Student'], 'Alice')
        self.assertEqual(len(report.columns), 3)  # 2 subjects + average grade

    def test_multiple_students(self):
        """Test the function with multiple students and subjects."""
        report = task_func(['Alice', 'Bob'], ['Math', 'English'], seed=1)
        self.assertEqual(len(report), 2)
        self.assertIn('Alice', report['Student'].values)
        self.assertIn('Bob', report['Student'].values)

    def test_average_calculation(self):
        """Test if the average grade calculation is correct."""
        report = task_func(['Alice'], ['Math', 'English'], seed=1)
        grades = report.iloc[0][1:-1].values  # Get only the grades
        avg_grade = statistics.mean(grades)
        self.assertAlmostEqual(report.iloc[0]['Average Grade'], avg_grade)

    def test_seed_reproducibility(self):
        """Test that the output is the same with the same seed."""
        report1 = task_func(['Alice'], ['Math', 'English'], seed=1)
        report2 = task_func(['Alice'], ['Math', 'English'], seed=1)
        pd.testing.assert_frame_equal(report1, report2)

if __name__ == '__main__':
    unittest.main()