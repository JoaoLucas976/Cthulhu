x = 0
pi = 3.1415
nome = input ('Insira o seu nome: ') 
spc = ("=") * 38

print ('Seja bem vindo,' , nome)

y = int (input ('Quantas formas você quer calcular ? ') )

while x < y:

    print (spc) 

    selecao = int ( input ('De qual forma geométrica você quer calcular a área ? \n 1 = quadrado \n 2 = retangulo \n 3 = circulo \n 4 = triângulo \n' ) )

    if (selecao == 1):
        print ('Você escolheu o Quadrado')
        L = int (input ('Insira a medida do lado: ') )
        A = L ** 2
        print ('A área dessa forma é: ', A)
    elif (selecao == 2):
        print ('Você escolheu o Retângulo')
        B = int (input ('Insira a medida da base: ') )
        H = int (input ('Insira a medida da altura: ') )
        A = B * H
        print ('A área dessa forma é: ', A)
    elif (selecao == 3):
        print ('Você escolheu o Círculo')
        R = int (input ('Insira a medida do raio: ') )
        A = pi * (R ** 2)
        print ('A área dessa forma é: ', A)
    elif (selecao == 4):
        print ('Você escolheu o triângulo')
        B = int (input ('Insira a medida da base: ') )
        H = int (input ('Insira a medida da altura: ') )
        A = (B * H) / 2
        print ('A área dessa forma é: ', A)
    else:
        print ('Escolha Inválida')
    x = x + 1

print ('Obrigado por usar o meu programa')

