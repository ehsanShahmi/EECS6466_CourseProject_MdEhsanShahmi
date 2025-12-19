import pandas as pd
import time
import unittest

# Here is your prompt:
# import pandas as pd
# import time

# def task_func(df, letter):
#     """
#     The function filters rows in a dict of list in which the values of the 'Word' column begin with a specified letter.
#     It first convert the dict to Datafrome, then calculates the length of the words in the filtered column and returns
#     a dictionary of word lengths and their respective counts.

#     Parameters:
#     df (dict of list): A dictionary where the key 'Word' maps to a list of strings.
#     letter (str): The letter to filter the 'Word' column by. 

#     Returns:
#     dict: A dictionary of word lengths and their counts.
    
#     Requirements:
#     - pandas
#     - time

#     Example:
#     >>> df = {'Word': ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi']}
#     >>> task_func(df, 'a')
#     {5: 1}
#     """
#     start_time = time.time()
#     df = pd.DataFrame(df)
#     regex = '^' + letter
#     filtered_df = df[df['Word'].str.contains(regex, regex=True)]
#     word_lengths = filtered_df['Word'].str.len()
#     count_dict = word_lengths.value_counts().to_dict()
#     end_time = time.time()  # End timing
#     cost = f"Operation completed in {end_time - start_time} seconds."

#     return count_dict


class TestTaskFunc(unittest.TestCase):

    def test_task_func_with_valid_input(self):
        df = {'Word': ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi']}
        result = task_func(df, 'a')
        expected = {5: 2, 6: 1}  # 'apple' and 'banana' have lengths 5 and 6 respectively
        self.assertEqual(result, expected)

    def test_task_func_with_empty_input(self):
        df = {'Word': []}
        result = task_func(df, 'a')
        expected = {}
        self.assertEqual(result, expected)

    def test_task_func_with_no_matching_letter(self):
        df = {'Word': ['banana', 'cherry', 'fig']}
        result = task_func(df, 'd')
        expected = {}
        self.assertEqual(result, expected)

    def test_task_func_with_case_insensitivity(self):
        df = {'Word': ['Apple', 'banana', 'cherry', 'date', 'fig']}
        result = task_func(df, 'a')  # Should match 'Apple' and 'banana'
        expected = {5: 1, 6: 1}
        self.assertEqual(result, expected)

    def test_task_func_with_special_characters(self):
        df = {'Word': ['apple!', 'banana*', 'cherry%', 'date$', 'fig']}
        result = task_func(df, 'a')
        expected = {6: 1}  # 'banana*' has length 6
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()