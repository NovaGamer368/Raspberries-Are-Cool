import sounddevice as sd
import wavio as wv
import speech_recognition as sr
import openai

openai.api_key = "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"

#sample frequency


#Recording duration (in seconds)

filename = "input.wav"
#sDuration is how long it records, freq is frequency of audio
def record_ai(sDuration, freq):
    print("RECORDING!!!!")
    recording = sd.rec(int(sDuration * freq),
                        samplerate=freq, channels=2)
    sd.wait()

    wv.write(filename, recording, freq, sampwidth=2)


    print("WE ARE DONE MAKING FILE")

    # Note: you need to be using OpenAI Python v0.27.0 for the code below to work
    audio_file= open(filename, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    print(filename + " was transcribes as: " + transcript['text'])

    return transcript['text']

