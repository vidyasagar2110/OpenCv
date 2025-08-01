import numpy as np

x = [3, 2, 3, 4]  # input sequence
X = np.fft.fft(x)
print("Input sequence:", x)
print("Fourier Transform:", X)