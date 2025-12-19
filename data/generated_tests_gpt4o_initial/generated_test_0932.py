from collections import Counter
import re
import unittest

def task_func(word: str) -> list:
    """
    Finds the most common two-letter combination in a given, cleaned word (lowercased and alphabetic characters only) 
    and returns its frequency. The search is case-insensitive and ignores non-alphabetic characters.
    
    Requirements:
    - collections.Counter
    - re
    
    Parameters:
    - word (str): The input string containing the word to analyze. The word should have a length of at least 2 to form pairs.
    
    Returns:
    - list: A list containing a single tuple. The tuple consists of the most frequent two-letter combination (str) 
      and its frequency (int). Returns an empty list if the word has fewer than 2 letters, or after cleaning, 
      the word has fewer than 2 alphabetic characters.
    
    Examples:
    >>> task_func("aaBBcc")
    [('aa', 1)]
    >>> task_func("abc!abc")
    [('ab', 2)]
    >>> task_func("a")
    []
    >>> task_func("abcd")
    [('ab', 1)]
    >>> task_func("a1b2c3")
    [('ab', 1)]
    """
    # Clean the word: lowercase and keep alphabetic characters only
    clean_word = re.sub('[^a-z]', '', word.lower())
    
    if len(clean_word) < 2:
        return []
    
    pairs = [clean_word[i:i+2] for i in range(len(clean_word) - 1)]
    pair_counter = Counter(pairs)
    most_common = pair_counter.most_common(1)
    
    return most_common

class TestTaskFunc(unittest.TestCase):

    def test_mixed_case_with_special_characters(self):
        self.assertEqual(task_func("aaBBcc"), [('aa', 1)])

    def test_repeated_pairs(self):
        self.assertEqual(task_func("abc!abc"), [('ab', 2)])

    def test_single_character_input(self):
        self.assertEqual(task_func("a"), [])

    def test_no_pairs_input(self):
        self.assertEqual(task_func("abcd"), [('ab', 1)])

    def test_numbers_in_input(self):
        self.assertEqual(task_func("a1b2c3"), [('ab', 1)])

if __name__ == '__main__':
    unittest.main()