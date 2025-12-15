import unittest
from collections import Counter

# Here is your prompt:
from collections import Counter
from itertools import chain

def task_func(list_of_lists):
    """
    Merge all sublists from a list of lists into a list and return a count of the elements.
    
    Parameters:
    - list_of_lists (list): The list to be processed.

    Returns:
    - collections.Counter: Counter object with the counts of the elements in the merged list.

    Requirements:
    - itertools
    - collections
    
    Example:
    >>> task_func([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1})
    """

    merged_list = list(chain.from_iterable(list_of_lists))
    return Counter(merged_list)

class TestTaskFunc(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(task_func([]), Counter())
    
    def test_single_empty_sublist(self):
        self.assertEqual(task_func([[]]), Counter())

    def test_single_non_empty_sublist(self):
        self.assertEqual(task_func([[1, 2, 3]]), Counter({1: 1, 2: 1, 3: 1}))

    def test_multiple_sublists_with_duplicates(self):
        self.assertEqual(task_func([[1, 2], [2, 3], [3, 4]]), Counter({2: 2, 1: 1, 3: 2, 4: 1}))

    def test_different_types(self):
        self.assertEqual(task_func([[1, 'a', 2], [2, 'b', 1]]), Counter({1: 2, 2: 2, 'a': 1, 'b': 1}))

if __name__ == '__main__':
    unittest.main()