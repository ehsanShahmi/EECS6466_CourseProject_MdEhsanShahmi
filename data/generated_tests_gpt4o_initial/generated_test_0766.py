import re
import collections
import unittest

def task_func(string, patterns=['nnn', 'aaa', 'sss', 'ddd', 'fff']):
    """
    Counts the occurrence of specific patterns in a string.
    
    Parameters:
    string (str): The input string.
    patterns (list[str], optional): List of patterns to search for. Defaults to ['nnn', 'aaa', 'sss', 'ddd', 'fff'].
    
    Returns:
    dict: A dictionary with patterns as keys and their counts as values.

    Raises:
    - TypeError: If string is not a str.
    - TypeError: If patterns is not a list of str.
    
    Requirements:
    - re
    - collections
    
    Example:
    >>> task_func("nnnaaaasssdddeeefffggg")
    {'nnn': 1, 'aaa': 1, 'sss': 1, 'ddd': 1, 'fff': 1}
    >>> task_func('asdfasdfasdfasdaaaaf', patterns=['a', 'asdf'])
    {'a': 8, 'asdf': 3}
    >>> task_func('123kajhdlkfah12345k,jk123', patterns=['123', '1234'])
    {'123': 3, '1234': 1}
    """

           
    if not isinstance(string, str):
        raise TypeError("Input string should be of type string.")

    if not isinstance(patterns, list):
        raise TypeError("patterns should be a list of strings.")
    
    if not all(isinstance(s, str) for s in patterns):
        raise TypeError("patterns should be a list of strings.")

    

    pattern_counts = collections.defaultdict(int)

    for pattern in patterns:
        pattern_counts[pattern] = len(re.findall(pattern, string))

    return dict(pattern_counts)

class TestTaskFunc(unittest.TestCase):

    def test_basic_occurrences(self):
        result = task_func("nnnaaaasssdddeeefffggg")
        expected = {'nnn': 1, 'aaa': 1, 'sss': 1, 'ddd': 1, 'fff': 1}
        self.assertEqual(result, expected)

    def test_custom_patterns(self):
        result = task_func('asdfasdfasdfasdaaaaf', patterns=['a', 'asdf'])
        expected = {'a': 8, 'asdf': 3}
        self.assertEqual(result, expected)

    def test_multiple_occurrences(self):
        result = task_func('123kajhdlkfah12345k,jk123', patterns=['123', '1234'])
        expected = {'123': 3, '1234': 1}
        self.assertEqual(result, expected)

    def test_empty_string(self):
        result = task_func('', patterns=['nnn', 'aaa'])
        expected = {'nnn': 0, 'aaa': 0}
        self.assertEqual(result, expected)

    def test_malformed_input(self):
        with self.assertRaises(TypeError):
            task_func(123, patterns=['nnn'])

        with self.assertRaises(TypeError):
            task_func("valid string", patterns="not a list")

        with self.assertRaises(TypeError):
            task_func("valid string", patterns=[1, 2, 3])

if __name__ == '__main__':
    unittest.main()