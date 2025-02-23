# Receba 4 notas de um aluno e exiba se ele foi aprovado (nota maior ou igual que 6)
# Se ele ficou de recuperação (nota maior ou igual a 4) ou se ele foi 
# reprovado (nota menor que 4)

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: ")) 
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 6:
    print (f'Aluno aprovado com a nota {media}')
elif media >= 4:
    print ('Aluno de recuperação com a nota {media}')
else:
    print ('Aluno reprovado com a nota {media}')
