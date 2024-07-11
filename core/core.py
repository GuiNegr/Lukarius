'''''
CLASSE RESPONSAVEL POR GERAR METODOS PARA GERENCIAR COMANDOS DO ASSISTENTE
'''''

# Arquivo: core/__init__.py

import datetime
import random


class SystemInfo:
    def __init__(self):
        pass
    
    
    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = f'São {now.hour} horas e {now.minute} minutos.'
        return answer
    
    
    @staticmethod
    def getAname():
        alfa = {'SIR', 'CHAPELO', 'SOUZONES', 'GIULIAN', 'MACEIÓ', 'OSVALDO', 'PERNA FURADA', 'ZÉ', 'ZECA'}
        omega = {'MAIA', 'DJAVAN', 'RAMALHO', 'PAGODINHO', 'JULIAN'}
        beta = {'ZEUS', 'ZIDAINE', 'PEREIRA', 'JUNIOR'}
        rand = random.randint(1, 3)
        
        if rand == 1:
            rand = random.randint(0, 2)  # Changed to 2 since indexing starts from 0
            answer = list(beta)[rand]
            return answer
        
        if rand == 2:
            rand = random.randint(0, 8)
            answer = list(alfa)[rand]
            rand = random.randint(0, 4)
            answer += ' ' + list(omega)[rand]  # Added space for readability
            return answer
        
        if rand == 3:
            rand = random.randint(0, 8)
            answer = list(alfa)[rand]
            rand = random.randint(0, 4)
            answer += ' ' + list(omega)[rand]  # Added space for readability
            rand = random.randint(0, 3)
            answer += ' ' + list(beta)[rand]  # Added space for readability
            return answer
