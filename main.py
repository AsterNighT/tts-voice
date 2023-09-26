
import asyncio
import os
import uuid
import sys
import threading 
import signal
from stream import Streamer
from tts import TTSConfiguration,TTS
from utils import GetDeviceNumber

def signal_handler(sig, frame):
    try:
        os.rmdir("tmp")
    except FileExistsError:
        pass
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

tts = TTS(TTSConfiguration())
streamer = Streamer(GetDeviceNumber())

async def play(text:str):
    comm = tts.tts(text)
    name = uuid.uuid4().hex
    await comm.save("tmp/"+name+".wav")
    try:
        streamer.play("tmp/"+name+".wav")
    finally:
        os.remove("tmp/"+name+".wav")

class TTSThread(threading.Thread):
    def __init__(self, text):
        threading.Thread.__init__(self)
        self.text = text
    def run(self):
        asyncio.run(play(self.text))

async def main():
    try:
        os.mkdir("tmp")
    except FileExistsError:
        pass

    while True:
        text = input("Text: ")
        thread = TTSThread(text)
        thread.start()
        thread.join()
        
asyncio.run(main())