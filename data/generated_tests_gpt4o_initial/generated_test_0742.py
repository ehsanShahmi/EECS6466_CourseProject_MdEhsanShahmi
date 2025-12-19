import unittest
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task_func(list_of_pairs):
    """
    Create a Pandas DataFrame from a list of pairs and normalize the data using MinMaxScaler.
    
    Parameters:
    list_of_pairs (list): A list of tuples, where the first element is the category and 
                          the second element is the value.
    
    Returns:
    DataFrame:  A pandas DataFrame containing the columns 'Category' and 'Value'.
                Category contains the the first elements of each tuple.
                Value contains the normalized values of each tuple.

    Raises:
        Exception: If the input array is empty.
        ValueError: If Values are not numeric.
    
    Requirements:
    - pandas
    - sklearn.preprocessing.MinMaxScaler
    """

    if len(list_of_pairs) == 0:
        raise Exception('The input array should not be empty.')

    df = pd.DataFrame(list_of_pairs, columns=['Category', 'Value'])

    if pd.api.types.is_numeric_dtype(df.Value) is not True:
        raise ValueError('The values have to be numeric.')

    scaler = MinMaxScaler()
    df['Value'] = scaler.fit_transform(df[['Value']])

    return df

class TestTaskFunc(unittest.TestCase):

    def test_normalize_positive_and_negative_values(self):
        list_of_pairs = [('Fruits', 5), ('Vegetables', 9), ('Dairy', -1), ('Bakery', -2), ('Meat', 4)]
        expected_data = {
            'Category': ['Fruits', 'Vegetables', 'Dairy', 'Bakery', 'Meat'],
            'Value': [0.636364, 1.0, 0.090909, 0.0, 0.545455]
        }
        result = task_func(list_of_pairs)
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(result, expected_df)

    def test_normalize_values_with_zero_and_negative(self):
        list_of_pairs = [('car', 3.2), ('bike', 0), ('train', -1), ('plane', -6.2), ('ship', 1234)]
        expected_data = {
            'Category': ['car', 'bike', 'train', 'plane', 'ship'],
            'Value': [0.007579, 0.004999, 0.004193, 0.0, 1.0]
        }
        result = task_func(list_of_pairs)
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(result, expected_df)

    def test_empty_list_raises_exception(self):
        with self.assertRaises(Exception) as context:
            task_func([])
        self.assertEqual(str(context.exception), 'The input array should not be empty.')

    def test_non_numeric_values_raises_valueerror(self):
        list_of_pairs = [('Fruits', 'five'), ('Vegetables', 'nine')]
        with self.assertRaises(ValueError) as context:
            task_func(list_of_pairs)
        self.assertEqual(str(context.exception), 'The values have to be numeric.')

    def test_mixed_types_raises_valueerror(self):
        list_of_pairs = [('Fruits', 5), ('Vegetables', 'two'), ('Dairy', 3)]
        with self.assertRaises(ValueError) as context:
            task_func(list_of_pairs)
        self.assertEqual(str(context.exception), 'The values have to be numeric.')

if __name__ == '__main__':
    unittest.main()