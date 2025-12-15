import random
import statistics
import unittest

def task_func(LETTERS):
    """
    Create a dictionary in which keys are random letters and values are lists of random integers.
    The dictionary is then sorted by the mean of the values in descending order, demonstrating the use of the statistics library.
    
    Parameters:
        LETTERS (list of str): A list of characters used as keys for the dictionary.
    
    Returns:
    dict: The sorted dictionary with letters as keys and lists of integers as values, sorted by their mean values.
    
    Requirements:
    - random
    - statistics
    
    Example:
    >>> import random
    >>> random.seed(42)
    >>> sorted_dict = task_func(['a', 'b', 'c'])
    >>> list(sorted_dict.keys())
    ['a', 'b', 'c']
    >>> isinstance(sorted_dict['a'], list)
    True
    >>> type(sorted_dict['a'])  # Check type of values
    <class 'list'>
    """

    random_dict = {k: [random.randint(0, 100) for _ in range(random.randint(1, 10))] for k in LETTERS}
    sorted_dict = dict(sorted(random_dict.items(), key=lambda item: statistics.mean(item[1]), reverse=True))
    return sorted_dict

class TestTaskFunc(unittest.TestCase):
    
    def test_keys_are_correct(self):
        random.seed(42)  # Set seed for reproducibility
        result = task_func(['a', 'b', 'c'])
        self.assertCountEqual(result.keys(), ['a', 'b', 'c'], "Keys of the resulting dictionary do not match the input letters")

    def test_values_are_lists(self):
        random.seed(42)
        result = task_func(['a', 'b', 'c'])
        for key in result.keys():
            self.assertIsInstance(result[key], list, f"Values for key '{key}' should be of type list")
    
    def test_average_calculation(self):
        random.seed(42)
        result = task_func(['a', 'b', 'c'])
        for key, value in result.items():
            average = statistics.mean(value)
            self.assertAlmostEqual(average, sum(value) / len(value), "Mean calculation is incorrect")
    
    def test_sorted_by_mean(self):
        random.seed(42)
        result = task_func(['a', 'b', 'c'])
        means = {key: statistics.mean(value) for key, value in result.items()}
        sorted_means = sorted(means.items(), key=lambda item: item[1], reverse=True)
        self.assertListEqual(list(result.keys()), [key for key, _ in sorted_means], "The dictionary is not sorted by mean values in descending order")
    
    def test_values_contain_integers(self):
        random.seed(42)
        result = task_func(['a', 'b', 'c'])
        for value in result.values():
            self.assertTrue(all(isinstance(i, int) for i in value), "All elements in the value lists should be integers")

if __name__ == "__main__":
    unittest.main()