import pandas as pd
import random
import csv
import unittest

def task_func(n, 
           categories=['Sports', 'Technology', 'Business', 'Politics', 'Entertainment'],
           news_sites=['New York Times', 'USA Today', 'Apple News', 'CNN', 'BBC'],
           likert_scale=['Strongly Disagree', 'Disagree', 'Neither Agree nor Disagree', 'Agree', 'Strongly Agree'],
           file_path='news_survey_data.csv',
           random_seed=None):

    survey_data = []

    random.seed(random_seed)
    
    for _ in range(n):
        site = random.choice(news_sites)
        category = random.choice(categories)
        response = random.choice(likert_scale)
        value = likert_scale.index(response) + 1
        survey_data.append({'Site': site, 'Category': category, 'Response': response, 'Value': value})
    
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['Site', 'Category', 'Response', 'Value']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(survey_data)
        
    df = pd.read_csv(file_path)
    
    return df

class TestTaskFunc(unittest.TestCase):

    def test_generate_dataframe_shape(self):
        df = task_func(10, random_seed=1)
        self.assertEqual(df.shape, (10, 4), "DataFrame should have 10 rows and 4 columns")

    def test_dataframe_columns(self):
        df = task_func(5, random_seed=2)
        expected_columns = ['Site', 'Category', 'Response', 'Value']
        self.assertListEqual(list(df.columns), expected_columns, "DataFrame should have the correct columns")

    def test_likert_scale_values(self):
        df = task_func(100, random_seed=3)
        self.assertTrue(all(df['Value'].isin([1, 2, 3, 4, 5])), "Values in 'Value' column should only be from the Likert scale (1-5)")

    def test_randomness_with_seed(self):
        df1 = task_func(5, random_seed=42)
        df2 = task_func(5, random_seed=42)
        pd.testing.assert_frame_equal(df1, df2, "DataFrames should be identical when using the same random seed")

    def test_non_default_params(self):
        df = task_func(3, categories=['Food', 'Travel'], news_sites=['SiteA', 'SiteB'], likert_scale=['Bad', 'Average', 'Good'], random_seed=10)
        self.assertTrue(set(df['Category']).issubset({'Food', 'Travel'}), "Categories should be from the specified non-default list")
        self.assertTrue(set(df['Site']).issubset({'SiteA', 'SiteB'}), "Sites should be from the specified non-default list")
        self.assertTrue(set(df['Response']).issubset({'Bad', 'Average', 'Good'}), "Responses should be from the specified non-default Likert scale")

if __name__ == '__main__':
    unittest.main()