A small tool that redirect tts output to audio input. Based on `edge-tts`.

# Prerequisites

You will need some audio cable device to do the redirection. I test it on [Virtual Audio Cable](https://vb-audio.com/Cable/). But I suppose it would work on other choices.

# Usage
If you are using a different audio cable device, you may need to change the device name in `utils.py`.

Just run `python main.py` and it will start accept tts input. Set your voice chat application input to audio cable output and it's done.

# Known issues
1. It seems not all audio API is usable. `WASAPI` complains about sample rate but `DirectSound` is OK.
2. There's significant delay between tts input and audio output.