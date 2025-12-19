from collections import Counter
from operator import itemgetter
import itertools
import unittest

#CONSTANT
ANIMAL = ['cat', 'camel', 'cow', 'dog', 'elephant', 'fox', 'giraffe', 'hippo', 'iguana', 'jaguar']

def task_func(animal_dict):
    """
    Given a dictionary of animals as keys and letters as values, count the frequency of each letter in the animals.
    
    Note:
    - Remove key in the dictionary if it is not an animal from ANIMAL constant

    Parameters:
    animal_dict (dict): The dictionary with animals as keys and their letters as values.
    
    Returns:
    dict: A dictionary with letters as keys and their frequencies as values, sorted in descending order by frequency. Format: {letter: frequency}.
    
    Requirements:
    - collections.Counter
    - operator.itemgetter
    - itertools
    
    Example:
    >>> animal_dict = {'cat': 'c', 'dog': 'd', 'elephant': 'e', 'fox': 'f', 'giraffe': 'g', 'hippo': 'h', 'iguana': 'i', 'jaguar': 'j'}
    >>> counts = task_func(animal_dict)
    >>> print(counts)
    {'a': 7, 'g': 4, 'o': 3, 'e': 3, 'p': 3, 'f': 3, 'i': 3, 't': 2, 'h': 2, 'n': 2, 'r': 2, 'u': 2, 'c': 1, 'd': 1, 'l': 1, 'x': 1, 'j': 1}
    """

    animal_dict_copy = {}
    for i in animal_dict:
        if i in ANIMAL:
            animal_dict_copy[i] = animal_dict[i]
    letters = list(itertools.chain.from_iterable(animal_dict_copy.keys()))
    count_dict = dict(Counter(letters))
    
    sorted_dict = dict(sorted(count_dict.items(), key=itemgetter(1), reverse=True))
    
    return sorted_dict

class TestAnimalLetterFrequency(unittest.TestCase):
    
    def test_empty_dict(self):
        self.assertEqual(task_func({}), {})
        
    def test_no_valid_animals(self):
        animal_dict = {'lion': 'l', 'tiger': 't', 'zebra': 'z'}
        self.assertEqual(task_func(animal_dict), {})
    
    def test_valid_animals_with_repeated_letters(self):
        animal_dict = {'cat': 'c', 'dog': 'd', 'elephant': 'e', 'fox': 'f'}
        expected_result = {'e': 2, 'c': 1, 'd': 1, 'f': 1}
        self.assertEqual(task_func(animal_dict), expected_result)
    
    def test_mixed_valid_and_invalid_animals(self):
        animal_dict = {'cat': 'c', 'dog': 'd', 'lion': 'l', 'elephant': 'e'}
        expected_result = {'e': 2, 'c': 1, 'd': 1}
        self.assertEqual(task_func(animal_dict), expected_result)

    def test_all_animals(self):
        animal_dict = {'cat': 'c', 'camel': 'c', 'cow': 'o', 'dog': 'd', 
                       'elephant': 'e', 'fox': 'f', 'giraffe': 'g', 
                       'hippo': 'h', 'iguana': 'i', 'jaguar': 'j'}
        expected_result = {'a': 6, 'g': 4, 'o': 3, 'e': 3, 'i': 3, 'h': 2, 
                           'd': 1, 'c': 1, 'f': 1, 'j': 1}
        self.assertEqual(task_func(animal_dict), expected_result)

if __name__ == '__main__':
    unittest.main()