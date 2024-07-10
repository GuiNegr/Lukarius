import pyttsx3
engine = pyttsx3.init()


voices = engine.getProperty('voices')


#para poder localizar o suporte de lingua portuguesa
voice_id = None
for voice in voices:
    if 'brazil' in voice.id.lower() and b'\x05pt-br' in voice.languages:  # Verifica se o ID contém 'brazil' e suporta pt-br
        voice_id = voice.id
        break

engine.setProperty('voice',voice_id)

engine.say("olá bom dia, meu nome é lukarius prazer")
engine.runAndWait()
