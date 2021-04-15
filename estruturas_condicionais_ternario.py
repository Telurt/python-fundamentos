"""

Estruturas condicionais

if (se)
else (senão)

"""
"""
idade = 20
condicao = idade >=18
if idade <= 13:
    print("criança")
elif idade <=18:
    print("adolescente")
else:
    print("adulto")
    
"""
"""
Operadores ternários
"""
idade = 20
#resultado = ("Menor idade", "Maior idade")[idade>=18]
resultado = 'Maior idade' if idade>=18 else 'Menor idade'
print(resultado)
