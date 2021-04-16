# dicionario = {
#     'correr': 'deslocar-se ou mover-se rapidamente',
#     'ligar': 'estabelecer uma comunicação',
# }
# print(dicionario['ligar'])

carro = {
    'modelo': 'Fusca',
    'marca': 'Volks',
    'ano': 1970,
    'donos': ['Marcos', 'Maria']
}

# print(carro['donos'][0]) imprime na tela o dono do carro na posição 0
# carro['donos'].append["Pedro"] adiciona mais um dono a lista de donos
# carro['km']= 8500 adiciona o campo ao dicionario
# carro['ano']= 1980 modifica o ano do carro
# carro.update({'ano': 1980, 'km':8500 }) atualiza o campo ano e cria o campo km no dicionario
# del carro['ano'] deleta o item do dicionario
# print(carro.keys()) pega as chaves do dicionario
# print(carro.values()) pega os valores do dicionario
# print(carro.items()) pega os itens do dicionario
# print(len(carro)) conta a quantidade de itens presentes no dicionario
# carro.clear() limpa por completo o dicionario

"""
set -> conjuntos (Não é indexado) é feito com as {}
"""

itens = {"Telson", "Isaias", "Chris"}
itens2 = {"Maria", "Joao", "Telson"}
# novo = itens.union(itens2) Faz a união dos conjuntos
# novo = itens.intersection(itens2) Faz a interseção dos conjuntos elementos iguais
# itens.add("Joao") adiciona um novo item ao conjunto
# itens.remove("Joao") remove o item do conjunto
print(novo)
