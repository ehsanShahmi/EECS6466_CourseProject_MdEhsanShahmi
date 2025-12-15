import pandas as pd
import random
import re
import unittest

def task_func(data_list, seed=None):
    """
    Apply a random operation (remove, replace, shuffle, or randomize) to substrings in a list of strings.

    This function processes a list of comma-separated strings by applying one of four random operations to
    their substrings: remove, replace, shuffle, or randomize. Here, a substring refers to the individual
    items in the string that are separated by commas, sensitive to leading/trailing whitespace, i.e.
    'apple' != 'apple ', and sensitive to case, i.e. 'APPLE' != 'aPPLE'.

    The choice of operation and the substrings it affects are determined randomly. The operations are:
    - Remove: Randomly selects and removes a substring.
              If a string contains only one substring, no 'remove' operation is applied.
    - Replace: Randomly selects a substring and replaces it with 'random_string'.
    - Shuffle: Randomly shuffles the order of the substrings.
    - Randomize: Assigns a new, random order to the substrings.

    Finally, the function returns a DataFrame with column 'Original String' containing the input strings
    and the 'Modified String' column containing the strings after applying the random operation.

    Parameters:
    - data_list (list): The list of strings. If empty, function will return a DataFrame with the expected
                        columns that is otherwise empty.
    - seed (int, optional): A seed for the random operations to ensure reproducibility. Default is None.

    Returns:
    df (pd.DataFrame): DataFrame containing original and modified strings.
    """
    random.seed(seed)

    df = pd.DataFrame(data_list, columns=["Original String"])

    modified_strings = []
    for s in data_list:
        substrings = re.split(", ", s)
        operation = random.choice(["remove", "replace", "shuffle", "randomize"])
        if operation == "remove":
            if len(substrings) > 1:
                random_substring = random.choice(substrings)
                substrings.remove(random_substring)
                modified_s = ", ".join(substrings)
            else:
                modified_s = s
        elif operation == "replace":
            random_substring_index = random.choice(range(len(substrings)))
            substrings[random_substring_index] = "random_string"
            modified_s = ", ".join(substrings)
        elif operation == "shuffle":
            random.shuffle(substrings)
            modified_s = ", ".join(substrings)
        elif operation == "randomize":
            random_positions = random.sample(range(len(substrings)), len(substrings))
            modified_s = ", ".join([substrings[i] for i in random_positions])
        modified_strings.append(modified_s)

    df["Modified String"] = modified_strings

    return df

class TestTaskFunc(unittest.TestCase):

    def test_empty_input(self):
        result = task_func([])
        expected = pd.DataFrame(columns=["Original String", "Modified String"])
        pd.testing.assert_frame_equal(result, expected)

    def test_single_string_no_remove(self):
        result = task_func(['apple'], seed=0)
        expected = pd.DataFrame({
            "Original String": ['apple'],
            "Modified String": ['apple']
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_remove_operation(self):
        result = task_func(['apple, banana, cherry'], seed=0)
        original_string = result['Original String'][0]
        modified_string = result['Modified String'][0]
        self.assertNotIn(modified_string, original_string)

    def test_replace_operation(self):
        result = task_func(['apple, banana'], seed=0)
        self.assertIn('random_string', result['Modified String'][0])

    def test_shuffle_operation(self):
        result = task_func(['apple, banana, cherry'], seed=0)
        original_list = result['Original String'][0].split(', ')
        modified_list = result['Modified String'][0].split(', ')
        self.assertNotEqual(original_list, modified_list)

if __name__ == "__main__":
    unittest.main()