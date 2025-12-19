import unittest
import string
import wordninja

def task_func(word):
    """
    Converts a word into a list of tuples, with each tuple containing a lowercase English letter from the word and its position in the alphabet.
    Then, split the given word into a list of words.
    
    Requirements:
    - string
    - wordninja
    
    Parameters:
    - word (str): A string composed of lowercase letters.
    
    Returns:
    - list of tuples: Each tuple consists of a letter from the input string and its corresponding position in the alphabet.
    
    Examples:
    >>> task_func('abc')
    ([('a', 1), ('b', 2), ('c', 3)], ['abc'])
    >>> task_func('howistheweathertoday')
    ([('h', 8), ('o', 15), ('w', 23), ('i', 9), ('s', 19), ('t', 20), ('h', 8), ('e', 5), ('w', 23), ('e', 5), ('a', 1), ('t', 20), ('h', 8), ('e', 5), ('r', 18), ('t', 20), ('o', 15), ('d', 4), ('a', 1), ('y', 25)], ['how', 'is', 'the', 'weather', 'today'])
    """
    ALPHABET = list(string.ascii_lowercase)
    # Map each letter in the word to its corresponding alphabetical number
    word_numbers = [ALPHABET.index(letter) + 1 for letter in word]
    
    # Combine each letter with its alphabetical number in a tuple
    return [(word[i], word_numbers[i]) for i in range(len(word))],  wordninja.split(word)

class TestTaskFunc(unittest.TestCase):
    
    def test_single_word(self):
        result = task_func('abc')
        expected = ([('a', 1), ('b', 2), ('c', 3)], ['abc'])
        self.assertEqual(result, expected)

    def test_howistheweathertoday(self):
        result = task_func('howistheweathertoday')
        expected = ([('h', 8), ('o', 15), ('w', 23), ('i', 9), ('s', 19), ('t', 20), 
                      ('h', 8), ('e', 5), ('w', 23), ('e', 5), ('a', 1), ('t', 20), 
                      ('h', 8), ('e', 5), ('r', 18), ('t', 20), ('o', 15), ('d', 4), 
                      ('a', 1), ('y', 25)], ['how', 'is', 'the', 'weather', 'today'])
        self.assertEqual(result, expected)

    def test_empty_string(self):
        result = task_func('')
        expected = ([], [])
        self.assertEqual(result, expected)

    def test_single_letter(self):
        result = task_func('z')
        expected = ([('z', 26)], ['z'])
        self.assertEqual(result, expected)

    def test_compound_word(self):
        result = task_func('wordninja')
        expected = ([('w', 23), ('o', 15), ('r', 18), ('d', 4), ('n', 14), ('i', 9), 
                      ('n', 14), ('j', 10), ('a', 1)], ['word', 'ninja'])
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()