"""
Polimorfismo -> QUalidade ou estado de ser capaz de assumir diferentes formas
Poli = muitas
morfo = formas
"""
class Animal: #superclasse ou classe pai

    def __init__(self, cor, tamanho, peso):
        self.cor = cor
        self.tamanho = tamanho
        self.peso = peso

    def correr(self):
        print('correr como um')

    def dormir(self):
        print('dormir')

    def __str__(self):
        return f'cor: {self.cor}, tamanho: {self.tamanho}, peso: {self.peso}'

class Cao(Animal): # subclasse ou classe filha

    #def __init__(self, cor, tamanho, peso, raca):
    def __init__(self, cor, tamanho, peso):
        super().__init__(cor, tamanho, peso)
        self.peso = f'{peso} Kg'
        #self.raca = raca

    def latir(self):
        print('latir')

    #sobrescrita de método -> override
    def correr(self):
        super().correr()
        print('cao')

    def __str__(self):
        return super().__str__() + f', raca: {self.raca}'

class Passaro(Animal): # subclasse ou classe filha

    def __init__(self, cor, tamanho, peso):
        super().__init__(cor, tamanho, peso)


    def voar(self):
        print('voar')

    # def correr(self):
    #     super().correr()
    #     print('passaro')

class Papagaio(Passaro, Cao):
    def __init__(self, cor, tamanho, peso):
        super().__init__(cor, tamanho, peso)

    def correr(self):
        print('Correr')

    def falar(self):
        print('falar')

cao = Cao('Marrom', '40cm', '1')
# cao.correr()

passaro = Passaro('Amarelo', '30cm', '500g')
# passaro.correr()

papagaio = Papagaio('verde', '20cm', '800g')
papagaio.correr() # animal
papagaio.voar() # passaro
papagaio.falar() # papagaio
papagaio.latir() # cao