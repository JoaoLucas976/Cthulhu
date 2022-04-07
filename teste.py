nome = input ('Qual o seu nome ? ')
print (nome)
n1 = len (nome)
print ("Seu nome tem", n1, "letras") 
while n1 > 0:
    print (nome [-n1])
    n1 = n1 - 1
    
print ("É assim que se assuletra")
