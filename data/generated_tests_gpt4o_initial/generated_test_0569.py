import unittest
import inspect
import types
import math

def task_func(f):
    """
    Analyzes a given function 'f' and returns a dictionary containing its name, the square root of
    the number of arguments, and the count of lambda functions present in its default values.
    This function demonstrates introspection of Python functions and the use of mathematical
    operations on the introspected data.

    Parameters:
    f (function): The function to inspect.

    Returns:
    dict: A dictionary containing the function's name, the square root of the number of arguments,
          and the count of lambda functions in default values.

    Requirements:
    - inspect
    - types
    - math
    """
    spec = inspect.getfullargspec(f)

    info = {
        'function_name': f.__name__,
        'sqrt_args': math.sqrt(len(spec.args)),
    }

    if spec.defaults:
        info['lambda_in_defaults'] = sum(1 for d in spec.defaults if isinstance(d, types.LambdaType))
    else:
        info['lambda_in_defaults'] = 0

    return info

class TestTaskFunc(unittest.TestCase):

    def test_no_arguments(self):
        # Test a function with no arguments
        def no_arg_func():
            return "No arguments"
        result = task_func(no_arg_func)
        self.assertEqual(result['function_name'], 'no_arg_func')
        self.assertEqual(result['sqrt_args'], math.sqrt(0))
        self.assertEqual(result['lambda_in_defaults'], 0)

    def test_single_argument(self):
        # Test a function with one argument
        def single_arg_func(x):
            return x
        result = task_func(single_arg_func)
        self.assertEqual(result['function_name'], 'single_arg_func')
        self.assertEqual(result['sqrt_args'], math.sqrt(1))
        self.assertEqual(result['lambda_in_defaults'], 0)

    def test_multiple_arguments_with_defaults(self):
        # Test a function with multiple arguments and default values
        def multi_arg_func(x, y=2, z=3):
            return x + y + z
        result = task_func(multi_arg_func)
        self.assertEqual(result['function_name'], 'multi_arg_func')
        self.assertEqual(result['sqrt_args'], math.sqrt(3))
        self.assertEqual(result['lambda_in_defaults'], 0)

    def test_lambda_default_argument(self):
        # Test a function with a lambda function as a default argument
        def func_with_lambda(x, y=lambda: 10):
            return x + y()
        result = task_func(func_with_lambda)
        self.assertEqual(result['function_name'], 'func_with_lambda')
        self.assertEqual(result['sqrt_args'], math.sqrt(2))
        self.assertEqual(result['lambda_in_defaults'], 1)

    def test_multiple_lambda_defaults(self):
        # Test a function with multiple default arguments, including lambda functions
        def func_multiple_lambdas(a=1, b=lambda x: x * 2, c=lambda: 5):
            return a + b(2) + c()
        result = task_func(func_multiple_lambdas)
        self.assertEqual(result['function_name'], 'func_multiple_lambdas')
        self.assertEqual(result['sqrt_args'], math.sqrt(3))
        self.assertEqual(result['lambda_in_defaults'], 2)

if __name__ == '__main__':
    unittest.main()