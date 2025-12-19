import unittest
import inspect
import types

def task_func(f):
    """
    Inspects a given function 'f' and returns its specifications, including the function's name,
    whether it is a lambda function, its arguments, defaults, and annotations. This method
    utilizes the inspect and types modules to introspect function properties.

    Parameters:
    f (function): The function to inspect.

    Returns:
    dict: A dictionary containing details about the function, such as its name, if it's a lambda function,
          arguments, default values, and annotations.

    Requirements:
    - inspect
    - types

    Examples:
    >>> def sample_function(x, y=5): return x + y
    >>> result = task_func(sample_function)
    >>> 'sample_function' == result['function_name'] and len(result['args']) == 2
    True
    >>> lambda_func = lambda x: x * 2
    >>> task_func(lambda_func)['is_lambda']
    True
    """

    spec = inspect.getfullargspec(f)

    return {
        'function_name': f.__name__,
        'is_lambda': isinstance(f, types.LambdaType),
        'args': spec.args,
        'defaults': spec.defaults,
        'annotations': spec.annotations
    }

class TestTaskFunc(unittest.TestCase):
    
    def test_regular_function(self):
        def sample_function(x, y=5):
            return x + y
        
        expected = {
            'function_name': 'sample_function',
            'is_lambda': False,
            'args': ['x', 'y'],
            'defaults': (5,),
            'annotations': {}
        }
        
        result = task_func(sample_function)
        self.assertEqual(result, expected)

    def test_lambda_function(self):
        lambda_func = lambda x: x * 2
        
        expected = {
            'function_name': '<lambda>',
            'is_lambda': True,
            'args': ['x'],
            'defaults': None,
            'annotations': {}
        }
        
        result = task_func(lambda_func)
        self.assertEqual(result, expected)

    def test_function_with_annotations(self):
        def annotated_function(a: int, b: str = 'default') -> None:
            pass
        
        expected = {
            'function_name': 'annotated_function',
            'is_lambda': False,
            'args': ['a', 'b'],
            'defaults': ('default',),
            'annotations': {'a': int, 'b': str, 'return': None}
        }
        
        result = task_func(annotated_function)
        self.assertEqual(result, expected)

    def test_function_with_no_arguments(self):
        def no_arg_function():
            return "No arguments"
        
        expected = {
            'function_name': 'no_arg_function',
            'is_lambda': False,
            'args': [],
            'defaults': None,
            'annotations': {}
        }
        
        result = task_func(no_arg_function)
        self.assertEqual(result, expected)

    def test_method_in_class(self):
        class MyClass:
            def method(self, x, y=10):
                return x + y
        
        expected = {
            'function_name': 'method',
            'is_lambda': False,
            'args': ['self', 'x', 'y'],
            'defaults': (10,),
            'annotations': {}
        }
        
        result = task_func(MyClass.method)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()