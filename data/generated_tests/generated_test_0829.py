import pandas as pd
import unittest
from statistics import mean

# Here is your prompt:
def task_func(df: pd.DataFrame) -> dict:
    """
    Convert a Pandas DataFrame into a dictionary of generator objects in which 
    each generator generates a sequence of tuples that contain a unique name 
    and the corresponding average score for that name.

    Parameters:
    df (DataFrame): The DataFrame containing 'Name' (string) and 'Score' (number) columns to analyze.

    Returns:
    dict: A dictionary of generator objects. Each generator generates a tuple 
          containing a unique name and the corresponding average score for that name.

    Raises:
    ValueError: If the DataFrame does not have the 'Name' and 'Score' columns.

    Requirements:
    - pandas
    - statistics

    Example:
    >>> df_sample = pd.DataFrame({
    ...     'Name': ['Tom', 'Nick', 'John', 'Tom', 'John'],
    ...     'Score': [85, 79, 90, 88, 82]
    ... })
    >>> gen_dict = task_func(df_sample)
    >>> {key: next(value) for key, value in gen_dict.items()}
    {'John': ('John', 86), 'Nick': ('Nick', 79), 'Tom': ('Tom', 86.5)}

    >>> df_sample = pd.DataFrame({
    ...     'Name': ['Micky', 'Donald', 'Girl'],
    ...     'Score': [25.2, 9, -1]
    ... })
    >>> gen_dict = task_func(df_sample)
    >>> {key: next(value) for key, value in gen_dict.items()}
    {'Donald': ('Donald', 9.0), 'Girl': ('Girl', -1.0), 'Micky': ('Micky', 25.2)}
    """

           
    if 'Name' not in df.columns or 'Score' not in df.columns:
        raise ValueError('The DataFram should have the columns "Name" and "Score".')

    grouped = df.groupby('Name')
    result_dict = {}
    for name, group in grouped:
        avg_score = mean(group['Score'])
        result_dict[name] = iter([(name, avg_score)])

    return result_dict


class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        self.valid_df = pd.DataFrame({
            'Name': ['Tom', 'Nick', 'John', 'Tom', 'John'],
            'Score': [85, 79, 90, 88, 82]
        })

        self.valid_df2 = pd.DataFrame({
            'Name': ['Micky', 'Donald', 'Girl'],
            'Score': [25.2, 9, -1]
        })

        self.empty_df = pd.DataFrame(columns=['Name', 'Score'])

    def test_average_score_calculation(self):
        gen_dict = task_func(self.valid_df)
        results = {key: next(value) for key, value in gen_dict.items()}

        self.assertAlmostEqual(results['Tom'][1], 86.5)
        self.assertAlmostEqual(results['Nick'][1], 79.0)
        self.assertAlmostEqual(results['John'][1], 86.0)

    def test_multiple_names(self):
        gen_dict = task_func(self.valid_df2)
        results = {key: next(value) for key, value in gen_dict.items()}

        self.assertAlmostEqual(results['Micky'][1], 25.2)
        self.assertAlmostEqual(results['Donald'][1], 9.0)
        self.assertAlmostEqual(results['Girl'][1], -1.0)

    def test_empty_dataframe(self):
        gen_dict = task_func(self.empty_df)
        self.assertEqual(gen_dict, {})

    def test_no_name_column(self):
        df_no_name = pd.DataFrame({
            'Score': [85, 78, 90]
        })
        with self.assertRaises(ValueError) as context:
            task_func(df_no_name)
        self.assertEqual(str(context.exception), 'The DataFram should have the columns "Name" and "Score".')

    def test_no_score_column(self):
        df_no_score = pd.DataFrame({
            'Name': ['Tom', 'Nick', 'John']
        })
        with self.assertRaises(ValueError) as context:
            task_func(df_no_score)
        self.assertEqual(str(context.exception), 'The DataFram should have the columns "Name" and "Score".')


if __name__ == '__main__':
    unittest.main()