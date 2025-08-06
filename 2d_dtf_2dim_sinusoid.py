import numpy as np
import matplotlib.pyplot as plt

# Create a 2D signal (e.g., 2D sinusoidal pattern or a small grayscale image)
N = 64
x = np.arange(N)
y = np.arange(N)
X, Y = np.meshgrid(x, y)

# Create 2D sine wave pattern
f1, f2 = 5, 10  # frequencies in x and y directions
image = np.sin(2 * np.pi * f1 * X / N) + np.sin(2 * np.pi * f2 * Y / N)

# Compute 2D DFT
dft2d = np.fft.fft2(image)
dft_shifted = np.fft.fftshift(dft2d)  # shift zero freq to center
magnitude_spectrum = np.abs(dft_shifted)

# Plot original 2D signal and its magnitude spectrum
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Original 2D Signal (Sine Pattern)")
plt.colorbar()

plt.subplot(1, 2, 2)
plt.imshow(np.log1p(magnitude_spectrum), cmap='gray')  # log scale for visibility
plt.title("2D DFT Magnitude Spectrum (log scale)")
plt.colorbar()

plt.tight_layout()
plt.show()