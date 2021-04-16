"""
Packing - Múltiplos parâmetros
"""
#Multiplos parametros (packing)

def somar(*numeros):
    total = 0
    for numero in numeros:
        total += numero
        print(f'total: {total}')

# somar(1,10,9)

# Multiplos parametros (unpacking)

def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    print(f'Média: {media}')

notas = [6, 7]
#calcular_media(*notas)

# parametros opcionais & nomeados
def calcular_media2(nota1, nota2, ponto_extra=0):
    media = (nota1 + nota2) / 2 + ponto_extra
    print(f'Média: {media}')

calcular_media2(9, 9, ponto_extra=1)