import numpy as np
import os
import soundfile as sf
import librosa
import matplotlib.pyplot as plt
import unittest

class TestTaskFunction(unittest.TestCase):

    def setUp(self):
        """Prepare the test environment."""
        self.test_audio_file = 'test_audio.wav'
        # Create a test audio file
        self.create_test_audio_file(self.test_audio_file)

    def tearDown(self):
        """Clean up the test environment."""
        if os.path.isfile(self.test_audio_file):
            os.remove(self.test_audio_file)

    def create_test_audio_file(self, filename):
        """Create a simple test audio file."""
        # Generate a 1-second sine wave at 440 Hz
        fs = 44100  # Sampling frequency
        t = np.linspace(0, 1, fs, endpoint=False)  # Generate time values
        audio_data = 0.5 * np.sin(2 * np.pi * 440 * t)  # Generate sine wave
        sf.write(filename, audio_data, fs)  # Write to file

    def test_empty_list(self):
        """Test with an empty list"""
        with self.assertRaises(ValueError):
            task_func([], 1, 1, self.test_audio_file)

    def test_matrix_shape(self):
        """Test if the output matrix has the correct shape."""
        matrix, _ = task_func([i for i in range(100)], 10, 10, self.test_audio_file)
        self.assertEqual(matrix.shape, (10, 10))

    def test_output_type(self):
        """Test if the output is of correct type."""
        matrix, fig = task_func([i for i in range(100)], 10, 10, self.test_audio_file)
        self.assertIsInstance(matrix, np.ndarray)
        self.assertIsInstance(fig, plt.Figure)

    def test_file_not_found(self):
        """Test with a non-existent audio file."""
        with self.assertRaises(FileNotFoundError):
            task_func([i for i in range(100)], 10, 10, 'non_existent_file.wav')

    def test_spl_normalization(self):
        """Test if the matrix is normalized correctly based on SPL."""
        matrix, _ = task_func([i for i in range(100)], 10, 10, self.test_audio_file)
        max_value = np.max(matrix)
        self.assertAlmostEqual(max_value, 20 * np.log10(np.sqrt(np.mean(np.sin(2 * np.pi * 440 * np.linspace(0, 1, 44100) ** 2))), places=5)


if __name__ == '__main__':
    unittest.main()