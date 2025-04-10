x = lambda nome, idade: print(f"Nome: {nome}\n Idade: {idade}")
x('Janio', 38)

y = [12, 13, 14, 15, 16, 17, 18, 19, 20]
y = list(filter(lambda x: x > 15, y))
print(y)