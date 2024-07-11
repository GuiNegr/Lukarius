#!/usr/bin/env python3

######IMPORTS DO PROJETO E SUAS EXPLICAÇÕES#######

'''ESSES ABAIXOS SÃO OS IMPORTS RESPOSANVEL PELO VOSK'''
# -> O VOSK É RESPONSAVEL POR PEGAR MINHA VOZ E CONSEGUIR TRANSOFARMAR ELA EM UMA STRING COM AJUDA DO JSON
from vosk import Model, KaldiRecognizer
import os
import pyaudio
import json


'''ESSE IMPORT SÃO PARA O PYTTX3 '''
# - > SERVE PARA TRAZER A BIBLIOTECA DO SINTESE DE VOZ UTILIZADO PARA OUVIRMOS A VOZ DO LUKARIUS
import pyttsx3


'''IMPOR REFERNTE AOS COMANDOS UTILIZADOS'''
# -> O PROPRIO NOME JA FALA
import cor


# -> INICIALIZAÇÃO DO SINTESE DE VOZ / CONSEGUIR ALOCAR PARA FICAR COM VOZ DE BRASILEIRO / INICALIZAÇÃO DE APRESENTAÇÃO

engine = pyttsx3.init()
voices = engine.getProperty('voices')
voice_id = None
for voice in voices:
    if 'brazil' in voice.id.lower() and b'\x05pt-br' in voice.languages: 
        voice_id = voice.id
        break
engine.setProperty('voice',voice_id)
engine.say("olá bom dia, meu nome é lukarius prazer")
engine.runAndWait()


# - > FUNÇÃO RESPOSANVEL POR MANDAR O LUKARIUS FALAR ALGUM TEXTO ESPECIFICO
def speak(text):
    engine.say(text)
    engine.runAndWait()




# - > UTILIZAÇÃO DO VOSK PARA CONSEGUIR CAPTAR MEU MICROFONE
model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
stream.start_stream()


# - > LAÇO DE REPETIÇÃO UTILIZADO PARA MANTER O LUKARIUS "VIVO"
while True:
    data = stream.read(2048)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        #UTILIZANDO O VOSK PARA RECUPERAR OQUE FOI DITO NO MICROFONE E TRANSFORMAR EM UM JSON PARA APOS ISSO CONSEGUIR SILIZAR OQUE SERIA TEXTO
        result = rec.Result()
        result = json.loads(result)
        
        if result is not None:
            
            text = result['text']
            print('VOCÊ FALA: ',text)

            if text == 'que horas são' or text == 'me diga as hora' or text == 'horas por favor':
                print(text)
                print('LUKARIUS RESPONDE: ',cor.SystemInfo.get_time())
                speak(cor.SystemInfo.get_time())
            else:
                speak("LUKARIUS REPETE: ",text)
  



