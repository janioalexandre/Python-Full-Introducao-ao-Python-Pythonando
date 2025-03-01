pessoas = [{'nome': 'Janio', 'sexo': 'M', 'idade': 38},
           {'nome': 'Alexandre', 'sexo': 'M', 'idade': 38},
           {'nome': 'Maria', 'sexo': 'F', 'idade': 64},]

for pessoa in pessoas:
    print(f'{pessoa["nome"]} tem {pessoa["idade"]} anos.')