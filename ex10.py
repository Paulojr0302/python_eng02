from os import system
import os
os.system('cls')

letra = input('Digite uma letra:  ')

if(letra == 'a') or (letra == 'e') or (letra == 'i') or (letra == 'o') or (letra == 'u'):
    {
        print('Vogal')
    }

elif(letra == 'A') or (letra == 'E') or (letra == 'I') or (letra == 'O') or (letra == 'U'):
    {
        print('Volgal')
    }

else:
    {
        print('Consoante')
    }