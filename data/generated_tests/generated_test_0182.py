import unittest
import pandas as pd

class TestTaskFunc(unittest.TestCase):

    def test_basic_functionality(self):
        df = pd.DataFrame({
            'Title': ['How to code?', 'What is Python?', 'The art of programming', 'How to cook?', 'What is life?'],
            'Content': ['This is a tutorial about coding...', 'Python is a programming language...',
                        'Programming is an art...', 'This is a cooking tutorial...', 'Life is complicated...']
        })
        expected_output = [0, 1, 0, 1]
        self.assertEqual(task_func(df), expected_output)

    def test_no_keywords(self):
        df = pd.DataFrame({
            'Title': ['Learn Java', 'Programming Basics', 'Introduction to SQL'],
            'Content': ['Java is a programming language...', 'Basics of programming...', 'Learn SQL with examples...']
        })
        expected_output = []
        self.assertEqual(task_func(df), expected_output)

    def test_single_keyword(self):
        df = pd.DataFrame({
            'Title': ['How to learn Python?', 'Best practices in coding'],
            'Content': ['Python is easy to learn...', 'Coding practices are essential...']
        })
        expected_output = [0, 1]  # "How" should be in one cluster, and other article not counted
        self.assertEqual(task_func(df), expected_output)

    def test_identical_titles(self):
        df = pd.DataFrame({
            'Title': ['How to travel?', 'How to travel?'],
            'Content': ['Traveling tips and tricks...', 'Traveling abroad...']
        })
        expected_output = [0, 0]  # Both articles should fall into the same cluster
        self.assertEqual(task_func(df), expected_output)

    def test_empty_dataframe(self):
        df = pd.DataFrame(columns=['Title', 'Content'])
        expected_output = []
        self.assertEqual(task_func(df), expected_output)

if __name__ == '__main__':
    unittest.main()