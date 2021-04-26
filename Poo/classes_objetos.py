class Conta:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

conta = Conta("Telson", 1000)
conta.sacar(100)
print(f'nome:{conta.nome} - saldo: R$ {conta.saldo}')