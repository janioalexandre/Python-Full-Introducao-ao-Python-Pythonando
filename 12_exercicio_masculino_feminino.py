# Receba F para feminino e M para masculino e mostre o sexo da pessoa.

sexo = input('Digite F para feminino e M para masculino: ')

if sexo == 'F' or sexo == 'f':
    print('Feminino')
elif sexo == 'M' or sexo == 'm':
    print('Masculino')
else:
    print('Sexo inválido')
