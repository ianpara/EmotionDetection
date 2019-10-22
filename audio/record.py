import sounddevice as sd
from scipy.io.wavfile import write
import audio.plot as plot
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile

fs = 44100  # Sample rate
seconds = 3  # Duration of recording

def start_recording():
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('audio/output.wav', fs, myrecording)  # Save as WAV file
    ims = plot.plotstft("output.wav")
