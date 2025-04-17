arquivo = open('pessoas.txt', 'r')
resultados = arquivo.readlines()
for i in resultados:
    print(i.strip())
arquivo.close()