import random
import statistics
import unittest

# Constants
AGE_RANGE = (22, 60)

# Provided prompt with the function definition
def task_func(dict1):
    """
    Calculate the mean, the median, and the mode(s) of the age of the employees in the department "EMP$$." 
    Generate random ages for each employee within the range [22, 60].

    Parameters:
    dict1 (dict): A dictionary with department codes as keys and number of employees 
                  as values.

    Returns:
    tuple: A tuple of mean, median, and a list of mode(s) of employee ages.

    Requirements:
    - random
    - statistics

    Example:
    >>> random.seed(0)
    >>> d = {'EMP$$': 10, 'MAN$$': 5, 'DEV$$': 8, 'HR$$': 7}
    >>> stats = task_func(d)
    >>> print(stats)
    (44.7, 46.5, [46, 48, 24, 38, 54, 53, 47, 41, 52, 44])
    """

    emp_ages = []
    
    for prefix, num_employees in dict1.items():
        if not prefix.startswith('EMP$$'):
            continue

        for _ in range(num_employees):
            age = random.randint(*AGE_RANGE)
            emp_ages.append(age)

    # If no employees in EMP$$ department
    if not emp_ages:
        return 0, 0, []
    
    mean_age = statistics.mean(emp_ages)
    median_age = statistics.median(emp_ages)
    mode_age = statistics.multimode(emp_ages)

    return mean_age, median_age, mode_age

class TestTaskFunc(unittest.TestCase):

    def test_case_1(self):
        random.seed(1)
        d = {'EMP$$': 5, 'MAN$$': 2, 'DEV$$': 3}
        stats = task_func(d)
        self.assertEqual(len(stats), 3)
        self.assertIsInstance(stats[0], float)
        self.assertIsInstance(stats[1], float)
        self.assertIsInstance(stats[2], list)

    def test_case_2(self):
        random.seed(2)
        d = {'EMP$$': 0, 'MAN$$': 0}
        stats = task_func(d)
        self.assertEqual(stats, (0, 0, []))

    def test_case_3(self):
        random.seed(3)
        d = {'EMP$$': 10, 'DEV$$': 5}
        stats = task_func(d)
        self.assertGreater(stats[0], 22)
        self.assertLess(stats[0], 60)
        self.assertGreater(stats[1], 22)
        self.assertLess(stats[1], 60)

    def test_case_4(self):
        random.seed(4)
        d = {'EMP$$': 10}
        stats = task_func(d)
        # Check that the mode is from the range
        self.assertTrue(all(age in range(AGE_RANGE[0], AGE_RANGE[1] + 1) for age in stats[2]))

    def test_case_5(self):
        random.seed(5)
        d = {'OTHER$$': 5, 'EMP$$': 7, 'DEV$$': 2}
        stats = task_func(d)
        self.assertEqual(len(stats), 3)

if __name__ == '__main__':
    unittest.main()