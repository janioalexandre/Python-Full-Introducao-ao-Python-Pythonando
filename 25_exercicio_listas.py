# Receba 10 valores e exiba a soma de todos eles

x = [int(input('Digite um número: ')) for i in range(0, 10)]

soma = 0
for i in x:
    soma = soma + i

print(f'A soma dos valores é: {soma}')