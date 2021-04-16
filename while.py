"""

While(condicao):
    executa quando a condicao é verdadeira
"""

# count = 1
# while count <= 4:
#     print(f"executou {count}")
#     count +=1

postagens = [
    "Hoje eu estou trabalhando com python", #0
    "Estudando um pouco do básico", #1
    "Precisamos deixar o conteudo sempre atualizado", #2
    "Na dǘvida é melhor voltar e verificar o básico" #3
]
totalPostagens = len(postagens)
count = 0
while count < totalPostagens:
    print(f'{count} - {postagens[count]}')
    count += 1
    if count == 1:
        continue
    print('+++++++++')
    # if count == 1:
    #     break
    # if count != totalPostagens:
    #     print('+++++++++')
print("fim")
