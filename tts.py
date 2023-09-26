"""
Generate audio from texts
"""

import edge_tts

class TTSConfiguration:
    def __init__(self, voice:str = "zh-CN-XiaoyiNeural", rate:str = "+0%", volume:str = "+0%", pitch:str = "+0HZ"):
        self.voice = voice
        self.rate = rate
        self.volume = volume
        self.pitch = pitch
        

class TTS:
    def __init__(self, config:TTSConfiguration):
        self.config = config

    def tts(self, text:str):
        communicate = edge_tts.Communicate(text, voice = self.config.voice, rate=self.config.rate, volume=self.config.volume)
        return communicate