import unittest
import numpy as np
import pandas as pd

from sklearn.exceptions import NotFittedError

# Here is your prompt:
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def task_func(data, columns, target_column):
    """
    Perform a logistic regression on a DataFrame to predict a specific target column.
    
    Parameters:
    - data (numpy.array): The input data as a NumPy array.
    - columns (list): The list of column names.
    - target_column (str): The target column name.

    Returns:
    - accuracy (float): The accuracy of the logistic regression model.

    Requirements:
    - pandas
    - sklearn
    
    Example:
    >>> import numpy as np
    >>> np.random.seed(42)
    >>> data = np.random.randint(0, 100, size=(100, 4))  # Using np to generate random data
    >>> columns = ['A', 'B', 'C', 'target']
    >>> task_func(data, columns, 'target')
    0.0
    """
    
    df = pd.DataFrame(data, columns=columns)
    if target_column not in df.columns:
        raise ValueError('Target column does not exist in DataFrame')

    X = df.drop(columns=target_column)  # Operate directly on the DataFrame
    y = df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    return accuracy

class TestTaskFunc(unittest.TestCase):

    def test_with_valid_input(self):
        np.random.seed(42)
        data = np.random.randint(0, 100, size=(100, 4))
        columns = ['A', 'B', 'C', 'target']
        accuracy = task_func(data, columns, 'target')
        self.assertIsInstance(accuracy, float)
        self.assertGreaterEqual(accuracy, 0.0)
        self.assertLessEqual(accuracy, 1.0)

    def test_with_nonexistent_target_column(self):
        data = np.random.randint(0, 100, size=(100, 4))
        columns = ['A', 'B', 'C', 'target']
        with self.assertRaises(ValueError):
            task_func(data, columns, 'nonexistent_column')

    def test_with_binary_classification(self):
        data = np.array([[0, 0, 0, 0], 
                         [1, 1, 1, 1],
                         [0, 0, 0, 0],
                         [1, 1, 1, 1]])
        columns = ['A', 'B', 'C', 'target']
        accuracy = task_func(data, columns, 'target')
        self.assertIsInstance(accuracy, float)
        self.assertEqual(accuracy, 1.0)  # Perfect accuracy due to binary case

    def test_with_insufficient_data(self):
        # Inputting very limited data points (less than 2 for train-test split)
        data = np.array([[0, 0, 0, 0], 
                         [1, 1, 1, 1]])
        columns = ['A', 'B', 'C', 'target']
        with self.assertRaises(ValueError):
            task_func(data, columns, 'target')

    def test_with_prediction_on_unfitted_model(self):
        # Directly testing if the model can be predict on unfitted data (though it doesn't invoke here)
        data = np.random.randint(0, 100, size=(100, 4))
        columns = ['A', 'B', 'C', 'target']
        X = pd.DataFrame(data, columns=columns[:-1])
        model = LogisticRegression()
        with self.assertRaises(NotFittedError):
            model.predict(X)  # This should raise an error since the model isn't fitted

if __name__ == '__main__':
    unittest.main()