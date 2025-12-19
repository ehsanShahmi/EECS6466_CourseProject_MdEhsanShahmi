import unittest
import pandas as pd
from random import seed

# Here is your prompt:
import pandas as pd
from itertools import cycle
from random import randint, seed


def task_func(
    n_grades,
    students=['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    grade_range=range(1, 11),
    rng_seed=None
):
    """
    Generates a grade report for a specified number of grades.
    The function cycles through the given list of students, assigning each a
    random grade from a predefined range, and compiles this information into
    a pandas DataFrame.
    The random grades can be made reproducable by providing a seed in 'rng_seed'.

    Parameters:
    n_grades (int): The number of grades to include in the report.
    students (list of str): The students to include in the report. Defaults to ['Alice', 'Bob', 'Charlie', 'David', 'Eve'].
    grade_range (range): The range of grades that can be assigned. Defaults to range(1, 11).
    rng_seed (int, optional): Seed used in the generation of random integers.
    
    Returns:
    DataFrame: A pandas DataFrame with two columns: 'Student' and 'Grade'. Each row represents a student's grade.

    Raises:
    ValueError: If list of students is empty.

    Requirements:
    - pandas
    - itertools
    - random

    Example:
    >>> grade_report = task_func(3, ['Alice', 'Bob'], range(1, 3), rng_seed=1)
    >>> print(grade_report)
      Student  Grade
    0   Alice      1
    1     Bob      1
    2   Alice      2

    >>> grade_report = task_func(5, rng_seed=12)
    >>> print(grade_report)
       Student  Grade
    0    Alice      8
    1      Bob      5
    2  Charlie      9
    3    David      6
    4      Eve      3
    """

class TestTaskFunc(unittest.TestCase):

    def test_generate_grades_correct_length(self):
        """Test that the generated DataFrame is of the correct length."""
        result = task_func(5)
        self.assertEqual(len(result), 5)

    def test_students_list_not_empty(self):
        """Test that ValueError is raised when the students list is empty."""
        with self.assertRaises(ValueError):
            task_func(5, students=[])

    def test_grades_in_range(self):
        """Test that all generated grades are within the specified range."""
        n_grades = 10
        grade_range = range(1, 6)  # Grades between 1 and 5
        result = task_func(n_grades, grade_range=grade_range)

        for grade in result['Grade']:
            self.assertGreaterEqual(grade, min(grade_range))
            self.assertLessEqual(grade, max(grade_range))

    def test_cycles_through_students(self):
        """Test that the function cycles correctly through the students."""
        students = ['Alice', 'Bob']
        result = task_func(4, students=students)
        
        expected_students = ['Alice', 'Bob', 'Alice', 'Bob']
        self.assertListEqual(result['Student'].tolist(), expected_students)

    def test_reproducibility_with_seed(self):
        """Test that the function produces the same output with a set seed."""
        seed_value = 42
        result1 = task_func(5, rng_seed=seed_value)
        result2 = task_func(5, rng_seed=seed_value)

        pd.testing.assert_frame_equal(result1, result2)

if __name__ == '__main__':
    unittest.main()