from os import system
import os
os.system('cls')

sexo = input('Digite seu sexo, M ou F:  ')

if(sexo == 'M') or (sexo == 'm'):
    {
        print('Sexo masculino')
    }
    
elif(sexo == 'F') or (sexo == 'f'):
    {
        print('Sexo feminino')
    }

else:
    {
        print('Sexo inválido')
    }