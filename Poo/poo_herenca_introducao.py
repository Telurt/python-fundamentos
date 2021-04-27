# Herança - Reutilização e manutenção
# Classe - Cão Passaro

class Animal: #superclasse ou classe pai

    def __init__(self):
        self.cor = ''
        self.tamanho = ''
        self.peso = ''

    def correr(self):
        print('correr')

    def dormir(self):
        print('dormir')


class Cao(Animal): # subclasse ou classe filha

    def latir(self):
        print('latir')


class Passaro(Animal): # subclasse ou classe filha

    def voar(self):
        print('voar')

passaro = Passaro()
passaro.cor = 'amarelo'
passaro.correr()
passaro.voar()