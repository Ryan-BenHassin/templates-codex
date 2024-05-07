#TODO
import librosa
import numpy as np
from scipy.io.wavfile import write
from pydub import AudioSegment
import os

class AudioProcessor:
 def __init__(self, file_path):
 self.file_path = file_path

 def load_audio(self):
 audio, sr = librosa.load(self.file_path)
 return audio, sr

 def trim_silence(self, audio, sr, threshold):
 intervals = librosa.effects.split(audio, top_db=threshold)
 trimmed_audio = np.concatenate([audio[i[0]:i[1]] for i in intervals])
 returntrimmed_audio

 def change_pitch(self, audio, sr, semitones):
 return librosa.effects.pitch_shift(audio, sr, semitones)

 def change_speed(self, audio, sr, speed_ratio):
 return librosa.effects.speed(audio, sr, speed_ratio)

 def export_wav(self, audio, sr):
 write("output.wav", sr, audio)

 def convert_mp3_to_wav(self):
 sound = AudioSegment.from_mp3(self.file_path)
 sound.export("output.wav", format="wav")

def main():
 processor = AudioProcessor("input.mp3")
 processor.convert_mp3_to_wav()
 audio, sr = processor.load_audio()
 trimmed_audio = processor.trim_silence(audio, sr, 20)
 pitched_audio = processor.change_pitch(trimmed_audio, sr, 2)
 sped_audio = processor.change_speed(pitched_audio, sr, 1.2)
 processor.export_wav(sped_audio, sr)

if __name__ == "__main__":
 main()
