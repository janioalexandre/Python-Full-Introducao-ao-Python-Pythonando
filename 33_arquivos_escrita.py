arquivo = open('pessoas.txt', 'w')
i = 0
while True:
    if i > 1:
        break
    arquivo.write(input('Digite o nome da pessoa: ') + " " + input('Digite a idade: ') + "\n")
    i += 1
