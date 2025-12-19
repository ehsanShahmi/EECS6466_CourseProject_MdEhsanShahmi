import pandas as pd
import collections
import unittest

def task_func(df):
    """
    Generate a sales report from a DataFrame, excluding duplicate customer names. 
    The report includes total sales and the most popular sales category.

    Parameters:
    df (DataFrame): A pandas DataFrame with columns 'Customer', 'Category', and 'Sales'.

    Returns:
    dict: A dictionary with keys 'Total Sales' (sum of sales) and 'Most Popular Category' (most frequent category).

    Requirements:
    - pandas
    - collections

    Raises:
    - The function will raise a ValueError is input df is not a DataFrame.

    Note:
    - The function would return the first category in alphabetical order for "Most Popular Category' in the case of tie

    Example:
    >>> data = pd.DataFrame([{'Customer': 'John', 'Category': 'Electronics', 'Sales': 500}, {'Customer': 'Mary', 'Category': 'Home', 'Sales': 300}])
    >>> report = task_func(data)
    >>> print(report)
    {'Total Sales': 800, 'Most Popular Category': 'Electronics'}
    """

               
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input df is not a DataFrame")
    
    df = df.drop_duplicates(subset='Customer')
    total_sales = df['Sales'].sum()
    popular_category = collections.Counter(df['Category']).most_common(1)[0][0]
    return {'Total Sales': total_sales, 'Most Popular Category': popular_category}


class TestTaskFunc(unittest.TestCase):
    
    def test_basic_functionality(self):
        data = pd.DataFrame([
            {'Customer': 'John', 'Category': 'Electronics', 'Sales': 500},
            {'Customer': 'Mary', 'Category': 'Home', 'Sales': 300}
        ])
        expected_report = {'Total Sales': 800, 'Most Popular Category': 'Electronics'}
        result = task_func(data)
        self.assertEqual(result, expected_report)

    def test_duplicate_customers(self):
        data = pd.DataFrame([
            {'Customer': 'John', 'Category': 'Electronics', 'Sales': 500},
            {'Customer': 'John', 'Category': 'Home', 'Sales': 300},
            {'Customer': 'Mary', 'Category': 'Home', 'Sales': 200}
        ])
        expected_report = {'Total Sales': 700, 'Most Popular Category': 'Home'}
        result = task_func(data)
        self.assertEqual(result, expected_report)

    def test_no_customers(self):
        data = pd.DataFrame(columns=['Customer', 'Category', 'Sales'])
        expected_report = {'Total Sales': 0, 'Most Popular Category': None}
        result = task_func(data)
        self.assertEqual(result['Total Sales'], expected_report['Total Sales'])
        self.assertIsNone(result['Most Popular Category'])

    def test_value_error_on_invalid_input(self):
        with self.assertRaises(ValueError) as context:
            task_func("invalid input")
        self.assertEqual(str(context.exception), "The input df is not a DataFrame")

    def test_tie_in_categories(self):
        data = pd.DataFrame([
            {'Customer': 'John', 'Category': 'A', 'Sales': 100},
            {'Customer': 'Mary', 'Category': 'B', 'Sales': 200},
            {'Customer': 'Alice', 'Category': 'A', 'Sales': 300}
        ])
        expected_report = {'Total Sales': 600, 'Most Popular Category': 'A'}
        result = task_func(data)
        self.assertEqual(result, expected_report)

if __name__ == '__main__':
    unittest.main()