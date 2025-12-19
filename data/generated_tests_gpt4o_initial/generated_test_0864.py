import pandas as pd
import numpy as np
import unittest

def task_func(fruit_data):
    """
    Calculate and return the total and average counts for each type of fruit.

    This function takes a list of tuples, each containing a fruit name and its count, 
    then calculates the total count and the average count for each type of fruit. 
    The results are returned as a pandas DataFrame with each row representing a different fruit.

    If fruit_data is an empty list, an empty dataFrame is returned.

    Parameters:
    fruit_data (list of tuples): Each tuple contains a string representing the fruit name and an integer for the count.

    Returns:
    DataFrame: A pandas DataFrame with two columns: 'Total Count' and 'Average Count'. 
               Each row's index is the fruit name.

    Requirements:
    - pandas
    - numpy

    Example:
    >>> fruit_list = [('apple', 5), ('banana', 3), ('apple', 6), ('banana', 4), ('cherry', 5), ('banana', 2), ('apple', 4), ('cherry', 5)]
    >>> report = task_func(fruit_list)
    >>> report.sort_index(inplace=True)
    >>> print(report)
            Total Count  Average Count
    apple            15            5.0
    banana            9            3.0
    cherry           10            5.0

    >>> fruit = [('apple', 1), ('orange', 25), ('apple', 111)]
    >>> df = task_func(fruit)
    >>> df.sort_index(inplace=True)
    >>> print(df)
            Total Count  Average Count
    apple           112           56.0
    orange           25           25.0
    """

    if len(fruit_data) == 0:
        return pd.DataFrame()

    # Unpacking the fruit names and counts separately
    fruits, counts = zip(*fruit_data)
    fruits = list(set(fruits))
    # Calculating total counts
    total_counts = {fruit: np.sum([count for fruit_, count in fruit_data if fruit_ == fruit])
                    for fruit in fruits}
    # Calculating average counts
    avg_counts = {fruit: np.mean([count for fruit_, count in fruit_data if fruit_ == fruit])
                  for fruit in fruits}

    # Creating a DataFrame to hold the report
    report_df = pd.DataFrame(list(zip(total_counts.values(), avg_counts.values())),
                             index=fruits,
                             columns=['Total Count', 'Average Count'])

    return report_df

class TestTaskFunc(unittest.TestCase):

    def test_empty_input(self):
        result = task_func([])
        expected = pd.DataFrame()
        pd.testing.assert_frame_equal(result, expected)

    def test_single_fruit(self):
        fruit_data = [('apple', 10)]
        result = task_func(fruit_data)
        expected = pd.DataFrame({'Total Count': [10], 'Average Count': [10]}, index=['apple'])
        pd.testing.assert_frame_equal(result, expected)

    def test_multiple_counts_for_same_fruit(self):
        fruit_data = [('banana', 3), ('banana', 5)]
        result = task_func(fruit_data)
        expected = pd.DataFrame({'Total Count': [8], 'Average Count': [4]}, index=['banana'])
        pd.testing.assert_frame_equal(result, expected)

    def test_multiple_fruits(self):
        fruit_data = [('apple', 5), ('banana', 3), ('apple', 6), ('banana', 4)]
        result = task_func(fruit_data)
        expected = pd.DataFrame({'Total Count': [11, 7], 'Average Count': [5.5, 3.5]}, index=['apple', 'banana'])
        pd.testing.assert_frame_equal(result.sort_index(), expected.sort_index())

    def test_fruits_with_varying_counts(self):
        fruit_data = [('apple', 1), ('banana', 2), ('apple', 3), ('cherry', 10)]
        result = task_func(fruit_data)
        expected = pd.DataFrame({'Total Count': [4, 2, 10], 'Average Count': [2.0, 2.0, 10.0]},
                                index=['apple', 'banana', 'cherry'])
        pd.testing.assert_frame_equal(result.sort_index(), expected.sort_index())

if __name__ == '__main__':
    unittest.main()