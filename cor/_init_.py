'''''
CLASSE RESPONSAVEL POR GERAR METODOS PARA GERENCIAR COMANDOS DO ASSISTENTE
'''''

import datetime
import random

class SystemInfo:
    def _init_(self):
        pass
    
    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = 'São {} horas e {} minutos. ',format(now.hour,now.minute)
        return answer
    
    @staticmethod
    def getAname():
        alfa = {'SIR ','CHAPELO ', 'SOUZONES ','GIULIAN ', 'MACEIÓ ', 'OSVALDO ', 'PERNA FURADA ','ZÉ ', 'ZECA '}
        omega = {'MAIA ', 'DJAVAN ', 'RAMALHO ', 'PAGODINHO ', 'JULIAN'}
        beta = {'ZEUS', 'ZIDAINE', 'PEREIRA', 'JUNIOR'}
        rand = random.randint(1, 3)
        
        if rand == 1:
            rand = random.randint(0,3)
            answer = list(beta)[rand]
            return answer
        
        if rand == 2:
            rand = random.randint(0,8)
            answer = list(alfa)[rand]
            rand = random.randint(0,4)
            answer += list(omega)[rand]
            return answer
        
        if rand == 3:
            rand = random.randint(0,8)
            answer = list(alfa)[rand]
            rand = random.randint(0,4)
            answer += list(omega)[rand]
            rand = random.randint(0,3)
            answer += list(beta)[rand]
            return answer
        