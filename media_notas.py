n = 1
x = 0
k = 0
m = 0
c = 0
menor = 1000
maior = 0

while (n != 0):
	n = float(input("Insira o valor da nota, insira 0 para encerrar: "))
	if (n > maior):
		maior = n
	elif (n != 0) and (n < menor):
		menor = n
	k = k + n
	x = x + 1

c = (x - 1)
m = (k/(x - 1))
print("Foram inseridas ", c, "notas")
print("O resultado da média é: ", '%1.2f' %(m))
print("A menor nota foi: ", menor)
print("A maior nota foi: ", maior)