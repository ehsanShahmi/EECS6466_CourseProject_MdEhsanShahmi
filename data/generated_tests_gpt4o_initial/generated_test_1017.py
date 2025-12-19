import pandas as pd
import unittest
from unittest.mock import patch, MagicMock
import numpy as np
from sklearn.exceptions import NotFittedError

# Here is your prompt:
def task_func(csv_file_path, target_column="target", test_size=0.2, n_estimators=100):
    """
    Processes a CSV file to train a Random Forest classifier and generates a formatted classification report.

    Parameters:
        csv_file_path (str): The path to the CSV file containing the data.
        target_column (str, optional): The name of the target variable column. Defaults to 'target'.
        test_size (float, optional): The proportion of the dataset to include in the test split. Defaults to 0.2.
        n_estimators (int, optional): The number of trees in the RandomForestClassifier. Defaults to 100.

    Returns:
        str: A formatted classification report. The report includes metrics such as precision, recall,
             f1-score for each class, as well as overall accuracy, macro average, and weighted average.

    Raises:
        ValueError: If the specified target_column is not found in the CSV file.

    Requirements:
        - pandas
        - sklearn

    Example:
    >>> report = task_func('/path/to/data.csv')
    >>> print(report)
    class 0        0.88       0.90       0.89          50
    class 1        0.89       0.87       0.88          48
    ...
    accuracy                           0.89         100
    macro avg       0.88       0.89       0.88         100
    weighted avg    0.89       0.89       0.89         100

    Note:
        The CSV file must have a column with the name specified by 'target_column', and it should be in a
        format readable by pandas.read_csv().
    """

    df = pd.read_csv(csv_file_path)
    if target_column not in df.columns:
        raise ValueError(f"'{target_column}' column not found in the CSV file.")

    X = df.drop(target_column, axis=1)
    y = df[target_column]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42
    )
    clf = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    report = classification_report(y_test, y_pred)

    # New formatting approach
    lines = report.split("\n")
    formatted_lines = []
    for line in lines:
        # Split the line into words and rejoin with specific spacing
        parts = line.split()
        if len(parts) == 5:  # Class-specific metrics
            formatted_line = f"{parts[0]:<15}{parts[1]:>10}{parts[2]:>10}{parts[3]:>10}{parts[4]:>10}"
        elif len(parts) == 4:  # Overall metrics
            formatted_line = f"{parts[0]:<15}{parts[1]:>10}{parts[2]:>10}{parts[3]:>10}"
        else:
            formatted_line = line  # Header or empty lines
        formatted_lines.append(formatted_line)

    formatted_report = "\n".join(formatted_lines)
    return formatted_report

class TestTaskFunc(unittest.TestCase):

    @patch('pandas.read_csv')
    def test_valid_csv_file(self, mock_read_csv):
        # Mock a dataframe that has the target column and features
        mock_df = pd.DataFrame({
            'feature1': [0, 1, 0, 1],
            'feature2': [1, 0, 1, 0],
            'target': [0, 1, 0, 1]
        })
        mock_read_csv.return_value = mock_df

        report = task_func('dummy_path.csv', 'target')
        self.assertIn("class 0", report)
        self.assertIn("class 1", report)

    @patch('pandas.read_csv')
    def test_value_error_for_missing_target_column(self, mock_read_csv):
        # Mock a dataframe that is missing the target column
        mock_df = pd.DataFrame({
            'feature1': [0, 1, 0, 1],
            'feature2': [1, 0, 1, 0]
        })
        mock_read_csv.return_value = mock_df

        with self.assertRaises(ValueError) as context:
            task_func('dummy_path.csv', 'target')
        self.assertEqual(str(context.exception), "'target' column not found in the CSV file.")

    @patch('pandas.read_csv')
    def test_test_size_parameter(self, mock_read_csv):
        mock_df = pd.DataFrame({
            'feature1': np.random.rand(100),
            'feature2': np.random.rand(100),
            'target': np.random.choice([0, 1], size=100)
        })
        mock_read_csv.return_value = mock_df

        report = task_func('dummy_path.csv', 'target', test_size=0.3)
        self.assertIn("accuracy", report)

    @patch('pandas.read_csv')
    def test_n_estimators_parameter(self, mock_read_csv):
        mock_df = pd.DataFrame({
            'feature1': np.random.rand(100),
            'feature2': np.random.rand(100),
            'target': np.random.choice([0, 1], size=100)
        })
        mock_read_csv.return_value = mock_df

        report = task_func('dummy_path.csv', 'target', n_estimators=50)
        self.assertIn("accuracy", report)

    @patch('pandas.read_csv')
    def test_classification_report_formatting(self, mock_read_csv):
        mock_df = pd.DataFrame({
            'feature1': [0, 1, 0, 1, 0],
            'feature2': [1, 0, 1, 0, 1],
            'target': [0, 1, 0, 1, 0]
        })
        mock_read_csv.return_value = mock_df

        report = task_func('dummy_path.csv', 'target')
        lines = report.split("\n")
        for line in lines[1:]:
            if line.strip():  # Skip empty lines
                parts = line.split()
                self.assertGreaterEqual(len(parts), 4)

if __name__ == '__main__':
    unittest.main()