x = input('Digite seu nome: ')

for i in x:
    print(i)

k = 0
for i in range(0 , 100):
    for j in range(0, 100):
        print(f"i = {i} j = {j}")
        k += 1

print(f"Total de iterações: {k}")
