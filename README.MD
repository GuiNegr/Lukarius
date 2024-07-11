--ANTES DE INICIAR IREI EXPLICAR ESTE README. PARA FINS ESTUDANTIS POSTERIOR, ESTOU SEPARANDO AS ATUALIZAÇÕES E COMENTARIOS AQUI. BOM TODA VEZ Q TIVER UM NOME DE VERSIONAMENTO SERÁ OQUE TEVE DE ADIÇÃO NOVA NO LUKARIUS.--

# LUKARIUS 
um assinstente virutal feito em python.
utilizado um guide no ytb para fazer esse projeto.


# para usar não esquece  de  conectar na vm
abaixo em observações aparece o como fazer isso

# foco:
    ver como funciona um assitente virtual, e explorar outros ares da programação (sai do javakk)

# Técnologia:
    reconhecimento de voz(VOSK)
    sintese de voz.(pyttsx3)
    algum tipo de tecnologia de IA

# Observações:
estou utilizando um ambiente ubuntu e tive que fazer algumas instalações de pacotes python, acredito que seja normal isto. vou anotar os "codigos" utilizados aqui para futuramente me ajudar

- tar -xvf //extrai o arquivo tar.gz e exibi no terminal 

- sudo apt-get //serve para buscar uma um dependecia que o ubuntu reconhece.

- python3// para executar o arquivo python no terminal

- pip// utilizado em python para executar uma instalação de dependecia. no momento não consegui     utilizar // conseguii kkk mas so posso usar na vm

- python3 -m venv myenv// myenv será o nome do meu ambiente virtual

# IMPORTANTE DEMAISE
- source myenv/bin/activate // para  conseguir utilizar minha vm
- deactivate // ṕara desativar a vm.

para executar algumas coisas acredito que vou precisar da minha vm. 


# dependecias instaladas necessarias
SpeechRecognition == 3.10.4 // ESTOU UTILIZANDO O VOSK, PÓREM NÃO TENHO O CONHECIMENTO SE PRECISA DO SPEECH JÁ Q ELE É UMA API Q FAZ A MESMA COISA
pyaudio == 0.2.11
vosk == 0.3.7
pyttsx3 == 2.90



# problemas infrentados
    - por eu estar utilizado o sistema ubuntu. algumas permissões foram necessarias. apos executar o programa do jeito proposto
            import speech_recognition as sr

            locutor = sr.Recognizer()

            with sr.Microphone() as source:
                #aqui ele vai definir nossa fonte de audio como o microfone
                audio = locutor.listen(source)
                print(locutor.recognize_google(audio))
    o problema foi. o programa não estáva reconhecendo o dispositivo de audio do meu sistema. coloquei meu user para poder utilizar as opções de audio
        usando sudo usermod -a -G audio $USER
    creio que não era necessario pois utilizo meu microfone para call no discord, gravar com o obs e nunca tive esse problema

    oque foi a solução foi utizar o with com isso with sr.Microphone(device_index=inx)
    esse device index mostra para o programa qual dispositivo utilizar


-   migrei para um maquina virtual para conseguir utilizar o ambiente e gerenciar as dependencias certas

# AJUDA
 o with em python é utilizado para executar programas em python e gerenciar recursos externos dentro de um bloco de codigo especifico no meu caso o with é utilziado para abrir o gerenciador de audio e executar oque seŕa pedido, oque seria oque e a bliboteca que contem o  filereader do java mais ou menos faz

 aparentemente o python estou entendendo como uma linguagem meio que gravitacional, meio esquisito sabendo que estou acostumado com sistema de classes do java. não tenho a certeza se há esse tipo de programação em python. porém sei que ela é orientada a objetos.

 dicionarios? aparentemente são um tipo de classe que podemos atribuir com atributos, não sei se há metodos em dicionarios. acredito que não já que ele funciona como um alocamento de espaço.
 tenho um ambiente de estudos python em meu github. consultar caso precise de alguma informação do tipo declaração de variavel
 como funciona o sistema de iterações etc...


 # AMBIENTE VIRTUAL?
 bom estava dando um erro no meu python, e pesquisando vi que poderia criar uma vm dentro do meu computador para poder rodar python e instalar as bibliotecas, como vosk por exemplo. isso me deu brexa para utilizar o comando pip, q eu estava com problema já que o ubuntu barra por algum motivo


 # OQUE TEM ATÉ ENTÃO NO PROJETO
 -irei descrever as branchs utilizadas pelo fim de memorização de conteudo

