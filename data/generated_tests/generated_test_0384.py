import collections
import random
import itertools
import unittest

ANIMALS = ['Cat', 'Dog', 'Elephant', 'Lion', 'Tiger', 'Bear', 'Giraffe', 'Horse', 'Rabbit', 'Snake', 'Zebra']

def task_func(animal_dict, max_count=10, seed=0):
    """
    Given a constant list of animals in ANIMALS, and a dictionary 'animal_dict' with keys as people's names and values
    as their favorite animal names, reverse the keys and values in a given dictionary and count the occurrences of each
    predefined animal name with a random count. Return the reversed dictionary and the counter with animal name
    occurrences.
    
    This function performs two tasks:
    1. It reverses the given dictionary (animal_dict) such that the original values become keys and the original 
    keys become lists of values.
    2. It counts the occurrences of each animal name in a predefined list (ANIMALS). The count of each animal name
    is a random integer between 1 and max_count (inclusive).
    
    Parameters:
    animal_dict (dict): A dictionary with keys as names and values as animal names.
    max_count (int, Optional): A positive integer denoting the maximum count of each animal. Default is 10.
    Must be greater than 0.
    seed (int, Optional): An integer to seed the random number generator. Default is 0.
    
    Returns:
    tuple: A tuple where the first element is a reversed dictionary and the second element is a counter with animal 
           name occurrences (with randomness in count).
    
    Requirements:
    - collections
    - random
    - itertools
    
    Example:
    >>> animal_dict = {'John': 'Cat', 'Alice': 'Dog', 'Bob': 'Elephant', 'Charlie': 'Lion', 'David': 'Tiger', 'Sue': 'Pangolin'}
    >>> reversed_dict, animal_counter = task_func(animal_dict, 15, 77)
    >>> reversed_dict
    {'Cat': ['John'], 'Dog': ['Alice'], 'Elephant': ['Bob'], 'Lion': ['Charlie'], 'Tiger': ['David']}
    >>> dict(animal_counter.most_common(5))
    {'Giraffe': 14, 'Cat': 13, 'Zebra': 9, 'Snake': 8, 'Elephant': 6}
    """
    if max_count < 1:
        raise ValueError("max_count must be a positive integer")

    random.seed(seed)

    reversed_dict = {v: [] for v in animal_dict.values() if isinstance(v, str) and v in ANIMALS}
    for k, v in animal_dict.items():
        if isinstance(v, str) and v in ANIMALS:
            reversed_dict[v].append(k)

    animal_counter = collections.Counter(itertools.chain.from_iterable([[v] * random.randint(1, max_count) for v in ANIMALS]))
    return reversed_dict, animal_counter

class TestTaskFunc(unittest.TestCase):
    
    def test_valid_entries(self):
        animal_dict = {'John': 'Cat', 'Alice': 'Dog', 'Bob': 'Elephant', 'Charlie': 'Lion', 'David': 'Tiger'}
        reversed_dict, animal_counter = task_func(animal_dict)
        self.assertEqual(reversed_dict['Cat'], ['John'])
        self.assertEqual(reversed_dict['Dog'], ['Alice'])
        self.assertTrue(set(reversed_dict.keys()).issubset(set(ANIMALS)))

    def test_no_favorites(self):
        animal_dict = {'Alice': 'Pangolin', 'Bob': 'Dragon'}
        reversed_dict, animal_counter = task_func(animal_dict)
        self.assertEqual(reversed_dict, {})
        self.assertTrue(all(value == 0 for value in animal_counter.values()))

    def test_max_count_behavior(self):
        animal_dict = {'John': 'Cat', 'Alice': 'Dog'}
        reversed_dict, animal_counter = task_func(animal_dict, max_count=5, seed=1)
        cat_count = animal_counter['Cat']
        dog_count = animal_counter['Dog']
        self.assertTrue(cat_count <= 5)
        self.assertTrue(dog_count <= 5)

    def test_empty_animal_dict(self):
        animal_dict = {}
        reversed_dict, animal_counter = task_func(animal_dict)
        self.assertEqual(reversed_dict, {})
        self.assertEqual(len(animal_counter), len(ANIMALS))

    def test_invalid_max_count(self):
        animal_dict = {'John': 'Cat'}
        with self.assertRaises(ValueError):
            task_func(animal_dict, max_count=0)

if __name__ == '__main__':
    unittest.main()