import unittest
import random
import string
from matplotlib import pyplot as plt

def task_func(elements, seed=100):
    """
    Format each string in the given list "elements" into a pattern "% {0}%", 
    where {0} is a randomly generated alphanumeric string of length 5. Additionally,
    return the plot axes of an histogram of the occurrence of each character across 
    all the strings and a dictionary containing the count of each character in all 
    the formatted strings.
    
    Parameters:
    elements (List[str]): A list of string elements to be formatted.
    seed (int, Optional): The seed for the random number generator. Defaults to 100.
    
    Returns:
    List[str]: A list of elements formatted with random patterns.
    plt.Axes: The axes object of the histogram plot.
    dict: A dictionary containing the count of each character in the formatted strings.
    
    Requirements:
    - random
    - string
    - matplotlib.pyplot
    
    Example:
    >>> patterns, ax, counts = task_func(['abc', 'def'])
    >>> patterns
    ['% jCVRT%', '% AXHeC%']
    >>> counts
    {'%': 4, ' ': 2, 'j': 1, 'C': 2, 'V': 1, 'R': 1, 'T': 1, 'A': 1, 'X': 1, 'H': 1, 'e': 1}
    """

    random.seed(seed)
    random_patterns = []

    for element in elements:
        random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        pattern = '% {}%'.format(random_str)
        random_patterns.append(pattern)

    # Histogram of character occurrences
    char_count = {}
    for pattern in random_patterns:
        for char in pattern:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
            
    # Getting the axes object for the histogram plot
    _, ax = plt.subplots()
    ax.bar(char_count.keys(), char_count.values())

    return random_patterns, ax, char_count


class TestTaskFunc(unittest.TestCase):

    def test_empty_input(self):
        patterns, ax, counts = task_func([])
        self.assertEqual(patterns, [])
        self.assertEqual(counts, {})

    def test_single_element(self):
        patterns, ax, counts = task_func(['test'])
        self.assertEqual(len(patterns), 1)
        self.assertIn('%', patterns[0])
        self.assertEqual(counts['%'], 2)  # 1 for starting '%', 1 for ending '%'

    def test_multiple_elements(self):
        elements = ['one', 'two', 'three']
        patterns, ax, counts = task_func(elements)
        self.assertEqual(len(patterns), len(elements))
        self.assertTrue(all(['%' in p for p in patterns]))

    def test_character_count(self):
        elements = ['abc', 'def']
        patterns, ax, counts = task_func(elements)
        total_count = sum(counts.values())
        self.assertEqual(total_count, 4 + len(patterns) * 5)  # 4 % + 5 chars for each pattern

    def test_fixed_seed_output(self):
        random.seed(100)
        expected_patterns = task_func(['abc', 'def'])[0]
        random.seed(100)
        actual_patterns = task_func(['abc', 'def'])[0]
        self.assertEqual(expected_patterns, actual_patterns)


if __name__ == '__main__':
    unittest.main()