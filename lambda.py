x = lambda nome, idade: print(f"Nome: {nome}\n Idade: {idade}")
x('Janio', 38)

y = [12, 13, 14, 15, 16, 17, 18, 19, 20]
y = list(filter(lambda x: x > 15, y))
print(y)

z = [{'nome': 'Janio', 'idade': 20}, {'nome':'Alexandre', 'idade': 38}]
z = list(map(lambda x: {'nome': x['nome'], 'idade': 'menor do que 30 anos'} if x['idade'] < 30 else (z), z))
print(z)