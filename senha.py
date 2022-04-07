from PySimpleGUI import PySimpleGUI as sg
from random import randint
import string 
import pyperclip

# Parte Operacional

as1 = string.ascii_lowercase
al1 = list(as1)
as2 = string.ascii_uppercase
al2 = list(as2)
n = ['0','1','2','3','4','5','6','7','8','9']
s = ['!','@','#','$','%','&','*','+']

c = ''
x = 0

while (x < 20):

    temp = randint(0,3)
    temp2 = randint(0,25)

    if (temp == 0):
        c = c + al1[temp2]
    elif (temp == 1):
        c = c + al2[temp2]
    elif (temp == 2):
        temp3 = randint(0,9)
        c = c + n[temp3]
    else:
        temp4 = randint(0,7)
        c = c + s[temp4]

    x = x + 1

# Interface

sg.theme('DarkBlack')
layout = [
    [sg.Text('Sua senha é:')],
    [sg.Text(c)],
    [sg.Button('Copiar'),sg.Button('OK')],
]

## Janela

janela = sg.Window('Gerador de senhas', layout)

## Ler os eventos

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break

    if eventos == 'OK':
        break

    if eventos == 'Copiar':
        pyperclip.copy(c)