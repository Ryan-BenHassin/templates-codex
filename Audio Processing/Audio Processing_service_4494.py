#TODO
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import wave
import pyaudio
import struct
import numpy as np

class AudioProcessor:
 def __init__(self, filename):
 self.filename = filename
 self.signal, self.sample_rate = librosa.load(filename)

 def display_waveform(self):
 plt.figure(figsize=(14, 5))
 librosa.display.waveplot(self.signal, sr=self.sample_rate)
 plt.title('Waveform')
 plt.show()

 def display_spectrogram(self):
 X = librosa.stft(self.signal)
 Xdb = librosa.amplitude_to_db(abs(X))
 plt.figure(figsize=(14, 5))
 librosa.display.specshow(Xdb, sr=self.sample_rate, x_axis='time', y_axis='hz')
 plt.title('Spectrogram')
 plt.colorbar()
 plt.show()

 def display_chroma(self):
 chroma = librosa.feature.chroma_stft(S=self.signal, sr=self.sample_rate)
 plt.figure(figsize=(14, 5))
 librosa.display.specshow(chroma, y_axis='chroma')
 plt.title('Chroma')
 plt.colorbar()
 plt.show()

 def reduce_dimensions(self):
 X = librosa.stft(self.signal)
 X = np.abs(X)
 scaler = StandardScaler()
 X_scaled = scaler.fit_transform(X)
 pca = PCA(n_components=2)
 X_pca = pca.fit_transform(X_scaled)
 return X_pca

class AudioStreamer:
 def __init__(self):
 self.FORMAT = pyaudio.paInt16
 self.CHANNELS = 2
 self.RATE = 44100
 self.CHUNK = 1024
 self.audio = pyaudio.PyAudio()
 self.stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)

 def start_streaming(self):
 while True:
 data = self.stream.read(self.CHUNK)
 data_int = struct.unpack(str(self.CHUNK) + 'B', data)
 data_np = np.array(data_int, dtype='b')[::2] + 128
 print(data_np)

 def close_stream(self):
 self.stream.stop_stream()
 self.stream.close()
 self.audio.terminate()

processor = AudioProcessor('audio_file.wav')
processor.display_waveform()
processor.display_spectrogram()
processor.display_chroma()
reduced_dimensions = processor.reduce_dimensions()
print(reduced_dimensions)

streamer = AudioStreamer()
streamer.start_streaming()
