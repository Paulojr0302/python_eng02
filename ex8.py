from os import system
import os
os.system('cls')

from os import system
import os
os.system('cls')

janeiro = float(input(f'Digite o valor de vendas do mes de janeiro '))
fevereiro = float(input(f'Digite o valor de vendas do mes de fevereiro '))
março = float(input(f'Digite o valor de vendas do mes de março '))
abril = float(input(f'Digite o valor de vendas do mes de abril '))

janeiro = janeiro * 0.1
fevereiro = fevereiro * 0.4
março = março * 0.1
abril = abril * 0.4
media = (janeiro+fevereiro+março+abril)
print(f'A media ponderada das vendas dos 4 primeiros meses do ano é {media}')

