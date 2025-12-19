import random
import string
from collections import Counter
import unittest

def task_func(num_strings, string_length):
    strings = [''.join(random.choices(string.ascii_lowercase, k=string_length)) for _ in range(num_strings)]
    characters = ''.join(strings)
    character_counter = Counter(characters)
    most_common_characters = character_counter.most_common()
    return most_common_characters

class TestTaskFunc(unittest.TestCase):

    def test_return_type(self):
        self.assertIsInstance(task_func(1000, 5), list)

    def test_tuple_elements(self):
        result = task_func(1000, 5)
        self.assertTrue(all(isinstance(pair, tuple) and len(pair) == 2 for pair in result))

    def test_empty_input(self):
        result = task_func(0, 5)
        self.assertEqual(result, [])

    def test_character_frequency(self):
        result = task_func(1000, 1)
        char_count = Counter(char for char, _ in result)
        total_count = sum(count for _, count in result)
        self.assertEqual(total_count, 1000)

    def test_string_length_variation(self):
        result_short = task_func(1000, 1)
        result_long = task_func(1000, 10)
        self.assertTrue(len(result_long) >= len(result_short))

if __name__ == '__main__':
    unittest.main()