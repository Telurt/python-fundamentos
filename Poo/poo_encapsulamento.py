# Pilar 2 - Encapsulamento

class Filtro:
    def __init__(self, imagem):
        self.imagem = imagem

    def preto_e_branco(self):
        print(f'{self.imagem} filtro preto e branco')

    def envelhecida(self):
        print(f'{self.imagem} filtro envelhecido')

# filtro = Filtro('foto_telson')
# filtro.preto_e_branco()

# Controle de acesso e Getter e Setter

class Conta:
    def __init__(self, saldo):
        self._numero = 0
        self._saldo = saldo

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self):
        return self._numero

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

conta = Conta(800)
conta.numero = 10589
print( conta.numero )
# conta.sacar(100)
# conta.depositar(200)
# print(conta._saldo)