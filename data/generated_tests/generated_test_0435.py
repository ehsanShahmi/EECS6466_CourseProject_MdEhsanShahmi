import pandas as pd
import unittest

# Here is your prompt:
import pandas as pd
from random import randint


def task_func(name: str, age: int, code: str, salary: float, bio: str) -> pd.DataFrame:
    """
    Generate a Pandas DataFrame of employees with their details based on the input provided.

    Parameters:
    - name (str): Name of the employee. This is case-sensitive. Must be one of the predefined
                  names: 'John', 'Alice', 'Bob', 'Charlie', 'David', otherwise the function raises
                  ValueError.
    - age (int): Age of the employee.
    - code (str): Code of the employee.
    - salary (float): Salary of the employee.
    - bio (str): Biography of the employee.

    Returns:
    data_df (pd.DataFrame): dataframe with columns: 'Name', 'Age', 'Code', 'Salary', 'Bio', 'Job Title'.
               The 'Job Title' is randomly assigned from the predefined job titles:
               'Engineer', 'Manager', 'Analyst', 'Developer', 'Tester'.

    Requirements:
    - pandas
    - random.randint

    Example:
    >>> random.seed(0)
    >>> df = task_func("John", 30, "A10B", 5000.0, "This is a bio with spaces")
    >>> print(df)
       Name  Age  Code  Salary                        Bio  Job Title
    0  John   30  A10B  5000.0  This is a bio with spaces  Developer
    """

               EMPLOYEES = ["John", "Alice", "Bob", "Charlie", "David"]
    JOBS = ["Engineer", "Manager", "Analyst", "Developer", "Tester"]

    if name not in EMPLOYEES:
        raise ValueError(f"Invalid employee name. Must be one of {EMPLOYEES}")

    job = JOBS[randint(0, len(JOBS) - 1)]
    data_df = pd.DataFrame(
        [[name, age, code, salary, bio, job]],
        columns=["Name", "Age", "Code", "Salary", "Bio", "Job Title"],
    )
    return data_df

class TestTaskFunc(unittest.TestCase):
    
    def test_valid_employee(self):
        df = task_func("John", 30, "A10B", 5000.0, "This is a bio")
        self.assertEqual(df.shape, (1, 6))
        self.assertEqual(df.at[0, 'Name'], "John")
        self.assertEqual(df.at[0, 'Age'], 30)
        self.assertEqual(df.at[0, 'Code'], "A10B")
        self.assertEqual(df.at[0, 'Salary'], 5000.0)
        self.assertEqual(df.at[0, 'Bio'], "This is a bio")
        
    def test_invalid_employee_name(self):
        with self.assertRaises(ValueError) as context:
            task_func("InvalidName", 30, "A10B", 5000.0, "This is a bio")
        self.assertTrue("Invalid employee name" in str(context.exception))
        
    def test_age_type(self):
        with self.assertRaises(TypeError):
            task_func("Alice", "Twenty", "A10B", 5000.0, "This is a bio")
        
    def test_salary_type(self):
        with self.assertRaises(TypeError):
            task_func("Bob", 30, "A10B", "Five Thousand", "This is a bio")
        
    def test_random_job_title(self):
        df1 = task_func("Charlie", 28, "C20D", 6000.0, "Charlie bio")
        df2 = task_func("David", 35, "D30E", 7000.0, "David bio")
        self.assertIn(df1.at[0, 'Job Title'], ["Engineer", "Manager", "Analyst", "Developer", "Tester"])
        self.assertIn(df2.at[0, 'Job Title'], ["Engineer", "Manager", "Analyst", "Developer", "Tester"])

if __name__ == '__main__':
    unittest.main()