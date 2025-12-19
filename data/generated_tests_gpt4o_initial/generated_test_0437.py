import unittest
import pandas as pd
import numpy as np
import os

# Here is your prompt:
import pickle

def task_func(df, file_name="save.pkl"):
    """
    Save the provided Pandas DataFrame "df" in a pickle file with the given name, read it
    back for validation, and delete the intermediate file.

    Parameters:
    df (DataFrame): The pandas DataFrame to be saved.
    file_name (str, optional): Name of the file where the DataFrame will be saved. Defaults to 'save.pkl'.

    Returns:
    loaded_df (pd.DataFrame): The loaded DataFrame from the specified file.

    Requirements:
    - pickle
    - os
    """

    with open(file_name, "wb") as file:
        pickle.dump(df, file)

    with open(file_name, "rb") as file:
        loaded_df = pickle.load(file)

    os.remove(file_name)

    return loaded_df


class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Create a sample DataFrame for testing
        self.df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
        self.file_name = "test_file.pkl"

    def test_dataframe_shape(self):
        loaded_df = task_func(self.df, self.file_name)
        self.assertEqual(self.df.shape, loaded_df.shape)

    def test_dataframe_equals(self):
        loaded_df = task_func(self.df, self.file_name)
        self.assertTrue(self.df.equals(loaded_df))

    def test_return_type(self):
        loaded_df = task_func(self.df, self.file_name)
        self.assertIsInstance(loaded_df, pd.DataFrame)

    def test_saved_file_deletion(self):
        task_func(self.df, self.file_name)
        self.assertFalse(os.path.exists(self.file_name))

    def test_empty_dataframe(self):
        empty_df = pd.DataFrame()
        loaded_df = task_func(empty_df, self.file_name)
        self.assertTrue(empty_df.equals(loaded_df))


if __name__ == '__main__':
    unittest.main()