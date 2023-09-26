import sounddevice as sd
import soundfile as sf

"""
Stream a audio file into a voice cable
"""

class Streamer:
    def __init__(self, device):
        sd.default.device = device
    def play(self, file:str):
        data, fs = sf.read(file)
        sd.play(data, fs)
        sd.wait()