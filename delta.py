﻿print ("Bem vindo ao Calculador de Funções do Segundo Grau !")
print ("A seguir, insira os valor de a, b e c de uma função")
print ("Do tipo: f(x) = ax² + bx + c")
A = int (input ("Insira aqui o valor de a: "))
B = int (input ("Insira aqui o valor de b: "))
C = int (input ("Insira aqui o valor de c: "))
delta = (B * B) - 4 * A * C
X1 = (- (B) + (delta ** 0.5))/(2 * A)
X2 = (- (B) - (delta ** 0.5))/(2 * A)
print ("O valor de X1 é: ", X1)
print ("O valor de X2 é: ", X2)
print ("Obrigado por utilizar o meu programa !")