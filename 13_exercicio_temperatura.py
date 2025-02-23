# Receba uma temperatura em farenheit e exiba em graus celsius.

farenheit = float(input('Digite a temperatura em Farenheit: '))
celsius = 5 * (farenheit - 32) / 9
print(f'A temperatura em Celsius é {celsius:.2f}')
