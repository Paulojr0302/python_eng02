from os import system
import os
os.system('cls')
import math

num1 = float(input('Digite um número:  '))
raiz = math.sqrt(num1)

if(num1>0):
    {
        print('A raiz quadrada do numero digitado é ', raiz)
    }
else:
    {
        print('Número inválido')
    }