'''''
CLASSE RESPONSAVEL POR GERAR METODOS PARA GERENCIAR COMANDOS DO ASSISTENTE
'''''

import datetime


class SystemInfo:
    def _init_(self):
        pass
    
    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = 'São {} horas e {} minutos. ',format(now.hour,now.minute)
        return answer
    
    