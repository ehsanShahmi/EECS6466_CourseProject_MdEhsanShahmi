import collections
import random
import unittest

# Constants
LETTERS = ['a', 'b', 'c', 'd', 'e']

# Here is your prompt:
# import collections
# from queue import PriorityQueue
# import random

# Constants
# LETTERS = ['a', 'b', 'c', 'd', 'e']

# def task_func(string_length=100):
#     """
#     Create a random string of a given length from a predefined list of letters and count the frequency 
#     of each letter, returning an ordered dictionary sorted by frequency in descending order.

#     Parameters:
#     - string_length (int, optional): The length of the random string to be generated. Default is 100.

#     Returns:
#     - collections.OrderedDict: An ordered dictionary where keys are letters and values are 
#       their frequencies in the generated string, sorted in descending order of frequency.

#     Requirements:
#     - collections
#     - queue.PriorityQueue
#     - random

#     Example:
#     >>> random.seed(0)
#     >>> freq = task_func(50)
#     >>> freq  # Example output: OrderedDict([('e', 15), ('a', 12), ('b', 10), ('d', 8), ('c', 5)])
#     OrderedDict(...)
#     """

def task_func(string_length=100):
    string = ''.join([LETTERS[random.randint(0, len(LETTERS)-1)] for _ in range(string_length)])
    freq = collections.Counter(string)
    pq = PriorityQueue()
    for letter, count in freq.items():
        pq.put((-count, letter))
    sorted_freq = collections.OrderedDict()
    while not pq.empty():
        count, letter = pq.get()
        sorted_freq[letter] = -count
    return sorted_freq

class TestTaskFunc(unittest.TestCase):

    def test_default_length(self):
        random.seed(0)
        result = task_func()
        self.assertIsInstance(result, collections.OrderedDict)
        self.assertGreaterEqual(len(result), 1)

    def test_length_zero(self):
        result = task_func(0)
        self.assertEqual(result, collections.OrderedDict())

    def test_frequency_count(self):
        random.seed(0)
        result = task_func(50)
        self.assertEqual(sum(result.values()), 50)

    def test_ordered_dict(self):
        random.seed(0)
        result = task_func(100)
        self.assertTrue(all(result.items()[i][1] >= result.items()[i + 1][1] for i in range(len(result) - 1)))

    def test_valid_letters(self):
        result = task_func(100)
        for letter in result.keys():
            self.assertIn(letter, LETTERS)

if __name__ == '__main__':
    unittest.main()