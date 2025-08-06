import numpy as np
import matplotlib.pyplot as plt

# Create a 1D signal with low + high frequency components
Fs = 1000  # Sampling frequency (Hz)
T = 1      # Duration (seconds)
t = np.linspace(0, T, Fs, endpoint=False)
f1 = 30    # Low freq
f2 = 24   # High freq

x = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)  # Mixed signal

# Compute FFT
X = np.fft.fft(x)
freqs = np.fft.fftfreq(len(x), d=1/Fs)

# Create a low-pass filter mask
cutoff = 27  # Hz
H = np.abs(freqs) < cutoff  # Boolean mask

# Apply the low-pass filter
X_filtered = X * H

# Inverse FFT to get filtered signal
x_filtered = np.fft.ifft(X_filtered).real

# Plot original and filtered signals
plt.figure(figsize=(14, 6))

plt.subplot(4, 1, 1)
plt.plot(t, x, label='Original Signal')
plt.title("Time Domain")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

plt.subplot(4, 1, 2)
plt.plot(freqs[:Fs//2], np.abs(X[:Fs//2]), label='Original Spectrum')
plt.title("Frequency Domain (Magnitude Spectrum)")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.legend()
plt.grid(True)


plt.subplot(4, 1, 3)
plt.plot(freqs[:Fs//2], np.abs(X_filtered[:Fs//2]), label='Filtered Spectrum', linestyle='--')
plt.title("Frequency Domain (Magnitude Spectrum)")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.legend()
plt.grid(True)

plt.subplot(4, 1, 4)
plt.plot(t, x_filtered, label='Low-pass Filtered', linestyle='--')
plt.title("Time Domain")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()