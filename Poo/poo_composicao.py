"""

Relação de composição -> a classe principal (todo) cria
uma instância da outra classe(parte), que se torna parte dela.
Quando a classe principal for destruída, sua instância da outra classe
também será

"""

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, cep, cidade, rua):
        endereco = Endereco(cep, cidade, rua)
        self.enderecos.append(endereco)

    def listar_endereco(self):
        print(f'Endereço para {self.nome}')
        for endereco in self.enderecos:
            print(endereco)

    def __del__(self):
        print(f'{self.nome} Apagado')

class Endereco: # parte
    def __int__(self, cep, cidade, rua):
        self.cep = cep
        self.cidade = cidade
        self.rua = rua

    def __del__(self):
        print(f'{self.rua} Apagado')

    def __str__(self):
        return f'cep: {self.cep}, cidade: {self.cidade}, rua: {self.rua}'

usuario = Usuario('Telson')
usuario.inserir_endereco('123456-78', 'Manaus', 'Rua Amazonas, Número 1')
usuario.inserir_endereco('123456-79', 'Manaus', 'Rua Amazonas, Número 2')

usuario.listar_endereco()