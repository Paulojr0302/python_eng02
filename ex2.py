    
x = str(input('Qual turno você estura? M, V ou N?  '))


if(x == 'M') or (x == 'm'):
    {
        print('Você estuda no tuno MATUTINO')
    }
elif(x == 'V') or (x == 'v'):
    {
        print('Você estuda no tuno VESPERTINO')
    }
elif(x == 'N') or (x == 'n'):
    {
        print('Você estuda no tuno NOTURO')
    }
else:
    {
        print('Resposta inválida')
    }