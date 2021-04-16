"""
Funções como objeto de primeira classe, são funçòes que se
comportam como qualquer tipo nativo de uma determinada linguagem
"""

def somar(a, b):
    return a + b
def subtrair(a, b):
    return a - b

# lista = [somar, subtrair]
# for funcao in lista:
#     print(funcao(1,2))

# a = somar
# print(a(1,2))

"""
Funções de ordem superior são funções que recebem funções como
parâmetro(s) e/ou retornam funções como resposta
"""

carrinho_compras = [
    {'produto': 'Fone de Ouvido', 'Preco': 500},
    {'produto': 'Controle Xbox', 'Preco': 400},
    {'produto': 'Celular', 'Preco': 800},
]

#print(carrinho_compras)

def calcular_desconto(lista, funcao):
    total = 0
    for produto in lista:
        #print(produto['Preco'])
        item_desconto = funcao(produto['Preco'], 10)
        print(item_desconto)
        total += item_desconto
    print(f'total: {total}')

calcular_desconto(carrinho_compras, subtrair)