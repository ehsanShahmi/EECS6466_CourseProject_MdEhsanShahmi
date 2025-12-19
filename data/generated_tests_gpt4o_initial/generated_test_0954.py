import unittest
import random
from your_module import task_func  # Replace 'your_module' with the actual module name where task_func is implemented

class TestTaskFunc(unittest.TestCase):

    def test_generate_sentences_with_target_word(self):
        random.seed(42)
        result = task_func(['apple banana'], 1, ['apple', 'banana', 'cherry'])
        expected = ['banana apple apple apple cherry cherry cherry apple_banana apple']
        self.assertEqual(result, expected)

    def test_multiple_target_words_case_insensitive(self):
        random.seed(42)
        result = task_func(['Alice Charlie', 'ALICE BOB', 'aLiCe dAn'], 1, ['alice', 'bob', 'charlie', 'dan'])
        expected = ['alice_charlie alice alice_charlie charlie alice_charlie dan alice']
        self.assertEqual(result, expected)

    def test_negative_sentences(self):
        with self.assertRaises(ValueError) as context:
            task_func(['apple'], -1, ['apple', 'banana'])
        self.assertEqual(str(context.exception), "n_sentences cannot be negative.")

    def test_empty_vocabulary(self):
        with self.assertRaises(ValueError) as context:
            task_func(['apple'], 1, [])
        self.assertEqual(str(context.exception), "Vocabulary cannot be empty.")

    def test_sentences_generated_with_valid_parameters(self):
        random.seed(42)
        result = task_func(['test phrase'], 5, ['this', 'is', 'a', 'test', 'sentence'])
        self.assertEqual(len(result), 5)

if __name__ == '__main__':
    unittest.main()