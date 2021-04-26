"""Uber"""

class Carro:
    def __init__(self, modelo, cor, placa):
        self.modelo = modelo
        self.cor = cor
        self.placa = placa
    def exibir_local_atual(self):
        print('carro está na rua tal número 10')

carro_maria = Carro('gol', 'prata', 'JHM-4567')
carro_telson = Carro('golf', 'preto', 'RTY-7890')

# Loja Virtual

class Produto:
#     #roupas
#     def __init__(self, tamanho, cor, preco):
#         self.tamanho = tamanho
#         self.cor = cor
#         sel.preco = preco
#
# produto = Produto('P', 'preto', 20.90)
    #eletronicos
        def __init__(self, largura, altura, cor, preco):
            self.largura = largura
            self.altura = altura
            self.cor = cor
            self.preco = preco

produto = Produto('50cm','90cm', 'preto', 99.99)
print(produto)