import pandas as pd
import numpy as np
import unittest

# Here is your prompt:

def task_func(test_scores, student):
    """
    Convert a dictionary of test results into a pandas DataFrame and
    Calculate the average test score and the standard deviation for a particular student from this DataFrame.
    
    Parameters:
    test_scores (dictionary): The dictionary containing keys 'Student' and 'Score'.
        The Student values are of dtype int and contain student IDs. The Score 
        values are of dtype float.
    student (int): The specific student ID for which the average score needs to be calculated.
    
    Returns:
    np.array([float, float]): A numpy array containing the average score and the standard deviation for the student.
    DataFrame: the converted dictionary.

    Raises:
    ValueError: student is not present in the test_scores dataframe
                
    Requirements:
    - pandas
    - numpy
    
    Example:
    >>> STUDENTS = range(1, 101)
    >>> np.random.seed(10)
    >>> scores = {'Student': list(np.random.choice(STUDENTS, 50, replace=True)), 
    ...                        'Score': np.random.randint(50, 101, size=50)}
    >>> task_func(scores, 10)
    (array([70.        ,  7.07106781]),     Student  Score
    0        10     65
    1        16     68
    2        65     66
    3        29     57
    4        90     74
    5        94     61
    6        30     67
    7         9     96
    8        74     57
    9         1     61
    10       41     78
    11       37     83
    12       17     70
    13       12     82
    14       55     74
    15       89     94
    16       63     55
    17       34     54
    18       73     57
    19       79     74
    20       50     74
    21       52    100
    22       55     94
    23       78     84
    24       70     90
    25       14     65
    26       26     63
    27       14     74
    28       93     65
    29       87     56
    30       31     71
    31       31     92
    32       90     72
    33       13     61
    34       66     98
    35       32     62
    36       58     78
    37       37     82
    38       28     99
    39       19     65
    40       94     94
    41       78     90
    42       23     92
    43       24     95
    44       95     93
    45       12     83
    46       29    100
    47       75     95
    48       89     90
    49       10     75)

    >>> scores = {'Student': [1, 2, 1, 1], 'Score': [10, 1, 1, 1]}
    >>> task_func(scores, 1)
    (array([4.        , 5.19615242]),    Student  Score
    0        1     10
    1        2      1
    2        1      1
    3        1      1)
    """
    test_scores = pd.DataFrame(test_scores)
    if student not in test_scores['Student'].values:
        raise ValueError(f"The student with ID {student} is not present in the test scores DataFrame.")
    student_scores = test_scores[test_scores['Student'] == student]['Score']
    average_score = student_scores.mean()
    std = student_scores.std()
    
    return np.array([average_score, std]), test_scores

class TestTaskFunc(unittest.TestCase):

    def test_average_and_std_for_existing_student(self):
        scores = {'Student': [1, 2, 1, 1], 'Score': [10, 1, 1, 1]}
        result, df = task_func(scores, 1)
        expected = np.array([4.0, 5.19615242])
        self.assertTrue(np.allclose(result, expected))

    def test_dataframe_conversion(self):
        scores = {'Student': [1, 2, 1, 1], 'Score': [10, 1, 1, 1]}
        _, df = task_func(scores, 1)
        expected_df = pd.DataFrame(scores)
        pd.testing.assert_frame_equal(df, expected_df)

    def test_average_and_std_for_student_with_multiple_entries(self):
        scores = {'Student': [1, 1, 1, 1], 'Score': [80, 90, 100, 70]}
        result, _ = task_func(scores, 1)
        expected = np.array([85.0, 12.24744871])
        self.assertTrue(np.allclose(result, expected))

    def test_student_not_in_dataframe(self):
        scores = {'Student': [1, 2, 3], 'Score': [10, 20, 30]}
        with self.assertRaises(ValueError) as context:
            task_func(scores, 4)
        self.assertEqual(str(context.exception), "The student with ID 4 is not present in the test scores DataFrame.")

    def test_average_and_std_for_student_with_no_scores(self):
        scores = {'Student': [2, 3, 4], 'Score': [30, 40, 50]}
        with self.assertRaises(ValueError) as context:
            task_func(scores, 1)
        self.assertEqual(str(context.exception), "The student with ID 1 is not present in the test scores DataFrame.")

if __name__ == '__main__':
    unittest.main()