import numpy as np
import matplotlib.pyplot as plt

# Define two signals
x = np.array([1, 2, 3, 4])
h = np.array([1, 1, 1])

# 1. Time-domain convolution
conv_time = np.convolve(x, h)

# 2. Frequency-domain multiplication
N = len(conv_time)  # length needed to avoid circular convolution
X = np.fft.fft(x, N)
H = np.fft.fft(h, N)
Y_freq = X * H
conv_freq = np.fft.ifft(Y_freq).real  # back to time domain

# Round small imaginary parts caused by numerical errors
conv_freq = np.round(conv_freq, decimals=5)

# Print results
print("Time domain convolution:     ", conv_time)
print("Freq domain (IFFT of mult):  ", conv_freq)

# Optional: plot to visualize
plt.figure(figsize=(10, 4))
plt.stem(range(len(conv_time)), conv_time, linefmt='b-', markerfmt='bo', basefmt=' ', label='Time-domain Convolution')
plt.stem(range(len(conv_freq)), conv_freq, linefmt='r--', markerfmt='ro', basefmt=' ', label='Freq-domain IFFT(X*H)')
plt.title("Convolution Theorem Demo")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()