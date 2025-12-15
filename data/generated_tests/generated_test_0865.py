import pandas as pd
import numpy as np
from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler
import unittest

def task_func(data):
    """
    This function takes a list of tuples containing elements and their respective counts and weights. 
    It normalizes the counts using z-score normalization and the weights using min-max scaling. 
    Finally, it returns a pandas DataFrame with the items, normalized counts, and normalized weights.
    (Implementation not shown)
    """
    # Extracting items, counts, and weights from the input data
    items, counts, weights = zip(*data)
    
    # Normalizing the counts and weights
    counts_normalized = zscore(counts)
    scaler = MinMaxScaler()
    weights_normalized = scaler.fit_transform(np.array(weights).reshape(-1, 1)).flatten()

    # Creating a DataFrame with the normalized data
    report_df = pd.DataFrame({
        'Item': items,
        'Normalized Count': counts_normalized,
        'Normalized Weight': weights_normalized
    })

    return report_df

class TestTaskFunc(unittest.TestCase):

    def test_basic_functionality(self):
        data = [('A', 100, 0.5), ('B', 200, 0.6), ('C', 150, 0.7)]
        expected_items = ['A', 'B', 'C']
        expected_counts = [-1.224745, 1.224745, 0.0]  # Z-score normalization
        expected_weights = [0.0, 0.5, 1.0]  # Min-Max normalization
        result = task_func(data)
        
        self.assertListEqual(result['Item'].tolist(), expected_items)
        self.assertAlmostEqual(result['Normalized Count'][0], expected_counts[0], places=6)
        self.assertAlmostEqual(result['Normalized Count'][1], expected_counts[1], places=6)
        self.assertAlmostEqual(result['Normalized Count'][2], expected_counts[2], places=6)
        self.assertAlmostEqual(result['Normalized Weight'][0], expected_weights[0], places=6)
        self.assertAlmostEqual(result['Normalized Weight'][1], expected_weights[1], places=6)
        self.assertAlmostEqual(result['Normalized Weight'][2], expected_weights[2], places=6)

    def test_negative_values(self):
        data = [('A', -50, 0.2), ('B', -100, 0.05), ('C', -75, 0.1)]
        expected_items = ['A', 'B', 'C']
        result = task_func(data)
        
        self.assertListEqual(result['Item'].tolist(), expected_items)

    def test_empty_input(self):
        data = []
        result = task_func(data)
        
        self.assertTrue(result.empty)

    def test_single_element(self):
        data = [('A', 1, 0.5)]
        expected_items = ['A']
        expected_counts = [0.0]  # Z-score normalization of single element
        expected_weights = [0.0]  # Min-Max scaling of single weight
        result = task_func(data)
        
        self.assertListEqual(result['Item'].tolist(), expected_items)
        self.assertAlmostEqual(result['Normalized Count'][0], expected_counts[0], places=6)
        self.assertAlmostEqual(result['Normalized Weight'][0], expected_weights[0], places=6)

    def test_large_numbers(self):
        data = [('A', 1000000, 1.0), ('B', 2000000, 0.5), ('C', 1500000, 0.75)]
        expected_items = ['A', 'B', 'C']
        result = task_func(data)
        
        self.assertListEqual(result['Item'].tolist(), expected_items)

if __name__ == '__main__':
    unittest.main()