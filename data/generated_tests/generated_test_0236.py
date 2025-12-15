import pandas as pd
import unittest

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Sample data for the test cases
        self.valid_data = pd.DataFrame([
            {'Name': 'James', 'Age': 30, 'Score': 85, 'Category': 'Electronics'},
            {'Name': 'Lily', 'Age': 28, 'Score': 92, 'Category': 'Home'},
            {'Name': 'Tom', 'Age': 25, 'Score': 78, 'Category': 'Garden'}
        ])

        self.duplicate_data = pd.DataFrame([
            {'Name': 'James', 'Age': 30, 'Score': 85, 'Category': 'Electronics'},
            {'Name': 'James', 'Age': 30, 'Score': 85, 'Category': 'Home'},
            {'Name': 'Tom', 'Age': 25, 'Score': 78, 'Category': 'Garden'}
        ])

        self.empty_data = pd.DataFrame(columns=['Name', 'Age', 'Score', 'Category'])

        self.non_dataframe_input = "Not a dataframe"

    def test_valid_input_accuracy(self):
        accuracy = task_func(self.valid_data)
        self.assertIsInstance(accuracy, float)
        self.assertGreaterEqual(accuracy, 0.0)
        self.assertLessEqual(accuracy, 1.0)

    def test_accuracy_with_duplicates(self):
        accuracy = task_func(self.duplicate_data)
        self.assertIsInstance(accuracy, float)
        self.assertGreaterEqual(accuracy, 0.0)
        self.assertLessEqual(accuracy, 1.0)

    def test_empty_dataframe(self):
        accuracy = task_func(self.empty_data)
        self.assertIsInstance(accuracy, float)
        self.assertEqual(accuracy, 0.0)

    def test_non_dataframe_input(self):
        with self.assertRaises(ValueError) as context:
            task_func(self.non_dataframe_input)
        self.assertEqual(str(context.exception), "The input df is not a DataFrame")

    def test_accuracy_range(self):
        accuracy = task_func(self.valid_data)
        self.assertTrue(0.0 <= accuracy <= 1.0)

if __name__ == '__main__':
    unittest.main()