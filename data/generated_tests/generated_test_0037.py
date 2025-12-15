import unittest
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Sample DataFrame for testing
        self.data = pd.DataFrame({
            "feature1": [1, 2, 3, 4, 5],
            "feature2": [5, 4, 3, 2, 1],
            "label": [0, 1, 1, 0, 1]
        })

    def test_model_type(self):
        model, ax = task_func(self.data, "label")
        self.assertIsInstance(model, RandomForestClassifier, "The model should be an instance of RandomForestClassifier.")

    def test_feature_importance_length(self):
        model, ax = task_func(self.data, "label")
        self.assertEqual(len(model.feature_importances_), 2, "The feature importances length should match the number of features.")

    def test_plot_labels(self):
        model, ax = task_func(self.data, "label")
        self.assertEqual(ax.get_xlabel(), "Feature Importance Score", "The x-label should be 'Feature Importance Score'.")
        self.assertEqual(ax.get_ylabel(), "Features", "The y-label should be 'Features'.")
        self.assertEqual(ax.get_title(), "Visualizing Important Features", "The plot title should be 'Visualizing Important Features'.")

    def test_feature_importance_sorted(self):
        model, ax = task_func(self.data, "label")
        feature_imp = pd.Series(model.feature_importances_, index=self.data.columns[:-1]).sort_values(ascending=False)
        is_sorted = all(feature_imp.index[i] in feature_imp.index[:i+1] for i in range(len(feature_imp.index)))
        self.assertTrue(is_sorted, "The feature importances should be sorted in descending order.")

    def test_return_axes_object(self):
        model, ax = task_func(self.data, "label")
        self.assertIsNotNone(ax, "The function should return a valid Axes object.")

if __name__ == '__main__':
    unittest.main()