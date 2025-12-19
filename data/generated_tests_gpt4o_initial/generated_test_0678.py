import unittest
import pandas as pd
import os
import json
import shutil

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Set up a temporary directory and create sample JSON files for testing."""
        self.test_dir = 'test_data'
        os.mkdir(self.test_dir)

        # Create test JSON files
        self.json_data1 = '[{"a": 1, "b": 2}, {"a": 3, "b": 4}]'
        self.json_data2 = '[{"a": 5, "b": 6}, {"a": 7, "b": 8}]'
        with open(os.path.join(self.test_dir, 'a.json'), 'w') as f:
            f.write(self.json_data1)
        with open(os.path.join(self.test_dir, 'b.json'), 'w') as f:
            f.write(self.json_data2)

    def tearDown(self):
        """Clean up the temporary directory after tests are run."""
        shutil.rmtree(self.test_dir)

    def test_task_func_output_structure(self):
        """Test that the output DataFrame has the correct structure."""
        df = task_func(self.test_dir)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIn('source', df.columns)
        self.assertEqual(len(df), 4)  # 4 rows from both JSON files

    def test_task_func_source_column(self):
        """Test that the source column contains the correct filenames."""
        df = task_func(self.test_dir)
        expected_sources = ['b.json', 'b.json', 'a.json', 'a.json']
        self.assertListEqual(df['source'].tolist(), expected_sources)

    def test_task_func_json_content(self):
        """Test that the content of the DataFrame matches the JSON files."""
        df = task_func(self.test_dir)
        expected_data = [
            {'a': 5, 'b': 6, 'source': 'b.json'},
            {'a': 7, 'b': 8, 'source': 'b.json'},
            {'a': 1, 'b': 2, 'source': 'a.json'},
            {'a': 3, 'b': 4, 'source': 'a.json'},
        ]
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(df.reset_index(drop=True), expected_df)

    def test_task_func_processed_directory(self):
        """Test that the JSON files are moved to the 'processed' directory."""
        task_func(self.test_dir)
        processed_path = os.path.join(self.test_dir, 'processed')
        self.assertTrue(os.path.exists(processed_path))
        self.assertEqual(len(os.listdir(processed_path)), 2)
        self.assertNotIn('a.json', os.listdir(self.test_dir))
        self.assertNotIn('b.json', os.listdir(self.test_dir))

if __name__ == '__main__':
    unittest.main()