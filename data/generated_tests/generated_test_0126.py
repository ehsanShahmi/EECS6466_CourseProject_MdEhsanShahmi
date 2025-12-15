import pandas as pd
from random import randint, seed as random_seed
import statistics
import numpy as np
import unittest

def task_func(animals=None, seed=42):
    """
    Create a report on the number of animals in a zoo. For each animal, generate a random count within 
    a specified range, calculate the mean, median, and standard deviation of these counts, and return 
    a DataFrame with these statistics. Additionally, generate a bar chart of the counts.

    Parameters:
    - animals (list of str, optional): List of animals to include in the report. 
        Defaults to ['Lion', 'Elephant', 'Tiger', 'Giraffe', 'Panda'].
    - seed (int, optional): Random seed for reproducibility. Defaults to 42.

    Returns:
    - DataFrame: A pandas DataFrame with columns ['Animal', 'Mean', 'Median', 'Mode', 'Standard Deviation'].
      Each animal's count is randomly generated 10 times within the range 1 to 100, inclusive.

    Requirements:
    - pandas
    - random
    - statistics
    - numpy

    Example:
    >>> report = task_func()
    >>> print(report)
         Animal  Mean  Median  Mode  Standard Deviation
    0      Lion  42.0    30.5    95           33.250564
    1  Elephant  44.4    41.5    12           34.197076
    2     Tiger  61.1    71.0    30           28.762649
    3   Giraffe  51.8    54.5    54           29.208903
    4     Panda  35.8    32.0    44           24.595935

    Note: The mode is not included in the returned DataFrame due to the possibility of no repeating values 
    in the randomly generated counts.
    """

    random_seed(seed)
    animals = animals or ['Lion', 'Elephant', 'Tiger', 'Giraffe', 'Panda']
    report_data = []

    for animal in animals:
        counts = [randint(1, 100) for _ in range(10)]
        mean = statistics.mean(counts)
        median = statistics.median(counts)
        mode = statistics.mode(counts)
        std_dev = np.std(counts)
        report_data.append([animal, mean, median, mode, std_dev])
    
    report_df = pd.DataFrame(report_data, columns=['Animal', 'Mean', 'Median', 'Mode', 'Standard Deviation'])

    return report_df

class TestTaskFunc(unittest.TestCase):
    
    def test_default_animals_report_shape(self):
        report = task_func()
        self.assertEqual(report.shape, (5, 5), "Report should have 5 rows and 5 columns")

    def test_custom_animals_report_shape(self):
        report = task_func(animals=['Dog', 'Cat'])
        self.assertEqual(report.shape, (2, 5), "Report should have 2 rows for custom animals")

    def test_mean_median_stddev_values(self):
        report = task_func()
        for index, row in report.iterrows():
            self.assertTrue(1 <= row['Mean'] <= 100, "Mean should be between 1 and 100")
            self.assertTrue(1 <= row['Median'] <= 100, "Median should be between 1 and 100")
            self.assertTrue(row['Standard Deviation'] >= 0, "Standard Deviation should be non-negative")

    def test_random_seed_consistency(self):
        report1 = task_func(seed=42)
        report2 = task_func(seed=42)
        pd.testing.assert_frame_equal(report1, report2, "Reports should be the same when seed is fixed")

    def test_return_dataframe_columns(self):
        report = task_func()
        expected_columns = ['Animal', 'Mean', 'Median', 'Mode', 'Standard Deviation']
        self.assertListEqual(list(report.columns), expected_columns, "DataFrame should contain the correct columns")

if __name__ == '__main__':
    unittest.main()