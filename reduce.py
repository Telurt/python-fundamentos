# Reduce (reduzir) -> acumula e reduz uma lista em um único valor
# não vem dentro de Bultin

from functools import reduce

# lista_numero = [10,10,10]
# acumula = 0
# for item in lista_numero:
#     #acumula = acumula + item
#     acumula += item
# print(acumula)

lista = [
    {'produto': 'Fone de Ouvido', 'preco': 500},
    {'produto': 'Controle Xbox', 'preco': 400},
    {'produto': 'Celular', 'preco': 800},
]
funcao = lambda acumulador, produto: acumulador + produto['preco']
resultado = reduce(funcao, lista, 0)
print(resultado)