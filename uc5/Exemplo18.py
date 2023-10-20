class dispositivoEletronico():
    def acao(self):
        pass
    def produto(self):
        pass

class Celular(dispositivoEletronico):
    def acao(self):
        return 'carregando'
    def produto(self):
        return 'Samsung Galaxy A14'
    
class FoneDeOuvido(dispositivoEletronico):
    def acao(self):
        return 'conectado'
    def produto(self):
        return 'Galaxy Buds2 '

class Computador(dispositivoEletronico):
    def acao(self):
        return 'sendo atualizado...'
    def produto(self):
        return 'Notebook Dell Inspiron 15'
    
class Impressora(dispositivoEletronico):
    def acao(self):
        return 'imprimindo'
    def produto(self):
        return 'Epson l3250'
    
class Relogio(dispositivoEletronico):
    def acao(self):
        return 'conectado'
    def produto(self):
        return 'Galaxy Watch6'
    
def oQueEstaAcontecendo(dispositivos):
    for dispositivo in dispositivos:
        print(f'O dispositivo {dispositivo.produto()} está {dispositivo.acao()}.')


dispositivos = [Celular(), FoneDeOuvido(), Computador(), Relogio(), Impressora()]
oQueEstaAcontecendo(dispositivos)

        
