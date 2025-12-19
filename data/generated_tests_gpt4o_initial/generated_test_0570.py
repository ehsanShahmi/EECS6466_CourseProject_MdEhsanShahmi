import unittest
import json
import types
import inspect

# Provided prompt code
def task_func(f):
    """
    Inspects the given function 'f' and returns its specifications as a JSON string. This includes
    the function's name, arguments, default values, annotations in a string format, and a boolean
    indicating if it's a lambda function.

    Parameters:
    f (function): The function to inspect.

    Returns:
    str: A JSON string containing the function's specifications.

    Requirements:
    - inspect
    - types
    - json

    Examples:
    >>> def sample_function(x, y=2): return x + y
    >>> 'sample_function' in task_func(sample_function)
    True
    >>> def sample_function2(x, y=2): return x * y
    >>> 'sample_function2' in task_func(sample_function2)
    True
    """

    spec = inspect.getfullargspec(f)
    annotations = {k: v.__name__ if isinstance(v, type) else str(v) for k, v in spec.annotations.items()}

    info = {
        'function_name': f.__name__,
        'args': spec.args,
        'defaults': spec.defaults,
        'annotations': annotations,
        'is_lambda': isinstance(f, types.LambdaType)
    }

    return json.dumps(info)

# Test Suite
class TestTaskFunc(unittest.TestCase):

    def test_function_name(self):
        def sample_function(x, y=2): return x + y
        self.assertIn('sample_function', task_func(sample_function))

    def test_arguments(self):
        def sample_function(x, y=2): return x + y
        expected_args = ['x', 'y']
        self.assertEqual(json.loads(task_func(sample_function))['args'], expected_args)

    def test_default_values(self):
        def sample_function(x, y=2): return x + y
        expected_defaults = (2,)
        self.assertEqual(json.loads(task_func(sample_function))['defaults'], expected_defaults)

    def test_annotations(self):
        def sample_function(x: int, y: int = 2) -> int: return x + y
        expected_annotations = {'x': 'int', 'y': 'int', 'return': 'int'}
        self.assertEqual(json.loads(task_func(sample_function))['annotations'], expected_annotations)

    def test_lambda_function_detection(self):
        lambda_function = lambda x, y=2: x + y
        self.assertTrue(json.loads(task_func(lambda_function))['is_lambda'])
        
if __name__ == '__main__':
    unittest.main()