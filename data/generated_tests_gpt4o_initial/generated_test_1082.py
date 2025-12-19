import unittest
import pandas as pd
from scipy.stats import pearsonr

# Here is your prompt:
def task_func(data):
    """
    Calculates the Pearson correlation coefficient between numerical scores and categorical grades.

    This function performs three main tasks:
    1. Converts scores from string format to floats.
    2. Encodes categorical grades into numerical values based on their rank order.
    3. Computes the Pearson correlation coefficient between the numerical scores and the encoded grades.

    Parameters:
    - data (dict): A dictionary containing two keys:
                 - 'Score_String': A list of scores in string format.
                 - 'Grade': A list of corresponding grades in string format.
                 Each list under these keys must have the same length.

    Returns:
    - correlation (float): The Pearson correlation coefficient between the converted numerical scores and encoded grades.
           Returns NaN if the input data frame has less than 2 rows, as the correlation coefficient cannot be calculated in this case.

    Requirements:
    - pandas
    - scipy

    Example:
    >>> round(task_func({'Score_String': ['80.5', '85.7', '90.2'], 'Grade': ['B', 'B+', 'A-']}),2)
    -0.46
    """

    df = pd.DataFrame(data)
    if len(df) < 2:  # Check if the data frame has less than 2 rows
        return float("nan")  # or return None

    df["Score_Float"] = df["Score_String"].astype(float)
    df["Grade_Encoded"] = df["Grade"].astype("category").cat.codes
    correlation = pearsonr(df["Score_Float"], df["Grade_Encoded"])[0]
    return correlation


class TestTaskFunc(unittest.TestCase):

    def test_valid_input(self):
        data = {
            'Score_String': ['80.5', '85.7', '90.2'],
            'Grade': ['B', 'B+', 'A-']
        }
        result = task_func(data)
        self.assertAlmostEqual(round(result, 2), -0.46)

    def test_highly_correlated_data(self):
        data = {
            'Score_String': ['70', '75', '80', '85'],
            'Grade': ['C', 'C+', 'B', 'A']
        }
        result = task_func(data)
        self.assertAlmostEqual(round(result, 2), 0.97)

    def test_reverse_correlated_data(self):
        data = {
            'Score_String': ['100', '90', '80', '70'],
            'Grade': ['A+', 'A', 'B', 'C']
        }
        result = task_func(data)
        self.assertAlmostEqual(round(result, 2), -0.97)

    def test_empty_data(self):
        data = {
            'Score_String': [],
            'Grade': []
        }
        result = task_func(data)
        self.assertTrue(pd.isna(result))

    def test_single_entry_data(self):
        data = {
            'Score_String': ['85.0'],
            'Grade': ['B']
        }
        result = task_func(data)
        self.assertTrue(pd.isna(result))


if __name__ == '__main__':
    unittest.main()