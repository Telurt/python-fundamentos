"""
Funções
"""

#Media do Telson
# totalNotas = 10 + 7 + 8
# media = totalNotas/3
# print(f'Média do Telson é {media}')

#media da Maria
# totalNotas = 7 + 7 + 5
# media = totalNotas/3
# print(f'Média da Maria é {media}')

# def calcular_media(nota1, nota2, nota3):
#     totalNotas = nota1 + nota2 + nota3
#     media = totalNotas / 3
#     return media
#     #print(f'Media do {nome} é: {media}')
#
# #Media do Telson
#
# retorno = calcular_media(9,8,10)
# print(f'Média do Telson é {retorno}')

alunos = [
    {'nome': 'Telson', 'notas': [8,9,10]},
    {'nome': 'Joao', 'notas': [7, 9, 10]},
    {'nome': 'Maria', 'notas': [10, 9, 10]},
]

def calcular_media(notas):
    totalNotas = 0
    for nota in notas:
        totalNotas += nota
    media = totalNotas / len(notas)
    return media

for aluno in alunos:
    nome = aluno['nome']
    notas = aluno['notas']
    media = calcular_media(notas)
    print(f'A Média do(a) {nome} é {media}')
