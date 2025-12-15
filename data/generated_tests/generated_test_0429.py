import pandas as pd
import unittest
import seaborn as sns
from sklearn.feature_selection import SelectKBest, f_classif
from your_module import task_func  # Replace 'your_module' with the name of your module where task_func is defined

class TestTaskFunc(unittest.TestCase):
    
    def test_feature_selection_shape(self):
        df1 = pd.DataFrame({
            'id': [1, 2, 3, 4],
            'feature1': [1.0, 2.0, 3.0, 4.0],
            'feature2': [5.0, 6.0, 7.0, 8.0],
            'feature3': [9.0, 10.0, 11.0, 12.0]
        })
        df2 = pd.DataFrame({
            'id': [1, 2, 3, 4],
            'target': [1, 2, 3, 4]
        })
        selected_features, heatmap = task_func(df1, df2)
        self.assertEqual(len(selected_features), 2)

    def test_selected_features_correctness(self):
        df1 = pd.DataFrame({
            'id': [1, 2, 3],
            'feature1': [1.2, 3.4, 5.6],
            'feature2': [2.3, 4.5, 6.7],
            'feature3': [3.4, 5.6, 7.8]
        })
        df2 = pd.DataFrame({
            'id': [1, 2, 3],
            'target': [4.5, 6.7, 8.9]
        })
        selected_features, heatmap = task_func(df1, df2)
        self.assertIn('feature2', selected_features)
        self.assertIn('feature3', selected_features)

    def test_heatmap_output_type(self):
        df1 = pd.DataFrame({
            'id': [1, 2, 3],
            'feature1': [1, 2, 3],
            'feature2': [4, 5, 6],
            'feature3': [7, 8, 9]
        })
        df2 = pd.DataFrame({
            'id': [1, 2, 3],
            'target': [1, 0, 1]
        })
        selected_features, heatmap = task_func(df1, df2)
        self.assertIsInstance(heatmap, sns.axisgrid.Heatmap)

    def test_feature_selection_with_non_matching_ids(self):
        df1 = pd.DataFrame({
            'id': [1, 2],
            'feature1': [1, 2],
            'feature2': [3, 4]
        })
        df2 = pd.DataFrame({
            'id': [3, 4],
            'target': [5, 6]
        })
        with self.assertRaises(KeyError):
            task_func(df1, df2)

    def test_empty_dataframes(self):
        df1 = pd.DataFrame(columns=['id', 'feature1', 'feature2'])
        df2 = pd.DataFrame(columns=['id', 'target'])
        with self.assertRaises(ValueError):
            task_func(df1, df2)

if __name__ == '__main__':
    unittest.main()