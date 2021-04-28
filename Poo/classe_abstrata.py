from abc import ABC, abstractmethod

# class Animal(ABC):
#
#     def correr(self):
#         print('correr')
#
#     @abstractmethod
#     def respirar(self):
#         pass
#
# class Cao(Animal):
#     def respirar(self):
#         print('respirar como um cao')
#
# class Passaro(Animal):
#     def respirar(self):
#         print('respirar como um passaro')

""" Conta bancaria
    Conta, conta corrente e conta poupança
"""
class Conta(ABC):
    def __init__(self, numero_conta, saldo):
        self._numero_conta = numero_conta
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter

    def saldo(self, valor):
        self._saldo =  valor

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor

    @abstractmethod
    def sacar(self, valor):
        pass

class ContaPoupanca(Conta):

    def __init__(self, numero_conta, saldo):
        super().__init__(numero_conta, saldo)

    def sacar(self, valor):
        limite = 300
        if valor <= limite:
            self.saldo -= valor
        else:
            print('Limite excedido (300)')


class ContaCorrente(Conta):

    def __init__(self, numero_conta, saldo):
        super().__init__(numero_conta, saldo)

    def sacar(self, valor):
        limite = 600
        if valor <= limite:
            self.saldo -= valor
        else:
            print('Limite excedido (600)')


conta_corrente = ContaCorrente(1580,1000)
conta_corrente.depositar(200)
conta_corrente.sacar(600)
print(conta_corrente.saldo)

# conta = Conta(1058,1000)
# conta.depositar(200)
# print(conta.saldo)
