lista = [
    {'produto': 'Fone de Ouvido', 'preco': 500},
    {'produto':'Controle Xbox', 'preco': 400},
    {'produto':'Celular', 'preco': 800},
]

def calcular_desconto(lista, funcao):
    total = 0
    for produto in lista:
        item_desconto = funcao(produto['preco'], 10)
        total += item_desconto
        print(item_desconto)
    print(f'total: {total}')

calcular_desconto(lista, lambda a,b: a-b)