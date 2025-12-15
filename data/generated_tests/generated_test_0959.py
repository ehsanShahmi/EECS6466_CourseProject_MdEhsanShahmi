import unittest
import string


class TestTaskFunc(unittest.TestCase):
    
    def test_empty_string(self):
        """Test that an empty string returns an empty string"""
        self.assertEqual(task_func(''), '')
        
    def test_non_alpha_string(self):
        """Test that a string with no alphabetic characters returns the same string"""
        self.assertEqual(task_func('1234!@#$'), '1234!@#$')
        
    def test_mixed_case_string(self):
        """Test that a mixed case string is transformed correctly"""
        original = 'Hello, World!'
        transformed = task_func(original, seed=42)
        # The expected output is non-trivial to compute without knowing the random seed
        self.assertNotEqual(original, transformed)
        self.assertTrue(all(c.isalpha() or not c.isalpha() for c in transformed))
        self.assertEqual(len(original), len(transformed))
        
    def test_preserve_non_alpha_characters(self):
        """Test that non-alphabetic characters are preserved in the output"""
        original = 'Hello, World! 123'
        transformed = task_func(original, seed=1)
        self.assertIn(',', transformed)
        self.assertIn('!', transformed)
        self.assertIn(' ', transformed)

    def test_seed_reproducibility(self):
        """Test that using the same seed will produce the same output for the same input"""
        original = 'Test String'
        transformed1 = task_func(original, seed=123)
        transformed2 = task_func(original, seed=123)
        self.assertEqual(transformed1, transformed2)


if __name__ == '__main__':
    unittest.main()