import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft, fftfreq

# Load audio file
data, samplerate = sf.read("voice_recording.wav")  # Use your own file path
print(f"Sample rate: {samplerate}, Length: {len(data)} samples")

# Use only one channel if stereo
if len(data.shape) > 1:
    data = data[:, 0]

# Time vector
t = np.arange(len(data)) / samplerate

# FFT
N = len(data)
yf = fft(data)
xf = fftfreq(N, 1 / samplerate)

# Low-pass filter: Keep frequencies < 1000 Hz
cutoff = 9000
low_pass_mask = np.abs(xf) < cutoff
low_passed = ifft(yf * low_pass_mask)

# High-pass filter: Keep frequencies > 1000 Hz
high_pass_mask = np.abs(xf) > cutoff
high_passed = ifft(yf * high_pass_mask)

# Save filtered outputs
sf.write("low_passed.wav", np.real(low_passed), samplerate)
sf.write("high_passed.wav", np.real(high_passed), samplerate)

# Plot
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(xf[:N//2], np.abs(yf[:N//2]))
plt.title("Original Frequency Spectrum")
plt.xlabel("Frequency (Hz)")
plt.subplot(1, 2, 2)
plt.plot(t[:1000], data[:1000])
plt.title("Time Domain Signal")
plt.tight_layout()
plt.show()