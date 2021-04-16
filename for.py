# postagens = [
#     "Hoje eu estou trabalhando com python", #0
#     "Estudando um pouco do básico", #1
#     "Precisamos deixar o conteudo sempre atualizado", #2
#     "Na dǘvida é melhor voltar e verificar o básico" #3
#]
# totalPostagens = len(postagens)
# count = 0
# while count < totalPostagens:
#     print(f'{count} - {postagens[count]}')
#     count += 1
#     if count == 1:
#         continue
#     print('+++++++++')

postagens = [
    "Hoje eu estou trabalhando com python", #0
    "Estudando um pouco do básico", #1
    "Precisamos deixar o conteudo sempre atualizado", #2
    "Na dǘvida é melhor voltar e verificar o básico" #3
]
# for postagem in postagens:
#     print(postagem)

# for indice, postagem in enumerate(postagens):
#     print(f'{indice} - {postagem}')
#     print("++++++")

# totalPostagens = len(postagens)
# for indice in range(totalPostagens):
#     print(postagens[indice])

# palavra = "Telson"
# for letra in palavra:
#     print(f'{letra}')

frutas = {'banana', 'maca', 'mamao', 'limao'} #utilizando set
for fruta in frutas:
    print(f' - {fruta} - ')
