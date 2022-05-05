# Comentários são feitos usando hashtag

import os # Importando uma biblioteca
import random as rd # Importando uma biblioteca e dando um apelido pra ela "rd"

# VARIÁVEIS
numero = -10.5 # Variavel numerica 
frase = "Beleza" # Variavel string
booleana = True # Variavel booleana
lista1 = [] # Variavel do tipo lista vazia
lista2 = ['Banana','Maçã','Laranja'] # Variavel do tipo lista preenchida
nome = input("Insira um valor: ") # Variavel recebida pelo usuário
x1 = len(lista1) # Armazena o numero de itens da lista 1
x2 = len(lista2) # Armazena o numero de itens da lista 2
f = input("Insira o seu nome: ") # Variavel recebida pelo usuário
i = 0 # Variavel numerica usada como contador

# Mostrando algo na tela
print("Bem vindo ao referencial", nome) # Mostrando uma mensagem na tela/ unindo mensagem e variável

# IF/ElSE (Condicional)

if numero < 0: # If 
	print("É menor do que 0")
elif numero == 0: # Else com uma condicional 
	print("É igual a 0")
else: # Else 
	print("É maior do que 0")

# WHILE/FOR (Laço de Repetição)

while i < 3: # Enquando i for menor do que 3
	print("Mensagem genérica 1") # Mostrando a mensagem na tela
	i += 1 # Aumentando a variável i

i = 0 # Zerando a variável i

for i in range(3): # Enquando i for menor do que 3
	print("Mensagem genérica 2") # Mostrando a mensagem na tela

# MOSTRANDO LISTAS
print("Lista 1: ",lista1) # Mostrando a lista 1 com print
print("Lista 2: ",lista2) # Mostrando a lista 2 com print

for i in range(x2):
	print("Lista2[" , i , "] = ", lista2[i]) # Mostrando a lista na tela com um laço for

# MANIPULANDO LISTAS
for i in range(x2):
	lista1.append(lista2[i]) # Adicionando itens da lista 2 à lista 1

x3 = len(lista1) # Pegando o novo tamanho da lista 1

for i in range(x3):
	print("Lista1[" , i , "] = ", lista1[i]) # Mostrando a lista 1, agora com os itens, usando um laço for

# DECLARANDO FUNÇÕES
def Sorte(): # Criando uma função Sorte
	sorte = rd.randint(0,10) # Usando a biblioteca random e a função randint pra gerar um numero aleatorio
	return sorte # Retornando o valor da variavel sorte

# CHAMANDO FUNÇÕES
print("Está com sorte hoje ?")
luck = Sorte() # Recebendo o valor da função Sorte

if luck <= 4:
	print("Eu acho que não")
elif luck >= 5 and luck < 8:
	print("Só um pouco")
else:
	print("Estou sim")
