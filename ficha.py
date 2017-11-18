#RESOLUÇÃO FICHA PYTHON
#
#OBS:
#1. Eu uso a versão 3.5 do python para resolve-los.
#2. Caso tenha dúvidas, pode fazer realizar uma pergunta que ajuda a resolver.
#3. Siga a apostila criada, para conseguir compreender o código, pois nela tem o algoritmo.
#4. Lembrando que existe várias forma de resolver a questão, so precisamos nos atentar ao "ZEN OF PYTHON".
#5. Quando for testar o código, só precisa comentar as questões que são relevantes.

# 1) 
add=0                                                    # Criei uma variavel com valor inteiro de 0
for i in range(2):                                       # Faço uma repitação em 2 etapas, para pegar esses valores.
	add=int(input("Por favor informe o número deseja:"))
	add+=add                                             # Realizo um autoincrementação no valor da variavel, para obter a soma.
print("A soma dos números informado foi: ", add)         # Exibo o valor atual de add.

# 2)
# Irei resolver de forma simples, sem usar a biblioteca MATH.

import random                                          				 	 # Importei a biblioteca random, para criar uma lista com 3 valores
num=[]																	 # criei uma lista chamada "num"
for i in range(3):															
	num.append(random.randrange(10))									 # Armazenei esses valores escolhidos aleatóriamente em "num"
num.sort()											 				     # Reorganizei os valores dentro da lista.
print("O maior número é: ", num[2], "e o menor valor é: ", num[0])       # Exibi esses valores.

# 3)
c=0																	 # Variavel contadora
login=input("Por favor, digite o nickname escolhido: ")			 	 # Criando variavel com valor login
while(c==0):
	senha=input("Por favor, digite a senha escolhida: ")				 # Criando variavel com valor senha
	if(login==senha):													 # Criando condição, para verificar se login é igual a senha. Senhdo o loop acontece.
		print("Senha igual ao login, favor cadastrar nova senha.")
	else:																 # Encerrando loop, pois ela foi satisfeita e o valor de "c" foi alterado.
		print("senha cadastrada com sucesso!")
		c+=1

# 4)
n = input("Infome um inteiro a partir da casa das dezenas: ") 			 # Criando variavel de entrada.
print(n[::-1])															 # Percendo que o valor de "n" é do tipo 'string', so precisei fazer um 'slice' inverso!

# 5)
import random																# Importei a biblioteca random
IMPAR=[]																	# Criando as listas solicitadas.
PAR=[]
LISTA= random.sample(range(1,101),20)										# Nessa lista, a preenchi com conteudo aleatório, nos valores pedidos.	
for i in LISTA:																# Crio o laço, para preso na quantidade de elementos de LISTA.
	if(i%2==0):																# Condição para verificar e adicionar o elemento par dentro da lista PAR
		PAR.append(i)
	elif(i%2!=0):															# Condição para verificar e adicionar o elemento impar dentro da lista IMPAR
		IMPAR.append(i)														
print('Os elementos da lista geral são: ', LISTA)
print('Os elementos pares da lista são: ', PAR)
print('Os elementos impares da lista são: ', IMPAR)

# 6)
salario = float(input("Por favor, informe o valor do seu salário: "))		# Armazenei o valor do salário do cliente.
p = float(input("Por favor, informe o valor da porcentagem: "))				# Armazenei o valor da porcentagem de aumento do cliente.
aumento = salario * (p/100)													# Calculo o valor do aumento salarial do cliente.
print("O valor do seu aumento foi: R$", aumento)
print("O valor atual do seu salário é: R$", aumento + salario)

# 7)
cigarro = int(input("Por favor, informe quanto cigarros você fuma por dia: "))	 # Armazenando valor de cigarro fumados por dias.
anos = int(input("Por favor, informe a quantidade de anos que você fuma: "))	 # Armazenando valor de anos de cigarro consumido.
vida = (cigarro*10*(anos*365))/1440												 # Calculo feito iniciando a conversão de valores de anos para minutos e depois o total para dias novamente.
print("O valor em dias perdidos foi de: ", round(vida))

# 8)
kw = float(input("Por favor, informe a quantidade de quilowatts consumidos da sua residência: ")) 		# Armazenando valor de quilowatts consumidos
salario = float(input("Agora informe o valor do salário minimo: "))										# Armazenando valor do salário minimo
def calculo_kw(kw,salario):																				# Criando uma função de calculo
	valor_kw = 1 * salario/5																			# Realizando o calculo do valor de 1 KW
	mes=kw*valor_kw																						# Realizando o valor do consumo mensal da residência
	desconto = mes*0.15																					# Descobrindo o valor com desconto de 15%
	return(valor_kw,mes,desconto)																		# Retornando os valores da função
	
print("Os valores do Kw, do consumo mensal e da mensalidade com desconto, são respectivamente: ", calculo_kw(kw,salario))

# 9)
class Info(): 																# Criando classe com as respostas. Lembrando que toda classe possui metódos que são funções contendo os calculos e retornando valores.
	def fim():																# Para chamar uma função, só precisa usar a sintaxe "NOME_DA_CLASSE.NOME_DO_METODO(PAREMETRO SE ELE RECEBER@)"
		return("Fim de serviço")
	def saudacao():
		return("Olá. Como vai?")
	def bronca():
		return("Vamos estudar mais")
	def felicitacao():
		return("Meus Parabéns!")

op=5																		# Criação de variavel contadora
while(op!=0): 																# Criando laço de repetição condicional
	print(('''																
		OPÇÕES:
		1 - SAUDAÇÃO
		2 - BRONCA
		3 - FELICITAÇÃO
		0 - FIM 
		'''))																# Exibindo tabela de opções.
	op=int(input("Por favor escolha uma dessas opções acima: "))			# Armazenado valores escolhidos pelo usuário
	if(op==0): 																# Tomada de decisão baseado no valor escolhido pelo usuário.
		print(Info.fim())
	elif(op==1):
		print(Info.saudacao())
	elif(op==2):
		print(Info.bronca())
	elif(op==3):
		print(Info.felicitacao())

	
# 10)


