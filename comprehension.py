"""
List Comprehension (compreensão de lista)
É uma construção sintática para criação de uma lista baseada em listas existentes.
"""

lista = [10,20,30]

# Usada como Map

# nova_lista = [item* 2 for item in lista]
# print(nova_lista)

# Usada como Filter
#nova_lista = [item for item in lista if item >= 20 if item < 30]
# nova_lista = [i if i >= 20 and i< 30 else 0 for i in lista]
# print(nova_lista)

dicionario = {f'chave{i}': i for i in lista }
print(dicionario)