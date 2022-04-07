import math

def TestFunction(Nx, Ny, n, a, b):
	errpermed = 0
	ct = 0
	while (ct < n):
		temp1 = Nx[ct]
		temp2 = Ny[ct]
		erropercent = (((a * temp1) + b) - temp2) / temp2
		errpermed = errpermed + erropercent 
		ct = ct + 1
	errpermed = (errpermed / n) * 100
	return errpermed

print("Método dos mínimos quadrados")
n = int(input("Insira o número de pares de dados a ser inserido: "))
count = 0 # Contador
Sx = 0 # Somatório de x
Sy = 0 # Somatório de y
Sx2 = 0 # Somatório de x²
Sxy = 0 # Somatório de xy
Nx = [] # Valores de x
Ny = [] # Valores de y

while (count < n):
	x = float(input("Insira a coordenada x do ponto: "))
	y = float(input("Insira a coordenada y do ponto: "))
	Nx.append(x)
	Ny.append(y)
	Sx = Sx + x
	Sy = Sy + y
	Sx2 = Sx2 + (x * x)
	Sxy = Sxy + (x * y)
	count = count + 1

print("Somatório de x: ", Sx)
print("Somatório de x²: ", Sx2)
print("Somatório de y: ", Sy)
print("Somatório de xy: ", Sxy)

a = ((Sxy * n) - (Sy * Sx)) / ((Sx2 * n) - (Sx * Sx))
b = (Sy - (a * Sx))/n

erromedio = TestFunction(Nx, Ny, n, a, b)

print("a: ", a)
print("b: ", b)
print("F(x) = ", a, "x +", b)
print("Valores de x:", Nx)
print("Valores de y:", Ny)
print("Erro medio percentual: ", erromedio, "%")