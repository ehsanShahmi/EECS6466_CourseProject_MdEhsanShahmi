import unittest
import numpy as np

# The provided prompt
import tensorflow as tf
from sklearn.model_selection import KFold
from sklearn.preprocessing import MinMaxScaler

def task_func(X, y, n_splits, batch_size, epochs):
    """
    Trains a simple neural network on provided data using k-fold cross-validation.
    The network has one hidden layer with 20 neurons and ReLU activation, and
    an output layer with sigmoid activation for binary classification.

    Parameters:
        X (numpy.array): The input data.
        y (numpy.array): The target data.
        n_splits (int): The number of splits for k-fold cross-validation. Default is 5.
        batch_size (int): The size of the batch used during training. Default is 32.
        epochs (int): The number of epochs for training the model. Default is 1.

    Returns:
        list: A list containing the training history of the model for each fold. Each history
              object includes training loss and accuracy.

    Requirements:
    - tensorflow
    - sklearn.model_selection.KFold
    - sklearn.preprocessing.MinMaxScaler

    Examples:
    >>> import numpy as np
    >>> X = np.random.rand(100, 10)
    >>> y = np.random.randint(0, 2, 100)
    >>> history = task_func(X, y, 5, 32, 1)
    >>> isinstance(history, list)
    True
    >>> len(history)
    5
    >>> all('loss' in hist.history.keys() for hist in history)
    True
    """

    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    kf = KFold(n_splits=n_splits)
    history = []

    for train_index, test_index in kf.split(X_scaled):
        X_train, X_test = X_scaled[train_index], X_scaled[test_index]
        y_train, y_test = y[train_index], y[test_index]

        model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(20, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])

        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

        hist = model.fit(X_train, y_train, validation_data=(X_test, y_test), batch_size=batch_size, epochs=epochs, verbose=0)
        history.append(hist)

    return history


class TestTaskFunc(unittest.TestCase):

    def test_output_is_list(self):
        X = np.random.rand(100, 10)
        y = np.random.randint(0, 2, 100)
        history = task_func(X, y, 5, 32, 1)
        self.assertIsInstance(history, list)

    def test_output_length(self):
        X = np.random.rand(100, 10)
        y = np.random.randint(0, 2, 100)
        history = task_func(X, y, 5, 32, 1)
        self.assertEqual(len(history), 5)

    def test_history_contains_loss(self):
        X = np.random.rand(100, 10)
        y = np.random.randint(0, 2, 100)
        history = task_func(X, y, 5, 32, 1)
        self.assertTrue(all('loss' in hist.history.keys() for hist in history))

    def test_training_accuracy(self):
        X = np.random.rand(100, 10)
        y = np.random.randint(0, 2, 100)
        history = task_func(X, y, 5, 32, 1)
        self.assertTrue(all('accuracy' in hist.history.keys() for hist in history))

    def test_n_splits(self):
        X = np.random.rand(100, 10)
        y = np.random.randint(0, 2, 100)
        history = task_func(X, y, 3, 32, 1)  # Testing with different n_splits
        self.assertEqual(len(history), 3)


if __name__ == '__main__':
    unittest.main()