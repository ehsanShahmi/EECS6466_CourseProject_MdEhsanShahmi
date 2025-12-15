import numpy as np
import unittest
import matplotlib.pyplot as plt
from scipy.signal import get_window

def task_func(amplitude, frequency, time):
    """
    Generates and plots a complex wave with a specified amplitude and frequency over given time points,
    applying a Hann window to reduce edge effects. The wave is represented as a complex number where the real part 
    is the cosine component, and the imaginary part is the sine component. It returns both the wave and the plot object.

    Parameters:
        amplitude (float): The amplitude of the complex wave.
        frequency (float): The frequency of the complex wave.
        time (numpy.ndarray): The time points to generate the wave.

    Returns:
        numpy.ndarray: The generated complex wave as a numpy array of complex numbers.
        matplotlib.figure.Figure: The figure object of the plot.
        matplotlib.axes.Axes: The axes object of the plot.

    Requirements:
    - numpy
    - math
    - matplotlib.pyplot
    - scipy.signal.get_window

    Notes:
    - The plot title is "Complex Wave with Hann Window".
    - The x-label of the plot is "Time".
    - The y-label of the plot is "Amplitude".
    - The plot displays both the real and imaginary parts of the complex wave.

    Examples:
    >>> wave, fig, ax = task_func(1, 1, np.linspace(0, 1, 10, endpoint=False))
    >>> len(wave) == 10
    True
    >>> isinstance(wave[0], complex)
    True
    """

    wave = amplitude * np.exp(1j * 2 * math.pi * frequency * time)
    window = get_window('hann', time.size)  # Apply a Hann window
    wave *= window  # Apply the window to the wave

    # Plot the wave
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(time, np.real(wave), label="Real Part")
    ax.plot(time, np.imag(wave), label="Imaginary Part")
    ax.set_title("Complex Wave with Hann Window")
    ax.set_xlabel("Time")
    ax.set_ylabel("Amplitude")
    ax.legend()

    return wave, fig, ax

class TestTaskFunction(unittest.TestCase):
    
    def test_wave_length(self):
        """Test if the wave has the correct length."""
        time_points = np.linspace(0, 1, 10, endpoint=False)
        wave, _, _ = task_func(1, 1, time_points)
        self.assertEqual(len(wave), len(time_points), "Length of wave should match time points.")
    
    def test_wave_complex_type(self):
        """Test if the wave is composed of complex numbers."""
        time_points = np.linspace(0, 1, 10, endpoint=False)
        wave, _, _ = task_func(1, 1, time_points)
        self.assertTrue(np.all(np.iscomplex(wave)), "All elements in the wave should be complex.")

    def test_amplitude_effect(self):
        """Test if the amplitude scales the wave correctly."""
        time_points = np.linspace(0, 1, 100, endpoint=False)
        amplitude = 2
        wave1, _, _ = task_func(amplitude, 1, time_points)
        wave2, _, _ = task_func(1, 1, time_points)
        self.assertTrue(np.allclose(np.real(wave1), 2 * np.real(wave2)), "Wave should scale linearly with amplitude.")

    def test_plot_labels(self):
        """Test if the plot has the correct labels."""
        time_points = np.linspace(0, 1, 10, endpoint=False)
        _, fig, ax = task_func(1, 1, time_points)
        self.assertEqual(ax.get_xlabel(), "Time", "X-axis label should be 'Time'.")
        self.assertEqual(ax.get_ylabel(), "Amplitude", "Y-axis label should be 'Amplitude'.")
        self.assertEqual(ax.get_title(), "Complex Wave with Hann Window", "Plot title should be correct.")

    def test_wave_frequency_effect(self):
        """Test if the frequency affects the wave's oscillation."""
        time_points = np.linspace(0, 1, 100, endpoint=False)
        wave1, _, _ = task_func(1, 1, time_points)
        wave2, _, _ = task_func(2, time_points)
        self.assertFalse(np.array_equal(wave1, wave2), "Waves with different frequencies should not be identical.")

if __name__ == '__main__':
    unittest.main()