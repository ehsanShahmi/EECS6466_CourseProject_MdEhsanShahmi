import inspect
import pandas as pd
import unittest
import os

# Here is your prompt:

def task_func(f_list, file_path):
    """
    Exports the specifications of functions in 'f_list' to a CSV file at 'file_path'.

    The CSV file columns are as follows:
    - 'Function Name': The name of the function.
    - 'Number of Arguments': The number of arguments the function takes.
    - 'Defaults': Default values for the function's arguments, if any.
    - 'Annotations': Type annotations of the function's arguments and return value, if any.
    - 'Is Lambda': Boolean value indicating whether the function is a lambda function.

    Each row in the CSV file corresponds to a function in 'f_list'.

    Parameters:
    f_list (list): A list of function objects to inspect. Each element should be a callable object.
    file_path (str): The path (including filename) where the CSV file will be saved. Should be a writable path.

    Returns:
    None

    Requirements:
    - inspect
    - pandas

    Raises:
    - ValueError: If 'f_list' is not a list of functions, 'f_list' is empty, or 'file_path' is not a valid path.
    - IOError: If there's an error in writing to the specified file path.

    Example:
    >>> def f(x): return 2 * x
    >>> def g(x, y=2): return x * y
    >>> task_func([f, g], './function_info.csv')
    >>> os.remove('./function_info.csv')
    """

    if not all(callable(f) for f in f_list):
        raise ValueError("All elements in f_list must be callable functions.")
    if not f_list:
        raise ValueError("f_list should not be empty.")
    if not isinstance(file_path, str):
        raise ValueError("file_path must be a string.")

    func_info = []
    for f in f_list:
        spec = inspect.getfullargspec(f)
        is_lambda = lambda x: x.__name__ == (lambda: None).__name__
        func_info.append([
            f.__name__, 
            len(spec.args), 
            spec.defaults, 
            spec.annotations, 
            is_lambda(f)
        ])

    df = pd.DataFrame(func_info, columns=['Function Name', 'Number of Arguments', 'Defaults', 'Annotations', 'Is Lambda'])
    try:
        df.to_csv(file_path, index=False)
    except IOError as e:
        raise IOError(f"Error writing to file: {e}")

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.test_file_path = './test_function_info.csv'
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def tearDown(self):
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_empty_function_list(self):
        with self.assertRaises(ValueError) as context:
            task_func([], self.test_file_path)
        self.assertEqual(str(context.exception), "f_list should not be empty.")

    def test_non_callable_in_function_list(self):
        with self.assertRaises(ValueError) as context:
            task_func([1, 2, 3], self.test_file_path)
        self.assertEqual(str(context.exception), "All elements in f_list must be callable functions.")

    def test_invalid_file_path_type(self):
        def f(x): return x
        with self.assertRaises(ValueError) as context:
            task_func([f], 12345)
        self.assertEqual(str(context.exception), "file_path must be a string.")

    def test_correct_function_info_export(self):
        def f(x): return 2 * x
        def g(x, y=2): return x * y
        task_func([f, g], self.test_file_path)
        df = pd.read_csv(self.test_file_path)
        self.assertEqual(len(df), 2)
        self.assertEqual(df.iloc[0]['Function Name'], 'f')
        self.assertEqual(df.iloc[0]['Number of Arguments'], 1)
        self.assertEqual(df.iloc[1]['Function Name'], 'g')
        self.assertEqual(df.iloc[1]['Number of Arguments'], 2)

    def test_io_error_handling(self):
        def f(x): return x
        # Create a read-only file to trigger IOError
        with open(self.test_file_path, 'w') as f:
            f.write('test')
        os.chmod(self.test_file_path, 0o444)  # Make file read-only
        with self.assertRaises(IOError):
            task_func([f], self.test_file_path)
        os.chmod(self.test_file_path, 0o666)  # Restore file permissions
        os.remove(self.test_file_path)

if __name__ == '__main__':
    unittest.main()