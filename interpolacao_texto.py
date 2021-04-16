carro = "fusca"
preco = 1200.58

#print("carro: " + carro +", preco: " + str(preco)) concatenando o texto com as variaveis, str transforma em string o valor numerico

#Versões mais antigas
#print('carro: %s, preco: %.2f' %(carro,preco)) %s para string %d para numeros inteiros e %f para float .2 para duas casas decimais apos o ponto
#print('carro: {0}, preco: {1}' .format(carro, preco)) definindo entre chaves o parametro a ser utilizado na string

#Versoes mais novas
print(f'carro: {carro}, preco:{preco}') #colocando o f antes da string facilita a visualizacao da string e sua construcao, pegando diretamente os valores