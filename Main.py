#!/usr/bin/env python3

#vosk para ouvir meu mic
from vosk import Model, KaldiRecognizer
import os
import pyaudio
import json

#sintese de fala ##########################################################
import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')


#para poder localizar o suporte ded lingua portuguesa
voice_id = None
for voice in voices:
    if 'brazil' in voice.id.lower() and b'\x05pt-br' in voice.languages:  # Verifica se o ID contém 'brazil' e suporta pt-br
        voice_id = voice.id
        break

engine.setProperty('voice',voice_id)

engine.say("olá bom dia, meu nome é lukarius prazer")
engine.runAndWait()

#func feita para utilizar o sintese para reproduzir minhas falas
def speak(text):
    engine.say(text)
    engine.runAndWait()


#####################################################################################################

#FERRAMENTA DO VOSK PARA CONSEGUIR CAPTAR AUDIO
model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()


#ESSE É O CORPO PRINCIPAL ATÉ ENTÃO
while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
    #transformando o valor e um dicionario para posteriormente conseguir ler
        result = json.loads(result)
        
        if result is not None:
            text = result['text']
            print(text)
            speak(text)
  



