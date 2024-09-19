from os import system
import os
os.system('cls')

salario = float(input('Digite o seu salário:  '))

sm = 1412
mediaSalario = salario/sm

if(mediaSalario<=1):
    {
        print('O salario era: ', salario ,' recebeu um aumento de 20%, sendo o valor aumentado: ' ,salario*0.2, ' e o novo salário é: ' ,salario +(salario*0.2))
    }
elif(mediaSalario<=2):
    {
        print('O salario era: ', salario ,' recebeu um aumento de 15%, sendo o valor aumentado: ' ,salario*0.15, ' e o novo salário é: ' ,salario +(salario*0.15))
    }
elif(mediaSalario<=5):
    {
        print('O salario era: ', salario ,' recebeu um aumento de 10%, sendo o valor aumentado: ' ,salario*0.1, ' e o novo salário é: ' ,salario +(salario*0.1))
    }
else:
    {
        print('O salario era: ', salario ,' recebeu um aumento de 5%, sendo o valor aumentado: ' ,salario*0.05, ' e o novo salário é: ' ,salario +(salario*0.05))
    }