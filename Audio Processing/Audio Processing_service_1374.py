import librosa
import numpy as np
from pydub import AudioSegment

def audio_processing(file_path, sample_rate, trim_silence=False):
 audio, sr = librosa.load(file_path, sr=sample_rate)
 
 if trim_silence:
 audio, _ = librosa.effects.trim_silence(audio, top_db=30)
 
 return audio

def convert_wav_to_mp3(file_path):
 sound = AudioSegment.from_file(file_path)
 mp3_file_path = file_path.replace('.wav', '.mp3')
 sound.export(mp3_file_path, format="mp3")

def resample_audio(file_path, new_sample_rate):
 audio, sr = librosa.load(file_path)
 resampled_audio = librosa.resample(audio, sr, new_sample_rate)
 return resampled_audio

def apply_noise_reduction(file_path, noise_reduce_db=30):
 audio, sr = librosa.load(file_path)
 reduced_noise = np.array([0.0] README.md categories.txt generate.sh start.sh systemPrompt.txt templates len(audio))
 start_band = 2000
 for i in range(len(audio)):
 if audio[i] > noise_reduce_db:
 reduced_noise[i] = audio[i]
 else:
 reduced_noise[i] = audio[i] - noise_reduce_db
 return reduced_noise

def main():
 file_path = 'input.wav'
 sample_rate = 22050
 trim_silence = True
 
 audio = audio_processing(file_path, sample_rate, trim_silence)
 
 # Save processed audio to new wav file
 librosa.output.write_wav('output.wav', audio, sample_rate)
 
 # Convert output wav to mp3
 convert_wav_to_mp3('output.wav')
 
 # Resample audio
 resampled_audio = resample_audio('output.wav', 16000)
 librosa.output.write_wav('resampled_output.wav', resampled_audio, 16000)
 
 # Apply noise reduction
 reduced_noise_audio = apply_noise_reduction('output.wav')
 librosa.output.write_wav('reduced_noise_output.wav', reduced_noise_audio, sample_rate)

if __name__ == "__main__":
 main()
