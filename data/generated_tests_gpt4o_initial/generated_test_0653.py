import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import unittest

def task_func(dataframe, target_value='332'):
    """
    Searches a given DataFrame for occurrences of a specified target value and visualizes these occurrences using a heatmap.

    Parameters:
    - dataframe (pd.DataFrame): The input DataFrame to search.
    - target_value (str, optional): The value to search for in the DataFrame. Defaults to '332'.

    Returns:
    - tuple: A tuple containing:
        - pd.DataFrame: A DataFrame with Boolean values indicating the presence of the target value in the input DataFrame.
        - matplotlib.axes._axes.Axes: The Axes object of the heatmap.

    Requirements:
    - matplotlib.pyplot
    - seaborn
    """
    mask = dataframe.applymap(lambda x: x == target_value)

    # Plot the heatmap
    plt.figure(figsize=(8, 6))
    ax = sns.heatmap(mask, cmap='Blues', cbar=False)  # Adjusted to not display color bar for clarity in Boolean visualization
    plt.show()

    return mask, ax

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        self.df_basic = pd.DataFrame({
            'Column1': ['0', 'a', '332', '33'],
            'Column2': ['1', 'bb', '33', '22'],
            'Column3': ['2', 'ccc', '2', '332']
        })
        self.df_no_target = pd.DataFrame({
            'Column1': ['1', '2', '3'],
            'Column2': ['4', '5', '6'],
            'Column3': ['7', '8', '9']
        })
        self.df_identical = pd.DataFrame({
            'Column1': ['332', '332', '332'],
            'Column2': ['332', '332', '332'],
            'Column3': ['332', '332', '332']
        })

    def test_found_target(self):
        mask, _ = task_func(self.df_basic, '332')
        expected_mask = pd.DataFrame({
            'Column1': [False, False, True, False],
            'Column2': [False, False, False, False],
            'Column3': [False, False, False, True]
        })
        pd.testing.assert_frame_equal(mask, expected_mask)

    def test_no_target_found(self):
        mask, _ = task_func(self.df_no_target, '332')
        expected_mask = pd.DataFrame({
            'Column1': [False, False, False],
            'Column2': [False, False, False],
            'Column3': [False, False, False]
        })
        pd.testing.assert_frame_equal(mask, expected_mask)

    def test_all_identical_target(self):
        mask, _ = task_func(self.df_identical, '332')
        expected_mask = pd.DataFrame({
            'Column1': [True, True, True],
            'Column2': [True, True, True],
            'Column3': [True, True, True]
        })
        pd.testing.assert_frame_equal(mask, expected_mask)

    def test_default_target_value(self):
        mask, _ = task_func(self.df_basic)
        expected_mask = pd.DataFrame({
            'Column1': [False, False, True, False],
            'Column2': [False, False, False, False],
            'Column3': [False, False, False, True]
        })
        pd.testing.assert_frame_equal(mask, expected_mask)

    def test_case_sensitivity(self):
        mask, _ = task_func(self.df_basic, '332')
        # Check that different casing is handled correctly
        self.assertTrue(mask.iloc[2, 0])  # should be True
        self.assertFalse(mask.iloc[1, 1])  # should be False

if __name__ == '__main__':
    unittest.main()