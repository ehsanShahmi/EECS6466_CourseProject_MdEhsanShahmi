import unittest
import numpy as np
from sympy import symbols, solve

def task_func(precision=2, seed=0):
    """
    Solve a quadratic equation in the form of ax ^ 2 + bx + c = 0, where a, b, and c randomly generated numbers are between -10 and 10. The solutions are complex numbers rounded to the specified accuracy.

    Parameters:
    precision (int): The number of decimal places to which to round the solutions.
    seed (int, Optional): The seed for the random number generator.

    Returns:
    tuple: A tuple of two solutions formatted as complex numbers (rounded to the specified precision).

    Requirements:
    - numpy
    - math
    - sympy

    Example:
    >>> result = task_func()
    >>> len(result)
    2
    >>> result
    ((-3.86+0j), (-0.54+0j))
    """

    np.random.seed(seed)
    a = np.random.uniform(-10, 10)
    b = np.random.uniform(-10, 10)
    c = np.random.uniform(-10, 10)

    x = symbols('x')
    equation = a * x**2 + b * x + c

    solutions = solve(equation, x)
    solutions = [complex(round(complex(solution).real, precision), round(complex(solution).imag, precision)) for solution in solutions]

    return tuple(solutions)

class TestTaskFunc(unittest.TestCase):

    def test_solution_length(self):
        result = task_func()
        self.assertEqual(len(result), 2)

    def test_solution_type(self):
        result = task_func()
        self.assertIsInstance(result, tuple)
        self.assertTrue(all(isinstance(s, complex) for s in result))

    def test_precision(self):
        result = task_func(precision=3)
        self.assertTrue(all(len(str(s).split('.')[1]) <= 3 for s in result))

    def test_different_seeds(self):
        result1 = task_func(seed=42)
        result2 = task_func(seed=42)
        self.assertEqual(result1, result2)

    def test_negative_coefficients(self):
        result = task_func()
        a, b, c = np.random.uniform(-10, 0, 3)
        x = symbols('x')
        equation = a * x**2 + b * x + c
        solutions = solve(equation, x)
        expected_solutions = [complex(round(complex(solution).real, 2), round(complex(solution).imag, 2)) for solution in solutions]
        self.assertEqual(result, tuple(expected_solutions))

if __name__ == '__main__':
    unittest.main()