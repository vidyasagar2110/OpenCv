import sounddevice as sd
import soundfile as sf

duration = 5  # seconds
samplerate = 44100

print("Recording...")
audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
sd.wait()
print("Recording complete.")
sf.write('voice_recording.wav', audio, samplerate)