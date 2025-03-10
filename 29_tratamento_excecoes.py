n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

try:
    print(n1 / n2)
except:
    print('Não consegui')
finally:
    print('Finalizado!')