# BranchWithLocutor
        - BRANCH INICIAL, ADICIONEI A POSSIBLIDADE DE UTILIZAR SPEECH. PORÉM SEGUINDO O TUTORIAL MIGRAMOS PARA O VOSK QUE É UMA API QUE CONSEGUE FAZER O RECONHECIMENTO DE MICROFONE PORÉM É OFFLINE. NÃO ENTENDO O PORQUE O SPEECH É ONLINE. OU SE O VOSK UTILIZA O SPEECH, ESSAS DUAS BIBLIOTECAS FORAM INSTALADA E TESTADAS, PORÉM OQUE RESTA NO CODIGO É A UTILIZAÇÃO DO VOSK. COM ISSO COLOQUEI UMA FERRAMENTA CHAMADA PYTTSX QUE SERVE PARA UTILIZAR O FAMOSO LOCUTOR DO GOOGLE PARA LER OQUE VOSK TRAZ COM MEU MICROFONE. AINDA NÃO FOI IMPLEMENTADA NENHUMA FUNÇÃO O CODIGO BASICO AGORA É ESTE ->

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
            

BOM ATÉ ENTÃO O PROGRAMA USA O LAÇO WHILE PARA FICAR EM FUNCIONAMENTO INFINITO ATÉ HOUVER UMA INTERRUPÇÃO, QUE NO CASO É PRESSIONAR UMA TECLA. A FUNC(DECLARADA COM DEF) speak faz com que execute a engine de reprodução do pytstx. dentro do loop é possivel ver metodos do vosk para captação do audio. é possivel ver que eu converto o valor para json(uma forma de dado de comunicação humana(ou seja humanamnete mais facil de compreender)) para conseguir um resultado chamado text. que sim é printado pelo metodo e então conseguir o valor desse text passando para a func speak para conseguir reproduizr o audio.




# BRANCH LUK0.3
    - BRANCH COM O FOCO DE ADIÇÃO DE COMANDOS PARA FUNCIONALIDADE DO ASSISTENTE VIRTUAL
    - ORGANIZAÇÃO DO MAIN
    - SÓ UM DETALHE BOBO(ACREDITO EU QUE VOU FICAR MUITO BOM EM IDENTAÇÃO POR CONTA DO PYTHON)

# BIBLIOTECAS NOVAS 
    - SNPIS NLU EXTRAI INFORMAÇÕES NO TEXTO QUE FOR EXTRAIDO DO SINTESE DE VOZ

# COMANDOS
    - CARA A SINTESE DO CODIO PARA ISSO É SIMPLES, O CODIGO JÁ RETORNA UMA STRING(O VOSK EM SI SÓ), COM UMA CLASSE CUJA AS FUNÇÃO DELA É SOMENTE GERAR METODOS. POSSO UTILIZAR PARA FAZER COMPARAÇOES

# AJUDA
     - COMPREENSÃO DE LINGUAGEM NATURAL(NLU)?
        UMA FORMA DE EXTRAIR UMA INFORMAÇÃO APARTIR DA FALA DO USUARIO QUE CONSIGUIMOS TRADUZIR PARA DADO COMPUTACIONAL E VICE VERSA

    - SIM APARENTEMENTE HÁ SISTEMAS DE CLASSES EM PYTHON 0_0

#!/usr/bin/env python3


# CODIGO DA VERSÃO luk0.3

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
  


    