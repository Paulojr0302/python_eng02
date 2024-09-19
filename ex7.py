from os import system
import os
os.system('cls')

nota1 = float(input('Digite a primeira nota:  '))
nota2 = float(input('Digite a segunda nota:  '))
nota3 = float(input('Digite a terceira nota:  '))

media = (nota1+nota2+nota3)/3

if(media == 10):
    {
        print('Aprovado com distinção, media ', media)
    }
elif(media>=7):
    {
        print('Aprovado com média ', media)
    }
else:
    {
        print('Reprovado com média ', media)
    }
