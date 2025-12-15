import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import unittest

def task_func(student_grades, possible_grades=["A", "B", "C", "D", "F"]):
    if not student_grades:
        raise ValueError("student_grades cannot be empty")
    possible_grades = [*dict.fromkeys([g.upper() for g in possible_grades])]
    grade_counts = dict(Counter([g.upper() for g in student_grades]))
    report_data = {grade: grade_counts.get(grade, 0) for grade in possible_grades}
    report_df = pd.DataFrame.from_dict(report_data, orient="index", columns=["Count"])
    report_df.index.name = "Grade"

    ax = report_df.plot(kind="bar", legend=False, title="Grade Distribution")
    ax.set_ylabel("Number of Students")
    ax.set_xlabel("Grade")

    plt.tight_layout()

    return report_df, ax

class TestGradeReport(unittest.TestCase):

    def test_empty_grades(self):
        with self.assertRaises(ValueError):
            task_func([])

    def test_valid_grades(self):
        student_grades = ['A', 'B', 'B', 'C', 'A', 'D', 'F', 'B', 'A', 'C']
        report_df, ax = task_func(student_grades)
        self.assertEqual(report_df.loc['A', 'Count'], 3)
        self.assertEqual(report_df.loc['B', 'Count'], 3)
        self.assertEqual(report_df.loc['C', 'Count'], 2)
        self.assertEqual(report_df.loc['D', 'Count'], 1)
        self.assertEqual(report_df.loc['F', 'Count'], 1)

    def test_case_insensitivity(self):
        student_grades = ['a', 'B', 'b', 'C', 'a', 'D', 'f']
        report_df, ax = task_func(student_grades)
        self.assertEqual(report_df.loc['A', 'Count'], 2)
        self.assertEqual(report_df.loc['B', 'Count'], 2)
        self.assertEqual(report_df.loc['C', 'Count'], 1)
        self.assertEqual(report_df.loc['D', 'Count'], 1)
        self.assertEqual(report_df.loc['F', 'Count'], 1)

    def test_invalid_grades(self):
        student_grades = ['A', 'B', 'Z', 'A', 'Invalid', 'A']
        report_df, ax = task_func(student_grades)
        self.assertEqual(report_df.loc['A', 'Count'], 3)
        self.assertEqual(report_df.loc['B', 'Count'], 1)
        self.assertEqual(report_df.loc['C', 'Count'], 0)
        self.assertEqual(report_df.loc['D', 'Count'], 0)
        self.assertEqual(report_df.loc['F', 'Count'], 0)

    def test_custom_possible_grades(self):
        student_grades = ['A', 'B', 'B', 'C', 'A', 'D', 'B', 'A', 'C']
        possible_grades = ['A', 'B', 'C', 'D', 'E']
        report_df, ax = task_func(student_grades, possible_grades)
        self.assertEqual(report_df.loc['A', 'Count'], 3)
        self.assertEqual(report_df.loc['B', 'Count'], 3)
        self.assertEqual(report_df.loc['C', 'Count'], 2)
        self.assertEqual(report_df.loc['D', 'Count'], 1)
        self.assertEqual(report_df.loc['E', 'Count'], 0)

if __name__ == '__main__':
    unittest.main()