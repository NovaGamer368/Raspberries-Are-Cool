import openai
import os
import tempfile
import time
import traceback

from aiy.voice.audio import AudioFormat, play_wav, record_file

openai.api_key = "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"

#sample frequency


#Recording duration (in seconds)

#filename = "input.wav"
#sDuration is how long it records, freq is frequency of audio
#def record_ai(sDuration, freq):
#    print("RECORDING!!!!")
#    recording = sd.rec(int(sDuration * freq),
#                        samplerate=freq, channels=2)
#    sd.wait()
#
#    wv.write(filename, recording, freq, sampwidth=2)
#
#
#   print("WE ARE DONE MAKING FILE")
#
#   # Note: you need to be using OpenAI Python v0.27.0 for the code below to work
#  audio_file= open(filename, "rb")
# transcript = openai.Audio.transcribe("whisper-1", audio_file)
#
#   print(filename + " was transcribes as: " + transcript['text'])
#
#   return transcript['text']

#-----------------------------------------------------------------------------

def get_input(RECORD_DURATION_SECONDS):
    with tempfile.NamedTemporaryFile(suffix=".wav") as f:
        print('RECORDING!!!! YOU GOT 7 SECONDS')
        #Making recording file to the tempfile
        record_file(AudioFormat.CD, filename=f.name, filetype='wav',
                        wait=lambda: time.sleep(RECORD_DURATION_SECONDS))
        #print('Playing back recorded audio...')
        #play_wav(f.name)
        
        print('FINISHED')
        print('transcribing\n')
        audio_file= open(f.name, "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file)

        print(f.name + " was transcribes as: " + transcript['text'])
        return transcript['text']
    
