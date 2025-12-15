import os
import time
import pandas as pd
import unittest

OUTPUT_DIR = './output'


def task_func(dataset, filename, output_dir=OUTPUT_DIR):
    """
    Writes multiple Pandas DataFrames to a single CSV file, separating each DataFrame by a line of hyphens ("------").

    Parameters:
    - dataset (list of pd.DataFrame): A list containing the DataFrames to be written to the file.
    - filename (str): The name of the file (excluding the path) where the DataFrames will be written.
    - output_dir (str, optional): the ouput directory.

    Returns:
    None: The function writes the DataFrames to a CSV file but does not return any value.

    Requirements:
    - os
    - time

    Example:
    >>> import pandas as pd
    >>> df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    >>> df2 = pd.DataFrame({"D": [5, 6], "E": [7, 8]})
    >>> task_func([df1, df2], 'sample.csv')
    """

    start_time = time.time()

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w', newline='') as f:
        for i, df in enumerate(dataset):
            if i > 0:
                # Write the separator with a newline at the end only
                f.write('------\n')
            # Avoid writing the index and ensure no extra newline is added at the end of the DataFrame
            df.to_csv(f, index=False, header=True, mode='a')
            if i < len(dataset) - 1:
                # Add a newline after the DataFrame content, except after the last DataFrame
                f.write('\n')

    end_time = time.time()  # End timing
    cost = f"Operation completed in {end_time - start_time} seconds."


class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Set up the test environment and output directory before each test."""
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

    def tearDown(self):
        """Clean up the output directory after each test."""
        for file in os.listdir(OUTPUT_DIR):
            file_path = os.path.join(OUTPUT_DIR, file)
            if os.path.isfile(file_path):
                os.remove(file_path)

    def test_single_dataframe(self):
        """Test that a single DataFrame is written correctly to CSV."""
        df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
        task_func([df], 'single_df.csv')
        with open(os.path.join(OUTPUT_DIR, 'single_df.csv'), 'r') as f:
            content = f.read()
        self.assertIn('A,B\n1,3\n2,4\n', content)

    def test_multiple_dataframes(self):
        """Test that multiple DataFrames are written correctly to a CSV with separators."""
        df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
        df2 = pd.DataFrame({"D": [5, 6], "E": [7, 8]})
        task_func([df1, df2], 'multiple_dfs.csv')
        with open(os.path.join(OUTPUT_DIR, 'multiple_dfs.csv'), 'r') as f:
            content = f.read()
        self.assertIn('A,B\n1,3\n2,4\n------\nD,E\n5,7\n6,8\n', content)

    def test_empty_dataframe_list(self):
        """Test that no errors occur when an empty list of DataFrames is input."""
        task_func([], 'empty_dfs.csv')
        self.assertTrue(os.path.exists(os.path.join(OUTPUT_DIR, 'empty_dfs.csv')))
        with open(os.path.join(OUTPUT_DIR, 'empty_dfs.csv'), 'r') as f:
            content = f.read()
        self.assertEqual(content, '')  # Expecting an empty file

    def test_dataframe_with_no_rows(self):
        """Test that an empty DataFrame behaves correctly."""
        df_empty = pd.DataFrame(columns=["A", "B"])
        task_func([df_empty], 'empty_content.csv')
        with open(os.path.join(OUTPUT_DIR, 'empty_content.csv'), 'r') as f:
            content = f.read()
        self.assertIn('A,B\n', content)  # Check only headers are written


if __name__ == "__main__":
    unittest.main()