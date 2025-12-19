import string
import random
import re
import unittest

def task_func(elements, pattern, seed=100):
    """
    Replace each character in each element of the Elements list with a random 
    character and format the element into a pattern "%{0}%", where {0} is the
    replaced element. Finally, concatenate all the formatted elements into a 
    single string and search for the regex pattern specified in the parameter 
    pattern. Return the true or false value based on the search result.
        
    Parameters:
        elements (List[str]): The list of elements.
        pattern (str): The pattern to format the elements.
        seed (int, Optional): The seed for the random number generator. Defaults to 100.
    
    Returns:    
        List[str]: The list of formatted elements with replaced characters.
        bool: The search result based on the regex pattern.
        
    Requirements:
        - re
        - string
        - random
        
    Example:
    >>> ELEMENTS = ["abc", "def"]
    >>> pattern = ".*"
    >>> replaced_elements, result = task_func(ELEMENTS, pattern, 234)
    >>> print(replaced_elements)
    ['%vqd%', '%LAG%']
    """

    # Set the seed for reproducibility
    random.seed(seed)
    replaced_elements = []
    
    for element in elements:
        replaced = ''.join([random.choice(string.ascii_letters) for _ in element])
        formatted = '%{}%'.format(replaced)
        replaced_elements.append(formatted)
        
    # Concatenate all the formatted elements into a single string
    concatenated_elements = ''.join(replaced_elements)
    # Search for the regex pattern in the concatenated string
    search_result = re.search(pattern, concatenated_elements)
    # Return the search result
    return replaced_elements, bool(search_result)

class TestTaskFunc(unittest.TestCase):

    def test_empty_elements(self):
        elements = []
        pattern = ".*"
        replaced_elements, result = task_func(elements, pattern)
        self.assertEqual(replaced_elements, [])
        self.assertFalse(result)

    def test_single_element_empty_pattern(self):
        elements = ["abc"]
        pattern = ""
        replaced_elements, result = task_func(elements, pattern)
        self.assertEqual(len(replaced_elements), 1)
        self.assertTrue(result)

    def test_single_element_non_empty_pattern(self):
        elements = ["abc"]
        pattern = "^%.*%$"  # Pattern to match any formatted element
        replaced_elements, result = task_func(elements, pattern)
        self.assertEqual(len(replaced_elements), 1)
        self.assertTrue(result)

    def test_multiple_elements_pattern(self):
        elements = ["a", "b", "c"]
        pattern = "^%[a-zA-Z]{1}%$"  # Pattern to match single character formatted elements
        replaced_elements, result = task_func(elements, pattern)
        self.assertTrue(all(len(e) == 3 and e[0] == '%' and e[-1] == '%' for e in replaced_elements))
        self.assertTrue(result)

    def test_pattern_not_matched(self):
        elements = ["abc", "def"]
        pattern = "xyz"  # Pattern that won't match anything
        replaced_elements, result = task_func(elements, pattern)
        self.assertEqual(len(replaced_elements), 2)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()