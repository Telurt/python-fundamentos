#Filter -> filtrar os dados
# lista_numero = [10,20,30]
# nova_lista = filter(lambda n: n >= 20, lista_numero)
# print(list(nova_lista))

lista = [
    {'produto': 'Fone de Ouvido', 'preco': 500},
    {'produto': 'Controle Xbox', 'preco': 400},
    {'produto': 'Celular', 'preco': 800},
]
#funcao = lambda p: p['preco'] >= 500
def funcao(produto):
    return produto['preco'] >= 500

nova_lista = filter(funcao, lista)
print(list(nova_lista))