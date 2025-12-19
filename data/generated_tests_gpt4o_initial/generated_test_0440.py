import numpy as np
import pandas as pd
import unittest
from sklearn.preprocessing import StandardScaler

# Here is your prompt:
def task_func(P, T):
    """
    Calculate the product of matrix "P" and 3D tensor "T" then return dataframe of normalized results.

    This function performs matrix-tensor multiplication between a matrix "P" and a 3D tensor "T" using numpy.
    It checks if the shapes of P and T are compatible for multiplication, raising a ValueError if they are not.
    The function then normalizes the resulting 2D array using sklearn's StandardScaler. The final output
    is returned as a pandas DataFrame, with columns named feature_0, feature_1, ..., feature_n,
    where n is the number of features in the flattened result of the matrix-tensor multiplication.

    Parameters:
    - P (numpy.ndarray): The input matrix. Must not be empty.
    - T (numpy.ndarray): The input tensor. Must not be empty.

    Returns:
    pandas.DataFrame: A DataFrame with the normalized result.

    Requirements:
    - numpy
    - pandas
    - sklearn.preprocessing
    """

    if P.size == 0 or T.size == 0:
        raise ValueError("Inputs cannot be empty.")
    if P.shape[1] != T.shape[0]:
        raise ValueError(
            f"Matrix P shape {P.shape[1]} and Tensor T shape {T.shape[0]} are incompatible for tensor multiplication."
        )

    result = np.tensordot(P, T, axes=[1, 0]).swapaxes(0, 1)
    result = result.reshape(result.shape[0], -1)

    scaler = StandardScaler()
    result = scaler.fit_transform(result)

    adjusted_feature_names = [f"feature_{i}" for i in range(result.shape[1])]
    result = pd.DataFrame(result, columns=adjusted_feature_names)

    return result


class TestTaskFunc(unittest.TestCase):

    def test_empty_matrix(self):
        """Test with empty matrix P"""
        P = np.array([]).reshape(0, 3)
        T = np.random.rand(3, 5, 5)
        with self.assertRaises(ValueError) as context:
            task_func(P, T)
        self.assertEqual(str(context.exception), "Inputs cannot be empty.")

    def test_empty_tensor(self):
        """Test with empty tensor T"""
        P = np.random.rand(5, 3)
        T = np.array([]).reshape(3, 0, 0)
        with self.assertRaises(ValueError) as context:
            task_func(P, T)
        self.assertEqual(str(context.exception), "Inputs cannot be empty.")

    def test_incompatible_shapes(self):
        """Test with incompatible shapes"""
        P = np.random.rand(5, 2)
        T = np.random.rand(3, 5, 5)  # 3 != 2
        with self.assertRaises(ValueError) as context:
            task_func(P, T)
        self.assertEqual(str(context.exception), "Matrix P shape 2 and Tensor T shape 3 are incompatible for tensor multiplication.")

    def test_valid_input_shape(self):
        """Test with valid shapes and check output type"""
        P = np.random.rand(5, 3)
        T = np.random.rand(3, 5, 5)
        result = task_func(P, T)
        self.assertIsInstance(result, pd.DataFrame)

    def test_normalization_of_output(self):
        """Test to check if the output is normalized"""
        P = np.random.rand(5, 3)
        T = np.random.rand(3, 5, 5)
        result = task_func(P, T)
        self.assertAlmostEqual(result.mean().mean(), 0, delta=0.1)
        self.assertAlmostEqual(result.std().mean(), 1, delta=0.1)


if __name__ == '__main__':
    unittest.main()