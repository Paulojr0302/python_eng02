from os import system
import os
os.system('cls')
maca = int(input('Digite a quantidade de maças:  '))

if(maca<12):
    {
        print('O preco das maças é: R$', maca*0.30)
    }
else:
    {
        print('O preco das maças é: R$', maca*0.25)
    }