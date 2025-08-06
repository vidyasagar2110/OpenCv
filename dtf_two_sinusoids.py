import numpy as np
import matplotlib.pyplot as plt

# Parameters
Fs = 1000          # Sampling frequency in Hz
T = 1              # Duration in seconds
f = 49            # Frequency of sine wave in Hz
t = np.linspace(0, T, int(Fs*T), endpoint=False)  # Time vector

# Generate sine wave
x = np.sin(2 * np.pi * f * t)+np.sin(2 * np.pi * 25 * t)

# Compute DFT using FFT
X = np.fft.fft(x)
N = len(X)
frequencies = np.fft.fftfreq(N, 1/Fs)

# Plot time-domain signal
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(t, x)
plt.title("Sine Wave in Time Domain")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

# Plot magnitude spectrum (only positive frequencies)
plt.subplot(1, 2, 2)
plt.stem(frequencies[:N//2], np.abs(X[:N//2]) * 2 / N)
plt.title("Magnitude Spectrum (DFT)")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.tight_layout()
plt.grid(True)
plt.show()